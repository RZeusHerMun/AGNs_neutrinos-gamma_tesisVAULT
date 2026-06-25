---
status: en-proceso
capitulo: 4
tags: [tesis/escritura, tesis/analisis, estadistica]
---
# IV. Análisis y Resultados

> **Estado:** 🟠 En proceso — resultados estadísticos completos, falta redacción formal

---
Cruzamos los dos catálogos de datos que tenemos a disposición; por una parte el Shift Pass 5 del HAWC que integra nueva informacíon a un rango más bajo de energía (bines B0 y B1) y por otra parte el catálogo de alertas de neutrinos del IceCube (IceCat-1).

Antes de iniciar el análisis usamos los valores de una detección verificada (TXS-0506) esto para validar nuestro algoritmo de detección. Se cargan los 135 núcleos activos de galaxias en pandas y las 324 alertas de IceCube con sus respectivas áreas de error. 

Se usará la fórmula de Vicenty para plotear las áreas de error en distancias angulares, esto es $$\cos\theta = \sin\delta_1 \sin\delta_2 + \cos\delta_1 \cos\delta_2 \cos(\alpha_1 - \alpha_2)$$ donde nuestros parámetros delta_1 y delta_2 son validados bajo el siguiente criterio:
Un AGN en $(\alpha, \delta)$ está dentro de la elipse de error del neutrino si:$$\left(\frac{\Delta\alpha \cos\delta_\nu}{\sigma_\alpha}\right)^2 + \left(\frac{\Delta\delta}{\sigma_\delta}\right)^2 \leq 1$$
Estas elipses las construimos con los valores de incertidumbre que nos proporciona el IceCube. 


Estoy en el proceso de escritura de la tesis, te comparto el apartado del análisis que se le realizaron a distintos datos. Con la información que te comparto puedes escribir el apartado del análisis que va a ir directamente en ese espacio de la tesis? Que información te faltaría? Como podríamos complementarla y sobre todo ir añadiendo las distintas citas que son necesarias en la construcción del texto de la parte del análisis. 
Que más podríamos agregar para suplementar esta parte, podrías hacer una investigación más exhaustiva para poder tener una escritura de nivel tesis de maestría en este apartado? 


# Capítulo X. Análisis estadístico de correlación espacial entre AGN de HAWC y neutrinos de IceCube

> **Nota:** Los marcadores del tipo **[REF-n]** indican puntos donde debe insertarse una cita bibliográfica. Al final del documento se incluye la lista de referencias sugeridas para cada marcador. Los marcadores **[COMPLETAR: ...]** señalan información que debe verificarse o añadirse con datos propios del trabajo.

## X.1 Planteamiento del problema y muestras de datos

El objetivo de este análisis es determinar si existe una correlación espacial estadísticamente significativa entre las posiciones de 135 núcleos activos de galaxias (AGN) detectados por el observatorio HAWC **[REF-1]** y las 324 alertas de neutrinos de alta energía del catálogo ICECAT-1 de IceCube **[REF-2]**. La hipótesis nula (H₀) establece que las posiciones de los AGN no están correlacionadas con las posiciones de los neutrinos más allá de lo esperado por azar.

La muestra de AGN proviene del catálogo de fuentes de HAWC **[REF-1]** **[COMPLETAR: especificar si es el 3HWC u otra versión del catálogo, y describir explícitamente los criterios de selección que redujeron la muestra a 135 fuentes]**, filtrada para conservar fuentes cuya emisión de rayos gamma se atribuye predominantemente a procesos leptónicos, en particular Compton inverso y _synchrotron self-Compton_ (SSC) **[REF-3]**. La composición de la muestra está dominada por objetos BL Lac (114 fuentes), seguidos de blazares de tipo incierto (bcu, 8), radiogalaxias (rdg, 6), FSRQ (6) y una galaxia con brote de formación estelar (sbg). El rango de declinación de la muestra, [−20.8°, +58.9°], refleja directamente el campo de visión de HAWC, cuya banda de sensibilidad abarca aproximadamente de −26° a +64° en declinación **[REF-1]**.

