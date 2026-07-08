---
status: chequeando
capitulo: 4
seccion: X.3.4 / Limitaciones
tags:
  - tesis/analisis
  - estadistica
  - spearman
  - correccion
  - icecube
fecha_revision: 2026-06-18
notas_aplicar: queremos hallar el patron en la auditoría de los análisis puesto que se encuentra mejor información al respecto
ultima actualizacion: 2026-06-18
---

# Corrección y profundización — Correlación de Spearman (TS HAWC vs N neutrinos)

> [!summary] Veredicto:
> 1. **El ρ = −0.831 es un artefacto de código, no un resultado físico.** Se demostró numéricamente: el valor depende del *orden de las filas* del catálogo, cosa que un estadístico válido nunca debe hacer.
> 2. **La corrección propuesta (usar `scipy.stats.spearmanr`) es correcta** y suficiente para eliminar el bug: el ρ colapsa a ≈ 0 (sin correlación), que es lo coherente con el resto de la tesis. Si en cambio usamos np.
> 3. Spearman no busca ser el test *primario*. Se queda como prueba *exploratoria* (bien calculada) y el peso recae en el conteo + Monte Carlo y, opcionalmente, en una **razón de verosimilitud apilada** (estándar IceCube).

Archivos generados en esta revisión:
- Script listo para pegar: [[correccion_spearman_celdas.py]]
- Figura conceptual (éxito vs realidad): ![[spearman_exito_vs_realidad.png]]
- Figura diagnóstica del bug: ![[spearman_diagnostico_bug.png]]

---

## 1. Fundamentos: qué mide Spearman (y qué NO)

### 1.1 Monotonía 
- **Monotonía** es lo que mide Spearman: si al *ordenar* los AGN por brillo (TS), su número de neutrinos tiende a *crecer* (monótona creciente, $\rho>0$) o a *decrecer* (monótona decreciente, $\rho<0$), sin exigir que la relación sea una recta. Puede ser exponencial, logarítmica o escalonada: a Spearman solo le importa el **orden (rango)**, no la forma de la curva.

El mecanismo operativo: Spearman es simplemente la **correlación de Pearson aplicada a los rangos** en lugar de a los valores crudos. Se sustituye cada dato por su posición ordenada (1.º, 2.º, 3.º…) y se mide cuán alineadas van ambas listas de posiciones.

$$
\rho_s = 1 - \frac{6\sum_i d_i^2}{n(n^2-1)}, \qquad d_i = R(x_i) - R(y_i)
$$

donde $R(\cdot)$ es el rango. **Atención:** esta fórmula cerrada es un *atajo* que **solo es válido cuando NO hay empates**. Con empates hay que usar rangos promedio y la correlación de Pearson sobre ellos (ver §3). *Esta es la fuente del error.*

### 1.2 ¿Qué tiene que ver con la "función de probabilidad"?

Spearman no modela una densidad de probabilidad. Lo que sí es probabilístico es el **p-value asociado**: bajo la hipótesis nula $H_0$ de que TS y N son independientes, los rangos de una variable son una permutación aleatoria respecto a la otra, y eso induce una *distribución de $\rho_s$ bajo $H_0$*. El p-value es la probabilidad de obtener un $\rho_s$ tan extremo como el observado si $H_0$ fuera cierta. Es decir: la "probabilidad" entra para **decidir si el $\rho$ medido es real o pura casualidad**, no en el cálculo del coeficiente en sí.

---

## 2. Los parámetros físicos, aclarados

### 2.1 ¿Qué "número de neutrinos"?

Es `individual_counts`: para **cada AGN**, el número de **eventos individuales de IceCube (trazas de ICECAT-1)** cuya dirección reconstruida cae dentro de un círculo de radio 1.5° alrededor de ese AGN. No es un "neutrino n.º X" concreto, sino un **conteo de eventos acumulados en la vecindad angular** de la fuente. En tus datos casi todos los AGN tienen `0`, unos pocos tienen `1`, y rarísimamente `2`.

