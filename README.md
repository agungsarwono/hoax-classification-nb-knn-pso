# Komparasi Naive Bayes dan K-Nearest Neighbor Berbasis Particle Swarm Optimization untuk Klasifikasi Berita Hoaks Politik Berbahasa Indonesia

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Dataset: Indonesian Political Hoax News](https://img.shields.io/badge/Dataset-Kaggle_Political_Hoax-orange.svg)](https://www.kaggle.com/datasets/linkgish/indonesian-fact-and-hoax-political-news)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-green.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**Mata Kuliah:** Pemrograman Mobile Lanjut  
**Program Studi:** Teknik Informatika, Fakultas Sains dan Teknologi, Universitas Islam Nahdlatul Ulama (UNISNU) Jepara  
**Nama / NIM / Kelas:** _(isi)_  

---

## 1. Deskripsi Proyek

Proyek ini meneliti dan membandingkan performa dua algoritma klasifikasi teks fundamental, yaitu **Naive Bayes (NB)** dan **K-Nearest Neighbor (KNN)**, yang masing-masing dioptimasi menggunakan algoritma metaheuristik **Particle Swarm Optimization (PSO)** untuk mendeteksi berita hoaks politik berbahasa Indonesia pada dataset publik *Indonesian Fact and Hoax Political News*.

Dalam ekosistem pengembangan perangkat lunak modern, model pembelajaran mesin ringan dan efisien ini dirancang sebagai *core intelligence engine* yang dapat diintegrasikan ke dalam backend layanan aplikasi mobile (*mobile intelligent services*) guna memverifikasi keaslian narasi informasi secara cepat dan akurat.

Fokus utama penelitian meliputi:
- **Pengaruh Seleksi Fitur PSO terhadap Naive Bayes:** Reduksi dimensi vektor fitur TF-IDF untuk menghilangkan fitur kata yang redundan atau bising (*noise*).
- **Pengaruh Optimasi Simultan terhadap KNN:** Seleksi subset fitur TF-IDF sekaligus penentuan nilai tetangga terdekat ($k$) secara otomatis oleh partikel swarm.
- **Komparasi Model Berpasangan:** Evaluasi 4 konfigurasi model (NB, KNN, NB-PSO, KNN-PSO) dengan protokol evaluasi identik (*nested cross-validation*) guna mencegah kebocoran data (*data leakage*).
- **Pengujian Signifikansi Statistik:** Menguji apakah peningkatan metrik performa (*Accuracy, Precision, Recall, F1-Score, ROC-AUC*) terbukti signifikan secara statistik menggunakan uji *Paired t-test* dan *Wilcoxon Signed-Rank Test*.

Lembar jawaban dan dokumen tugas Bab III lengkap tersedia di:
- [`docs/SOAL_BAB_3.md`](docs/SOAL_BAB_3.md) – Butir soal resmi Bab III (Identifikasi Masalah & Studi Literatur).
- [`docs/TUGAS_BAB_3.md`](docs/TUGAS_BAB_3.md) – Lembar jawaban lengkap Soal 1 s.d. 6.
- [`docs/STATE_OF_THE_ART.md`](docs/STATE_OF_THE_ART.md) – Tabel sintesis 10 artikel penelitian terdahulu.
- [`docs/CATATAN_VERIFIKASI.md`](docs/CATATAN_VERIFIKASI.md) – Hasil verifikasi mandiri naskah artikel primer.

---

## 2. Struktur Folder Proyek

```text
hoax-classification-nb-knn-pso/
├── data/
│   ├── raw/                  # Dataset mentah asli (diunduh dari Kaggle, diabaikan oleh git)
│   └── processed/            # Data hasil pembersihan dan pra-pemrosesan teks
├── docs/
│   ├── SOAL_BAB_3.md         # Butir soal resmi latihan Bab III buku ajar
│   ├── TUGAS_BAB_3.md        # Lembar jawaban resmi Bab III (Soal 1 s.d. 6)
│   ├── STATE_OF_THE_ART.md   # Tabel perbandingan 10 artikel penelitian terdahulu
│   ├── CATATAN_VERIFIKASI.md # Catatan verifikasi outline terhadap artikel asli
│   ├── SETUP.md              # Panduan persiapan lingkungan pengembangan lokal
│   └── references.bib        # Koleksi referensi BibTeX (impor ke Zotero/Mendeley)
├── notebooks/                # Jupyter Notebook untuk Exploratory Data Analysis (EDA)
├── src/
│   ├── __init__.py
│   ├── data.py               # Modul pemuatan data, pembersihan teks, dan balancing
│   ├── pso.py                # Implementasi PSO untuk seleksi fitur dan optimasi K
│   ├── experiment.py         # Pipeline eksperimen utama (nested CV pada 4 model)
│   └── stats.py              # Pengujian signifikansi statistik (t-test, Wilcoxon, McNemar)
├── results/                  # Keluaran metrik evaluasi dan laporan signifikansi
├── .gitignore                # Berkas pengecualian Git
├── README.md                 # Dokumentasi utama proyek
├── requirements.txt          # Daftar pustaka dependensi Python
└── tugas.md                  # Checklist kemajuan pengerjaan tugas
```

---

## 3. Panduan Memulai

### 3.1 Prasyarat dan Instalasi Lingkungan
Pastikan Python 3.9+ telah terpasang pada komputer Anda:

```bash
# 1. Buat dan aktifkan virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 2. Perbarui pip dan pasang pustaka yang dibutuhkan
pip install --upgrade pip
pip install -r requirements.txt
```

### 3.2 Unduh Dataset
Dataset dapat diunduh langsung melalui Kaggle CLI atau manual dari web Kaggle:

```bash
kaggle datasets download -d linkgish/indonesian-fact-and-hoax-political-news -p data/raw --unzip
```

Setelah berkas CSV berada di dalam `data/raw/`, periksa dimensi dan struktur kolom dataset:
```bash
python -c "import pandas as pd, glob; f=glob.glob('data/raw/*.csv')[0]; d=pd.read_csv(f); print(f, d.shape, d.columns.tolist())"
```

### 3.3 Menjalankan Eksperimen Klasifikasi
Jalankan modul eksperimen untuk melatih keempat model dan menguji signifikansi statistik:

```bash
# Menjalankan pipeline eksperimen utama
python -m src.experiment --data data/raw/NAMA_FILE.csv --text-col text --label-col label --hoax-value hoax

# Menghitung uji signifikansi statistik selisih performa
python -m src.stats
```

Untuk pengujian cepat (*debug mode*), gunakan parameter subset:
```bash
python -m src.experiment --sample 1000 --folds 3 --particles 5 --iters 3
```

### 3.4 Integrasi Zotero / Mendeley
1. Buka aplikasi **Zotero** atau **Mendeley Desktop**.
2. Pilih menu **File > Import...**
3. Pilih berkas [`docs/references.bib`](docs/references.bib) untuk mengimpor seluruh metadata 10 artikel ilmiah primer.

---

## 4. Spesifikasi Dataset

| Atribut | Keterangan |
|---|---|
| **Nama Dataset** | Indonesian Fact and Hoax Political News |
| **Penyusun** | M. R. Rizqullah & R. H. Ghaida (2023) |
| **Sumber Data** | Kaggle (`linkgish/indonesian-fact-and-hoax-political-news`) |
| **Sumber Berita** | CNN Indonesia, Kompas, Tempo, dan TurnBackHoax (MAFINDO) |
| **Lisensi** | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| **Tanggal Akses** | 12 Oktober 2026 |
| **Kategori Masalah** | Klasifikasi Teks Biner (*Binary Text Classification*) |
| **Target Label** | `hoaks` vs `fakta/valid` |

---

## 5. Desain Protokol Eksperimen

1. **Pra-pemrosesan Teks:** Case folding, pembersihan tanda baca/angka/URL, penghapusan stopword bahasa Indonesia, dan ekstraksi fitur n-gram TF-IDF.
2. **Pencegahan Kebocoran Data (*No Data Leakage*):** Pembobotan TF-IDF dan seleksi fitur PSO hanya dilakukan pada data latih (*train fold*). Data uji (*test fold*) tidak pernah dilihat selama proses pencarian PSO.
3. **Optimasi PSO:** Swarm mengevaluasi partikel biner (masking fitur) untuk memaksimalkan fitness berupa rata-rata F1-Score kelas hoaks pada validasi silang internal.
4. **Metrik Evaluasi:** Accuracy, Precision, Recall, F1-Score, dan ROC-AUC.
5. **Uji Hipotesis Statistik:** Paired t-test, Wilcoxon signed-rank test, dan uji McNemar dengan batas signifikansi $\alpha = 0{,}05$.

---

## 6. Lisensi dan Etika Akademik

Kode sumber pada repositori ini dilisensikan untuk keperluan akademik dan penelitian di Program Studi Teknik Informatika UNISNU Jepara. Seluruh penggunaan data pihak ketiga tunduk pada ketentuan lisensi penyedia dataset di Kaggle. Seluruh referensi ilmiah telah diverifikasi langsung ke sumber aslinya guna memastikan integritas akademik bebas fabrikasi sitasi.