La fuente J0509.9+0550 (TXS 0506+056), incluida originalmente como referencia por su asociación bien establecida con emisión de neutrinos **[REF-4]**, fue excluida del análisis poblacional por no pertenecer al catálogo original y por constituir un sesgo de selección _a posteriori_.

La muestra de neutrinos corresponde a las 324 alertas del catálogo ICECAT-1 **[REF-2]**, que recopila eventos de tipo traza (_track-like_) de alta energía del programa de alertas en tiempo real de IceCube **[REF-5]**, con regiones de error asimétricas al 90% de nivel de confianza (CL), estimadores de _signalness_ (probabilidad de origen astrofísico) y energía reconstruida. El rango de declinación de las alertas, [−86.1°, +84.6°], cubre prácticamente todo el cielo, aunque la eficiencia de detección de trazas de IceCube depende fuertemente de la declinación **[REF-6]**.

**Contexto físico.** Las dos fuentes con evidencia más sólida de emisión conjunta de neutrinos, TXS 0506+056 **[REF-4]** y NGC 1068 **[REF-7]**, requieren componentes hadrónicas (interacciones pγ o pp) para explicar la producción de neutrinos. Dado que la muestra analizada fue seleccionada precisamente por sus características leptónicas, un resultado nulo es la expectativa física _a priori_, y el valor del análisis radica en cuantificar límites superiores a una posible componente hadrónica "oculta" en estas fuentes.

## X.2 Metodología

### X.2.1 Distancia angular y criterios de coincidencia

Las separaciones angulares entre fuentes y neutrinos se calcularon sobre la esfera celeste mediante la fórmula del coseno esférico:

$$\cos\theta = \sin\delta_1 \sin\delta_2 + \cos\delta_1 \cos\delta_2 \cos(\alpha_1 - \alpha_2)$$

Se emplearon dos criterios complementarios de coincidencia espacial:

**(a) Contornos elípticos al 90% CL.** Se aprovecharon las regiones de error asimétricas reportadas por IceCube para cada alerta. En la aproximación de campo plano, un AGN en $(\alpha, \delta)$ se considera coincidente con el neutrino $\nu$ si:

$$\left(\frac{\Delta\alpha \cos\delta_\nu}{\sigma_\alpha}\right)^2 + \left(\frac{\Delta\delta}{\sigma_\delta}\right)^2 \leq 1$$

donde $\sigma_\alpha$ y $\sigma_\delta$ se obtuvieron promediando los errores positivos y negativos reportados en ICECAT-1. Este criterio respeta la morfología real de las regiones de incertidumbre de cada evento y es análogo al utilizado en búsquedas de contrapartes de alertas individuales **[REF-2]** **[REF-8]**.

**(b) Radios circulares fijos.** Como prueba complementaria, se contaron las fuentes con al menos un neutrino dentro de un radio angular θ para una malla de radios θ ∈ {0.5°, 1.0°, 1.5°, 2.0°, 3.0°}, que abarca desde la escala típica de la resolución angular de los eventos de traza hasta escalas conservadoras que absorben colas de las distribuciones de error **[COMPLETAR: justificar la elección de la malla con la mediana del radio de error al 90% de ICECAT-1]**.

En ambos casos el estadístico de prueba fue el número de AGN con al menos una coincidencia, $N_{\text{obs}}$, evitando el doble conteo de fuentes con múltiples neutrinos cercanos.

### X.2.2 Construcción del modelo nulo: Monte Carlo por aleatorización %%_scrambling_%% 

La significancia de $N_{\text{obs}}$ se evaluó frente a la distribución del mismo estadístico bajo H₀, generada mediante $10^4$ realizaciones Monte Carlo (MC) por _scrambling_ de las posiciones del catálogo, técnica estándar en búsquedas de fuentes puntuales de neutrinos **[REF-9]**. Se compararon dos modelos nulos:

1. **Modelo isotrópico:** ascensión recta uniforme en [0°, 360°) y declinación distribuida uniformemente en $\sin\delta$, lo que produce una distribución uniforme sobre la esfera.
2. **Modelo de banda HAWC:** ascensión recta uniforme en [0°, 360°) manteniendo fija la declinación de cada fuente, lo que conserva exactamente la distribución en declinación del catálogo y, por tanto, la cobertura observacional de HAWC.

