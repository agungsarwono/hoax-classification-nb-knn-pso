# Checklist Tugas – Pemrograman Mobile Lanjut

**Topik:** Komparasi Naive Bayes dan K-Nearest Neighbor Berbasis Particle Swarm Optimization untuk Klasifikasi Berita Hoaks Politik Berbahasa Indonesia  
**Program Studi:** Teknik Informatika, FST, UNISNU Jepara  
**Dokumen Acuan:** [`docs/SOAL_BAB_3.md`](docs/SOAL_BAB_3.md) & [`docs/TUGAS_BAB_3.md`](docs/TUGAS_BAB_3.md)

---

### Progres Pengerjaan Tugas

- [x] **1. Pemilihan dan Dokumentasi Dataset Publik**
  - [x] Dataset dipilih: *Indonesian Fact and Hoax Political News* (Kaggle)
  - [x] Sumber, lisensi (CC BY-SA 4.0), dan tanggal akses dicatat di `README.md` dan `docs/TUGAS_BAB_3.md`
  - [x] Variabel target biner (`hoaks` vs `fakta/valid`) diidentifikasi
  - [ ] Pengunduhan dataset mentah ke `data/raw/` dan penghitungan jumlah baris per kelas secara langsung (`df['label'].value_counts()`)

- [x] **2. Persiapan Lingkungan Pengembangan Lokal**
  - [x] Panduan instalasi disusun di [`docs/SETUP.md`](docs/SETUP.md)
  - [x] Daftar pustaka dependensi dicatat di [`requirements.txt`](requirements.txt)
  - [ ] Pembuatan virtual environment lokal (`.venv`) dan `pip install -r requirements.txt`

- [x] **3. Penentuan Topik Proyek/Penelitian**
  - [x] Topik: Klasifikasi Berita Hoaks Politik Berbahasa Indonesia Berbasis Machine Learning dan Optimasi Heuristik (relevan untuk backend layanan cerdas mobile)

- [x] **4. Perumusan Judul Penelitian**
  - [x] Judul: *Komparasi Naive Bayes dan K-Nearest Neighbor Berbasis Particle Swarm Optimization untuk Klasifikasi Berita Hoaks Politik Berbahasa Indonesia*

- [x] **5. Perumusan Pertanyaan Penelitian & Hipotesis**
  - [x] 3 Pertanyaan Penelitian (RQ1, RQ2, RQ3) dirumuskan
  - [x] 3 Hipotesis statistik teruji ($\alpha = 0{,}05$) dirumuskan

- [x] **6. Studi Literatur & State of the Art (10 Artikel)**
  - [x] Penelusuran kata kunci Boolean 5 tahun terakhir (2020–2025)
  - [x] Tabel perbandingan penelitian terdahulu disusun di [`docs/STATE_OF_THE_ART.md`](docs/STATE_OF_THE_ART.md)
  - [x] Perumusan celah penelitian (*research gap*) spesifik
  - [x] Catatan verifikasi naskah artikel primer disusun di [`docs/CATATAN_VERIFIKASI.md`](docs/CATATAN_VERIFIKASI.md)
  - [x] Berkas BibTeX lengkap & tervalidasi disusun di [`docs/references.bib`](docs/references.bib)

- [x] **7. Penyusunan Lembar Jawaban Resmi Tugas Bab III**
  - [x] Teks butir soal resmi disediakan di [`docs/SOAL_BAB_3.md`](docs/SOAL_BAB_3.md)
  - [x] Lembar jawaban komprehensif Soal 1 s.d. 6 disusun di [`docs/TUGAS_BAB_3.md`](docs/TUGAS_BAB_3.md):
    - [x] Soal 1: Dokumentasi dataset publik & hipotesis
    - [x] Soal 2: Strategi Boolean & 10 artikel format APA 7th Edition
    - [x] Soal 3: Tabel 5 artikel inti & perumusan *research gap*
    - [x] Soal 4: Tiga saringan kelayakan ide & contoh kasus gagal
    - [x] Soal 5: Alasan pemilihan dataset standar/Kaggle untuk komparasi algoritma
    - [x] Soal 6: Analisis studi kasus etika rujukan AI dan transparansi akademik

- [x] **8. Dokumentasi Repositori Berstandar Rian Mubarok**
  - [x] Header badges (*Python 3.9+*, *Dataset Kaggle*, *License CC BY-SA 4.0*)
  - [x] Struktur direktori proyek yang rapi dan deskriptif di [`README.md`](README.md)
  - [x] Panduan instalasi dan instruksi eksekusi kode eksperimen

- [x] **9. Version Control (Git & GitHub)**
  - [x] Inisialisasi git lokal (`git init`)
  - [x] Commit seluruh dokumen dan kerangka kode
  - [x] Push ke repositori GitHub pribadi (`agungsarwono/hoax-classification-nb-knn-pso`)
