# Cameron Harding Model Portfolio — Session Summary & Context Guide

**Generated Date**: 2026-09-15  
**Project**: Cameron Harding Official Model Portfolio & Business Card Suite  
**Workspace Path**: `C:\Users\leroy\Desktop\Antigravity apps\cameron harding`  

---

## 🌐 Live Deployments & Key Links

| Asset | Location / URL | Notes |
|---|---|---|
| **GitHub Repository** | [https://github.com/leroyharding/cameron_harding](https://github.com/leroyharding/cameron_harding) | Branch `main`, up to date |
| **Vercel Live Website** | [https://cameron-harding.vercel.app/](https://cameron-harding.vercel.app/) | Auto-deploys on push to `main` |
| **Local Preview Server** | `http://localhost:8080` | Python HTTP Server (`python -m http.server 8080`) |
| **Local Standalone Edition** | `portfolio_standalone.html` | Double-click to open offline on any device |
| **3D Business Card Tool** | `business_card.html` | Interactive 3D flip + print layout |

---

## 📋 Model Specifications (Official & Verified)

- **Name**: Cameron Harding
- **Profession**: Professional Male Model (Runway, Commercial, Editorial, Fitness, Swimwear)
- **Height**: 189 cm / 6'2.5"
- **Chest**: 42″ (106.5 cm)
- **Waist**: 34″ (86.3 cm)
- **Trouser**: 34″
- **Shoe**: UK 12 / EU 47
- **Collar**: 17″ (43 cm)
- **T-Shirt**: M / L Regular
- **Hair**: Black Curly
- **Eyes**: Brown
- **Location**: Yorkshire, United Kingdom (Available for UK & Worldwide travel)
- **Instagram**: [@Cameronharding11](https://instagram.com/Cameronharding11)
- **Direct Email**: [cameronhardingmodel@gmail.com](mailto:cameronhardingmodel@gmail.com)

---

## 📁 Repository & Project File Architecture

```
cameron_harding/
├── index.html                  # Main responsive web portfolio (references photos/web/)
├── portfolio_standalone.html   # 100% self-contained single-file edition (Base64 embedded images)
├── index_external.html         # Backup modular version
├── business_card.html          # Interactive 3D flippable credit card tool + @media print sheet
├── business_card_front.png     # 300 DPI high-res print file (1012 × 638 px, CR80 standard)
├── business_card_back.png      # 300 DPI high-res print file (1012 × 638 px, CR80 standard)
├── generate_card_images.py     # Python script (Pillow + qrcode) to regenerate card PNGs
├── fix_enquiry_form.py         # Script managing form submission & multi-channel modal
├── README.md                   # Public GitHub documentation with deployment guide
├── SESSION_SUMMARY.md          # Session restore guide for next assistant session
├── .gitignore                  # Ignores temp files (.bat, scratch data)
└── photos/                     # 38 original master photo files (~125 MB)
    └── web/                    # 38 web-optimized images (LANCZOS, max 1400px, ~6 MB)
        └── qr_code.png         # Scannable QR code pointing to https://cameron-harding.vercel.app/
```

---

## 🛠 Completed Features & Accomplishments

### 1. Web Portfolio (`index.html` & `portfolio_standalone.html`)
- **Primary Hero Portrait**: Set to `WhatsApp Image 2026-09-15 at 16.10.02.jpeg` with responsive dark gradient backdrop.
- **Filterable Gallery**: 38 photos categorized into *All*, *Runway & High Fashion*, *Commercial & Lifestyle*, *Fitness & Activewear*, and *Digitals & Polaroids*.
- **Interactive Lightbox Carousel**: Full-screen preview with Previous/Next controls, arrow keys (`←`/`→`/`Esc`), live counter (`X / 38`), and raw master downloads.
- **Unit Measurement Switcher**: Instant interactive toggle between Metric (cm/EU) and Imperial (in/UK).
- **Official Digital Comp Card**: Working modal with 4-photo composite sheet and `@media print` styling for 1-click PDF/print export.
- **Booking Enquiry Desk**:
  - Validates shoot parameters.
  - Multi-channel dispatch popup offering:
    1. 🚀 **Send via Gmail Web** (pre-fills Gmail in new tab).
    2. 📧 **Open Default Mail App** (native `mailto:` trigger).
    3. 📋 **Copy Brief to Clipboard** (1-click copy with toast notification).

### 2. Standalone Single-File Edition (`portfolio_standalone.html`)
- Completely self-contained file (10.62 MB).
- All 38 photos embedded as Base64 data URIs.
- Requires **zero external folders** or active internet connection; can be emailed as an attachment, sent via WhatsApp, or stored on a USB drive.

### 3. CR80 Credit Card Sized Model Business Card
- **Dimensions**: ISO/IEC 7810 ID-1 standard (85.60 mm × 53.98 mm / 3.37″ × 2.125″, 3.18 mm corner radius).
- **Front Side**:
  - Cropped lead portrait of Cameron to the left side with seamless gradient blend into luxury dark background.
  - Name: `CAMERON HARDING`.
  - Title: `MODEL` with category disciplines (`RUNWAY • COMMERCIAL • EDITORIAL • FITNESS`).
  - Globe icon in front of `cameron-harding.vercel.app/`.
  - Body measurements and location removed as requested for minimal luxury look.
- **Back Side**:
  - Prominent, enlarged high-contrast scannable QR code linking to Vercel site.
  - Box 1: `INSTAGRAM` → `@Cameronharding11` (properly padded, no text overflow).
  - Box 2: `DIRECT BOOKINGS & CASTING` → `cameronhardingmodel@gmail.com`.
  - Box 3: `WEBSITE` → 🌐 `cameron-harding.vercel.app/`.
  - Measurements removed for a clean, professional aesthetic.
- **Print Files**: High-resolution 300 DPI PNGs (`business_card_front.png` & `business_card_back.png`) ready for professional printers (Vistaprint, Moo, etc.).

---

## ⚡ Useful Terminal Commands

```powershell
# 1. Start local development server
python -m http.server 8080

# 2. Regenerate 300 DPI business card PNG files
python generate_card_images.py

# 3. Push new updates to GitHub and auto-deploy to Vercel
git add .
git commit -m "Your commit message"
git push
```

---

## 💡 Recommended Next Steps for Future Sessions
1. **Custom Domain**: Connect a domain like `cameronharding.com` via Vercel Project Settings → Domains.
2. **Video / Runway Showreel**: Embed a high-definition video reel if Cameron provides video clips.
3. **Analytics**: Enable Vercel Web Analytics or Google Analytics if traffic insights are desired.
