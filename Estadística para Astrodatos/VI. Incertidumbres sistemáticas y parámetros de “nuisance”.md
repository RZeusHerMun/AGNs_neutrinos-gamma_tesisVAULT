# 📘 Estadística en Astrofísica de Altas Energías  
## Bloque VI – Incertidumbres sistemáticas y parámetros de “nuisance”

---

### 1) ¿Qué son las sistemáticas y por qué dominan?
Las **incertidumbres sistemáticas** son sesgos o variaciones reproducibles que no decrecen con más datos (a diferencia del error estadístico ~ 1/√N). En HAWC/IceCube afectan sensibilidad, significancias y límites superiores.

**Fuentes típicas**
- **Instrumentales**: calibración de PMTs, ganancia, tiempos, eficiencia de disparo.  
- **Respuesta del detector**: área efectiva \($A_{\text{eff}}(E,\theta))$, PSF, resolución/disp. en energía $(D(E_{\text{rec}}|E))$.  
- **Ambiente**: atmósfera (densidad, aerosoles), nieve/hielo (IceCube), temperatura.  
- **Modelado del fondo**: hadrones residuales (HAWC), neutrinos/muones atmosféricos (IceCube).  
- **Astrofísicas**: modelos espectrales, EBL (atenuación γγ), morfología espacial.

---

### 2) Tratamiento formal: “nuisance parameters” (perfilado o marginalización)
Introducimos parámetros de sistema \(\eta\) (vector) en la verosimilitud:
$$\mathcal{L}(\mu,\eta) = P(D \mid \mu,\eta)\,\prod_j \pi_j(\eta_j)$$
- \($\mu$\): parámetros físicos de interés (p.ej., normalización \($N_0$\), índice \($\gamma$\)).  
- \($\eta$\): parámetros de sistema (escala de energía, eficiencia, fondo, etc.).  
- \($\pi_j(\eta_j)$\): **términos de penalización/constraints** (p. ej., Gaussianas con media 0 y σ conocida), que incorporan conocimiento externo (calibraciones).

**Dos enfoques:**
- **Perfilado (frecuentista)**: \($\hat{\eta}(\mu) = \arg\max_\eta \mathcal{L}(\mu,\eta)$\).  
  Intervalos por **razón de verosimilitudes perfilada**:
  $TS(\mu)=-2\ln\frac{\mathcal{L}(\mu,\hat{\eta}(\mu))}{\mathcal{L}(\hat{\mu},\hat{\eta})}$

- **Marginalización (bayesiano)**: $p(\mu\mid D)=\int \mathcal{L}(\mu,\eta),d\eta$.

**Observación clave**: si las constraints de \($\eta$\) son informativas, el perfilado suele aproximar bien la marginalización para propósitos de intervalos/exclusiones.

---

### 3) “Pull terms” y matriz de covarianza
Para $N$ sistemáticas gaussianas:  
$$-2\ln \mathcal{L}_\text{tot} = -2\ln P(D\mid \mu,\eta) + \sum_{j=1}^N \left(\frac{\eta_j}{\sigma_j}\right)^2$$
o, más general, con correlaciones:
$$-2\ln \mathcal{L}_\text{tot} = -2\ln P(D\mid \mu,\eta) + \boldsymbol{\eta}^\top \mathbf{C}^{-1} \boldsymbol{\eta}$$

donde \($\mathbf{C}$\) es la **covarianza** de sistemáticas (crítico si, p. ej., escala de energía y eficiencia están correlacionadas).

Los **pulls** \($\eta_j/\sigma_j$\) sirven para diagnosticar si el ajuste “tensiona” excesivamente alguna sistemática.

---

### 4) Significancias y límites con sistemáticas
- Con sistemáticas, el **TS** disminuye (incertidumbre efectiva aumenta).  
- El **Asimov dataset** (Cowan et al.) permite estimar significancias esperadas incluyendo términos de penalización (útil para optimización de análisis).  
- **Cobertura**: verificar con pseudo-experimentos que los intervalos mantienen la fracción nominal (90%, 95%) *en presencia* de sistemáticas.

---

### 5) Métodos data–driven para fondo y control de sesgos
- **Regiones laterales (sidebands)**: estimar el fondo en ON extrapolando desde OFF con correcciones controladas.  
- **ABCD**: dos variables (aprox. independientes) para factorizar señal/fondo y predecir fondo en la celda “signal-like”.  
- **Scrambling** (IceCube): aleatoriza RA para construir \(H_0\) empírica conservando declinación/energía.  
- **Inyección–recuperación**: inyectar señales simuladas en datos reales para medir sesgo y potencia.

---

