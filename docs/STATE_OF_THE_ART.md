# Tabel Penelitian Terdahulu (State of the Art)

Format mengikuti Tabel 3.2 buku ajar: peneliti (tahun), dataset, algoritma, metrik, hasil, celah.

**Cara membaca status verifikasi:**
- ✅ = judul, metadata, dan angka hasil dicocokkan dengan teks/abstrak artikel asli.
- ⚠️ = artikel terbukti ada, tetapi angka hasilnya belum dicocokkan dengan teks lengkap. Baca sendiri sebelum dikutip.

Kolom **Celah** adalah analisis penyusun repositori ini (bukan klaim penulis artikel). Cek ulang setelah kamu membaca artikelnya.

| No | Peneliti (Tahun) | Dataset | Algoritma | Metrik | Hasil | Celah | Status |
|---|---|---|---|---|---|---|---|
| 1 | Wati (2020) | 150 berita media sosial (75 hoaks, 75 non-hoaks) dari TurnBackHoax | NB vs NB-PSO (RapidMiner 5.3) | Accuracy, sensitivity, specificity, PPV, NPV | NB 74,67% → NB-PSO 85,19% (+10,52 poin). PSO terbaik: populasi 6, inertia 1,0 | Dataset sangat kecil; tanpa KNN; tanpa uji signifikansi; skema validasi di RapidMiner tidak dirinci; teks artikel menyebut 85,19% dan 85,14% untuk hasil yang sama | ✅ |
| 2 | Nugroho dkk. (2020) | Teks pengaduan e-government (multi-label) | NBC, k-NN, NBC-PSO | Accuracy (CV 10-fold) | NBC 64,38%; k-NN 75%; NBC-PSO 87,44% | Domain pengaduan, bukan hoaks; k-NN tidak dioptimasi PSO; hanya accuracy | ✅ |
| 3 | Pajri dkk. (2020) | Tweet tentang Tokopedia (3 kelas sentimen) | KNN vs KNN-PSO (seleksi fitur) | Accuracy, precision, recall, F-measure | KNN 88,11% (k=1, split 90:10) → KNN-PSO 97,9%; PSO 20 iterasi, 10 partikel | Domain sentimen, bukan hoaks; tanpa pembanding NB; tanpa uji signifikansi | ✅ |
| 4 | Soleman (2021) | 250 artikel (159 valid, 91 hoaks), 10 topik | NB + atribut tambahan (situs, status situs); TF-IDF + SGD | Accuracy | 72% (split 80:20 dan 70:30), turun 6,6 poin dari penelitian sebelumnya (78,6%) | Dataset kecil dan tua; atribut situs tidak tahan lama (domain kedaluwarsa); tanpa optimasi parameter | ✅ |
| 5 | Hendriyanto & Sari (2022) | 150 judul berita (75 fakta, 75 hoaks) | KNN, k ∈ {1,3,5,7,9,11}, TF-IDF | Accuracy, precision, recall, F1 | Terbaik: 93,33% (k=3, split 90:10; uji hanya 15 judul), precision 100%, recall 80%, F1 88,89% | Data uji sangat kecil sehingga hasil tidak stabil; k dicoba manual, tanpa optimasi; hanya judul | ✅ |
| 6 | Sani dkk. (2022) | 287 berita kesehatan (200 valid, 87 hoaks) | 4 varian NB vs 4 kernel SVM, TF-IDF | Precision, recall, F1, accuracy | ComplementNB 93,1%; SVM kernel sigmoid 96,5% (split 80:20) | Hanya topik kesehatan; tanpa KNN; tanpa optimasi; satu split | ✅ |
| 7 | Devita dkk. (2018) | Artikel berbahasa Indonesia (umum, bukan hoaks) | NB vs KNN | Accuracy | NB unggul atas KNN (angka persis belum diverifikasi) | Bukan domain hoaks; tanpa optimasi | ⚠️ |
| 8 | Kurnia dkk. (2024) | Indonesian Fact and Hoax Political News (sampel 10.000 artikel; RapidMiner) | NB, NB-PSO, CNN, CNN-PSO | Accuracy, precision, recall, AUC | Accuracy: NB 90,71%; NB-PSO 90,25%; CNN 80,86%; CNN-PSO 79,68%. AUC: NB 0,827; NB-PSO 0,860; CNN 0,837; CNN-PSO 0,842 | PSO tidak menaikkan accuracy; tanpa KNN; tanpa F1 dan uji signifikansi; angka precision/recall berbeda antar tabel di artikelnya | ✅ |
| 9 | Nayoga dkk. (2021) | Berita hoaks dan valid berbahasa Indonesia | LSTM, Bi-LSTM, GRU, Bi-GRU, 1D-CNN; SVM dan NB sebagai pembanding | Accuracy | 1D-CNN terbaik 97,90% (angka dari kutipan pihak ketiga) | Deep learning, bukan NB/KNN; tanpa PSO | ⚠️ |
| 10 | Hermawan dkk. (2025) | Mengutip dataset Indonesian Fact and Hoax Political News di daftar pustakanya | CNN-PSO (PSO menyetel filter, kernel size, learning rate) | Accuracy, precision, recall | Accuracy 92,06%, precision 91,6%, recall 96,19% | CNN, bukan NB/KNN; tanpa pembanding tanpa-PSO pada abstrak; tanpa uji signifikansi | ✅ |

## Sintesis

1. **PSO untuk NB:** Wati (+10,52 poin accuracy, 150 data) dan Nugroho (NBC 64,38% → 87,44%, domain pengaduan) melaporkan kenaikan besar. Kurnia dkk. pada data hoaks politik yang jauh lebih besar justru melaporkan NB-PSO sedikit di bawah NB pada accuracy (90,25% vs 90,71%), tetapi AUC naik (0,827 → 0,860).
2. **PSO untuk KNN:** satu-satunya bukti adalah Pajri dkk. (sentimen, bukan hoaks) dengan kenaikan 88,11% → 97,9%.
3. **Hipotesis kerja** (belum diuji): manfaat PSO tampak besar pada data kecil dan berkurang pada data besar. Ini kandidat penjelasan, bukan temuan.
4. **Tidak ada** artikel yang membandingkan NB-PSO dan KNN-PSO secara langsung pada tugas hoaks, dan tidak ada yang menyertakan uji signifikansi.

## Yang masih harus kamu lakukan

- Baca sendiri minimal abstrak, metode, dan hasil tiap artikel (subbab 3.7 langkah 3), terutama baris bertanda ⚠️.
- Lengkapi metadata yang kosong di `references.bib` (volume, halaman, DOI untuk entri Wati dan Hermawan).
- Tambahkan artikel lain bila perlu, terutama pada jalur yang masih tipis: KNN-PSO untuk teks berbahasa Indonesia dan penelitian PSO pada dataset hoaks ini.
