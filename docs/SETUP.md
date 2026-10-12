# Persiapan Lingkungan Pengembangan Lokal

## 1. Python

Butuh Python 3.9 atau lebih baru (kode diuji pada 3.12).

```bash
python --version
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Cek instalasi:

```bash
python -c "import sklearn, scipy, pandas, numpy; print(sklearn.__version__)"
```

## 2. Kaggle API (untuk mengunduh dataset)

1. Masuk ke Kaggle, buka *Settings > API*, buat token, lalu simpan `kaggle.json` di `~/.kaggle/` (Windows: `C:\Users\<nama>\.kaggle\`).
2. Jangan pernah meng-commit `kaggle.json` (sudah ada di `.gitignore`).
3. Unduh:

```bash
kaggle datasets download -d linkgish/indonesian-fact-and-hoax-political-news -p data/raw --unzip
```

Alternatif tanpa API: unduh manual dari halaman Kaggle dan taruh berkasnya di `data/raw/`.

## 3. Alat bantu koding berbasis agen (opsional)

Untuk alat seperti opencode atau hermes, ikuti dokumentasi resmi masing-masing untuk instalasi dan konfigurasi. Catat di bawah ini versi dan cara pemasangan yang kamu pakai agar tugas bisa direproduksi:

- [ ] Alat: ______  Versi: ______  Cara instal: ______
- [ ] Alat: ______  Versi: ______  Cara instal: ______

Bila alat AI dipakai membantu menulis kode atau referensi, verifikasi hasilnya sendiri (Bab III subbab 3.7) dan catat penggunaannya.

## 4. Git dan GitHub

```bash
git init
git add .
git status                      # pastikan data/raw TIDAK ikut
git commit -m "Tugas Bab III: topik, judul, studi literatur, kerangka kode"
git branch -M main
git remote add origin https://github.com/<username>/<nama-repo>.git
git push -u origin main
```

Buat repositori kosong di GitHub lebih dulu (tanpa README otomatis) agar `git push` pertama tidak bentrok.
