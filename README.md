📌 Overview

Proyek ini merupakan implementasi dari Tugas Akhir berjudul
“Klasifikasi Citra Batuan Sedimen Klastik dan Nonklastik Menggunakan YOLOv8 sebagai Media Pembelajaran Digital”.
Sistem ini memanfaatkan model object detection YOLOv8 untuk mengklasifikasikan berbagai jenis batuan sedimen secara otomatis berdasarkan citra. Proyek ini dikembangkan untuk mendukung pembelajaran digital di bidang geologi, khususnya pengenalan jenis batuan sedimen secara cepat, interaktif, dan mudah dipahami.

🎯 Project Goals

Mengembangkan sistem klasifikasi gambar batuan sedimen berbasis deep learning.
Menyediakan media pembelajaran digital yang dapat membantu mahasiswa dan peneliti geologi.
Mendesain aplikasi berbasis Streamlit untuk visualisasi hasil klasifikasi secara real-time.
Menguji performa model YOLOv8 pada dataset besar dengan variasi jenis tekstur batuan.

🧠 Features

YOLOv8-based Image Classification
Model dilatih menggunakan ribuan citra batuan untuk mendeteksi dan mengklasifikasi kategori batuan sedimen.

Interactive Web App (Streamlit)
Pengguna dapat mengunggah banyak gambar sekaligus dan melihat hasil klasifikasi secara langsung.

Real-time Bounding Box Visualization
Output berupa citra dengan label dan probabilitas prediksi.

Custom Dataset (±3,000+ Images)
Dataset batuan mencakup berbagai kategori sedimen klastik dan nonklastik.

🗂 Dataset

Dataset terdiri dari ±3,000 citra batuan sedimen yang telah melalui proses:

Labeling & bounding box
Augmentasi
Normalisasi & preprocessing
Kategori klastik & nonklastik
Dataset disiapkan menggunakan Roboflow.

⚙️ Tech Stack

Python
YOLOv8 (Ultralytics)
Google Colab Pro
OpenCV
Streamlit
Roboflow

🚀 How It Works

Pengguna mengunggah gambar batuan ke aplikasi Streamlit.
Model YOLOv8 memproses gambar dan memprediksi jenis batuan.
Aplikasi menampilkan hasil klasifikasi dan confidence score.
Gambar hasil deteksi dapat dilihat secara individual atau batch.

📈 Model Performance

Model diuji menggunakan beberapa metrik:
mAP50
mAP50-95
Precision & Recall
Loss Graph (Train/Val)

![Image Alt](https://github.com/Rianmontilalu/Sedimentary-Rock-Classification-System-YOLOv8-based-/blob/a07f3066af753130575b2fe721de197aff60dadf/CodeTA/Backend%20%26%20User%20interface/Clastic%20stone.png)

![Image Alt](https://github.com/Rianmontilalu/Sedimentary-Rock-Classification-System-YOLOv8-based-/blob/b959601c9ee8e8f2098863412fbfe21af6469751/CodeTA/Backend%20%26%20User%20interface/Non-klastik.png)
