# LEMBAR JAWABAN TUGAS / LATIHAN SOAL
**Mata Kuliah:** Pemrograman Mobile Lanjut  
**Bab:** III – Identifikasi Masalah dan Studi Literatur  
**Buku Ajar:** *Metodologi Penelitian: Riset Berbasis Data dan Data Mining untuk Informatika* (Akhmad Khanif Zyen, S.Kom., M.Kom.)  
**Program Studi:** Teknik Informatika, Fakultas Sains dan Teknologi, Universitas Islam Nahdlatul Ulama (UNISNU) Jepara  
**Topik Proyek:** Deteksi dan Klasifikasi Berita Hoaks Politik Berbahasa Indonesia Berbasis Machine Learning untuk Layanan Cerdas Mobile  
**Judul Penelitian:** Komparasi Naive Bayes dan K-Nearest Neighbor Berbasis Particle Swarm Optimization untuk Klasifikasi Berita Hoaks Politik Berbahasa Indonesia  

---

## **Soal 1 (Praktik)**
> **Soal:** Pilih satu dataset dari Tabel 3.1, unduh dari repositori asalnya, dan tuliskan satu paragraf dokumentasi yang memuat sumber, lisensi, tanggal unduh, deskripsi singkat, dan hipotesis satu masalah yang dapat diteliti darinya.

### **Jawaban:**
**Dataset Pilihan:** *Indonesian Fact and Hoax Political News* dari repositori publik Kaggle (`linkgish/indonesian-fact-and-hoax-political-news`).

**Dokumentasi Dataset:**
Dataset *Indonesian Fact and Hoax Political News* yang digunakan dalam penelitian ini disusun oleh M. R. Rizqullah dan R. H. Ghaida (2023), dipublikasikan di repositori resmi **Kaggle**, dan diakses/diunduh pada tanggal **12 Oktober 2026** di bawah lisensi terbuka **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. Dataset ini memuat ribuan artikel berita bertema dinamika politik Indonesia yang dikompilasi dari portal berita kredibel (*Kompas, Tempo, CNN Indonesia*) serta arsip klarifikasi disinformasi pemeriksa fakta *TurnBackHoax* (MAFINDO). Setiap rekaman memuat atribut teks berita (judul dan isi artikel) beserta variabel target klasifikasi biner yang menandai status kebenaran berita (`hoaks` vs `fakta/valid`). Berdasarkan eksplorasi awal karakteristik teks berita politik berbahasa Indonesia yang sarat ambiguitas istilah, hipotesis penelitian yang dirumuskan adalah: *"Penerapan Particle Swarm Optimization (PSO) untuk seleksi subset fitur TF-IDF pada Naive Bayes serta seleksi fitur dan optimasi parameter $k$ pada K-Nearest Neighbor mampu meningkatkan performa F1-Score kelas hoaks secara signifikan secara statistik ($\alpha = 0{,}05$) dibandingkan algoritma konvensional tanpa optimasi, menghasilkan model klasifikasi yang lebih ringkas dan komputasionalnya efisien untuk diintegrasikan ke dalam ekosistem aplikasi mobile."*

---

## **Soal 2 (Praktik)**
> **Soal:** Lakukan penelusuran di Google Scholar dengan kata kunci Boolean untuk tema riset/proyek, terapkan filter 5 tahun terakhir, dan kumpulkan 10 artikel; simpan seluruhnya ke koleksi Zotero/Mendeley.

### **Jawaban:**

#### **A. Kata Kunci dan Strategi Penelusuran Boolean:**
* **Tema Pilihan:** Klasifikasi Berita Hoaks Politik Menggunakan Machine Learning dan Optimasi Heuristik (Naive Bayes, KNN, dan PSO).
* **Query Boolean Utama:**  
  `("hoax" OR "fake news" OR "berita hoaks") AND ("naive bayes" OR "k-nearest neighbor" OR "knn") AND ("particle swarm optimization" OR "pso") AND ("indonesia" OR "indonesian")`
* **Filter Rentang Tahun:** 2020 – 2025 (lima tahun terakhir).
* **Pangkalan Data / Mesin Pencari:** Google Scholar, Portal Garuda (Kemdikbudristek), SINTA, IEEE Xplore, ScienceDirect, Procedia Computer Science.

#### **B. Daftar 10 Artikel Ilmiah Terkumpul & Terverifikasi (Format APA 7th Edition):**

