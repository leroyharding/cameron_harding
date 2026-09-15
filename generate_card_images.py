import os
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1012, 638  # Standard CR80 credit card size at 300 DPI (85.6mm x 54mm)

# Ensure QR code exists
qr_path = "photos/web/qr_code.png"
if not os.path.exists(qr_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1,
    )
    qr.add_data("https://cameron-harding.vercel.app/")
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#0b0c0e", back_color="#ffffff")
    qr_img.save(qr_path)

# Load fonts
font_dir = "C:\\Windows\\Fonts"
try:
    font_serif_lg = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 52)
    font_serif_md = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 38)
    font_serif_sm = ImageFont.truetype(os.path.join(font_dir, "georgia.ttf"), 28)
    font_sans_bold = ImageFont.truetype(os.path.join(font_dir, "calibrib.ttf"), 26)
    font_sans_reg = ImageFont.truetype(os.path.join(font_dir, "calibri.ttf"), 24)
    font_sans_sm = ImageFont.truetype(os.path.join(font_dir, "calibri.ttf"), 20)
    font_sans_xs = ImageFont.truetype(os.path.join(font_dir, "calibri.ttf"), 16)
except Exception:
    font_serif_lg = font_serif_md = font_serif_sm = font_sans_bold = font_sans_reg = font_sans_sm = font_sans_xs = ImageFont.load_default()

# -------------------------------------------------------------
# 1. GENERATE FRONT SIDE
# -------------------------------------------------------------
front = Image.new("RGBA", (W, H), (11, 12, 14, 255))
draw = ImageDraw.Draw(front)

# Load & crop photo to the left side
photo_src = "photos/WhatsApp Image 2026-09-15 at 16.10.02.jpeg"
photo_w = 420
photo_h = H

with Image.open(photo_src) as img:
    img = ImageOps.exif_transpose(img).convert("RGBA")
    aspect = img.width / img.height
    target_aspect = photo_w / photo_h
    if aspect > target_aspect:
        new_h = photo_h
        new_w = int(photo_h * aspect)
    else:
        new_w = photo_w
        new_h = int(photo_w / aspect)
    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    left = (new_w - photo_w) // 2
    top = (new_h - photo_h) // 2
    img_cropped = img_resized.crop((left, top, left + photo_w, top + photo_h))

# Paste photo onto front
front.paste(img_cropped, (0, 0))