### 6) Respuesta instrumental: forward-folding vs. unfolding
**Forward-folding (recomendado)**  
Se ajusta el **modelo físico** con convolución de la respuesta:
\[
$$\mu_i(\theta) = \int R_i(E)\,\Phi(E;\theta)\, dE
$$\]
donde \($R_i$\) combina \($A_{\text{eff}}$, $D(E_\text{rec}|E)$, $\text{PSF}$\), y exposición del bin $(i)$. La verosimilitud Poisson por bin:
$$\ln \mathcal{L} = \sum_i \left[ n_i \ln \mu_i - \mu_i - \ln(n_i!) \right]
$$
- Pros: bien condicionada; fácil incluir sistemáticas como \($\eta$\) que deforman \($R$\).

**Unfolding (deconvolución)**
- Problema inverso mal condicionado; requiere regularización (Tikhonov, Bayes iterativo).  
- Útil para publicar **espectros independientes de instrumento**, pero más sensible a sistemáticas y regularización.  
- Recomendación: usar unfolding solo con estudios y bandas de covarianza claros; preferir forward-folding en análisis principales.

---

### 7) Ejemplos concretos (HAWC/IceCube)
- **HAWC**:  
  - Sistemáticas dominantes: rechazo hadrónico, \(A_{\text{eff}}\) vs. zenit, calibración de tiempo/charge, atmósfera.  
  - Tratamiento: templates de fondo data–driven; \(\eta\) de escala de energía; PSF dependiente de “nHit” o fracción de tanques activados.  
  - Publicación: espectros via forward-folding; límites con perfilado + constraints.

- **IceCube**:  
  - Sistemáticas: modelo de hielo (scattering/absorption), eficiencia DOM, flujo atmosférico (π/K/Prompt), cross sections.  
  - Tratamiento: parámetros de hielo como \(\eta\) con priors; scrambling en RA para p-values globales; MLE no binned (dirección+energía).

---

### 8) Checklist práctico de sistemáticas (para cada análisis)
1. **Enumerar** todas las fuentes plausibles (instrumento, ambiente, fondo, teoría).  
2. **Cuantificarlas**: prior gaussiano/log–normal; rango físico; correlaciones.  
3. **Implementarlas** como \(\eta\) en la verosimilitud con constraints.  
4. **Validar** cobertura y potencia con pseudo-experimentos (con y sin \(\eta\)).  
5. **Reportar** impactos en parámetros y TS (tablas de “impact ranking”/pulls).  
6. **Plots clave**: residuals por bin, pulls, curvas TS vs. \(\eta\), bandas de error (covarianza total).

---

## Bloque VII – Análisis conjuntos, “stacking” y poblaciones

---

### 1) “Joint likelihood” multi–dataset/multi–instrumento
Para combinar campañas, bines en zenit o instrumentos (HAWC+Fermi+MAGIC+VERITAS/CTA):
\[
$$\ln \mathcal{L}_\text{joint}(\theta,\eta) = \sum_{k}\ln \mathcal{L}_k(\theta,\eta_k)$$
\]
- Compartir \($\theta$\) físicos (p.ej., \($\gamma$\), \($E_{\text{cut}}$\)).  
- \($\eta_k$\) específicos por dataset (calibración, escala de energía).  
- Ventaja: sensibilidad y control de sistemáticas instrumentales independientes.

### 2) Stacking de fuentes y de transitorios
- **Stacking de fuentes**: sumar señales esperadas de una **población** (SNRs, PWNe, blazars).  
$$TS = -2\ln \frac{\mathcal{L}(\mu=0)}{\mathcal{L}(\hat{\mu})}, 
  \quad \mu = \sum_j w_j \mu_j(\theta)$$
  Pesos \(w_j\) por exposición, distancia, predicción teórica.  
- **Stacking temporal**: múltiples ventanas (GRBs, TDEs). Peligro: **trials factor**; usar MC para p-value global.

### 3) Plantillas espaciales y espectrales
- Mapas de plantillas (p.ej., gas/ISM para emisión difusa).  
- Ajustes de componentes con regularización (L1/L2) si hay degeneraciones.

---

## Bloque VIII – Transitorios, dominio temporal y tasas de falsas alarmas

---

### 1) Búsqueda de estallidos/transitorios
- **Ventanas móviles** (sliding windows) en tiempo, multi-escala.  
- **Bayesian Blocks** para segmentar series temporales (detección de cambios de tasa).  
- Métrica: **False Alarm Rate (FAR)** y **False Alarm Probability (FAP)**, estimadas con MC de fondo.

### 2) Alertas en tiempo (casi) real
- Estimadores robustos y simples (On/Off por ventana).  
- **Pre–definición** de umbrales de TS/FAR (blinding).  
- Control de latencias vs. calidad de reconstrucción.

### 3) Coincidencias multi–mensajero
- Coincidencia espacio–temporal–energética con GW/GRBs/ATels.  
- p-value combinado (Fisher, Stouffer) con corrección por ensayos.

---

## Bloque IX – Aprendizaje automático para separación γ/hadrón y clasificación

---

### 1) Objetivo y datos
- **Features**: morfología de la cascada, fracción de tanques activados, tiempos, energía reconstruida, calidad.  
- **Modelos**: árboles potenciados (XGBoost, LightGBM), RF, DNN.  
- Métricas: **ROC/AUC**, curva precisión–recobrado, **background rejection** a eficiencia fija de señal.

