import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CIDB Dashboard Hub", layout="wide")

# ---------- helpers ----------
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

def img_exists(rel_path: str) -> bool:
    return (ASSETS_DIR / rel_path).exists()

def dashboard_card(tag, title, bullets, url, image_file=None):
    st.markdown(f"""
    <div class="card">
      <div class="badge">{tag}</div>
      <h4>{title}</h4>
      <div class="bullets">
        {''.join([f'<div class="b">• {b}</div>' for b in bullets])}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Glimpse image (if available)
    if image_file:
        img_path = ASSETS_DIR / image_file
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)
        else:
            st.info(f"Preview image not found: assets/{image_file}")

    st.link_button("🚀 Open dashboard", url, use_container_width=True)


# ---------- CSS ----------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, #F9F6FF 0%, #FFFFFF 100%) !important;
  background-attachment: fixed !important;
}
.hub-title{
  font-size: 2.1rem;
  font-weight: 900;
  margin-bottom: 0.2rem;
}
.hub-sub{
  color: rgba(17,24,39,0.70);
  margin-bottom: 1.0rem;
}

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

/* Make preview images look like "glimpse cards" */
img{
  border-radius: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- header ----------
st.markdown('<div class="hub-title">CIDB Dashboard Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="hub-sub">Quick access to your key dashboards (with previews).</div>', unsafe_allow_html=True)

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
    dashboards = [
        d for d in dashboards
        if q.lower() in (d["title"] + " " + " ".join(d["bullets"]) + " " + d["tag"]).lower()
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
st.caption("Tip: Share this hub link to PTJ. Update previews anytime by replacing images in /assets.")