# Gradient overlay from photo into dark background
gradient = Image.new("RGBA", (140, H), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(gradient)
for x in range(140):
    alpha = int(255 * (x / 140.0))
    g_draw.line([(x, 0), (x, H)], fill=(11, 12, 14, alpha))

front.paste(gradient, (photo_w - 140, 0), gradient)

# Subtle Gold Border around entire card
gold = (212, 175, 55, 255)
draw.rounded_rectangle([(18, 18), (W - 18, H - 18)], radius=24, outline=(212, 175, 55, 90), width=2)

# Text on right side
text_x = 450
y = 150

# Small badge
draw.text((text_x, y), "PROFESSIONAL MALE MODEL", fill=gold, font=font_sans_xs)
y += 35

def draw_spaced_text(draw, text, x, y, font, fill, spacing=3):
    cur_x = x
    for ch in text:
        draw.text((cur_x, y), ch, font=font, fill=fill)
        bbox = draw.textbbox((cur_x, y), ch, font=font)
        cur_x += (bbox[2] - bbox[0]) + spacing

draw_spaced_text(draw, "CAMERON", text_x, y, font_serif_lg, (255, 255, 255, 255), spacing=5)
y += 58
draw_spaced_text(draw, "HARDING", text_x, y, font_serif_lg, (220, 222, 226, 255), spacing=5)
y += 68

# Gold Divider Line
draw.line([(text_x, y), (W - 60, y)], fill=gold, width=2)
y += 26

# Title "MODEL"
draw_spaced_text(draw, "M O D E L", text_x, y, font_sans_bold, gold, spacing=8)
y += 60

# Disciplines (Location & height measurement removed as requested)
draw.text((text_x, y), "RUNWAY • COMMERCIAL • EDITORIAL • FITNESS", fill=(180, 184, 192, 255), font=font_sans_xs)
y += 42

# Web icon (globe) + website link
icon_r = 10
icon_cx = text_x + icon_r
icon_cy = y + icon_r
# Draw globe icon
draw.ellipse([(icon_cx - icon_r, icon_cy - icon_r), (icon_cx + icon_r, icon_cy + icon_r)], outline=gold, width=2)
draw.ellipse([(icon_cx - icon_r // 2, icon_cy - icon_r), (icon_cx + icon_r // 2, icon_cy + icon_r)], outline=gold, width=1)
draw.line([(icon_cx - icon_r, icon_cy), (icon_cx + icon_r, icon_cy)], fill=gold, width=1)

draw.text((text_x + 30, y - 2), "cameron-harding.vercel.app/", fill=gold, font=font_sans_reg)

front_rgb = front.convert("RGB")
front_rgb.save("business_card_front.png", dpi=(300, 300))
print("Saved business_card_front.png (300 DPI, 1012x638)")

# -------------------------------------------------------------
# 2. GENERATE BACK SIDE (Measurements removed, bigger QR code)
# -------------------------------------------------------------
back = Image.new("RGBA", (W, H), (11, 12, 14, 255))
b_draw = ImageDraw.Draw(back)

# Border
b_draw.rounded_rectangle([(18, 18), (W - 18, H - 18)], radius=24, outline=(212, 175, 55, 90), width=2)

# Header
b_draw.text((60, 48), "CAMERON HARDING", fill=(255, 255, 255, 255), font=font_serif_md)
b_draw.text((W - 200, 56), "OFFICIAL PORTFOLIO", fill=gold, font=font_sans_xs)
b_draw.line([(60, 96), (W - 60, 96)], fill=(212, 175, 55, 100), width=1)

# Left Column: BIGGER QR Code Container (410 x 410 px!)
qr_box_size = 400
qr_x = 60
qr_y = 135

# High-contrast white backing with gold border
b_draw.rounded_rectangle([(qr_x - 12, qr_y - 12), (qr_x + qr_box_size + 12, qr_y + qr_box_size + 12)], radius=20, fill=(255, 255, 255, 255), outline=gold, width=3)

with Image.open(qr_path) as qr_raw:
    qr_resized = qr_raw.resize((qr_box_size, qr_box_size), Image.Resampling.LANCZOS)
    back.paste(qr_resized, (qr_x, qr_y))

# Text below QR Code
b_draw.text((qr_x + 85, qr_y + qr_box_size + 24), "SCAN TO VIEW DIGITAL PORTFOLIO", fill=gold, font=font_sans_xs)

# Right Column: Instagram, Email, and Website details (Measurements removed!)
rx = 500
ry = 145
box_w = W - 50  # 962 px, giving 462 px box width

font_insta = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 30)
font_email = ImageFont.truetype(os.path.join(font_dir, "calibri.ttf"), 23)
font_web = ImageFont.truetype(os.path.join(font_dir, "calibrib.ttf"), 23)

# Instagram Card Box (Clean padding, fits perfectly)
b_draw.rounded_rectangle([(rx, ry), (box_w, ry + 105)], radius=16, fill=(20, 22, 27, 255), outline=(212, 175, 55, 90), width=1)
b_draw.text((rx + 24, ry + 20), "INSTAGRAM", fill=gold, font=font_sans_xs)
b_draw.text((rx + 24, ry + 48), "@Cameronharding11", fill=(255, 255, 255, 255), font=font_insta)

# Email Card Box
ry += 130
b_draw.rounded_rectangle([(rx, ry), (box_w, ry + 105)], radius=16, fill=(20, 22, 27, 255), outline=(212, 175, 55, 90), width=1)
b_draw.text((rx + 24, ry + 20), "DIRECT BOOKINGS & CASTING", fill=gold, font=font_sans_xs)
b_draw.text((rx + 24, ry + 50), "cameronhardingmodel@gmail.com", fill=(255, 255, 255, 255), font=font_email)

# Website Box with Web Icon
ry += 130
b_draw.rounded_rectangle([(rx, ry), (box_w, ry + 90)], radius=16, fill=(20, 22, 27, 255), outline=(212, 175, 55, 90), width=1)
# Draw web icon
b_icon_r = 10
b_icon_cx = rx + 34
b_icon_cy = ry + 45
b_draw.ellipse([(b_icon_cx - b_icon_r, b_icon_cy - b_icon_r), (b_icon_cx + b_icon_r, b_icon_cy + b_icon_r)], outline=gold, width=2)
b_draw.ellipse([(b_icon_cx - b_icon_r // 2, b_icon_cy - b_icon_r), (b_icon_cx + b_icon_r // 2, b_icon_cy + b_icon_r)], outline=gold, width=1)
b_draw.line([(b_icon_cx - b_icon_r, b_icon_cy), (b_icon_cx + b_icon_r, b_icon_cy)], fill=gold, width=1)

b_draw.text((rx + 58, ry + 32), "cameron-harding.vercel.app/", fill=gold, font=font_web)

# Bottom Agency note
b_draw.text((rx, H - 42), "AVAILABLE FOR UK NATIONWIDE & INTERNATIONAL BOOKINGS", fill=(120, 125, 135, 255), font=font_sans_xs)

back_rgb = back.convert("RGB")
back_rgb.save("business_card_back.png", dpi=(300, 300))
print("Saved business_card_back.png (300 DPI, 1012x638)")