%%La distinción entre ambos modelos es el punto metodológico central de este capítulo.%% El modelo isotrópico **no** constituye una hipótesis nula válida para esta búsqueda: al redistribuir las fuentes simuladas sobre toda la esfera, una fracción sustancial cae fuera de la banda de declinación de HAWC y en regiones donde la densidad de alertas de IceCube y su eficiencia de detección de trazas son distintas a las de la banda real **[REF-6]**. Esto deprime artificialmente la media del MC y, en consecuencia, infla la significancia aparente de los datos reales. El efecto es puramente geométrico-instrumental, no físico: un modelo nulo válido debe preservar los efectos de selección observacional de ambos instrumentos **[REF-9]** **[REF-10]**. Por ello, todos los resultados de significancia de este trabajo se reportan con respecto al modelo de banda HAWC, y los resultados isotrópicos se presentan únicamente con fines ilustrativos de este sesgo.

El p-value empírico se definió como la fracción de realizaciones MC con un número de coincidencias mayor o igual al observado, $p = P(N_{\text{MC}} \geq N_{\text{obs}})$, y la significancia gaussiana equivalente como $z = (N_{\text{obs}} - \mu_{\text{MC}})/\sigma_{\text{MC}}$.

### X.2.3 Corrección por múltiples pruebas (_look-elsewhere effect_)

La evaluación de múltiples radios de búsqueda incrementa la probabilidad de obtener fluctuaciones significativas por azar **[REF-11]**. Se aplicó una corrección por _trials_ empírica: para cada realización MC se calculó el p-value mínimo entre todos los radios, y el p-value global _post-trials_ se definió como la fracción de realizaciones cuyo mínimo es menor o igual al mínimo observado. Como verificación conservadora se reporta además la cota de Bonferroni, $p_{\text{global}} \leq N_{\text{trials}} \cdot p_{\text{min}}$ **[REF-12]**.

### X.2.4 Pruebas complementarias

Para robustecer las conclusiones se realizaron cuatro pruebas independientes del conteo de coincidencias:

- **Test de Kolmogorov–Smirnov (KS) de dos muestras** **[REF-13]** sobre la distribución de distancias angulares mínimas de cada AGN a su neutrino más cercano, comparando los datos reales contra 1000 realizaciones del modelo nulo de banda HAWC. Esta prueba es sensible a desviaciones distribucionales que un conteo a radio fijo podría no capturar.
- **Estadístico ponderado por _signalness_:** $\text{Score} = \sum_i \max_j (S_j \cdot \mathbb{1}[\theta_{ij} < \theta_{\max}])$, que otorga mayor peso a coincidencias con neutrinos de alta probabilidad astrofísica.
- **Estadístico ponderado por energía:** análogo al anterior con pesos $\log_{10} E_j$, motivado por el aumento de la fracción astrofísica con la energía **[REF-14]**.
- **Correlación de Spearman** entre el _test statistic_ (TS) de HAWC de cada fuente y el número de neutrinos dentro de 1.5°, bajo la premisa de que si las fuentes gamma más brillantes produjeran neutrinos, se esperaría una correlación positiva.

## X.3 Resultados

### X.3.1 Coincidencias con contornos elípticos

Se observaron $N_{\text{obs}} = 32$ AGN dentro de algún contorno elíptico al 90% CL. La distribución MC (banda HAWC) arrojó $\mu = 34.9 \pm 4.9$, es decir, el número observado se encuentra ligeramente _por debajo_ de la expectativa de fondo: $p = 0.753$, $z = -0.60\sigma$. El resultado es plenamente compatible con la hipótesis nula.

### X.3.2 Coincidencias con radios fijos y comparación de modelos nulos

La Tabla X.1 resume los resultados para ambos modelos nulos.

