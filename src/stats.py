"""Uji signifikansi antar model dari hasil src.experiment.

  * Paired t-test dan Wilcoxon pada metrik per fold (fold yang sama = berpasangan).
  * McNemar (uji binomial eksak) pada prediksi gabungan seluruh fold.

Catatan: skor antar fold CV tidak sepenuhnya independen, sehingga p-value uji
berpasangan per fold cenderung terlalu optimis. Laporkan bersama ukuran selisih
(mean diff) dan jangan hanya bergantung pada p-value.
"""
import argparse
import warnings

import pandas as pd
from scipy import stats

warnings.filterwarnings("ignore", category=RuntimeWarning)

PAIRS = [("NB", "NB-PSO"), ("KNN", "KNN-PSO"), ("NB-PSO", "KNN-PSO")]


def paired_tests(fold_df, metric):
    rows = []
    for a, b in PAIRS:
        xa = fold_df[fold_df.model == a].sort_values("fold")[metric].to_numpy()
        xb = fold_df[fold_df.model == b].sort_values("fold")[metric].to_numpy()
        diff = xb - xa
        t = stats.ttest_rel(xb, xa)
        try:
            w = stats.wilcoxon(xb, xa).pvalue
        except ValueError:  # semua selisih nol
            w = float("nan")
        rows.append({"metrik": metric, "A": a, "B": b, "mean_A": xa.mean(),
                     "mean_B": xb.mean(), "selisih(B-A)": diff.mean(),
                     "p_paired_t": t.pvalue, "p_wilcoxon": w})
    return rows


def mcnemar(pred_df):
    rows = []
    for a, b in PAIRS:
        pa = pred_df[pred_df.model == a].set_index(["fold", "idx"])
        pb = pred_df[pred_df.model == b].set_index(["fold", "idx"])
        ok_a = (pa.y_pred == pa.y_true)
        ok_b = (pb.y_pred == pb.y_true).reindex(ok_a.index)
        n01 = int(((~ok_a) & ok_b).sum())   # A salah, B benar
        n10 = int((ok_a & (~ok_b)).sum())   # A benar, B salah
        n = n01 + n10
        p = stats.binomtest(n01, n, 0.5).pvalue if n > 0 else float("nan")
        rows.append({"A": a, "B": b, "A_salah_B_benar": n01,
                     "A_benar_B_salah": n10, "p_mcnemar": p})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="results")
    a = ap.parse_args()
    fold_df = pd.read_csv(f"{a.results}/fold_metrics.csv")
    pred_df = pd.read_csv(f"{a.results}/predictions.csv")

    rows = []
    for metric in ("f1", "accuracy", "auc"):
        rows += paired_tests(fold_df, metric)
    t = pd.DataFrame(rows)
    m = pd.DataFrame(mcnemar(pred_df))
    t.to_csv(f"{a.results}/significance_paired.csv", index=False)
    m.to_csv(f"{a.results}/significance_mcnemar.csv", index=False)
    pd.set_option("display.width", 160)
    print(t.round(4).to_string(index=False))
    print()
    print(m.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
