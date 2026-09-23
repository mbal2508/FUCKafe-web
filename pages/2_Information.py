import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
import os

st.title("📊Informasi FUCKafe", text_alignment="left")
st.sidebar.success("Silakan pilih menu di atas.")
st.set_page_config(
    page_title="Information",
    page_icon="☕",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

excel_kandungan_dalam_produk = os.path.join(ASSETS_DIR, "Rancangan Data Excel untuk Streamlit.xlsx")

df = pd.read_excel(excel_kandungan_dalam_produk)

nama_menu = df["Menu"]
persenan_kopi = df["Kopi"]
persenan_susu = df["Susu"]
persenan_gula = df["Gula"]
persenan_matcha = df["Matcha"]
kopisusu = "Kopi Susu"
latte = "Latte"
matcha = "Matcha"

st.write("\n\n")
st.write("\n\n")
with st.container(border=True) :
    st.header("Kandungan dalam produk", text_alignment="center")

    col1, col2, col3 = st.columns(3)
    warna = ["darkgreen","orange", "navy"]

    with col1 :

        categories = ["kopi (%)", "susu (%)", "gula (%)"]
        values = np.array([persenan_kopi.iloc[0], persenan_susu.iloc[0], persenan_gula.iloc[0]])

        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie(values, labels=categories, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title(kopisusu, color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

    with col2 :

        categories = ["kopi (%)", "susu (%)", "gula (%)"]
        values = np.array([persenan_kopi.iloc[1], persenan_susu.iloc[1], persenan_gula.iloc[1]])

        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie(values, labels=categories, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title(latte, color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

    with col3 :

        categories = ["Matcha (%)", "susu (%)", "gula (%)"]
        values = np.array([
        persenan_matcha.iloc[-1],
        persenan_susu.iloc[-1],
        persenan_gula.iloc[-1]
    ])

        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie(values, labels=categories, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title(matcha, color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

with st.container(border=True) :

    excel_penjualan = os.path.join(ASSETS_DIR, "penjualan.xlsx")
    df_penjualan = pd.read_excel(excel_penjualan)

    penjualan_terbanyak = df_penjualan["Terjual"].idxmax()
    best_seller = df_penjualan.loc[penjualan_terbanyak, "Menu"]

    total_penjualan_kopsu = df_penjualan["Terjual"].iloc[0]
    total_penjualan_latte = df_penjualan["Terjual"].iloc[1]
    total_penjualan_matcha = df_penjualan["Terjual"].iloc[2]
    total_penjualan = total_penjualan_kopsu + total_penjualan_latte + total_penjualan_matcha

    persenan_penjualan_kopsu = total_penjualan_kopsu * 100 // total_penjualan
    persenan_penjualan_latte = total_penjualan_latte * 100 // total_penjualan
    persenan_penjualan_matcha = total_penjualan_matcha * 100 // total_penjualan

    st.header("Tentukan Pilihan Mu", text_alignment="center")

    col1, col2, col3 = st.columns(3)

    with col1 :
        st.subheader(f"{persenan_penjualan_kopsu}% orang memilih Kopi Susu", text_alignment="center")
    with col2 :
        st.subheader(f"{persenan_penjualan_latte}% orang memilih Latte", text_alignment="center")
    with col3 :
        st.subheader(f"{persenan_penjualan_matcha}% orang memilih Matcha", text_alignment="center")

    st.write("\n\n")
    st.subheader(f"{best_seller} masih menjadi favorit sebagian besar konsumen kami..", text_alignment="center")
    st.write("\n\n")
    st.write("\n\n")

with st.container(border=True):

    excel_keramaian_cabang1 = os.path.join(ASSETS_DIR, "keramaian cabang1.xlsx")
    excel_keramaian_cabang2 = os.path.join(ASSETS_DIR, "keramaian cabang2.xlsx")
    excel_keramaian_cabang3 = os.path.join(ASSETS_DIR, "keramaian cabang3.xlsx")

    df_keramaian_cabang1 = pd.read_excel(excel_keramaian_cabang1)
    df_keramaian_cabang2 = pd.read_excel(excel_keramaian_cabang2)
    df_keramaian_cabang3 = pd.read_excel(excel_keramaian_cabang3)

    persenan_keramaian_cabang1 = df_keramaian_cabang1["keramaian"]
    persenan_keramaian_cabang2 = df_keramaian_cabang2["keramaian"]
    persenan_keramaian_cabang3 = df_keramaian_cabang3["keramaian"]

    hari_ini = datetime.now().strftime("%A")
    # hari_ini = "Friday"

    hari_index = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    idx = hari_index.get(hari_ini, 0)

    keramaian1 = int(persenan_keramaian_cabang1.iloc[idx])
    keramaian2 = int(persenan_keramaian_cabang2.iloc[idx])
    keramaian3 = int(persenan_keramaian_cabang3.iloc[idx])

    bangku_kosong1 = 100 - keramaian1
    bangku_kosong2 = 100 - keramaian2
    bangku_kosong3 = 100 - keramaian3

    st.header("Keadaan Tiap Cabang Hari Ini", text_alignment="center")

    col1, col2, col3 = st.columns(3)

    kategori = ["Bangku Terisi", "Bangku Kosong"]
    warna = ["orange","grey"]

    with col1:
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie([keramaian1, bangku_kosong1], labels=kategori, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title("Cabang 1", color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie([keramaian2, bangku_kosong2], labels=kategori, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title("Cabang 2", color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

    with col3:
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.pie([keramaian3, bangku_kosong3], labels=kategori, autopct="%1.0f%%", colors=warna, textprops={'color':"white"})
        ax.set_title("Cabang 3", color="white")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

    col1, col2, col3 = st.columns(3)

    with col1 :
        if 20 < keramaian1 <= 40 :
            kondisi = "Sepi"
        if 40 < keramaian1 <= 60 :
            kondisi = "Cukup Ramai"
        if keramaian1 > 60 :
            kondisi = "Sangat Ramai"
        if keramaian1 <= 20 :
            kondisi = "Sangat sepi"
        
        st.subheader(f"Kondisi: {kondisi}")

    with col2 :
        if 20 < keramaian2 <= 40 :
            kondisi = "Sepi"
        if 40 < keramaian2 <= 60 :
            kondisi = "Cukup Ramai"
        if keramaian2 > 60 :
            kondisi = "Sangat Ramai"
        if keramaian2 <= 20 :
            kondisi = "Sangat sepi"
        
        st.subheader(f"Kondisi: {kondisi}")

    with col3 :
        if 20 < keramaian3 <= 40 :
            kondisi = "Sepi"
        if 40 < keramaian3 <= 60 :
            kondisi = "Cukup Ramai"
        if keramaian3 > 60 :
            kondisi = "Sangat Ramai"
        if keramaian3 <= 20 :
            kondisi = "Sangat sepi"
        
        st.subheader(f"Kondisi: {kondisi}")

with st.container(border=True):
    st.header("Data member FUCKafe", text_alignment="center")

    data_list_member = os.path.join(ASSETS_DIR, "list_member.csv")

    df_list_member = pd.read_csv(data_list_member, sep=';')

    level_member = df_list_member[df_list_member["level_member"] == "Gold"]
    member_tertinggi = " dan ".join(level_member['nama'].tolist())

    st.write(df_list_member)

    st.subheader(f"Member dengan level tertinggi: {member_tertinggi}")