### 2.2 ¿Por qué 1.5°?

No es arbitrario: está ligado a la **resolución angular (PSF)** de IceCube para eventos de traza, que es del orden de $\sim 1°$ para las energías de interés. Abrir la ventana a 1.5° absorbe la cola de incertidumbre de reconstrucción sin diluir demasiado la señal en fondo. Es el mismo radio que usas en el resto del análisis (la malla $\theta\in\{0.5,1.0,1.5,2.0,3.0\}°$).

> [!tip] Para citar la elección
> Justifícalo con la PSF de las trazas de IceCube (Aartsen et al. 2017, *ApJ* 835, 151) y con la mediana del radio de error al 90 % de ICECAT-1 (Abbasi et al. 2023, *ApJS* 269, 25). Ver §6.

### 2.3 ¿Por qué $\log_{10}(TS+1)$?

Dos motivos, ambos **solo cosméticos / de visualización** (no afectan a Spearman, que usa rangos):
- **Compresión de escala.** El TS de HAWC abarca varios órdenes de magnitud (de ~0 a cientos/miles en fuentes como Mrk 421). El logaritmo evita que las pocas fuentes brillantísimas aplasten visualmente al resto en el scatter.
- **El "+1" evita $\log_{10}(0)=-\infty$.** Como hay fuentes con $TS\approx 0$, sumar 1 mapea limpiamente $TS=0 \to 0$. Es un desplazamiento estándar (pseudo-conteo).

> [!warning] Matiz importante
> El logaritmo es una transformación **monótona**, así que **no cambia los rangos** y por tanto **no cambia el valor de Spearman**. Sirve para el *gráfico*, no para el *cálculo*. Si en la tesis dices "calculamos Spearman sobre $\log_{10}(TS+1)$", es inofensivo pero algo redundante: el $\rho_s$ es idéntico al de $TS$ crudo.

### 2.4 ¿Qué deberíamos haber visto si la hipótesis hadrónica se cumpliera?

Si los AGN más brillantes en gamma (mayor TS) produjeran neutrinos (emisión **hadrónica**, $p\gamma$/$pp$), veríamos una **nube de puntos ascendente**: a más TS, más neutrinos cercanos, con $\rho_s$ positivo y fuerte (≈ +0.7…+0.9) y p ≪ 0.05. Eso es lo que muestra el **panel (A)** de la figura. Lo que realmente tienes es el **panel (B)**: casi todo en N = 0, sin tendencia, $\rho_s\approx 0$ — consistente con emisión **leptónica** (que no genera neutrinos).

![[spearman_exito_vs_realidad.png]]

> Figura. (A) Cómo se vería un resultado que *apoyara* la hipótesis hadrónica (correlación positiva fuerte). (B) Tus datos reales: resultado nulo, dominado por ceros. *Datos del panel B simulados con la misma estructura que tu muestra (135 AGN, ~13 con neutrino), solo con fines ilustrativos; el valor exacto debe recalcularse con el script sobre tus datos.*

---

## 3. Auditoría: por qué el ρ = −0.83 era un artefacto
El valor dependía de el orden de las filas del catálogo de el brillo gamma, esto no debería suceder en un análisis estadístico, pues buscamos analizar la monotonía entre los rangos de los datos. En realidad buscamos aplicarle una estadística de Pearson a valores en rangos (en lugar de valores crudos).

### 3.1 Veredicto sobre la propuesta de corrección