|θ (°)|N_obs|MC isotrópico: μ ± σ|p (iso)|MC banda HAWC: μ ± σ|p (HAWC)|
|---|---|---|---|---|---|
|0.5|1|0.8 ± 0.9|0.5543|1.4 ± 1.2|0.7515|
|1.0|5|3.2 ± 1.8|0.2170|5.5 ± 2.3|0.6604|
|1.5|11|7.0 ± 2.6|0.0930|11.7 ± 3.2|0.6392|
|2.0|20|11.8 ± 3.3|0.0134|19.5 ± 3.9|0.4926|
|3.0|39|23.6 ± 4.3|0.0007|38.2 ± 4.8|0.4723|

**Tabla X.1.** Coincidencias observadas y esperadas bajo los dos modelos nulos para cada radio de búsqueda.

El contraste entre columnas ilustra de forma directa el sesgo del modelo isotrópico: bajo dicho modelo, los p-values decrecen sistemáticamente con el radio hasta alcanzar $p = 0.0007$ ($\sim 3.2\sigma$) en θ = 3°, un "exceso" aparente. Bajo el modelo de banda HAWC, que preserva la cobertura de declinación del catálogo, el mismo conteo observado resulta plenamente compatible con el fondo ($p = 0.47$ en θ = 3°; todos los radios con $p > 0.4$). La discrepancia entre ambos modelos crece con el radio porque a radios mayores el conteo se vuelve más sensible a la densidad local de neutrinos en la banda de declinación, que es justamente lo que el modelo isotrópico no reproduce.

### X.3.3 Significancia global

El p-value mínimo _pre-trials_ bajo el modelo de banda HAWC fue $p_{\min} = 0.4723$ en θ = 3.0°. Tras la corrección empírica por múltiples pruebas, el p-value global resultó $p_{\text{global}} = 0.767$; la cota de Bonferroni satura en 1.0. No existe evidencia de exceso en ningún radio, ni individual ni globalmente.

### X.3.4 Pruebas complementarias

- **Test KS:** $D = 0.072$, $p = 0.473$. Las distribuciones de distancia mínima de los datos reales (media 5.23°, mediana 4.51°) y del MC (media 5.45°, mediana 4.56°) son estadísticamente indistinguibles.
- **Ponderado por _signalness_** (θ = 1.5°): score real 5.12 frente a MC $5.49 \pm 1.60$; $p = 0.567$, $z = -0.23\sigma$.
- **Ponderado por energía** (θ = 1.5°): score real 22.93 frente a MC $26.29 \pm 7.20$; $p = 0.673$, $z = -0.47\sigma$.
- **Correlación TS–neutrinos:** no se observa tendencia positiva entre la significancia de detección en HAWC y el número de neutrinos cercanos **[COMPLETAR: ver nota metodológica sobre el coeficiente de Spearman en la sección de limitaciones; el valor ρ = −0.83 debe recalcularse con corrección por empates antes de reportarse]**.

Ninguna de las pruebas, individualmente ni en conjunto, muestra desviación significativa respecto de la hipótesis nula.

### X.3.5 Límites superiores a la fracción de fuentes multimensajero

Ante la ausencia de señal, se calcularon límites superiores al número de AGN con coincidencias genuinas mediante la aproximación gaussiana del perfil de verosimilitud **[REF-15]**:

$$\text{UL}(95\%,\text{CL}) = \max(0,, N_{\text{obs}} - \mu_{\text{MC}}) + 1.645,\sigma_{\text{MC}}$$

|Método|N_obs|Fondo (μ)|UL 90%|UL 95%|Fracción 95%|
|---|---|---|---|---|---|
|Elíptico 90% CL|32|34.9|6.2|8.0|5.9%|
|θ = 0.5°|1|1.4|1.5|1.9|1.4%|
|θ = 1.0°|5|5.5|2.9|3.7|2.8%|
|θ = 1.5°|11|11.7|4.1|5.2|3.9%|
|θ = 2.0°|20|19.5|5.5|6.9|5.1%|
|θ = 3.0°|39|38.2|7.0|8.7|6.5%|

**Tabla X.2.** Límites superiores al número (y fracción) de AGN con emisión de neutrinos detectable.

Con un 95% de nivel de confianza, **menos del ~6% de los 135 AGN leptónicos** del catálogo presentan emisión de neutrinos detectable con las sensibilidades actuales de IceCube (método elíptico).