1. **Wati, R. (2020).** Penerapan Algoritma Naive Bayes dan Particle Swarm Optimization untuk Klasifikasi Berita Hoax pada Media Sosial. *Jurnal Ilmu Pengetahuan dan Teknologi Komputer*, 5(2), 9–14.
2. **Nugroho, K. S., Istiadi, I., & Marisa, F. (2020).** Optimasi naive Bayes classifier untuk klasifikasi teks pada e-government menggunakan particle swarm optimization. *Jurnal Teknologi dan Sistem Komputer*, 8(1), 21–26. https://doi.org/10.14710/jtsiskom.8.1.2020.21-26
3. **Pajri, D., Umaidah, Y., & Padilah, T. N. (2020).** K-Nearest Neighbor Berbasis Particle Swarm Optimization untuk Analisis Sentimen Terhadap Tokopedia. *Jurnal Teknik Informatika dan Sistem Informasi*, 6(2), 341–350. https://doi.org/10.28932/jutisi.v6i2.2658
4. **Soleman, S. (2021).** Pemanfaatan Metode Klasifikasi Naive Bayes untuk Pendeteksi Berita Hoax pada Artikel Berbahasa Indonesia. *Jurnal CoreIT*, 7(2), 83–93. https://doi.org/10.24014/coreit.v7i2.14290
5. **Hendriyanto, M. D., & Sari, B. N. (2022).** Penerapan Algoritma K-Nearest Neighbor dalam Klasifikasi Judul Berita Hoax. *Jurnal Ilmiah Informatika*, 10(2), 80–85. https://doi.org/10.33884/jif.v10i02.5477
6. **Sani, R. R., Pratiwi, Y. A., Winarno, S., Udayanti, E. D., & Alzami, F. (2022).** Analisis Perbandingan Algoritma Naive Bayes Classifier dan Support Vector Machine untuk Klasifikasi Hoax pada Berita Online Indonesia. *Jurnal Masyarakat Informatika*, 13(2), 85–98. https://doi.org/10.14710/jmasif.13.2.47983
7. **Devita, R. N., Herwanto, H. W., & Wibawa, A. P. (2018).** Perbandingan Kinerja Metode Naive Bayes dan K-Nearest Neighbor untuk Klasifikasi Artikel Berbahasa Indonesia. *Jurnal Teknologi Informasi dan Ilmu Komputer*, 5(4), 427–434. https://doi.org/10.25126/jtiik.201854773
8. **Kurnia, Y., Kusuma, E. D., Kusuma, L. W., Suwitno, S., & Apridius, W. (2024).** Perbandingan Naïve Bayes dan CNN yang Dioptimasi PSO pada Identifikasi Berita Hoax Politik Indonesia. *Bit-Tech (Binary Digital - Technology)*, 6(3), 341–352. https://doi.org/10.32877/bt.v6i3.1225
9. **Nayoga, B. P., Adipradana, R., Suryadi, R., & Suhartono, D. (2021).** Hoax Analyzer for Indonesian News Using Deep Learning Models. *Procedia Computer Science*, 179, 704–712. https://doi.org/10.1016/j.procs.2021.01.059
10. **Hermawan, A., Lunardi, L., Kurnia, Y., Daniawan, B., & Junaedi. (2025).** Optimizing Convolutional Neural Networks with Particle Swarm Optimization for Enhanced Hoax News Detection. *Journal of Information Systems Engineering and Business Intelligence*, 11(1), 45–56.

#### **C. Petunjuk Simpan ke Zotero / Mendeley:**
Seluruh metadata 10 artikel di atas telah disimpan dan divalidasi ke dalam berkas BibTeX resmi pada repositori ini di [`docs/references.bib`](references.bib). Berkas ini dapat langsung diimpor ke aplikasi Zotero atau Mendeley Desktop melalui menu **File > Import > references.bib**.

---

## **Soal 3 (Praktik)**
> **Soal:** Susun tabel penelitian terdahulu dari 5 artikel yang dikumpulkan pada soal 2 dengan kolom dataset-algoritma-metrik-hasil-celah, lalu rumuskan satu celah penelitian yang spesifik.

### **Jawaban:**

#### **A. Tabel Penelitian Terdahulu (State of the Art Table):**