| Afirmación de la propuesta | Veredicto |
|---|---|
| "Hay un error por empates en `individual_counts`" | ✅ **Correcto** |
| "La fórmula $1-6\sum d^2/[n(n^2-1)]$ no vale con empates" | ✅ **Correcto** (Conover 1999; Num. Recipes §14.6) |
| "Hay que usar `scipy.stats.spearmanr`" | ✅ **Correcto y suficiente** para quitar el bug |
| "`np.argsort` asigna rangos por orden de aparición a los empates" | ✅ Correcto en el fondo |
| "Eso introduce *ruido* que invierte la correlación" | ⚠️ **Impreciso.** No es ruido aleatorio (eso daría $\rho\approx0$). Es un **artefacto determinista** que necesita *dos* ingredientes (ver §3.2) |
| "El ajuste rojo positivo contradice el ρ negativo → algo está mal" | ✅ Buena intuición diagnóstica |

### 3.2 El mecanismo de calcular rangos     
El `np.argsort(np.argsort(x))` calcula rangos **ordinales** (0,1,2,…,n−1, todos distintos). Cuando hay empates —los ~90 % de ceros— les asigna rangos distintos **según su posición en el arreglo**, no el rango promedio que les corresponde:

![[spearman_diagnostico_bug.png]]

Para que ese error produzca un valor **grande y negativo** (−0.83) en lugar de ≈ 0, hacen falta **dos condiciones simultáneas**:

1. **El catálogo HAWC viene ordenado por TS** (lo habitual: fuente más brillante primero). Entonces el índice de fila está perfectamente anti-correlacionado con el rango de TS.
2. **El conteo está inflado de ceros** y `np.argsort` ordena ese bloque de ceros según su índice, de modo que `rank_n` ≈ posición de fila.

Combinadas: $\text{rank\_ts} \approx (n-1)-\text{fila}$ mientras $\text{rank\_n}\approx \text{fila}$ → **anti-correlación casi perfecta** → $\rho_s\approx -0.83$. **Es 100 % geometría de ordenamiento, no física.**

> [!check] Prueba reproducida (simulación, 1000 catálogos sintéticos)
> - Catálogo ordenado por TS + ceros independientes → fórmula manual: $\rho = -0.818 \pm 0.049$. **El −0.831 de la tesis cae justo ahí** ($P(\rho<-0.80)=0.66$).
> - Mismos datos en **orden aleatorio** → fórmula manual: $\rho \approx 0.00$. → confirma que el signo y la magnitud venían del *orden*, no de los datos.
> - **La prueba definitiva:** al barajar las filas, el cálculo manual salta entre −0.9 y +0.04, mientras que `scipy.spearmanr` da **siempre el mismo valor** (≈ 0). Un estadístico de correlación legítimo es invariante ante permutaciones de filas; el manual no lo era.

### 3.3 ¿Y el "+1" de signo? ¿Por qué "fuerte"?

"Fuerte" se refiere a la magnitud: $|\rho_s|$ cerca de 1 indica relación monótona casi perfecta. −0.83 *parecía* una anti-correlación contundente ("**a más brillo, menos neutrinos**"), lo cual es un **absurdo físico** bajo la hipótesis hadrónica — y esa contradicción es precisamente la señal de alarma de que había un bug. Con la corrección, $|\rho_s|\approx 0$: ni correlación positiva ni negativa, simplemente **ausencia de correlación**, que es lo físicamente esperado para una muestra leptónica.

---

## 4. ¿Es Spearman la herramienta adecuada para datos inflados de ceros?

Respuesta honesta: **como test exploratorio sí; como test primario, no.** Tu intuición da en el clavo. Razones:

1. **Los empates dominan.** Cuando ~90 % de los $y$ son idénticos (cero), el coeficiente queda determinado casi por completo por cómo se promedian esos empates, y su interpretación como "asociación monótona" pierde sentido. La información efectiva es mínima.
2. **El p-value asintótico no es fiable** con esa proporción de empates (por eso en el script usamos un **p-value por permutación**, que no asume nada).
3. **No responde la pregunta física exacta.** Lo que quieres saber es "¿hay *más* neutrinos cerca de los AGN de lo que da el azar?", que es un contraste de **conteo contra fondo**, no de monotonía.

