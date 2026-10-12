"""Pemuatan dan persiapan data: pembersihan teks dan undersampling."""
import re

import pandas as pd

_URL = re.compile(r"https?://\S+|www\.\S+")
_NONALPHA = re.compile(r"[^a-z\s]")
_SPACE = re.compile(r"\s+")


def clean_text(text) -> str:
    """Case folding, hapus URL, angka, dan tanda baca."""
    text = str(text).lower()
    text = _URL.sub(" ", text)
    text = _NONALPHA.sub(" ", text)
    return _SPACE.sub(" ", text).strip()


def make_stemmer():
    """Stemmer Sastrawi (opsional; lambat untuk korpus besar)."""
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

    return StemmerFactory().create_stemmer()


def load_dataset(path, text_col, label_col, hoax_value, stem=False):
    """Baca CSV, bersihkan teks, dan ubah label menjadi biner (1 = hoaks).

    Nama kolom TIDAK diasumsikan. Cek dulu dengan:
        python -c "import pandas as pd; print(pd.read_csv('data/raw/FILE.csv').columns)"
    lalu berikan lewat --text-col, --label-col, --hoax-value.
    """
    df = pd.read_csv(path)
    for col in (text_col, label_col):
        if col not in df.columns:
            raise KeyError(f"Kolom '{col}' tidak ada. Kolom tersedia: {list(df.columns)}")
    df = df[[text_col, label_col]].dropna().copy()
    df["y"] = (
        df[label_col].astype(str).str.strip().str.lower()
        == str(hoax_value).strip().lower()
    ).astype(int)
    df["text"] = df[text_col].map(clean_text)
    if stem:
        stemmer = make_stemmer()
        df["text"] = df["text"].map(stemmer.stem)
    df = df[df["text"].str.len() > 0].drop_duplicates(subset="text")
    return df[["text", "y"]].reset_index(drop=True)


def undersample(df, seed=42):
    """Samakan jumlah kelas mayoritas dengan kelas minoritas (acak)."""
    n_min = df["y"].value_counts().min()
    parts = [g.sample(n_min, random_state=seed) for _, g in df.groupby("y")]
    out = pd.concat(parts).sample(frac=1.0, random_state=seed)
    return out.reset_index(drop=True)


def class_report(df):
    vc = df["y"].value_counts().sort_index()
    return {"valid(0)": int(vc.get(0, 0)), "hoaks(1)": int(vc.get(1, 0)), "total": int(len(df))}
