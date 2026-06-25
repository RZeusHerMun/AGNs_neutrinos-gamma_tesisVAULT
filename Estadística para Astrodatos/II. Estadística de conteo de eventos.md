# 📘 Estadística en Astrofísica de Altas Energías  
## Bloque II – Estadística de Conteo de Eventos

---

## 1. Procesos de Poisson y conteo de eventos

En detección de rayos gamma/neutrinos, la cantidad de eventos por unidad de tiempo sigue típicamente una **distribución de Poisson**:
$$P(k;\lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$$
- \(k\): número de eventos observados.  
- \(\lambda\): número esperado (media).  
- Propiedad clave: \($\text{Var}(k) = \lambda$\).  

**Ejemplo:**  
Si se esperan ($\lambda=5$) fotones gamma/segundo del Crab, la probabilidad de ver exactamente 7 en un segundo es:  
$$P(7;5) = \frac{5^7 e^{-5}}{7!} \approx 0.104$$
---

## 2. Señal vs. fondo

En experimentos como **HAWC** o **IceCube**, se distinguen dos regiones:

- **ON**: región que contiene la fuente (señal + fondo).  
- **OFF**: región(s) que solo contienen fondo.  

Se introducen las siguientes variables:
- \($N_{\text{on}}$\): número de eventos en la región ON.  
- \($N_{\text{off}}$\): número de eventos en la(s) región(es) OFF.  
- \($\alpha$\): factor de normalización, que corrige por diferencias de tiempo/área:  
$$\alpha = \frac{\text{exposición(ON)}}{\text{exposición(OFF)}}$$
El **fondo esperado** en ON es:
$$B = \alpha N_{\text{off}}$$
El **exceso de señal** es:
$$N_{\text{exceso}} = N_{\text{on}} - B
$$
---
## 3. Estimadores simples de significancia

Un primer estimador de cuán significativa es una detección:
$$S \approx \frac{N_{\text{exceso}}}{\sqrt{B}}$$
- Válido solo cuando \(N\) es grande (aproximación Gaussiana).  
- Intuitivo, pero **no óptimo**: sesgado si las cuentas son bajas.

---

## 4. Fórmula de Li & Ma (1983)

El estándar en astrofísica de rayos gamma es la **significancia de Li & Ma** (ApJ 272, 317).   
$$S = \sqrt{2} \left\{ 
N_{\text{on}} \ln \left[ \frac{(1+\alpha)}{\alpha} \frac{N_{\text{on}}}{N_{\text{on}}+N_{\text{off}}} \right]+ 
N_{\text{off}} \ln \left[ (1+\alpha) \frac{N_{\text{off}}}{N_{\text{on}}+N_{\text{off}}} \right]
\right\}^{1/2}$$

Características:
- Reduce correctamente a la aproximación Gaussiana cuando \(N\) es grande.  
- Funciona también para conteos bajos.  
- Se considera **la referencia oficial** en experimentos Cherenkov.  

---

Supongamos que HAWC observa durante 1h:
- \($N_{\text{on}} = 1200$\)  
- \($N_{\text{off}} = 10000$\)  
- Región OFF es 10 veces más grande → \($\alpha = 0.1$\)  
Cálculos:

1. Fondo esperado:  
$$B = 0.1 \times 10000 = 1000$$
2. Exceso:  
$$N_{\text{exceso}} = 1200 - 1000 = 200$$
3. Aproximación Gaussiana:  
$$S \approx \frac{200}{\sqrt{1000}} \approx 6.3\sigma$$
4. Con fórmula de Li & Ma → \($S \approx 6.0\sigma$\) (valor más preciso).

---

## 6. Interpretación de la significancia

- \($S \sim 2\sigma$\): consistente con ruido.  
- \($S \sim 3\sigma$\): evidencia sugestiva, no concluyente.  
- \($S \geq 5\sigma$\): detección robusta (probabilidad de fluctuación ~ 1 en 3.5 millones).  
Por convención en física de partículas y astrofísica de altas energías, **5σ = descubrimiento**.

---
## 7. Aplicaciones prácticas

- **HAWC**: reporta su sensibilidad diaria en función de la detección del Crab a 5σ.  
- **IceCube**: usa ON/OFF y métodos de máxima verosimilitud (ver Bloque III) para neutrinos.  
- **Fermi-LAT**: combina significancia local con corrección por “trials factor” (se verá en Bloque V).

---
