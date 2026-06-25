# -*- coding: utf-8 -*-
# =====================================================================
#  CORRECCIÓN DE LA SECCIÓN 8 — CORRELACIÓN TS HAWC vs N NEUTRINOS
#  Tesis: correlación multimensajera neutrinos–rayos gamma
# ---------------------------------------------------------------------
#  Cómo usarlo:
#    - Pega cada bloque "# %%" como una celda nueva en tu notebook,
#      DESPUÉS de la celda donde ya preparaste los arrays
#      (agn_ra, agn_dec, agn_ts, src_ra_rad, src_dec_rad, nu_ra_rad,
#       sin_dec_nu, cos_dec_nu, N_MC, ...).
#    - Reusa exactamente las mismas variables que ya tenías cargadas.
#    - Reemplaza por completo tu antiguo bloque "Spearman (manual)".
#  Requisitos: numpy, scipy, matplotlib (ya los usas).
# =====================================================================


# %% ------------------------------------------------------------------
# CELDA 1 — Recontar neutrinos por AGN (idéntico a tu código, sin cambios)
# ---------------------------------------------------------------------
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

THETA_CORR_DEG = 1.5  # mismo radio que venías usando

individual_counts = np.zeros(len(agn_ra), dtype=int)
for k in range(len(agn_ra)):
    cos_th = (np.sin(src_dec_rad[k]) * sin_dec_nu +
              np.cos(src_dec_rad[k]) * cos_dec_nu *
              np.cos(src_ra_rad[k] - nu_ra_rad))
    individual_counts[k] = np.sum(cos_th >= np.cos(np.deg2rad(THETA_CORR_DEG)))

n = len(agn_ts)
n_cero   = int(np.sum(individual_counts == 0))
n_emp_ts = n - len(np.unique(agn_ts))            # empates en TS (deberían ser ~0)
print(f"AGN totales:                      {n}")
print(f"AGN con 0 neutrinos a {THETA_CORR_DEG}°:        {n_cero}  ({100*n_cero/n:.1f}%)  <-- datos INFLADOS DE CEROS")
print(f"Valores únicos de individual_counts: {np.unique(individual_counts)}")
print(f"Empates en agn_ts:                {n_emp_ts}")


# %% ------------------------------------------------------------------
# CELDA 2 — Spearman CORRECTO (scipy maneja los empates con rangos promedio)
#           Reemplaza tu bloque "Spearman (manual)".
# ---------------------------------------------------------------------
# scipy.stats.spearmanr = correlación de Pearson sobre rangos PROMEDIO.
# Esto corrige el error de la fórmula 1 - 6Σd²/[n(n²-1)], que SOLO es
# válida cuando NO hay empates (Conover 1999; Press et al. Num. Recipes §14.6).
rho, p_rho = stats.spearmanr(agn_ts, individual_counts)

print("== Spearman corregido (scipy, con corrección por empates) ==")
print(f"  ρ_s   = {rho:+.4f}")
print(f"  p     = {p_rho:.4f}   (aproximación asintótica de scipy)")
print(f"\n  Antiguo valor manual reportado: ρ = -0.831  <-- ARTEFACTO (ver CELDA 5)")


# %% ------------------------------------------------------------------
# CELDA 3 — p-value por PERMUTACIÓN (recomendado con tantos empates)
#           La aproximación asintótica de la CELDA 2 no es fiable cuando
#           ~90% de los valores están empatados en 0. El test de
#           permutación NO asume nada sobre la distribución.
# ---------------------------------------------------------------------
rng = np.random.default_rng(12345)
N_PERM = 20000
perm_rhos = np.empty(N_PERM)
counts_shuffled = individual_counts.copy()
for i in range(N_PERM):
    rng.shuffle(counts_shuffled)                       # rompe cualquier relación TS–N
    perm_rhos[i] = stats.spearmanr(agn_ts, counts_shuffled)[0]

# p two-sided: fracción de permutaciones con |ρ| >= |ρ_observado|
p_perm = np.mean(np.abs(perm_rhos) >= np.abs(rho))
print("== Test de permutación (20 000 reordenamientos del conteo) ==")
print(f"  ρ_s observado = {rho:+.4f}")
print(f"  ρ nulo: media = {perm_rhos.mean():+.4f},  σ = {perm_rhos.std():.4f}")
print(f"  p_perm (dos colas) = {p_perm:.4f}")
print(f"  z equivalente      = {(rho - perm_rhos.mean())/perm_rhos.std():+.2f}σ")


# %% ------------------------------------------------------------------
# CELDA 4 — Pruebas alternativas más adecuadas a la naturaleza de los datos
#   (a) Kendall tau-b: correlación de rangos diseñada para tolerar empates.
#   (b) Mann–Whitney U: como casi todo es 0 ó 1, la pregunta honesta es
#       "¿los AGN CON neutrino cercano tienen mayor TS que los que NO?".
#       Esto evita por completo el problema de los empates en el conteo.
# ---------------------------------------------------------------------
tau, p_tau = stats.kendalltau(agn_ts, individual_counts)   # tau-b (maneja empates)
print(f"(a) Kendall tau-b = {tau:+.4f},  p = {p_tau:.4f}")

tiene_nu = individual_counts > 0
ts_con = agn_ts[tiene_nu]
ts_sin = agn_ts[~tiene_nu]
if len(ts_con) > 0 and len(ts_sin) > 0:
    U, p_mw = stats.mannwhitneyu(ts_con, ts_sin, alternative='greater')
    print(f"(b) Mann-Whitney U  (H1: TS mayor en AGN con neutrino):")
    print(f"     n(con)={len(ts_con)}  n(sin)={len(ts_sin)}")
    print(f"     mediana TS con={np.median(ts_con):.2f}  vs sin={np.median(ts_sin):.2f}")
    print(f"     U={U:.1f},  p={p_mw:.4f}")