### X.3.6 Fuentes individuales de interés

Aunque el análisis poblacional no revela exceso, la inspección por fuente identifica casos con coincidencias angularmente cercanas que conservan interés como candidatos individuales —un tipo de evidencia complementaria y distinto de la afirmación poblacional, en analogía con el caso de TXS 0506+056, identificado primero como coincidencia individual **[REF-4]**. Las fuentes más cercanas a una alerta incluyen J0816.9+2050 (BL Lac, 0.31° de IC230217A), J0211.2+1051 (0.58° de IC131014A, _signalness_ 0.67) y Mkn 421 (J1104.4+3812, 0.77° de IC111208A) **[COMPLETAR: si estas fuentes se discuten en un capítulo de perfiles individuales, referenciar la sección correspondiente]**. Cabe enfatizar que, dado el tamaño de las muestras, el número esperado de coincidencias casuales a estas distancias es del orden de las observadas, por lo que ninguna asociación individual puede reclamarse a partir de la coincidencia espacial únicamente.

## X.4 Discusión y nota metodológica

El resultado central de este capítulo es doble. Primero, **no se detecta correlación espacial significativa** entre los 135 AGN leptónicos de HAWC y las alertas de ICECAT-1: todos los tests arrojan $|z| < 1\sigma$ bajo el modelo nulo correcto, con un p-value global _post-trials_ de 0.77. Segundo, y de relevancia metodológica general, **la elección del modelo nulo domina por completo la significancia aparente**: el mismo conjunto de datos arroja $p = 0.0007$ bajo un _scrambling_ isotrópico y $p = 0.47$ bajo el _scrambling_ en banda. La lección es que un procedimiento de aleatorización que no preserva los efectos de selección observacional —en este caso, el campo de visión de HAWC y la dependencia en declinación de la eficiencia de IceCube— no constituye una línea base válida, y la "significancia" resultante es un artefacto del Monte Carlo, no una propiedad de los datos **[REF-9]** **[REF-10]**.

Físicamente, el resultado nulo es consistente con la expectativa _a priori_: la muestra fue seleccionada por mecanismos de emisión leptónicos, mientras que las fuentes con evidencia de neutrinos (TXS 0506+056, NGC 1068) requieren procesos hadrónicos **[REF-4]** **[REF-7]**. El límite superior derivado (<6% al 95% CL) acota cuantitativamente la componente hadrónica oculta admisible en blazares clasificados como leptónicos, en línea con restricciones poblacionales previas sobre la contribución de blazares al flujo difuso de neutrinos **[REF-16]**.

**Limitaciones.** (i) La aproximación elíptica de campo plano subestima distorsiones a declinaciones altas, aunque el efecto es menor dado que los errores típicos son ≲ 2°. (ii) Los errores de ICECAT-1 al 90% CL son estadísticos; las incertidumbres sistemáticas de reconstrucción pueden ampliar las regiones reales **[REF-2]**. (iii) El coeficiente de Spearman reportado en el análisis exploratorio (ρ = −0.83) se calculó sin corrección por empates; dado que la gran mayoría de las fuentes tiene cero neutrinos cercanos, los rangos están masivamente empatados y el valor numérico no es interpretable tal cual; debe recalcularse con el tratamiento estándar de empates (rangos promedio) y acompañarse de su p-value **[REF-13]**. (iv) El análisis es puramente espacial; no incorpora información temporal, que ha sido decisiva en asociaciones como la de TXS 0506+056 **[REF-4]**.

---

## Referencias sugeridas para cada marcador (VERIFICAR antes de citar)