| Peneliti (Tahun) | Dataset | Algoritma / Metode | Metrik Evaluasi | Hasil Utama | Celah Penelitian (*Research Gap*) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Wati (2020)** | 150 artikel media sosial (75 hoaks, 75 fakta) TurnBackHoax | Naive Bayes vs Naive Bayes + PSO (RapidMiner) | Accuracy, Sensitivity, Specificity, PPV, NPV | Akurasi NB meningkat dari 74,67% menjadi 85,19% (+10,52 poin) dengan PSO. | Dataset berukuran sangat kecil (150 sampel); tidak menguji KNN; tidak menyertakan uji signifikansi statistik. |
| **Kurnia dkk. (2024)** | 10.000 sampel teks berita politik Indonesia (Kaggle) | Naive Bayes, NB-PSO, CNN, CNN-PSO | Accuracy, Precision, Recall, ROC-AUC | Akurasi NB 90,71% vs NB-PSO 90,25% (sedikit menurun), namun AUC meningkat dari 0,827 ke 0,860. | Terdapat anomali penurunan akurasi pada dataset besar; tidak menyertakan pembanding KNN; metrik F1-score dan uji signifikansi tidak dilaporkan. |
| **Hendriyanto & Sari (2022)** | 150 judul berita online Indonesia | K-Nearest Neighbor (nilai $k \in \{1,3,5,7,9,11\}$) + TF-IDF | Accuracy, Precision, Recall, F1-Score | Akurasi terbaik dicapai pada $k=3$ sebesar 93,33%, Precision 100%, Recall 80%, F1 88,89%. | Ukuran data uji sangat terbatas (hanya 15 judul); penentuan $k$ dicoba secara manual tanpa algoritma metaheuristik; hanya menguji judul bukan isi berita. |
| **Pajri dkk. (2020)** | Data teks ulasan media sosial (3 kelas sentimen) | K-Nearest Neighbor vs KNN + PSO (seleksi fitur) | Accuracy, Precision, Recall, F-measure | Akurasi KNN naik dari 88,11% menjadi 97,90% dengan optimasi PSO. | Berada pada domain analisis sentimen komersial, bukan deteksi berita hoaks politik; tidak menguji Naive Bayes sebagai pembanding; tanpa uji hipotesis statistik. |
| **Soleman (2021)** | 250 artikel berita Indonesia (159 valid, 91 hoaks) | Naive Bayes + Atribut Eksternal Domain Situs | Accuracy | Akurasi 72% pada split data 80:20 dan 70:30. | Fitur alamat domain web rentan usang (*expired domain*); tidak menggunakan optimasi parameter fitur; akurasi masih relatif rendah. |

#### **B. Perumusan Celah Penelitian (*Research Gap*) Spesifik:**
> **Rumusan Celah Penelitian:**  
> *"Penelitian deteksi berita hoaks berbahasa Indonesia sebelumnya menunjukkan temuan yang saling bertentangan terkait efektivitas PSO (efektif menaikkan akurasi pada data kecil seperti pada Wati (2020), namun mengalami penurunan akurasi pada data berskala besar pada Kurnia dkk. (2024)). Selain itu, belum ada penelitian yang membandingkan secara berpasangan antara NB-PSO dan KNN-PSO (dengan optimasi simultan seleksi fitur TF-IDF dan penyetelan nilai k) menggunakan protokol eksperimen identik berupa nested cross-validation untuk mencegah data leakage, serta menguji signifikansi perbedaannya melalui uji paired t-test dan Wilcoxon signed-rank test."*

---

## **Soal 4**
> **Soal:** Jelaskan tiga saringan kelayakan ide penelitian berbasis data dan berikan contoh gagasan yang gagal pada masing-masing saringan.

### **Jawaban:**

1. **Saringan Ketersediaan dan Kualitas Data (*Data Availability & Quality*):**
   * **Penjelasan:** Ide penelitian harus didukung oleh ketersediaan dataset yang legal untuk diakses, memiliki volume sampel yang memadai, label yang terverifikasi (*ground truth* kredibel), serta atribut yang relevan untuk menjawab rumusan masalah.
   * **Contoh Gagal:** Ingin meneliti pendeteksian pesan hoaks percakapan rahasia WhatsApp warga suatu kabupaten secara *real-time*, tetapi datanya bersifat privat terenkripsi *end-to-end* dan tidak ada akses legal maupun API untuk mengambil data tersebut.

2. **Saringan Kebermaknaan dan Keterukuran Masalah (*Meaningfulness & Measurability*):**
   * **Penjelasan:** Masalah yang diteliti harus memiliki urgensi ilmiah atau praktis yang nyata, bukan persoalan artifisial, dan variabel kinerjanya dapat diukur secara kuantitatif melalui metrik baku (*Accuracy, Precision, Recall, F1-Score, ROC-AUC*).
   * **Contoh Gagal:** Meneliti apakah panjang nama penulis artikel berita berkorelasi dengan kemungkinan berita tersebut hoaks tanpa dasar landasan teori linguistik atau jurnalistik yang masuk akal.

3. **Saringan Kelayakan Teknis dan Sumber Daya (*Technical Feasibility & Resources*):**
   * **Penjelasan:** Kompleksitas komputasi model, kebutuhan memori, dan ruang pencarian optimasi harus realistis untuk diselesaikan dengan perangkat komputasi serta tenggat waktu studi yang tersedia (misalnya durasi pengerjaan tugas/skripsi satu semester).
   * **Contoh Gagal:** Menjalankan pencarian arsitektur *Large Language Model* 70 Miliar parameter dengan algoritma genetika ribuan generasi menggunakan laptop standar berspesifikasi terbatas tanpa GPU akselerator dalam waktu 2 minggu.

