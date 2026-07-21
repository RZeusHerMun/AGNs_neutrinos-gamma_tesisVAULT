#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esquema de la distribución espectral de energía (SED) de un blazar,
en clave multimensajera. Genera SVG + PNG.
Paleta armonizada con 'Cascada conceptual - Jets Relativistas.svg'.
Autor: tesis multimensajera (Raph). Fecha: 2026-07-21.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---- paleta (coherente con la cascada) ----
C_BG    = "#f7f8fe"   # fondo lavanda claro
C_BORD  = "#d5d8ee"
C_TITLE = "#1e2145"
C_SYN   = "#4a52a8"   # sincrotrón (azul-morado)
C_GAM   = "#c2410c"   # 2ª joroba gamma (naranja acento)
C_NU    = "#0f766e"   # neutrinos (verde-azulado)
C_EBL   = "#8a8fb0"   # atenuación EBL (gris-morado)
C_TXT   = "#23264d"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Segoe UI", "Arial"],
    "svg.fonttype": "none",
    "mathtext.fontset": "dejavusans",
})

x = np.linspace(-7.5, 16.5, 3000)

def hump(x, mu, sig, amp):
    return amp * np.exp(-0.5 * ((x - mu) / sig) ** 2)

# --- componentes ---
syn      = hump(x, 0.3, 3.15, 1.00)                 # 1ª joroba: sincrotrón
gam_int  = hump(x, 9.2, 3.05, 0.93)                 # 2ª joroba: intrínseca (IC / pi0)
tau      = np.where(x > 11.3, ((x - 11.3) / 1.15) ** 2, 0.0)  # profundidad óptica EBL
gam_obs  = gam_int * np.exp(-tau)                   # 2ª joroba observada (atenuada)
nu       = hump(x, 14.3, 1.15, 0.52)                # joroba de neutrinos (pi+)

fig, ax = plt.subplots(figsize=(9.7, 5.8))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor("white")

# --- curvas ---
ax.plot(x, syn, color=C_SYN, lw=2.6, zorder=6)
ax.plot(x, gam_int, color=C_GAM, lw=1.3, ls=(0, (5, 3)), alpha=0.55, zorder=5)  # intrínseca
ax.plot(x, gam_obs, color=C_GAM, lw=2.6, zorder=6)                              # observada
nu_plot = np.where(nu > 0.010, nu, np.nan)   # oculta la cola plana ~0
ax.plot(x, nu_plot, color=C_NU, lw=2.4, ls=(0, (6, 3)), zorder=6)

# flujo gamma absorbido por la EBL (entre intrínseca y observada)
m = x > 11.3
ax.fill_between(x[m], gam_obs[m], gam_int[m], color=C_GAM, alpha=0.12, zorder=2)

# --- etiquetas de regímenes espectrales (arriba) ---
for xr, lab in [(-6.2, "radio"), (0.0, "IR / óptico"), (3.6, "rayos X"),
                (9.0, "$\\gamma$ (GeV)"), (12.2, "VHE (TeV)"), (15.2, "PeV")]:
    ax.text(xr, 1.245, lab, ha="center", va="center", fontsize=8.5,
            color="#6b6f99", style="italic")
ax.axhline(1.205, color=C_BORD, lw=1.0, zorder=1)

# --- anotaciones de mecanismos ---
ax.annotate("Sincrotrón\n(electrones $e^-$)", xy=(0.3, 1.00), xytext=(-5.6, 0.66),
            fontsize=11, fontweight="bold", color=C_SYN, ha="center",
            arrowprops=dict(arrowstyle="-|>", color=C_SYN, lw=1.6))
ax.text(-5.6, 0.545, "1ª joroba", ha="center", fontsize=8.5, color=C_SYN, style="italic")

ax.annotate("Compton inverso  /  $\\pi^0\\!\\to\\!\\gamma\\gamma$", xy=(9.2, 0.94),
            xytext=(5.0, 1.135), fontsize=11, fontweight="bold", color=C_GAM, ha="center",
            arrowprops=dict(arrowstyle="-|>", color=C_GAM, lw=1.6))
ax.text(5.0, 1.055, "2ª joroba  ·  leptónico / hadrónico", ha="center",
        fontsize=8.5, color=C_GAM, style="italic")

ax.annotate("Neutrinos\n$\\pi^+\\!\\to\\!\\mu^+\\nu_\\mu\\!\\to\\! e^+\\nu_e\\bar\\nu_\\mu\\nu_\\mu$",
            xy=(14.3, 0.52), xytext=(14.9, 0.85), fontsize=10, fontweight="bold",
            color=C_NU, ha="center",
            arrowprops=dict(arrowstyle="-|>", color=C_NU, lw=1.6))

# --- atenuación EBL ---
ax.annotate("atenuación EBL\n$e^{-\\tau(E,z)}$", xy=(12.55, 0.28), xytext=(10.3, 0.60),
            fontsize=9.5, color="#6a4a2a", ha="center",
            arrowprops=dict(arrowstyle="-|>", color=C_EBL, lw=1.4))

# --- barras de cobertura de instrumentos (abajo) ---
def coverage(x0, x1, y, color, edge, label):
    ax.add_patch(Rectangle((x0, y), x1 - x0, 0.045, facecolor=color,
                           edgecolor=edge, lw=1.2, zorder=4, clip_on=False))
    ax.text((x0 + x1) / 2, y + 0.022, label, ha="center", va="center",
            fontsize=8.8, fontweight="bold", color=edge, zorder=5)

coverage(8.0, 11.5, -0.055, "#e7e3f3", "#5c62b0", "Fermi-LAT")   # fotones GeV
coverage(11.5, 14.0, -0.055, "#f6ddc9", C_GAM, "HAWC")           # fotones VHE
coverage(12.0, 16.3, -0.125, "#cfeae6", C_NU, "IceCube  ($\\nu$)")  # neutrinos
ax.text(-7.1, -0.09, "cobertura\ninstrumental", fontsize=8.2, color="#6b6f99",
        style="italic", va="center")

# --- ejes ---
ax.set_xlim(-7.5, 16.5)
ax.set_ylim(-0.17, 1.30)
ax.set_xlabel("Energía   $\\log_{10}(E\\,/\\,\\mathrm{eV})$", fontsize=11, color=C_TXT)
ax.set_ylabel("$\\nu F_\\nu$   (potencia por década)   [u.a.]", fontsize=11, color=C_TXT)
ax.set_xticks([-6, -3, 0, 3, 6, 9, 12, 15])
ax.set_yticks([])
ax.tick_params(axis="x", labelsize=9, colors=C_TXT)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(C_BORD)

ax.set_title("Distribución espectral de energía (SED) de un blazar — esquema multimensajero",
             fontsize=12.5, fontweight="bold", color=C_TITLE, pad=12)

plt.tight_layout()
for ext in ("svg", "png"):
    fig.savefig(f"SED multimensajera - doble joroba.{ext}", dpi=200,
                facecolor=C_BG, bbox_inches="tight")
print("OK: figura generada")
