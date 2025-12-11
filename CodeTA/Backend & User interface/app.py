# app.py
import streamlit as st
from backend import detect_image
from PIL import Image
import numpy as np

st.set_page_config(page_title="Klasifikasi Batuan Sedimen Klastik", layout="wide")
st.title("🪨 Sistem Klasifikasi Batuan Sedimen Klastik dengan YOLOv8")

uploaded_file = st.file_uploader("Unggah Gambar Batuan Sedimen", type=["jpg", "jpeg", "png"])
show_original = st.checkbox("Tampilkan Gambar Asli", value=True)

if uploaded_file is not None:
    with st.spinner("🔍 Mendeteksi jenis batuan..."):
        result_img, labels = detect_image(uploaded_file)

    # Label header statis 
    st.markdown("""
    <div style='display: flex; justify-content: space-between; font-size: 24px; font-weight: bold; margin-bottom: 10px;'>
        <div>📷 Gambar Asli</div>
        <div>🔎 Hasil Klasifikasi YOLOv8</div>
        <div>📋 Jenis Batuan Terdeteksi</div>
    </div>
    """, unsafe_allow_html=True)

    # 3 kolom isi gambar dan hasil deteksi
    col1, col2, col3 = st.columns(3)

    with col1:
        if show_original:
            st.image(uploaded_file, use_container_width=True)
        else:
            st.info("Gambar asli disembunyikan.")

    with col2:
        st.image(result_img, use_container_width=True)

    with col3:
        if labels:
            for i, label in enumerate(labels, 1):
                st.markdown(
                    f"<p style='font-size:34px; font-weight:bold;'>{i}. {label}</p>",
                    unsafe_allow_html=True
                )
        else:
            st.warning("Tidak ada jenis batuan yang terdeteksi.")
else:
    st.info("Silakan unggah gambar terlebih dahulu.")