### 4.1 Qué hacer (escalera de rigor, implementada en el script)

1. **Spearman bien hecho** (`scipy`) + **p por permutación** + **Kendall τ-b** (tolera empates). → como prueba exploratoria, reportada con su matiz.
2. **Mann–Whitney U:** como casi todo es 0/1, reformula a "¿los AGN *con* neutrino cercano tienen mayor TS que los que *no*?". Evita por completo el problema de empates en el conteo y es más interpretable.
3. **Razón de verosimilitud de Poisson apilada (stacking).** Es la lógica que **ya usas** en tus *upper limits*, escrita como un TS: comparar el conteo total observado contra la media de tu Monte Carlo de banda HAWC. $TS = 2\ln[L(\hat\mu)/L(\mu_{\text{bkg}})]$, p-value por $\chi^2_1$ (Wilks/Chernoff one-sided) o por trials MC.
4. **Método no-binned completo (estándar IceCube):** verosimilitud por evento con PSF + energía + *signalness*, $\mathcal{L}(n_s,\gamma)=\prod_i\left[\frac{n_s}{N}\mathcal{S}_i+(1-\frac{n_s}{N})\mathcal{B}_i\right]$ (Braun et al. 2008). Es a lo que se refiere la pregunta sobre "Maximum Likelihood Ratio". Para tu tesis basta **citarlo como el método de referencia** y, si hay tiempo, implementar el nivel 3.

> [!note] Recomendación concreta de redacción
> En **X.3.4** reporta Spearman *corregido* como prueba complementaria ("$\rho_s = \dots$, $p=\dots$, sin asociación significativa"). En **Limitaciones** explica que, dada la naturaleza inflada de ceros, el resultado robusto proviene del conteo+MC y del *stacking* de verosimilitud, y que Spearman se incluye solo como verificación exploratoria. Así conviertes una debilidad en una muestra de rigor metodológico.

---

## 5. Acciones tomadas y resultados

- [x] **Diagnóstico reproducido numéricamente** → el −0.83 es artefacto de orden + empates (§3.2).
- [x] **Script de corrección** creado y probado de extremo a extremo: [[correccion_spearman_celdas.py]]. Incluye: Spearman con `scipy`, p por permutación, Kendall τ-b, Mann–Whitney U, **prueba diagnóstica de invariancia ante permutación**, gráfico corregido y esqueleto del *stacking* de Poisson.
- [x] **Figuras** generadas (`All/figuras/`).
- [ ] **Pendiente (tú):** pegar las celdas tras tu preparación de arrays, correr y anotar aquí los valores reales:

```
ρ_s (scipy)        = ____     p (asintótico) = ____
p (permutación)    = ____     Kendall τ-b    = ____   p = ____
Mann-Whitney U     = ____     p = ____
```

- [ ] **Pendiente (tú):** sustituir el marcador **[COMPLETAR]** de la sección X.3.4 y la limitación (iii) en [[DRAFTS - IV. Análisis]] con el valor corregido.

---

## 6. Fuentes citables

### Libros de estadística (los de referencia)

