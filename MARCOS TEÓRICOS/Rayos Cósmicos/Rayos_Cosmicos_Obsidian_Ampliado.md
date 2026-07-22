
# Rayos Cósmicos: Teoría Avanzada y Aplicaciones Multimensajero

## [[1. Contexto Histórico]]
Los rayos cósmicos fueron descubiertos por Victor Hess en 1912. Su experimento con globos aerostáticos reveló un aumento en la ionización con la altitud, lo que indicaba una fuente extraterrestre de radiación. Posteriormente, Pierre Auger descubrió las lluvias extensas de aire, confirmando que los rayos cósmicos pueden tener energías superiores a \(10^{19} \, 	ext{eV}\).

## [[2. Composición y Clasificación]]
Los rayos cósmicos están compuestos por:
- **Protones (~90%)**
- **Núcleos de helio (~9%)**
- **Electrones y núcleos pesados (~1%)**

Se clasifican según su energía:
- **Baja energía (< GeV):** modulados por el viento solar.
- **Alta energía (> TeV):** origen galáctico y extragaláctico.
- **Ultraenergéticos (> EeV):** posiblemente de AGN o GRBs.

## [[3. Espectro Energético y Quiebres]]
El espectro sigue una ley de potencia:
$$\phi(E) = k E^{-\gamma}$$

Donde \( $\gamma \approx 2.7$\) para energías < knee. Cambia en:
- **Knee (~10^{15} eV):** transición galáctica.
- **Ankle (~10^{18} eV):** transición extragaláctica.

## [[4. Mecanismos de Aceleración]]
### 4.1 Fermi de Primer Orden
En choques astrofísicos:
$$\Delta E = \frac{\Delta p}{p} E \propto eta E$$

### 4.2 Fermi de Segundo Orden
En turbulencias magnéticas:
$$\Delta E \propto \eta^2 E$$

### 4.3 Fuentes
- **SNRs:** aceleración en frentes de choque.
- **AGN:** jets relativistas.
- **GRBs:** choques internos y externos.

## [[5. Propagación y Atenuación]]
La ecuación de transporte es:

```latex
rac{\partial f}{\partial t} + ec{v} \cdot 
abla f = 
abla \cdot (D 
abla f) + Q - L
```

Donde:
- \( D \): coeficiente de difusión
- \( Q \): fuentes
- \( L \): pérdidas (sincrotrón, Compton, interacciones)

## [[6. Interacciones y Producción de Mensajeros]]
### 6.1 Interacciones hadrónicas
$$p + p \rightarrow \pi^0 $$ 
$$\rightarrow \gamma\gamma
p + p $$
\rightarrow \pi^\pm 
\rightarrow \mu^\pm 
\rightarrow 
u_\mu, 
u_e

```latex

```

### 6.2 Fotoproducción
```latex
p + \gamma 
ightarrow \Delta^+ 
ightarrow \pi^0/\pi^\pm
```

## [[7. Señales Multimensajero]]
- **Rayos gamma:** detectados por HAWC, Fermi.
- **Neutrinos:** detectados por IceCube.
- **CRs:** detectados por Auger, TA.

## [[8. Aplicaciones en HAWC e IceCube]]
### HAWC
Detecta rayos gamma TeV mediante cascadas atmosféricas usando detectores Cherenkov.

### IceCube
Detecta neutrinos mediante trazas de muones y cascadas en el hielo antártico.

## [[9. Modelado y Simulación en Python]]
```python
import numpy as np
import matplotlib.pyplot as plt

# Espectro de rayos cósmicos
E = np.logspace(9, 20, 100)  # Energía en eV
phi = E**-2.7

plt.figure(figsize=(8,5))
plt.loglog(E, phi)
plt.xlabel("Energía (eV)")
plt.ylabel("Flujo relativo")
plt.title("Espectro de Rayos Cósmicos")
plt.grid(True)
plt.savefig("espectro_cr.png")
```

## [[10. Estadística Aplicada]]
### Likelihood para detección de neutrinos
```python
from scipy.stats import poisson

# Eventos observados y esperados
n_obs = 5
mu_bkg = 2.0

# Probabilidad de observar n_obs dado fondo
p_value = 1 - poisson.cdf(n_obs-1, mu_bkg)
print(f"p-value: {p_value:.3e}")
```

## [[11. Referencias]]
- Gaisser, T.K. *Cosmic Rays and Particle Physics*
- Becker, J.K. *High-Energy Neutrinos in Astrophysics*
- IceCube Collaboration papers
- HAWC technical reports