### 2) Buenas prácticas
- **Validación cruzada** estratificada y por épocas (evitar leak temporal).  
- **Calibración probabilística** (Platt, isotónica) si se usa score como probabilidad.  
- **Robustez a sistemáticas**:  
  - *Domain adaptation* (adversarial training) para atenuar shift datos–MC.  
  - Data augmentation con variaciones de calibración/atmósfera.  
- **Interpretabilidad**: importancia de variables, SHAP, tests de estabilidad.

### 3) Integración en la verosimilitud
- Usar el score ML como **observables** (templates de señal/fondo en bins de score).  
- Verificar **monotonía** y **calibración** para evitar sesgos en TS.

---

## Bloque X – Buenas prácticas, validación y reproducibilidad

---

### 1) Blinding y análisis predefinido
- “Congelar” selección, verosimilitud, métricas y umbrales antes de mirar la señal.  
- Usar **datasets ciegos** o scrambling para evitar bias de confirmación.

### 2) Tests de bondad de ajuste (GoF)
- **KS**, **Anderson–Darling**, **Cramér–von Mises** para distribuciones 1D.  
- **Pearson χ²** y residuals pull por bin para mapas/energía.  
- **Q–Q plots** de TS bajo \(H_0\) vs. χ² teórica (o MC).

### 3) Cobertura, potencia y estudios de *closure*
- **Cobertura**: fracción de intervalos que contienen el verdadero valor.  
- **Potencia**: prob. de detectar una señal de tamaño dado (curvas poder vs. flujo).  
- **Closure tests**: recuperar parámetros inyectados dentro de incertidumbres.

### 4) Gestión y trazabilidad
- Versionado de código y de IRFs (respuesta).  
- Semillas aleatorias, configuración congelada, pipelines declarativos.  
- Reportes automáticos: tablas de pulls, impactos, curvas TS, sensibilidad.

---

## Bloque XI – Herramientas y ecosistema software

---

- **Gammapy** (γ-ray analysis en Python; mapas, espectros, IRFs, likelihood).  
- **ctools** (CTA, análisis de alta energía).  
- **3ML** (Multi-Mission Maximum Likelihood): combinar HAWC, Fermi, IACTs.  
- **RooFit/RooStats** (modelado probabilístico y estadística de tests).  
- **iminuit** (minimización MLE), **pyhf** (hist-factory, perfiles con sistemáticas).  
- **PyMC/Stan** (MCMC/HMC para bayesiano con priors complejos).  
- **HEALPix** (mapas all-sky), **CORSIKA/GEANT4** (MC físicos).  

**Sugerencia práctica**: prototipa con Gammapy/3ML + iminuit; para bayesiano pesado, PyMC/Stan; para perfiles con grandes plantillas y sistemáticas correlacionadas, pyhf/RooStats.

---

## Bloque XII – Ejercicios de consolidación (estilo posgrado)

---

1. **Perfilado con una sistemática**:  
   Modelo espectral \($dN/dE=N_0 (E/E_0)^{-\gamma}$\) con una escala de energía \($\eta_E \sim \mathcal{N}(0,\sigma_E)$\).  
   - Implementa \($\mathcal{L}(\mu,\eta_E)$\) con forward-folding.  
   - Compara intervalos de \($N_0,\gamma$\) con y sin constraint.  
   - Evalúa cobertura con pseudo-experimentos.

2. **TS y trials factor all-sky** (IceCube-like):  
   - Genera eventos de fondo con distribución en declinación/energía.  
   - Calcula TS por pixel HEALPix.  
   - Obtén p-value **local** vs. **global** con scrambling de RA.

3. **Stacking de PWNe** (HAWC-like):  
   - Define pesos por exposición/distancia.  
   - Ajusta un único \(\mu\) para la población y estima sensibilidad ganada vs. fuente individual.

4. **Upper limit con Feldman–Cousins y Bayes**:  
   - Caso de pocos conteos; compara coberturas y dependencia del prior.

5. **Clasificación γ/hadrón con XGBoost**:  
   - Entrena con MC etiquetado; valida AUC.  
   - Calibra scores (isotónica) y verifica estabilidad bajo shift de atmósfera.

---

## Referencias esenciales (para estudio profundo)
- Cowan et al., *Asymptotic formulae for likelihood-based tests of new physics* (JHEP 2011).  
- Li & Ma, *Analysis methods for results in gamma-ray astronomy* (ApJ 1983).  
- Feldman & Cousins, *Unified approach to classical statistical analysis of small signals* (PRD 1998).  
- Barlow, *Statistics: A Guide to the Use of Statistical Methods in the Physical Sciences*.  
- James, *Statistical Methods in Experimental Physics*.  
- Casella & Berger, *Statistical Inference* (fundamentos).  
- Gammapy/3ML/RooStats/pyhf documentations (práctica de software).

---
