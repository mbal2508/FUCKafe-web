import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="Order",
                   layout="wide", )


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

file_path = os.path.join(ASSETS_DIR, "menu.xlsx")
kopisusu = os.path.join(ASSETS_DIR, "kopisusu.png")
latte = os.path.join(ASSETS_DIR, "latte.png")
matcha = os.path.join(ASSETS_DIR, "matcha.png")

df = pd.read_excel(file_path)


st.title("📠Masukan Pesanan Anda...")
st.sidebar.success("Silakan pilih menu di atas.")
with st.container(border=True):
    st.header("Pesanan", text_alignment="center")
    nama = st.text_input("Masukan nama anda: ")

    col1, col2 = st.columns(2)
    cara_bayar = ["Gopay", "Paypal", "Dana", "Paylater"]

    with col1:
        list_menu = df['Menu'].tolist()
        pilihan = st.selectbox("Pilih Menu:", list_menu)
        berapa = st.number_input("Berapa: ", min_value=1)
        
        harga_item = df[df['Menu'] == pilihan]['Harga'].values[0]
        total_pesanan = harga_item * berapa
        st.write(f"Kamu memilih: {berapa} {pilihan} Rp. {total_pesanan:,}")

    with col2 :
        if pilihan == "Kopi Susu" :
            st.image(kopisusu)
        elif pilihan == "Latte" :
            st.image(latte)
        elif pilihan == "Matcha" :
            st.image(matcha)

nama_kota = ["Bandung", "Bogor", "Depok", "Bekasi", "Tanggerang"]
mapping_daerah = {
    "Bandung": ["Kiaracondong", "Gedebage", "Buahbatu"],
    "Bogor": ["Jonggol", "Baranangsiang", "Batutulis"],
    "Depok": ["Beji", "Sawangan", "Cinere"],
    "Bekasi": ["Jatiluhur", "Bantar Gebang", "Menteng"],
    "Tanggerang": ["Ciledug", "Ciputat", "Balaraja"]
}
data_kordinat = {
    'Bandung': {'lat': -6.9175, 'lon': 107.6191},
    'Bogor': {'lat': -6.5971, 'lon': 106.8060},
    'Depok': {'lat': -6.4025, 'lon': 106.7942},
    'Bekasi': {'lat': -6.2383, 'lon': 106.9756},
    'Tanggerang': {'lat': -6.1783, 'lon': 106.6319} # Pastikan ejaan sama dengan nama_kota
}
pengiriman = ["Gosend", "Ambil di Toko", "Jnt", "FUCKafe Delivery(Termurah)"]

ongkir = {
     "Gosend": 22000,
     "Ambil di Toko": 0,
     "Jnt": 18000,
     "FUCKafe Delivery(Termurah)": 11000
}

with st.container(border=True):
     st.header("Lokasi Anda", text_alignment="center")

     col1, col2 = st.columns(2)

     with col1:
            kota = st.selectbox("Masukan Kota: ", nama_kota)
            daerah = st.selectbox(f"{kota} bagian mana: ", mapping_daerah[kota])
            metode_pengiriman = st.selectbox("Metode Pengiriman: ", pengiriman)
            st.write(f"Ongkir: Rp.{ongkir[metode_pengiriman]:,}")

     with col2:
        posisi = data_kordinat[kota]
        
        df_lokasi_tunggal = pd.DataFrame({
            'lat': [posisi['lat']],
            'lon': [posisi['lon']]
        })
        st.map(df_lokasi_tunggal, zoom=11, height=250)

with st.container(border=True):
    st.header("Pembayaran", text_alignment="center")
    total_harga = total_pesanan + ongkir[metode_pengiriman]
    st.subheader(f"Total pesanan Anda: Rp.{total_harga:,}")
    metode_pembayaran = st.selectbox("Metode pembayaran: ", cara_bayar)
    if metode_pembayaran == "Paylater" :
            nomor_app = st.text_input(f"Masukan nomor {metode_pembayaran} anda: ")
            bulan_bayar = st.number_input("Berapa bulan: ", min_value=1, max_value=12)
            bayar_per_bulan = total_pesanan // bulan_bayar
            st.write(f"Pembayaran per-bulan: Rp. {bayar_per_bulan:,}")
    elif metode_pembayaran == "Gopay" :
            nomor_app = st.text_input(f"Masukan nomor {metode_pembayaran} anda: ")
    elif metode_pembayaran == "Dana" :
            nomor_app = st.text_input(f"Masukan nomor {metode_pembayaran} anda: ")
    elif metode_pembayaran == "Paypal" :
            nomor_app = st.text_input(f"Masukan nomor {metode_pembayaran} anda: ")
        
    if st.button("Bayar sekarang") :
            if not nomor_app.isnumeric() or nama == "" :
                st.warning(f"Pastikan anda telah mengisi nama dan nomor anda terlebih dahulu, dan nomor hanya bisa diisi dengan angka ..")
            
                status_text = st.empty()

            elif nomor_app.isnumeric() and nama != "" or bulan_bayar != 0 :
                
                status_text = st.empty()
                # 2. Mulai Spinner
                with st.spinner("Menghubungkan ke server..."):
                    # Update teks di dalam placeholder
                    status_text.text("⏳ Sedang memproses...") 
                    time.sleep(2)
                    
                    status_text.text("✅ Data terverifikasi...")
                    time.sleep(1)

                    # 3. Hapus teks status tadi dan ganti dengan pesan sukses permanen
                    status_text.empty() 
                    st.success(f"Pembayaran Berhasil, {nama}!")