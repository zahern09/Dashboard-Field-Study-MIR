import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

import gspread
from google.oauth2.service_account import Credentials

st.markdown("""
    <style>
    /* Mengubah warna background dan border kotak jam */
    div[data-testid="stExpander"] {
        background-color: #f0f7ff; /* Warna background (biru muda lembut) */
        border: 1px solid #b3d7ff; /* Warna garis pinggir */
        border-radius: 8px;        /* Sudut membulat */
        margin-bottom: 10px;       /* Jarak antar kotak */
    }
    
    /* Mengubah warna teks judul jam saat hover (diarahkan kursor) */
    div[data-testid="stExpander"]:hover {
        border-color: #0066cc;
    }
    </style>
""", unsafe_allow_html=True)


# Konfigurasi Akses
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Membaca credentials dari Secrets di Streamlit Cloud
if "gcp_service_account" in st.secrets:
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
else:
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

client = gspread.authorize(creds)

# Buka Spreadsheet
SPREADSHEET_ID = "1TfD7gopVYJ-fksgvqF3S6zc-BbRxLmYv4M-eY93Jf7g"
sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Kebutuhan_Surat")

LOGO = "Logo MIR 26.jfif"
st.set_page_config(page_title="Dashboard Itinerary & Perizinan MIR UNPAD", page_icon = LOGO, layout="wide")

st.sidebar.image(LOGO, width = 120)
st.sidebar.title("Dashboard Itinerary Field Study MIR UNPAD")
menu = st.sidebar.radio(
    "Pilih Menu:", 
    ["Itinerary Hari ke Hari", "Estimasi Biaya", "Peta Destinasi", "📄 Ajukan Surat Izin"]
)

if menu == "Itinerary Hari ke Hari":
    st.title("📅 Itinerary Field Study MIR UNPAD 2026")
    tab1, tab2, tab3 = st.tabs([
        "Hari 1 (Jumat, 16 Oktober 2026): Keberangkatan", 
        "Hari 2 (Sabtu, 17 Oktober 2026): Agenda Utama",
        "Hari 3 (Minggu, 18 Oktober 2026): Kepulangan"
    ])
    
    with tab1:
        st.subheader("Hari 1 - Keberangkatan")
        with st.expander("14:00 - 14:30 | Kumpul di Kampus SPS & Briefing"):
            st.write("Titik kumpul di Lobby Utama SPS Dipatiukur. Akan dilakukan briefing singkat")
        with st.expander("14:30 - 17:00 | Perjalanan Bandung-Jakarta"):
            st.write("Perjalanan ke Jakarta via Tol menggunakan Hiace. Jemput tim di Jakarta")
        with st.expander("17:00 - 19:00 | Perjalanan Jakarta-Merak"):
            st.write("Perjalanan ke Merak via Tol, setelah itu makan malam di sekitar Merak")
        with st.expander("19:00 - 20:30 | Makan Malam"):
            st.write("Makan malam bersama di sekitar pelabuhan")
        with st.expander("20:30 - 21:00 | Check in Kapal"):
            st.write("Persiapan check in kapal tujuan Bakauhuni")
        with st.expander("21:00 - 22:30 | Perjalanan Merak-Bakauhuni"):
            st.write("Perjalanan ke Bakauhuni memakan waktu sekitar 1,5 jam")
        with st.expander("22:30 - 00:30 | Perjalanan Bakauhuni-Bandar Lampung"):
            st.write("Perjalanan ke Bandar Lampung memakan waktu sekitar 2 jam")
        with st.expander("00:30 - 01:00 | Check in Hotel dan Istirahat"):
            st.write("Check in dan istirahat")
            
    with tab2:
        st.subheader("Hari 2 - Acara Workshop")
        with st.expander("06:00 - 08:00 | Sarapan dan Keberangkatan ke tempat Kegiatan Field Study"):
            st.write("Sarapan dan Perjalanan menuju Sollaterra untuk kuliah lapangan sekaligus checkout dari hotel")
        with st.expander("08:00 - 12:00 | Kegiatan Field Study"):
            st.write("Berlangsungnya kuliah di Sollaterra")
        with st.expander("12:00 - 13:00 | Makan Siang"):
            st.write("Selesai kuliah akan ada jamuan makan siang dan ramah tamah")
        with st.expander("13:00 - 15:00 | Kunjungan ke ITERA dan UNILA"):
            st.write("Kegiatan field study ke beberapa kampus untuk promosi SPS")
        with st.expander("15:00 - 17:00 | Starlight Cabin (resort kedua)"):
            st.write("Perjalanan menuju resort kedua sembari beli oleh2 di tengah perjalanan dan check in")
        with st.expander("17:00 - 20:00 | Santai bersama"):
            st.write("Menikmati sunset dan main air di pantai")
        with st.expander("20:00 - 22:00 | Barbeque dan ramah tamah"):
            st.write("Makan malam dan keakraban")
        with st.expander("22:00 - Besok | Istirahat"):
            st.write("Istirahat")

    with tab3:
        st.subheader("Hari 3 - Kepulangan")
        with st.expander("06:00 - 08:00 | Sarapan dan Persiapan Check out"):
            st.write("Sarapan dan persiapan check out atau masih ada yang ingin menikmati sunrise dipersilahkan")
        with st.expander("08:00 - 11:00 | Check out"):
            st.write("Check out dari hotel dan persiapan menuju pelabuhan")
        with st.expander("11:00 - 13:00 | Makan Siang"):
            st.write("Makan Siang sekaligus check in kapal")
        with st.expander("13:00 - 14:30 | Perjalanan Bakauhuni - Merak"):
            st.write("Perjalanan ke Merak memakan waktu sekitar 1,5 jam")
        with st.expander("14:30 - 16:30 | Titik Turun di Jakarta"):
            st.write("Perjalanan menuju Jakarta sembari menurunkan tim yang di Jakarta")
        with st.expander("16:30 - 19:00 | Jakarta - Bandung"):
            st.write("Perjalanan menuju Bandung dan berakhirnya kegiatan turun lapang MIR 2026")

