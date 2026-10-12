"""Particle Swarm Optimization untuk seleksi fitur (biner) dan, untuk KNN,
sekaligus optimasi parameter K.

Posisi partikel = [d nilai kontinu untuk fitur, (opsional) satu nilai untuk K].
Fitur ke-j aktif bila sigmoid(posisi_j) > 0.5; K dibulatkan ke bilangan ganjil
di dalam k_range. Fungsi fitness HARUS dievaluasi pada data latih saja
(lihat experiment.py) agar tidak ada kebocoran data ke data uji.
"""
import numpy as np


def _sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def _odd_k(v, k_min, k_max):
    k = int(round(float(v)))
    k = min(max(k, k_min), k_max)
    if k % 2 == 0:
        k = k + 1 if k + 1 <= k_max else k - 1
    return max(k, 1)


def run_pso(fitness, n_features, optimize_k=False, k_range=(1, 25),
            n_particles=10, n_iter=10, w=0.7, c1=1.5, c2=1.5,
            init_density=0.5, min_features=5, seed=42):
    """Maksimalkan fitness(mask, k) -> skor.

    Mengembalikan (mask_terbaik, k_terbaik, skor_terbaik, riwayat_skor).
    """
    rng = np.random.default_rng(seed)
    d = n_features
    dim = d + (1 if optimize_k else 0)
    k_min, k_max = k_range

    shift = np.log(init_density / (1 - init_density))
    pos = np.zeros((n_particles, dim))
    pos[:, :d] = rng.normal(0, 1, (n_particles, d)) + shift
    if optimize_k:
        pos[:, d] = rng.uniform(k_min, k_max, n_particles)
    vel = rng.normal(0, 0.1, (n_particles, dim))

    def decode(p):
        mask = _sigmoid(p[:d]) > 0.5
        if mask.sum() < min_features:  # jaga jumlah fitur minimum
            mask[np.argsort(-p[:d])[:min_features]] = True
        k = _odd_k(p[d], k_min, k_max) if optimize_k else None
        return mask, k

    pbest_pos = pos.copy()
    pbest_score = np.full(n_particles, -np.inf)
    gbest_pos, gbest_score = pos[0].copy(), -np.inf
    history = []

    for it in range(n_iter + 1):  # iterasi 0 = evaluasi populasi awal
        for i in range(n_particles):
            mask, k = decode(pos[i])
            score = fitness(mask, k)
            if score > pbest_score[i]:
                pbest_score[i], pbest_pos[i] = score, pos[i].copy()
            if score > gbest_score:
                gbest_score, gbest_pos = score, pos[i].copy()
        history.append(float(gbest_score))
        if it == n_iter:
            break
        r1 = rng.random((n_particles, dim))
        r2 = rng.random((n_particles, dim))
        vel = w * vel + c1 * r1 * (pbest_pos - pos) + c2 * r2 * (gbest_pos - pos)
        vel = np.clip(vel, -4, 4)
        pos = pos + vel
        if optimize_k:
            pos[:, d] = np.clip(pos[:, d], k_min, k_max)

    mask, k = decode(gbest_pos)
    return mask, k, float(gbest_score), history
