import streamlit as st
from pathlib import Path
from base64 import b64encode

st.set_page_config(page_title="CIDB Dashboard Hub", layout="wide")

# ---------- paths ----------
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"


# ---------- UI helpers ----------
def render_hover_image(img_path: Path, url: str, label: str = "🚀 Open dashboard"):
    """
    Render an image preview that shows a clickable overlay on hover.
    Uses base64 so it works reliably on Streamlit Cloud with local repo images.
    """
    img_bytes = img_path.read_bytes()
    img_b64 = b64encode(img_bytes).decode("utf-8")

    st.markdown(
        f"""
        <a href="{url}" target="_blank" style="text-decoration:none;">
          <div class="preview-wrapper" role="button" aria-label="{label}">
            <img src="data:image/png;base64,{img_b64}" />
            <div class="preview-overlay">
              <div class="preview-btn">{label}</div>
            </div>
          </div>
        </a>
        """,
        unsafe_allow_html=True
    )


def dashboard_card(tag: str, title: str, bullets: list[str], url: str, image_file: str | None = None):
    # Top card (text)
    st.markdown(
        f"""
        <div class="card">
          <div class="badge">{tag}</div>
          <h4>{title}</h4>
          <div class="bullets">
            {''.join([f'<div class="b">• {b}</div>' for b in bullets])}
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Image preview with hover overlay
    if image_file:
        img_path = ASSETS_DIR / image_file
        if img_path.exists():
            render_hover_image(img_path, url, "🚀 Open dashboard")
        else:
            st.warning(f"Preview image not found: assets/{image_file}")

    # Fallback button (still useful on mobile / accessibility)
    st.link_button("🚀 Open dashboard", url, use_container_width=True)


# ---------- CSS ----------
st.markdown(
    """
<style>
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, #F9F6FF 0%, #FFFFFF 100%) !important;
  background-attachment: fixed !important;
}

/* header */
.hub-title{
  font-size: 2.1rem;
  font-weight: 900;
  margin-bottom: 0.2rem;
}
.hub-sub{
  color: rgba(17,24,39,0.70);
  margin-bottom: 1.0rem;
}

/* info card */
.card{
  background: white;
  border: 1px solid rgba(167,139,250,0.35);
  border-radius: 18px;
  padding: 16px 16px 12px 16px;
  box-shadow: 0 10px 22px rgba(17,24,39,0.06);
  margin-bottom: 10px;
}
.card h4{
  margin: 6px 0 8px 0;
  font-size: 1.35rem;
  font-weight: 900;
  color: #111827;
}
.badge{
  display:inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(167,139,250,0.18);
  border: 1px solid rgba(167,139,250,0.35);
  font-size: 12px;
  margin-bottom: 6px;
}
.bullets .b{
  margin: 0 0 6px 0;
  color: rgba(17,24,39,0.75);
  font-size: 0.95rem;
}

/* ===== Hover preview effect ===== */
.preview-wrapper{
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(17,24,39,0.06);
  box-shadow: 0 10px 22px rgba(17,24,39,0.06);
  margin-bottom: 10px;
}
.preview-wrapper img{
  display: block;
  width: 100%;
  height: auto;
  transition: transform 0.35s ease;
}
.preview-wrapper:hover img{
  transform: scale(1.03);
}
.preview-overlay{
  position: absolute;
  inset: 0;
  background: rgba(17,24,39,0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.35s ease;
}
.preview-wrapper:hover .preview-overlay{
  opacity: 1;
}
.preview-btn{
  background: #7C3AED;
  color: white;
  padding: 12px 18px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 15px;
  text-decoration: none;
}
.preview-btn:hover{
  background: #6D28D9;
}
</style>
""",
    unsafe_allow_html=True
)

# ---------- header ----------
st.markdown('<div class="hub-title">CIDB Dashboard Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="hub-sub">Quick access to key dashboards (hover the preview to open).</div>', unsafe_allow_html=True)

# ---------- dashboard list ----------
dashboards = [
    {
        "title": "Dashboard Pendahuluan CIDB",
        "bullets": [
            "Ringkasan tunggakan pendahuluan diri & bekalan mengikut PTJ",
            "Terus nampak baki & fokus tindakan"
        ],
        "tag": "Finance",
        "url": "https://dashboard-pendahuluancidb.streamlit.app/",
        "img": "pendahuluan.png"
    },
    {
        "title": "Dashboard Aset (SAP vs Easset)",
        "bullets": [
            "Aset tidak sepadan antara SAP & Easset (missing / mismatch)",
            "Semak isu lokasi & klasifikasi dengan cepat"
        ],
        "tag": "Asset",
        "url": "https://dashboard-aset-sap-vs-easset.streamlit.app/",
        "img": "aset.png"
    },
    {
        "title": "Tunggakan Pesanan Tempatan",
        "bullets": [
            "Jumlah & nilai PO tertunggak (RM) terkini",
            "Kenal pasti PTJ/vendor yang perlu tindakan"
        ],
        "tag": "Procurement / Closing",
        "url": "https://dashboard-tunggakan-pesanan-tempatan-cidb.streamlit.app/",
        "img": "tunggakan.png"
    },
    {
        "title": "Senarai Pesanan Tempatan Cawangan & Perlis",
        "bullets": [
            "Trend pengeluaran PO ikut tahun (2023–2025)",
            "Banding prestasi cawangan & Perlis dalam satu paparan"
        ],
        "tag": "Usul MBJ",
        "url": "https://senaraipesanantempatan.streamlit.app/",
        "img": "senarai_po.png"
    },
]

# ---------- search ----------
q = st.text_input("🔎 Search dashboard", placeholder="Type: aset / tunggakan / pesanan / pendahuluan ...")
if q:
    ql = q.lower()
    dashboards = [
        d for d in dashboards
        if ql in (d["title"] + " " + " ".join(d["bullets"]) + " " + d["tag"]).lower()
    ]

# ---------- render ----------
cols = st.columns(2, gap="large")
for i, d in enumerate(dashboards):
    with cols[i % 2]:
        dashboard_card(
            tag=d["tag"],
            title=d["title"],
            bullets=d["bullets"],
            url=d["url"],
            image_file=d.get("img")
        )

st.markdown("---")
st.caption("Tip: Share this hub link to PTJ. Replace images in /assets anytime to update previews.")