---

## **Soal 5**
> **Soal:** Mengapa dataset UCI/Kaggle sering dipilih untuk skripsi yang membandingkan algoritma? Jelaskan dengan konsep perbandingan hasil antar penelitian.

### **Jawaban:**

Dataset publik dari pangkalan data standar seperti UCI Machine Learning Repository dan Kaggle menjadi standar utama pemilihan data dalam penelitian komparasi algoritma karena alasan-alasan metodologis berikut:

1. **Tolak Ukur Standar Internasional (*Standardized Benchmark*):**  
   Dataset standar telah digunakan berulang kali oleh ratusan peneliti di seluruh dunia. Karakteristik distribusi data, *noise*, dan tantangan klasifikasinya telah terdokumentasi dengan baik, sehingga berfungsi sebagai standar pembanding bersama (*common ground*).
2. **Keterbandingan yang Adil (*Fair & Objective Comparison*):**  
   Ketika dua atau lebih algoritma (misalnya Naive Bayes vs KNN dengan PSO) diuji pada dataset yang sama dengan protokol evaluasi identik, perbedaan angka performa murni mencerminkan keunggulan matematis algoritma dan mekanisme optimasinya, bukan akibat perbedaan kualitas atau keanehan data mentah yang dikumpulkan sepihak.
3. **Keterulangan dan Verifikasi Ilmiah (*Reproducibility & Auditability*):**  
   Penguji tugas, dosen pembimbing, maupun akademisi lain dapat mengunduh berkas yang sama dan menjalankan ulang kode sumber untuk mereplikasi serta memvalidasi klaim penelitian secara transparan.
4. **Efisiensi Waktu dan Legalitas:**  
   Menghindarkan peneliti dari hambatan perizinan data institusi tertutup serta kesalahan anotasi label manual yang subjektif, sehingga waktu penelitian dapat difokuskan pada pemodelan dan analisis kinerja.

---

## **Soal 6 (Studi Kasus)**
> **Soal:** AI memberi Anda lima referensi; tiga ditemukan persis di Google Scholar, satu ditemukan tetapi isi artikelnya berbeda dari klaim AI, dan satu tidak pernah ditemukan. Bagaimana perlakuan Anda terhadap masing-masing, dan apa yang Anda laporkan tentang penggunaan AI tersebut?

### **Jawaban:**

Sebagai peneliti yang memegang teguh integritas akademik dan etika kejujuran ilmiah (sebagaimana ditegaskan dalam Bab III subbab 3.7 Buku Ajar):

1. **Perlakuan terhadap 3 Referensi yang Ditemukan Persis:**
   * Wajib membuka naskah lengkap atau minimal abstrak dan kesimpulan artikel aslinya.
   * Memeriksa kesesuaian metadata (nama jurnal, volume, nomor, halaman, dan DOI).
   * Mengonfirmasi bahwa klaim angka atau metode yang dikutip memang benar-benar tertulis di artikel tersebut.
   * Jika seluruhnya terverifikasi, masukkan ke pustaka Zotero/Mendeley dan cantumkan sebagai rujukan resmi.

2. **Perlakuan terhadap 1 Referensi yang Ditemukan Tetapi Isinya Berbeda:**
   * **Dilarang keras menyalin klaim fiktif hasil halusinasi AI.**
   * Jika artikel asli tersebut memang membahas tema yang relevan, ubah narasi sitasi agar 100% mencerminkan temuan asli penulis artikel tersebut (sebagaimana dicontohkan dalam verifikasi artikel Soleman dan Kurnia dkk. pada catatan verifikasi).
   * Jika isi aslinya sama sekali tidak relevan dengan penelitian, gugurkan artikel tersebut dari daftar rujukan.

3. **Perlakuan terhadap 1 Referensi yang Tidak Pernah Ditemukan:**
   * Referensi ini merupakan **halusinasi murni AI** (*fabricated source*).
   * **Buang secara total** referensi tersebut dari dokumen dan daftar pustaka. Dilarang merekayasa tautan DOI atau menyamarkan metadata buatan.

4. **Pelaporan dan Transparansi Penggunaan AI:**
   * Melaporkan secara eksplisit pada bagian dokumentasi/metode bahwa alat bantu AI (seperti LLM/agen coding) digunakan pada tahap awal pencarian referensi dan pembuatan draf kerangka kerja.
   * Melampirkan pernyataan integritas bahwa **seluruh referensi yang dicantumkan dalam karya ilmiah telah melewati proses verifikasi mandiri (*human-in-the-loop validation*)** ke sumber primer, dan seluruh klaim data yang tidak terverifikasi telah disaring dan dibersihkan.
