# Catatan Verifikasi: Outline Awal vs Artikel Asli

Sesuai Bab III subbab 3.7, setiap rujukan berstatus **terduga** sampai dicocokkan dengan berkas aslinya. Dokumen ini mencatat hasil pencocokan outline awal (`outline_Komparasi.pdf`) terhadap artikel yang berhasil dibuka.

**Ringkasan:** keenam artikel pembanding di outline memang ada, tetapi **angka dan detail tiga di antaranya tidak cocok** dengan artikel aslinya, dan satu klaim tentang Kurnia dkk. berlawanan dengan isi artikel. Ini jenis kesalahan yang disebut buku ajar sebagai "mengutip artikel nyata dengan isi yang salah". Dalam kasus Soleman dan Sani, detail kedua artikel tampak tertukar.

| Artikel | Klaim di outline | Temuan di artikel asli | Tindakan |
|---|---|---|---|
| Soleman (2021), CoreIT 7(2), 83–93 | 287 artikel (200 valid, 87 hoaks); empat model NB; akurasi 88,89%, presisi 86,36%, recall 82,61% | 250 artikel (159 valid, 91 hoaks); NB dengan atribut tambahan (situs dan statusnya); akurasi **72%** (split 80:20 dan 70:30), turun dari 78,6% pada penelitian sebelumnya | Ganti dengan angka asli. Rincian "287 artikel, 200/87, empat model" justru milik Sani dkk. |
| Sani dkk. (2022), JMASIF 13(2), 85–98 | SVM 96,1% vs NB 94,2%; ukuran dataset tidak disebut | SVM kernel sigmoid **96,5%** vs ComplementNB **93,1%**; 287 berita **kesehatan** (200 valid, 87 hoaks); split 80:20 | Perbaiki angka; sebut bahwa topiknya kesehatan |
| Hendriyanto & Sari (2022), JIF 10(02), 80–85 | Akurasi terbaik 87,5% (90:10); nilai K "default tanpa optimasi" | Akurasi terbaik **93,33%** (k=3, 90:10); data 150 judul (75/75), uji hanya 15 judul; K dicoba manual pada {1,3,5,7,9,11} | Perbaiki angka dan klaim tentang K; sebut keterbatasan ukuran data |
| Kurnia dkk. (2024), bit-Tech 6(3), 341–352 | "PSO mampu meningkatkan performa Naive Bayes"; "peningkatan akurasi yang signifikan" | NB 90,71% vs NB-PSO **90,25%** (accuracy sedikit turun); AUC naik 0,827 → 0,860; CNN-PSO juga turun (80,86% → 79,68%). Penulis kelima (Apridius) tidak tercantum di outline; halaman 341–352 | Hapus klaim "meningkat signifikan". Gunakan temuan sebenarnya, justru memperkuat celah penelitianmu |
| Pajri dkk. (2020), JuTISI 6(2) | "Meningkatkan akurasi secara signifikan" | KNN 88,11% → KNN-PSO 97,9% pada **analisis sentimen Tokopedia**; tidak ada uji signifikansi | Tulis angka, sebut domain sentimen, hindari kata "signifikan" |
| Devita dkk. (2018), JTIIK 5(4) | NB 80,6% vs KNN 78,9% | Artikel terbukti ada (DOI tercantum di daftar pustaka karya lain); arah temuan (NB di atas KNN) sesuai, **angka persis belum bisa diverifikasi** | Buka artikelnya dan cocokkan angka sebelum dikutip |

## Hal lain di outline

- **Ukuran dataset:** angka 20.928 + 2.251 tidak cocok dengan angka per sumber di Kurnia dkk. (CNN 9.630, Kompas 4.750, Tempo 6.592, Turnbackhoax 10.381). Hitung sendiri dari berkas yang kamu unduh.
- **Ruang lingkup:** "di media sosial" (tujuan penelitian) tidak sesuai dengan sumber data berupa portal berita dan situs pemeriksa fakta.
- **Sitasi tidak konsisten:** "Masyarakat Antifitnah Indonesia (2024)" di teks vs "Mafindo (2024)" di daftar pustaka; "Amaly" vs "Amaly & Armiah"; "Siaran Pers Kominfo" vs "Kominfo (2024)". Kelola dengan Zotero/Mendeley.
- **Referensi non-penelitian** (Kominfo, Mafindo, We Are Social) tidak dihitung sebagai artikel studi literatur untuk butir 6 tugas.
- **Kurnia dkk. (2024)** memiliki inkonsistensi internal (precision dan recall berbeda antar tabel, jumlah sampel uji 8.000 dari 10.000 data yang seharusnya 20%). Gunakan angkanya dengan hati-hati dan sebut keterbatasan ini bila dikutip.

## Cara kerja verifikasi (subbab 3.7)

1. Cari judul persis di Google Scholar atau situs jurnal.
2. Cocokkan DOI, jurnal, volume, dan halaman.
3. Baca abstrak, metode, dan hasil; pastikan klaim di tulisanmu sama dengan isi artikel.
4. Simpan ke Zotero/Mendeley. Bila tidak ditemukan, buang dan catat.

Bila sebagian outline awal dibuat dengan bantuan AI, laporkan hal itu sesuai pertanyaan studi kasus no. 6 pada Latihan Soal Bab III.