elif menu == "Estimasi Biaya":
    st.title("💰 Estimasi & Rincian Biaya")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Anggaran (RAB)", "Rp 17.750.000")
    col2.metric("Target Peserta", "10 Orang")
    col3.metric("Biaya per Orang", "Rp 1.972.222")
    
    st.divider()
    st.write("### Rincian Anggaran Perjalanan")
    rab_data = pd.DataFrame({
       "No": [1, 2, 3, 4, 5],
       "Kegiatan": [
            "Sewa Hiace (Pulang Pergi - 9 Pax)",
            "Hotel",
            "Tiket Kapal",
            "Makan",
            "Bensin"
        ],
        "Qty": [1, 6, 1, 10, 1],
        "x": ["x", "x", "x", "x", "x"],
        "Volume": [3, 2, 2, 4, 1],
        "Harga/Pax (Rp)": ["1.750.000", "500.000", "750.000", "100.000", "1.000.000"],
        "Total Harga (Rp)": ["5.250.000", "6.000.000", "1.500.000", "4.000.000", "1.000.000"]
    })
    st.dataframe(rab_data, use_container_width=True, hide_index = True, 
         column_config={
            "No": st.column_config.Column(alignment="center"),
            "Qty": st.column_config.Column(alignment="center"),
            "x": st.column_config.Column(alignment="center"),
            "Volume": st.column_config.Column(alignment="center")
    })
    st.write("---")
    col_a, col_b = st.columns([2,1])
    with col_b:
        st.markdown("**Total Keseluruhan:** `Rp 17.750.000`")
        st.markdown("**Biaya per orang:** `Rp 1.972.222`")

elif menu == "Peta Destinasi":
    st.title("🗺️ Peta Rute Perjalanan (Bandung - Merak - Lampung)")
    
    # Fokus peta di pertengahan rute (Selat Sunda / Banten)
    m = folium.Map(location=[-5.85, 105.75], zoom_start=8)
    
    # Menambahkan Marker Rute
    folium.Marker([-6.8915, 107.6107], popup="Start: Kampus SPS UNPAD Dipatiukur", tooltip="Start: Bandung", icon=folium.Icon(color="red")).add_to(m)
    folium.Marker([-5.9322, 105.9982], popup="Pelabuhan Merak", tooltip="Pelabuhan Merak", icon=folium.Icon(color="orange")).add_to(m)
    folium.Marker([-5.8703, 105.7523], popup="Pelabuhan Bakauhuni", tooltip="Pelabuhan Bakauhuni", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker([-5.4292, 105.2625], popup="Tujuan: Bandar Lampung", tooltip="Hotel / Lampung", icon=folium.Icon(color="green")).add_to(m)
    
    st_folium(m, width=900, height=500)

elif menu == "📄 Ajukan Surat Izin":
    st.markdown("<h1 style='text-align: center;'>📄 Form Pengajuan Surat Izin</h1>", unsafe_allow_html=True)
    st.write("Isi data di bawah ini untuk mengajukan surat izin instansi/kantor")
    conn = st.connection("gsheets", type = GSheetsConnection)
    with st.form("form_surat_izin", clear_on_submit = True):
        Nama_Lengkap = st.text_input("Nama Lengkap *")
        Tujuan_Surat = st.text_input("Tujuan Surat *")
        st.caption("📌 *Tuliskan nama perusahaan/instansi resmi yang dituju.*")
        submitted = st.form_submit_button("Generate Surat Izin")
        
    if submitted:
        if not Nama_Lengkap or not Tujuan_Surat:
            st.error("Mohon isi semua kolom bertanda *!")
        else:
            try:
                # Read data eksis dari tab "Kebutuhan Surat"
                records = sheet.get_all_records()
                next_no = len(records) + 1
            
                sheet.append_row([next_no, Nama_Lengkap, Tujuan_Surat])
            
                st.success(f"Berhasil! Data {Nama_Lengkap} telah tersimpan di Google Sheets.")

            except Exception as e:
                st.error(f"Gagal menyimpan data: {e}")