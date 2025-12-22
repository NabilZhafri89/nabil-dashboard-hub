import streamlit as st

st.set_page_config(page_title="CIDB Dashboard Hub", layout="wide")

# ====== SIMPLE CLEAN CSS (card boxes) ======
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, #F9F6FF 0%, #FFFFFF 100%) !important;
  background-attachment: fixed !important;
}
.hub-title{
  font-size: 2.0rem;
  font-weight: 800;
  margin-bottom: 0.1rem;
}
.hub-sub{
  color: rgba(17,24,39,0.7);
  margin-bottom: 1.2rem;
}
.card{
  background: white;
  border: 1px solid rgba(167,139,250,0.35);
  border-radius: 16px;
  padding: 16px 16px 14px 16px;
  box-shadow: 0 10px 20px rgba(17,24,39,0.06);
  min-height: 160px;
}
.card h4{ margin: 0 0 6px 0; }
.card p{ margin: 0 0 12px 0; color: rgba(17,24,39,0.72); font-size: 0.95rem; }
.badge{
  display:inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(167,139,250,0.18);
  border: 1px solid rgba(167,139,250,0.35);
  font-size: 12px;
  margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hub-title">📌 CIDB Dashboard Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="hub-sub">One page to access all your Streamlit dashboards.</div>', unsafe_allow_html=True)

dashboards = [
    {
        "title": "Dashboard Pendahuluan CIDB",
        "desc": "Pendahuluan / monitoring (hubungan kepada proses kewangan).",
        "tag": "Finance",
        "url": "https://dashboard-pendahuluancidb.streamlit.app/"
    },
    {
        "title": "Dashboard Aset (SAP vs Easset)",
        "desc": "Semakan & reconciliation aset SAP vs Easset.",
        "tag": "Asset",
        "url": "https://dashboard-aset-sap-vs-easset.streamlit.app/"
    },
    {
        "title": "Tunggakan Pesanan Tempatan",
        "desc": "Laporan tunggakan PO/PL & tindakan susulan PTJ.",
        "tag": "Procurement",
        "url": "https://dashboard-tunggakan-pesanan-tempatan-cidb.streamlit.app/"
    },
    {
        "title": "Senarai Pesanan Tempatan",
        "desc": "Senarai pengeluaran pesanan tempatan (listing & semakan).",
        "tag": "Listing",
        "url": "https://senaraipesanantempatan.streamlit.app/"
    },
]

# Optional: search
q = st.text_input("🔎 Search dashboard", placeholder="Type: aset / tunggakan / pesanan / pendahuluan ...")
if q:
    dashboards = [d for d in dashboards if q.lower() in (d["title"] + " " + d["desc"] + " " + d["tag"]).lower()]

# Layout cards
cols = st.columns(2, gap="large")
for i, d in enumerate(dashboards):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
          <div class="badge">{d["tag"]}</div>
          <h4>{d["title"]}</h4>
          <p>{d["desc"]}</p>
        </div>
        """, unsafe_allow_html=True)

        # Streamlit button that opens link
        st.link_button("🚀 Open dashboard", d["url"], use_container_width=True)

st.markdown("---")
st.caption("Tip: set this app as your “main link” and share it to PTJ. You can update links anytime.")
