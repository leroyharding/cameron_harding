import os
import re
import base64
import json

def get_base64_data_uri(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    mime = "image/jpeg"
    if ext in [".png"]:
        mime = "image/png"
    elif ext in [".webp"]:
        mime = "image/webp"
    with open(filepath, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

print("Building standalone portfolio...")
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace all <img src="photos/web/..." with data URIs
# Also qr_code.png if referenced
img_src_matches = set(re.findall(r'src=["\'](photos/(?:web/)?([^"\']+))["\']', html))
print(f"Found {len(img_src_matches)} distinct <img> src references in index.html")

cache = {}
for full_match, filename in img_src_matches:
    local_path = full_match.replace("/", os.sep)
    if os.path.exists(local_path):
        if local_path not in cache:
            cache[local_path] = get_base64_data_uri(local_path)
        data_uri = cache[local_path]
        html = html.replace(f'src="{full_match}"', f'src="{data_uri}"')
        html = html.replace(f"src='{full_match}'", f"src='{data_uri}'")

# 2. In galleryPhotos array:
# For standalone edition, we want the lightbox to display the base64 data URI directly
# And raw download link to also work or download the base64 data URI
# Let's inspect how lightbox in portfolio_standalone handles photo.filename:
# In renderLightboxPhoto():
# img.src = 'photos/web/' + photo.filename;
# rawLink.href = 'photos/' + photo.filename;

# In portfolio_standalone.html, let's embed a photoMap of data URIs:
# photoDataUris = { "P1053071.jpg": "data:image/jpeg;base64,...", ... }
# And update renderLightboxPhoto() to use photoDataUris[photo.filename] || ('photos/web/' + photo.filename)!

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

start = text.find('const galleryPhotos = [')
end = text.find('let currentLightboxIndex = 0;', start)
array_text = text[start + len('const galleryPhotos = '):text.rfind('];', start, end) + 1]
photos = json.loads(array_text)

print(f"Embedding Base64 maps for {len(photos)} photos...")
photo_b64_map = {}
for p in photos:
    fn = p["filename"]
    web_p = os.path.join("photos", "web", fn)
    if os.path.exists(web_p):
        photo_b64_map[fn] = get_base64_data_uri(web_p)
    else:
        print(f"Warning: {web_p} not found")

b64_json_str = json.dumps(photo_b64_map)

# Replace the lightbox script in html
standalone_script = f"""
        const photoDataUris = {b64_json_str};

        function renderLightboxPhoto() {{
            const photo = galleryPhotos[currentLightboxIndex];
            const img = document.getElementById('lightbox-img');
            const cap = document.getElementById('lightbox-caption');
            const sub = document.getElementById('lightbox-sub');
            const badge = document.getElementById('lightbox-badge');
            const counter = document.getElementById('lightbox-counter');
            const rawLink = document.getElementById('lightbox-raw-link');

            img.style.opacity = '0.4';
            const srcUri = photoDataUris[photo.filename] || ('photos/web/' + photo.filename);
            img.src = srcUri;
            img.onload = () => {{ img.style.opacity = '1'; }};
            
            cap.innerText = photo.title;
            sub.innerText = photo.subtitle;
            badge.innerText = photo.badge;
            counter.innerText = `${{currentLightboxIndex + 1}} / ${{galleryPhotos.length}}`;
            rawLink.href = srcUri;
            rawLink.download = photo.filename;
        }}
"""

old_render_fn = re.search(r'function renderLightboxPhoto\(\) \{[\s\S]*?rawLink\.href = \'photos/\' \+ photo\.filename;\s*\}', html)
if old_render_fn:
    html = html.replace(old_render_fn.group(0), standalone_script.strip())
    print("Replaced renderLightboxPhoto with standalone data URI handler.")
else:
    print("Warning: old renderLightboxPhoto not matched exactly.")

with open("portfolio_standalone.html", "w", encoding="utf-8") as f:
    f.write(html)

size_mb = os.path.getsize("portfolio_standalone.html") / (1024 * 1024)
print(f"portfolio_standalone.html generated successfully! File size: {size_mb:.2f} MB")