- **[REF-1]** Catálogo HAWC: Albert, A., et al. (HAWC Collaboration), "3HWC: The Third HAWC Catalog of Very-high-energy Gamma-Ray Sources", _ApJ_ 905, 76 (2020). [Verificar que sea la versión del catálogo usada.]
- **[REF-2]** ICECAT-1: Abbasi, R., et al. (IceCube Collaboration), "ICECAT-1: The IceCube Event Catalog of Alert Tracks", _ApJS_ 269, 25 (2023).
- **[REF-3]** Mecanismos leptónicos en blazares: p. ej. Maraschi, Ghisellini & Celotti (1992); Böttcher et al. (2013), "Leptonic and Hadronic Modeling of Fermi-Detected Blazars", _ApJ_ 768, 54.
- **[REF-4]** TXS 0506+056: IceCube Collaboration et al., _Science_ 361, eaat1378 (2018) [multimensajero IC-170922A]; IceCube Collaboration, _Science_ 361, 147 (2018) [flare de neutrinos 2014–2015].
- **[REF-5]** Programa de alertas en tiempo real: Aartsen, M. G., et al., "The IceCube Realtime Alert System", _Astropart. Phys._ 92, 30 (2017).
- **[REF-6]** Sensibilidad de IceCube vs declinación: Aartsen, M. G., et al., "All-sky Search for Time-integrated Neutrino Emission from Astrophysical Sources with 7 yr of IceCube Data", _ApJ_ 835, 151 (2017), o la versión de 10 años (Aartsen et al. 2020, _PRL_ 124, 051103).
- **[REF-7]** NGC 1068: IceCube Collaboration, "Evidence for neutrino emission from the nearby active galaxy NGC 1068", _Science_ 378, 538 (2022).
- **[REF-8]** Búsquedas de contrapartes de alertas: p. ej. Giommi, P., et al. (2020), _A&A_ 640, L4, o trabajos de seguimiento de alertas individuales.
- **[REF-9]** Técnica de scrambling: Braun, J., et al., "Methods for point source analysis in high energy neutrino telescopes", _Astropart. Phys._ 29, 299 (2008).
- **[REF-10]** Importancia de preservar efectos de selección en el modelo nulo: puede citarse también Achterberg et al. (2006) o la metodología de los análisis de fuentes puntuales de IceCube.
- **[REF-11]** Look-elsewhere effect: Gross, E. & Vitells, O., "Trial factors for the look elsewhere effect in high energy physics", _Eur. Phys. J. C_ 70, 525 (2010); Lyons, L. (2008), _Ann. Appl. Stat._ 2, 887.
- **[REF-12]** Bonferroni: Bonferroni, C. E. (1936); o un texto estándar de estadística (p. ej. Feigelson & Babu, _Modern Statistical Methods for Astronomy_, 2012).
- **[REF-13]** Test KS y métodos numéricos: Press, W. H., et al., _Numerical Recipes_, 3.ª ed. (2007); Feigelson & Babu (2012).
- **[REF-14]** Flujo astrofísico difuso y fracción astrofísica vs energía: Aartsen, M. G., et al., "Evidence for High-Energy Extraterrestrial Neutrinos at the IceCube Detector", _Science_ 342, 1242856 (2013); actualizaciones del flujo difuso (p. ej. Abbasi et al. 2022).
- **[REF-15]** Límites superiores: para mayor rigor considerar Feldman, G. J. & Cousins, R. D., _Phys. Rev. D_ 57, 3873 (1998), o Rolke, Lopez & Conrad (2005); la aproximación gaussiana puede citarse vía Cowan, G., _Statistical Data Analysis_ (1998).
- **[REF-16]** Límites a la contribución de blazares: Aartsen, M. G., et al., "The contribution of Fermi-2LAC blazars to the diffuse TeV–PeV neutrino flux", _ApJ_ 835, 45 (2017).


## Estrategia Analítica

El análisis se estructura en componentes que se retroalimentan:

### Caracterización espectral

#### HAWC
- Se usan los datos de un nuevo estudio (aún sin publicar). Se tiene una muestra de 135 AGN cercanos a z<0.3 que son fuentes emisoras de rayos gamma, están incluidas en el Tercer Catálogo de Fuentes Duras de Fermi-LAT (3FHL) y localizadas dentro de 40$\degree$ del cenit dl HAWC, esta muestra fue analizada usando 9 años de datos del HAWC (2014-2024).
	- Se ajustó una serie de potencias con un término de atenuación por la luz de fondo extragaláctiva (EBM) a los espectros del HAWC.
		- Como resultado, tenemos que 5 fuentes presentan significancia >5$\sigma$ y 13 más fueron presentadas como detecciones marginales.
