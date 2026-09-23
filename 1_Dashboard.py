import streamlit as st
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

image_path = os.path.join(ASSETS_DIR, "Owner.png")
cofounder = os.path.join(ASSETS_DIR, "co-founder.png")
cabang1 = os.path.join(ASSETS_DIR, "cabang1.png")
cabang2 = os.path.join(ASSETS_DIR, "cabang2.png")
cabang3 = os.path.join(ASSETS_DIR, "cabang3.png")
kopisusu = os.path.join(ASSETS_DIR, "kopisusu.png")
latte = os.path.join(ASSETS_DIR, "latte.png")
matcha = os.path.join(ASSETS_DIR, "matcha.png")
banner = os.path.join(ASSETS_DIR, "FUCKafe (1).png")

st.image(
    banner,
    use_container_width=True, # <--- INI KUNCINYA! Artinya: "Pakai lebar penuh wadahnya"
)

st.set_page_config(
    page_title="FUCKafe Home",
    page_icon="☕",
    layout="wide"
)

st.sidebar.success("Silakan pilih menu di atas.")

with st.container(border=True) :
    st.write("\n\n")
    st.write("\n\n")
    st.title("FUCKafe", text_alignment="center")
    st.write("‎ ‎ ‎ ‎ ‎ FUCKafe hadir bukan untuk sekadar menyuguhkan kafein dalam cangkir porselen cantik. Kami adalah 'tamparan' realitas yang kamu butuhkan saat dunia memaksamu bangun di pagi hari, dan pelukan tanpa syarat saat beban kerja mulai mencekik di malam hari. Di sini, kami tidak peduli dengan basa-basi korporat atau standar estetika yang melelahkan. Kami adalah benteng terakhir, sebuah tempat perlindungan dari segala omong kosong rutinitas duniawi yang mencoba merenggut kewarasanmu. Datanglah apa adanya, bicara apa adanya, dan biarkan kopi kami melakukan sisanya.")

    st.subheader("Pendiri FUCKafe: ")

    col1, col2 = st.columns(2)

    with col1 :
        st.image(image_path)

    with col2 :
        st.image(cofounder)

with st.container(border=True):
    data_lokasi = pd.DataFrame({
        'lat': [-6.2000, -6.2146, -6.1751],
        'lon': [106.8166, 106.8451, 106.8272],
        'nama_cabang': ['FUCKafe Pusat', 'FUCKafe Sudirman', 'FUCKafe Monas']
    })

    st.subheader("Lokasi FUCKafe: ")
    st.map(data_lokasi)

    col1, col2, col3 = st.columns(3)

    with col1 :
        st.image(cabang1, caption="Cabang pertama FUCKafe")
    with col2 :
        st.image(cabang2, caption="Cabang kedua FUCKafe")
    with col3 :
        st.image(cabang3, caption="Cabang ketiga FUCKafe")

with st.container(border=True):
    st.subheader("Produk kami: ")

    col_img, col_desc = st.columns([1, 2])

    with col_img:
        st.image(kopisusu, use_container_width=True)

    with col_desc:
        st.subheader("Kopi Susu")
        st.write("Fresh. Bold. Creamy. Kopi susu buat kamu yang gak punya waktu buat basa-basi. Espresso asli, susu murni, sedikit gula aren (karena kita tahu hidupmu udah cukup pahit). It’s just a f#cking good coffee.")

    col_img, col_desc = st.columns([1, 2])

    with col_img:
        st.image(latte, use_container_width=True)

    with col_desc:
        st.subheader("Latte")
        st.write("Kadang kamu cuma butuh ketenangan tanpa harus banyak bicara. Latte kami nggak butuh sirup warna-warni atau topping berlebihan buat kelihatan menarik. Cukup susu berkualitas dan kopi yang dipanggang dengan bener. Cocok buat kamu yang lagi ingin 'istirahat' sejenak dari segala drama, tapi tetap butuh asupan kafein buat lanjut bertempur. Smooth as f#ck.")

    col_img, col_desc = st.columns([1, 2])

    with col_img:
        st.image(matcha, use_container_width=True)

    with col_desc:
        st.subheader("Matcha")
        st.write("Di saat yang lain jual matcha yang isinya cuma gula dan krimer, kami kasih kamu yang asli. Warna hijaunya sepekat rasa iri orang-orang yang lihat kesuksesanmu. Ini adalah minuman buat kamu yang pengen tetep 'calm' tapi siap buat ngasih jari tengah ke segala masalah yang datang hari ini. Stay focused, stay f#cking cool.")