print("\nInterpretación: si los tres tests dan p>>0.05 (no significativo),")
print("NO hay asociación TS–neutrinos -> consistente con emisión leptónica.")


# %% ------------------------------------------------------------------
# CELDA 5 — DIAGNÓSTICO: prueba de que el viejo ρ = -0.83 era un ARTEFACTO
#   Un estadístico de correlación válido es INVARIANTE ante el orden de
#   las filas. El cálculo manual con np.argsort(np.argsort(...)) NO lo es.
#   Demostración para tu sección de Limitaciones.
# ---------------------------------------------------------------------
def spearman_manual_buggy(ts_, c_):
    """Reproduce tu fórmula manual original (con el bug de empates)."""
    rank_ts = np.argsort(np.argsort(ts_)).astype(float)
    rank_n  = np.argsort(np.argsort(c_)).astype(float)
    d = rank_ts - rank_n
    m = len(ts_)
    return 1 - 6*np.sum(d**2) / (m*(m**2 - 1))

print("== El estadístico manual depende del ORDEN de las filas (= está mal) ==")
print(f"  Manual, orden original del catálogo : {spearman_manual_buggy(agn_ts, individual_counts):+.4f}")
for s in range(3):
    p = np.random.RandomState(s).permutation(n)
    man = spearman_manual_buggy(agn_ts[p], individual_counts[p])
    sci = stats.spearmanr(agn_ts[p], individual_counts[p])[0]
    print(f"  Filas barajadas (seed {s})           : manual={man:+.4f}   scipy={sci:+.4f}")
print("  -> El manual cambia con el orden (ARTEFACTO). scipy NO cambia (correcto).")
print("  -> El -0.83 aparecía porque el catálogo viene ordenado por TS y los")
print("     ~90% de ceros recibían rangos según su POSICIÓN, no su valor.")


# %% ------------------------------------------------------------------
# CELDA 6 — Gráfico corregido (título con el ρ ya correcto)
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ts_log = np.log10(agn_ts + 1)
ax.scatter(ts_log, individual_counts, c='steelblue', s=50, alpha=0.6, edgecolors='black')
ax.set_xlabel('log₁₀(TS + 1) [HAWC]')
ax.set_ylabel(f'N neutrinos dentro de {THETA_CORR_DEG}°')
ax.set_title(f'Correlación TS HAWC vs N neutrinos\n'
             f'Spearman ρ = {rho:+.3f}  (p = {p_rho:.2f}, permutación p = {p_perm:.2f})')
ax.grid(True, alpha=0.3)
z_fit = np.polyfit(ts_log, individual_counts, 1)
x_fit = np.linspace(ts_log.min(), ts_log.max(), 100)
ax.plot(x_fit, np.polyval(z_fit, x_fit), 'r--', lw=1.5, alpha=0.7, label='Ajuste lineal (guía visual)')
ax.legend()
plt.tight_layout()
plt.show()


# %% ------------------------------------------------------------------
# CELDA 7 (AVANZADO, OPCIONAL) — El análisis "correcto" para datos
#   inflados de ceros: razón de verosimilitud de Poisson apilada (stacking).
#   Es la lógica que ya usas en tus upper limits, escrita como un TS.
#   Método estándar en IceCube (Braun et al. 2008; Aartsen et al. 2017).
# ---------------------------------------------------------------------
# Idea: en vez de correlacionar rangos, comparamos el nº TOTAL de
# coincidencias observado contra el esperado por fondo (tu Monte Carlo),
# bajo un modelo de Poisson. Es lo que físicamente quieres responder:
# "¿hay MÁS neutrinos cerca de los AGN de lo que da el azar?"
#
# Requiere: n_real_theta / mean_e ya calculados en tu pipeline, o el MC
# de banda HAWC. Aquí una versión mínima con el conteo total a 1.5°:
N_obs_total = int(individual_counts.sum())          # nº total de pares AGN-neutrino a 1.5°
# Fondo esperado: usa la media de tu Monte Carlo de banda HAWC a 1.5°.
# Sustituye 'mu_bkg' por tu valor (p. ej. la media MC del conteo total).
mu_bkg = float(np.mean(individual_counts)) * n      # <-- PLACEHOLDER: reemplázalo por tu MC real

def poisson_llr(n_obs, mu0, mu1):
    # 2 ln L(mu1)/L(mu0) para Poisson (constante factorial se cancela)
    from scipy.special import xlogy
    return 2*((xlogy(n_obs, mu1) - mu1) - (xlogy(n_obs, mu0) - mu0))

mu_hat = max(N_obs_total, 1e-9)                     # MLE de la tasa (= observado)
TS_stack = poisson_llr(N_obs_total, mu_bkg, mu_hat)
TS_stack = TS_stack if N_obs_total >= mu_bkg else 0.0   # one-sided (solo excesos)
p_stack = 0.5 * stats.chi2.sf(TS_stack, df=1)           # Chernoff/Wilks one-sided
print("== (Opcional) Stacking de Poisson — razón de verosimilitud ==")
print(f"  N_obs total a {THETA_CORR_DEG}° = {N_obs_total},  fondo μ = {mu_bkg:.1f}  (REEMPLAZA por tu MC)")
print(f"  TS = {TS_stack:.2f},  p ≈ {p_stack:.3f}")
print("  NOTA: cambia 'mu_bkg' por la media de tu Monte Carlo de banda HAWC.")
print("  Para el análisis completo (PSF + energía + signalness por evento),")
print("  ver el método no-binned de Braun et al. 2008 (arXiv:0801.1604).")
