"""Eksperimen utama: NB, KNN, NB-PSO, KNN-PSO dengan protokol yang identik.

Protokol (mencegah kebocoran data):
  * Stratified k-fold luar. Pada tiap fold: TF-IDF di-fit HANYA pada data latih.
  * PSO (seleksi fitur; untuk KNN juga K) memakai fitness = rata-rata F1 kelas
    hoaks dari CV dalam (inner) pada data latih saja. Data uji tidak pernah
    dilihat PSO.
  * Metrik dihitung pada data uji fold luar: accuracy, precision, recall,
    F1 (kelas hoaks = positif), ROC-AUC.

Contoh:
    python -m src.experiment --data data/raw/NAMA_FILE.csv \
        --text-col NAMA_KOLOM_TEKS --label-col NAMA_KOLOM_LABEL --hoax-value hoax
"""
import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (accuracy_score, f1_score, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from .data import class_report, load_dataset, undersample
from .pso import run_pso

MODELS = ["NB", "KNN", "NB-PSO", "KNN-PSO"]


def make_model(name, k=5):
    if name.startswith("NB"):
        return MultinomialNB(alpha=1.0)
    return KNeighborsClassifier(n_neighbors=k, metric="cosine", algorithm="brute")


def inner_fitness(X, y, name, inner_folds, seed):
    """Bangun fungsi fitness (mask, k) -> rata-rata F1 hoaks pada CV dalam."""
    skf = StratifiedKFold(n_splits=inner_folds, shuffle=True, random_state=seed)
    splits = list(skf.split(X, y))

    def fitness(mask, k):
        cols = np.flatnonzero(mask)
        Xm = X[:, cols]
        scores = []
        for tr, va in splits:
            model = make_model(name, k if k else 5)
            model.fit(Xm[tr], y[tr])
            scores.append(f1_score(y[va], model.predict(Xm[va]), zero_division=0))
        return float(np.mean(scores))

    return fitness


def evaluate(model, Xte, yte):
    pred = model.predict(Xte)
    proba = model.predict_proba(Xte)[:, 1]
    return pred, {
        "accuracy": accuracy_score(yte, pred),
        "precision": precision_score(yte, pred, zero_division=0),
        "recall": recall_score(yte, pred, zero_division=0),
        "f1": f1_score(yte, pred, zero_division=0),
        "auc": roc_auc_score(yte, proba),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True)
    ap.add_argument("--text-col", required=True)
    ap.add_argument("--label-col", required=True)
    ap.add_argument("--hoax-value", required=True, help="nilai label yang berarti hoaks")
    ap.add_argument("--stem", action="store_true", help="stemming Sastrawi (lambat)")
    ap.add_argument("--no-undersample", action="store_true")
    ap.add_argument("--max-features", type=int, default=1000,
                    help="ukuran kosakata TF-IDF yang diserahkan ke PSO")
    ap.add_argument("--folds", type=int, default=10)
    ap.add_argument("--inner-folds", type=int, default=3)
    ap.add_argument("--particles", type=int, default=10)
    ap.add_argument("--iters", type=int, default=10)
    ap.add_argument("--k-max", type=int, default=25)
    ap.add_argument("--baseline-k", type=int, default=5)
    ap.add_argument("--sample", type=int, default=0,
                    help="(debug) pakai hanya N baris setelah undersampling")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="results")
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    df = load_dataset(a.data, a.text_col, a.label_col, a.hoax_value, stem=a.stem)
    print("Setelah pembersihan  :", class_report(df))
    if not a.no_undersample:
        df = undersample(df, a.seed)
        print("Setelah undersampling:", class_report(df))
    if a.sample:
        df = df.sample(min(a.sample, len(df)), random_state=a.seed).reset_index(drop=True)
        print("Mode debug (sample)  :", class_report(df))

    texts, y = df["text"].to_numpy(), df["y"].to_numpy()
    outer = StratifiedKFold(n_splits=a.folds, shuffle=True, random_state=a.seed)

    rows, preds = [], []
    t0 = time.time()
    for fold, (tr, te) in enumerate(outer.split(texts, y), start=1):
        vec = TfidfVectorizer(max_features=a.max_features, min_df=2)
        Xtr = vec.fit_transform(texts[tr]).tocsr()   # fit hanya pada data latih
        Xte = vec.transform(texts[te]).tocsr()
        ytr, yte = y[tr], y[te]
        d = Xtr.shape[1]

        for name in MODELS:
            info = {"fold": fold, "model": name, "n_features": d, "k": None}
            if name == "NB":
                model, cols = make_model(name), np.arange(d)
            elif name == "KNN":
                model, cols = make_model(name, a.baseline_k), np.arange(d)
                info["k"] = a.baseline_k
            else:
                is_knn = name.startswith("KNN")
                fit = inner_fitness(Xtr, ytr, name, a.inner_folds, a.seed + fold)
                mask, k, score, _ = run_pso(
                    fit, d, optimize_k=is_knn, k_range=(1, a.k_max),
                    n_particles=a.particles, n_iter=a.iters, seed=a.seed + fold)
                cols = np.flatnonzero(mask)
                model = make_model(name, k if k else 5)
                info.update(n_features=len(cols), k=k, pso_inner_f1=score)
            model.fit(Xtr[:, cols], ytr)
            pred, m = evaluate(model, Xte[:, cols], yte)
            rows.append({**info, **m})
            preds.append(pd.DataFrame({"fold": fold, "model": name,
                                       "idx": te, "y_true": yte, "y_pred": pred}))
        print(f"fold {fold}/{a.folds} selesai  ({time.time() - t0:.0f} dtk)")

    res = pd.DataFrame(rows)
    res.to_csv(out / "fold_metrics.csv", index=False)
    pd.concat(preds).to_csv(out / "predictions.csv", index=False)
    summary = (res.groupby("model")[["accuracy", "precision", "recall", "f1", "auc", "n_features"]]
               .agg(["mean", "std"]).round(4).loc[MODELS])
    summary.to_csv(out / "summary.csv")
    print("\nRingkasan (rata-rata ± std antar fold):\n", summary.to_string())
    print(f"\nTersimpan di {out}/ (fold_metrics.csv, predictions.csv, summary.csv)")


if __name__ == "__main__":
    main()