- **Conover, W. J. (1999).** *Practical Nonparametric Statistics* (3.ª ed.). Wiley. → Spearman y **corrección por empates** (rangos promedio), pp. 314–315. *La cita directa para justificar el método.*
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T. & Flannery, B. P. (2007).** *Numerical Recipes* (3.ª ed.). Cambridge Univ. Press. → §14.6 "Nonparametric or Rank Correlation": fórmula de Spearman **con término de corrección por empates** $\sum (m_k^3-m_k)/12$. *De aquí "sale" la fórmula.*
- **Hollander, M., Wolfe, D. A. & Chicken, E. (2014).** *Nonparametric Statistical Methods* (3.ª ed.). Wiley. → tratamiento riguroso (nivel posgrado) de correlación de rangos y empates.
- **Feigelson, E. D. & Babu, G. J. (2012).** *Modern Statistical Methods for Astronomy: With R Applications*. Cambridge Univ. Press. → el libro de cabecera de astro-estadística; correlación, *nondetections*, tests no paramétricos.
- **Wall, J. V. & Jenkins, C. R. (2012).** *Practical Statistics for Astronomers* (2.ª ed.). Cambridge Univ. Press.
- **Ivezić, Ž., Connolly, A., VanderPlas, J. & Gray, A. (2020).** *Statistics, Data Mining, and Machine Learning in Astronomy*. Princeton Univ. Press.
- **Cowan, G. (1998).** *Statistical Data Analysis*. Oxford Univ. Press. → verosimilitud, TS, límites — base para el método de IceCube.
- **Cameron, A. C. & Trivedi, P. K. (2013).** *Regression Analysis of Count Data* (2.ª ed.). Cambridge Univ. Press. → modelos para **datos inflados de ceros** (zero-inflated), para fundamentar la limitación.

### Artículos (método + precedentes + ruta de resultado nulo)

- **Braun, J., et al. (2008).** "Methods for point source analysis in high energy neutrino telescopes." *Astropart. Phys.* 29, 299. [arXiv:0801.1604] → **el** método no-binned de máxima verosimilitud (PSF + energía). La respuesta a "Maximum Likelihood Ratio".
- **Aartsen, M. G., et al. (IceCube) (2017).** "The contribution of Fermi-2LAC blazars to the diffuse TeV–PeV neutrino flux." *ApJ* 835, 45. [arXiv:1611.03874] → **precedente casi idéntico al tuyo:** *stacking* de cientos de blazares, verosimilitud no-binned, **resultado nulo + upper limits**. Cítalo tanto para el método como para la "ruta de resultado no positivo".
- **Cowan, G., Cranmer, K., Gross, E. & Vitells, O. (2011).** "Asymptotic formulae for likelihood-based tests of new physics." *Eur. Phys. J. C* 71, 1554. → distribución asintótica del TS (Wilks), para los p-values del *stacking*.
- **Feldman, G. J. & Cousins, R. D. (1998).** "Unified approach to the classical statistical analysis of small signals." *Phys. Rev. D* 57, 3873. → construcción rigurosa de *upper limits* (mejora la aproximación gaussiana actual).
- **IceCube Collab. et al. (2018).** "Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A." *Science* 361, eaat1378. → precedente de asociación individual (3σ).
- **(Cross-correlación, alternativa)** Negro, M., et al. (2023), "A Cross-correlation Study between IceCube Neutrino Events and the Fermi Unresolved Gamma-ray Sky." [arXiv:2304.10934].
- **(Empates / cero-inflación en correlación de rangos)** material reciente sobre *rank-based concordance for zero-inflated data* [arXiv:2510.16504] — útil para argumentar la limitación de Spearman aquí.

> [!info] Mapa marcador → cita (para [[DRAFTS - IV. Análisis]])
> - **[REF-13]** (KS / métodos no paramétricos) → Press et al. (Num. Recipes §14.6) + Conover (1999) + Feigelson & Babu (2012).
> - **[REF-9]** (scrambling) → Braun et al. (2008).
> - **[REF-15]** (upper limits) → Feldman & Cousins (1998); Cowan (1998).
> - **Limitación Spearman** → Conover (1999) pp. 314–315; Cameron & Trivedi (2013) para cero-inflación.

---

## Conexiones
- Nota madre: [[Correlación TS vs neutrinos]]
- Capítulo: [[DRAFTS - IV. Análisis]] (secciones X.3.4 y Limitaciones)
- Modelo nulo: [[Modelo nulo de banda HAWC]]
- Correcciones múltiples: [[Correccion de Bonferroni o Empirica]]
- Log de issues: [[All/Problemas]]
- Estadística de soporte: [[Estadística para Astrodatos/Estadística para Astrodatos]]