- El objetivo de usar esta muestra es buscar evidencia con respecto a la producción de neutrinos en AGNs que no han sido usados en estudios de este tipo, pues se integran esos nuevos 18 AGN detectados y disponibles a caracteriza su emision VHE promedio.

#### Fermi-LAT
- Parámetros del 4FHL
- SEDs GeV
- Análisis de variabilidad cuando exista curva de luz

#### SED combinada (GeV–TeV)
- Comparación directa entre Fermi y HAWC
- Evaluación de consistencia del espectro

### Búsqueda de coincidencias con IceCube
- Definir ventanas espaciales basadas en resolución combinada
- Buscar neutrinos dentro de esa región
- Corridas temporales centradas en flares gamma

### Significancia estadística
- Comparación con fondo atmosférico
- Número de coincidencias vs esperadas
- Corrección por búsquedas múltiples

---

# Pasos seguidos:
- Se documentaron unas pruebas


## Resultados Estadísticos (resumen)

| Test                            | Resultado         | p-value    | Interpretación                   |
| ------------------------------- | ----------------- | ---------- | -------------------------------- |
| Scrambling isotrópico 3°        | 39 vs 23.6        | 0.0007     | ⚠️ ARTEFACTO del modelo          |
| **Scrambling banda HAWC 3°**    | 39 vs 38.2        | **0.4723** | No significativo                 |
| Contornos elípticos 90% CL      | 32 vs 34.9        | 0.75       | Compatible con azar              |
| Corrección empírica post-trials | —                 | 0.7673     | No significativo                 |
| KS distancias angulares         | D=0.072           | 0.4725     | Distribuciones idénticas         |
| Ponderado signalness            | 5.12 vs 5.49      | 0.5674     | Sin señal (z=−0.23σ)             |
| Ponderado energía               | 22.9 vs 26.3      | 0.6728     | Sin señal (z=−0.47σ)             |
| Spearman TS vs neutrinos        | **ρ=−0.831**      | —          | Correlación negativa → leptónico |
| Upper limit 95% CL              | ~8 coinc. / ~5.9% | —          | Límite superior                  |

> **Conclusión global:** Ningún test muestra evidencia de correlación. Resultados consistentes con emisión leptónica para esta muestra.

## Detalles de cada análisis

Para el desarrollo completo de cada test, consultar las notas dedicadas:

- [[Modelo nulo de banda HAWC]] — Modelo isotrópico vs banda HAWC (la revelación clave)
- [[geometría de detecciones]] — Fórmula de Vincenty para distancias angulares
- [[Correccion de Bonferroni o Empirica]] — Look-Elsewhere Effect y correcciones post-trials
- [[Prueba KS de distancias angulares]] — Test de Kolmogorov-Smirnov
- [[Tests ponderados]] — Ponderación por signalness y energía
- [[Correlación TS vs neutrinos]] — Spearman ρ = −0.831
	- [[Corrección de Análisis - Spearman]]
- [[All/Problemas]] — Log de issues y correcciones aplicadas

## Mejoras propuestas (no implementadas)

1. **Stacking Likelihood**: Gaussiana 2D en vez de corte binario → $\Psi(\Delta r) = \frac{1}{2\pi\sigma^2} e^{-\Delta r^2/2\sigma^2}$
2. **Pesos astrofísicos**: por flujo/TS de HAWC → $S = \sum_i w_i \times \text{coincidencia}_i$
3. **Elipticidad completa**: Gaussiana 2D asimétrica → $\chi^2 = \Delta RA^2/\sigma_{RA}^2 + \Delta Dec^2/\sigma_{Dec}^2$
4. **Análisis TS formal**: $TS_{total} = \sum TS_i$ sobre todos los neutrinos
5. **Información temporal**: curvas de luz HAWC, flares, ventanas temporales

---

## Conexiones
- Anterior: [[DRAFTS - III.iii IceCube]]
- Siguiente: [[DRAFTS - V. Catálogo de Coincidencias]]
- Avances de reuniones: [[Avances Tesis]]
- Estadística de soporte: [[Estadística para Astrodatos/Estadística para Astrodatos]]
- Hub: [[XCRITURA]]
