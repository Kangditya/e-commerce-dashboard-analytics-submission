# 📊 Proyek Analisis Data E-Commerce

Proyek ini merupakan bagian dari submission kelas Analisis Data.  
Dashboard interaktif dibuat menggunakan Streamlit untuk menjawab pertanyaan bisnis berdasarkan dataset transaksi e-commerce.

---

## 🎯 Tujuan Proyek

Menganalisis performa bisnis e-commerce berdasarkan data transaksi dan pelanggan untuk menghasilkan insight yang dapat membantu pengambilan keputusan.

---

## ❓ Pertanyaan Bisnis

1. Bagaimana tren penjualan (jumlah transaksi dan revenue) dari waktu ke waktu?
2. Wilayah mana yang memiliki jumlah pelanggan dan transaksi tertinggi?

---

## 📈 Insight Utama

### 1️⃣ Tren Penjualan
- Terdapat fluktuasi jumlah transaksi setiap bulan.
- Pada periode tertentu terjadi peningkatan signifikan yang mengindikasikan pola musiman.
- Revenue cenderung mengikuti pola jumlah transaksi.

### 2️⃣ Analisis Wilayah
- Wilayah metropolitan mendominasi jumlah pelanggan dan transaksi.
- Konsentrasi pasar e-commerce lebih kuat di area urban dibandingkan rural.
- Wilayah dengan pelanggan tinggi juga menunjukkan volume transaksi tinggi.

---

## 🖥️ Dashboard Preview

Dashboard menampilkan:

- KPI (Total Orders, Total Revenue, Total Customers)
- Grafik tren transaksi bulanan
- Grafik tren revenue bulanan
- Top 10 wilayah berdasarkan jumlah pelanggan
- Top 10 wilayah berdasarkan jumlah transaksi
- Filter rentang tanggal interaktif

---

## 🛠️ Tools & Library

- Python
- Pandas
- Matplotlib
- Streamlit

---

## 📂 Struktur Folder

```
submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```
---

## ▶️ Cara Menjalankan Dashboard Secara Lokal

1. Masuk ke folder dashboard:

```

cd dashboard

```

2. Jalankan Streamlit:

```

streamlit run dashboard.py

```

3. Dashboard akan terbuka otomatis di browser.

---

## 🌐 Akses Dashboard Online

Link deployment Streamlit Cloud tersedia pada file:

```

url.txt

```

---

## 📌 Catatan

- Dataset yang digunakan merupakan data transaksi e-commerce yang telah dibersihkan dan digabungkan menjadi `main_data.csv`.
- Dashboard dibuat dalam satu file (`dashboard.py`) sesuai ketentuan submission.
- Tidak terdapat folder atau file tambahan di luar struktur yang ditentukan.

---

## 👤 Author

Aditya Nur'ahya  
Proyek Submission Analisis Data
