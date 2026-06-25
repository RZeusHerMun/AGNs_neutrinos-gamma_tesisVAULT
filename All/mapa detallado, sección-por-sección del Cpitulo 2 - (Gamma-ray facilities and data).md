con: 1) traducción / transcripción literal de las ecuaciones clave; 2) interpretación física y práctica (por qué importa cada párrafo / figura / tabla); y 3) **cómo y dónde** cada elemento instrumental o analítico se usa después (capítulos 3–5). Me aseguré de hilar conceptos — no sólo definir cosas, sino mostrar el encadenamiento lógico que conduce a decisiones de análisis y a límites físicos. Cada afirmación importante lleva la cita al PDF para que puedas verificar el pasaje exacto. Vamos allá.

---

# Mapa detallado — Capítulo 2 (sección por sección)

## 2.1 Gamma-ray astronomy — propósito y panorama general

- Qué contiene: panorama de técnicas y rangos energéticos (space telescopes, IACTs, surface detectors/WCDs), y la idea de complementariedad entre cobertura, sensibilidad y duty-cycle.
**Interpretación hilada:**
- Espacio (Fermi-LAT): monitoreo continuo → ideal para variabilidad en GeV y construir la "columna vertebral" temporal de una SED (**Distribución Espectral de Energía**) quasi-simultánea.
- IACTs: sensibilidad espectral fina 0.1–10 TeV, pero sesgo a flares por bajo duty-cycle.
- Surface/WCD (HAWC, LHAASO): amplio FOV y duty-cycle → mide estados promedio y transientes largos en VHE; menor sensibilidad y PSF que IACTs.  
    Esto establece la regla metodológica: **si usas HAWC para VHE, esperes un espectro promedio**, y al combinar con IACTs debes checar ventanas temporales.
    
**Dónde se usa más adelante:**
- Para justificar el uso de HAWC para estudiar emisión promedio de M87 (Cap.3) y la survey AGN (Cap.4).
    

---

## 2.2 The Fermi Gamma-ray Space Telescope (LAT & GBM)

- Contenido: descripción del LAT (pair conversion, tracker+calorimeter, anticoincidence) y del GBM; LAT cubre ≈20 MeV – > 0.5 TeV y monitorea todo el cielo cada ~3 h. Menciona herramientas: Fermitools / Fermipy y tipos de análisis (binned/unbinned likelihood).
**Ecuaciones / conceptos técnicos relevantes (transcripción):**
- Tipos de ajuste espectral: power-law, log-parabola (mencionados textualmente como opciones en Fermipy).
    
**Interpretación hilada:**
- LAT define la parte GeV «temporalmente confiable» de las SEDs. Si HAWC y LAT difieren, primero verifica intervalos temporales y elección de forma espectral (power-law vs log-parabola), porque la forma elegida puede absorber curvaturas reales o producir discrepancias aparentes.
    
**Dónde se usa más adelante:**
- Construcción de SEDs quasi-simultáneas para 1ES 1215+303 y PG 1218+304 (Cap.5) y para M87 (Cap.3): LAT da la base GeV en los fits.
    
---

## 2.3 HAWC detector and analysis — (el núcleo operativo del capítulo)

Esta sección es la más densa y la que condiciona más el resto de la tesis. La voy a desglosar con cuidado.
### 2.3.1 Descripción física del detector

- HAWC = 300 WCDs; cada WCD: tanque 7.3 m diámetro × 5 m alto, 180 m³ de agua, 4 PMTs (1 × 10″ central + 3 × 8″ en triángulo). Ubicación: Sierra Negra, 4100 m a.s.l. Rango sensible ≈ 0.1–100 TeV.
**Por qué importa:** geometría y configuración de PMTs determinan las variables topológicas usadas en reconstrucción (timing, carga, patrón espacial) que separan γ/hadrones y estiman dirección/energía.

### 2.3.2 Gamma/hadron separation — variables topológicas

- **Compactness (C)** — **ecuación (2.1)** en el texto:  
$$    C = \frac{N_{\rm hit}}{C!xPE40}  $$
    donde $N_{\rm hit}$ = número de PMT hits en el evento y $CxPE40$= carga máxima (PE) registrada por un PMT fuera del radio de 40 m del núcleo. Compactness pequeño → hadrón (porque hadrónicos presentan altos $CxPE40$).
    
- **PINCness (P)** — mide χ² entre cargas observadas y la expectativa local (axial smoothness); P mayor → hadrón.

**Interpretación hilada:**
- Estas variables explotan la morfología: las lluvias gamma son más "suaves" y centradas; las hadrónicas producen "hot spots" lejos del core (muones, sub-showers). Por tanto, la eficacia de separación condiciona la eficiencia ($s/n$) y el flujo residual de fondo que hay que modelar en likelihood.
    

**Uso posterior:**

- Afecta directamente la significancia ($TS$) y el nivel de fondo en las fits de HAWC en Capítulos 3–5; por ejemplo, en multisource fits para dos blazars próximos, la separación ineficiente empeora la cross-contamination.
    

### 2.3.3 Estimación de energía — métodos y elección

- Se listan tres estimadores:
    1. **fhit** = fraction of hits = (#PMT hits) / (available PMTs) — usado para binificar eventos (B0–B10) y relacionar estadísticamente con energía mediana por bin. Tabla 2.1 muestra los rangos de fhit y las energías medianas Pass4 vs Pass5.
    2. **Ground parameter (GP)** = densidad de carga a distancia óptima del eje → estima energía.
    3. **Neural Network (NN)** = estimador basado en red neuronal con varios inputs de reconstrucción → mejor para altísimas energías (∼100 TeV) pero requiere optimización para <1 TeV.
**Clave práctica (decisión del autor):**
- _El autor usa fhit exclusivamente_ para este trabajo porque AGN son mejor observados a bajas energías (≲ a unos TeV) y fhit está optimizado allí. Esto implica que los puntos VHE reportados son **energías medianas por bin** y no medidas energéticas puntuales por evento.
**Consecuencia hilada:**
- Las migraciones de energía (eventos que deberían estar en otro bin) y la dispersión de la respuesta instrumental introducen **sesgo** en el índice espectral y en la normalización cuando se ajusta un power-law → hay que incluir la respuesta y la matriz de migración en el fitting (el autor lo hace mediante likelihood binned). Esto afecta la interpretación física (p. ej. si un espectro se ve muy blando, ¿es producto físico o espectral/instrumental?).
### 2.3.4 Test statistic (TS) y log-likelihood — ecuaciones del análisis
- **TS** (ecuación 2.2):  
$$    {\rm TS} = 2\ln\left(\frac{\mathcal{L}(S+B)}{\mathcal{L}(B)}\right)  $$
    donde ($\mathcal{L}$) es la verosimilitud del modelo.
    
- **Log-likelihood (Poisson)** (ecuación 2.3, versión textual en tesis):  
    $$\ln\mathcal{L}(S+B)=\sum_{B}\sum_{p} \ln\left(\frac{(B_p+S_p)^{M_p} e^{-(B_p+S_p)}}{M_p!}\right) $$
    con sumas sobre bins y píxeles (p) — típico likelihood Poisson para conteos por píxel/bin.

**Interpretación hilada:**
- El TS es el estadístico de decisión para declarar detección (p.ej. $\sqrt{\rm TS}$ ≈ σ en aproximación). El cálculo requiere modelar background ($B_p$) y la señal ($S_p$) (que incluye $PSF$ y respuesta energética). Las elecciones de binning, de forma espectral asumida (poder/law fijo α o libre), y la respuesta de energía influyen en ($\mathcal{L}$), por eso el autor detalla usos de índices fijos en algunas surveys.
**Uso posterior:**
- En Cap.4 (survey) se usan fits power-law con EBL y a veces índice fijo (por motivos estadísticos); en Cap.5 se hacen multisource fits y se usan TS para declarar detecciones / upper-limits. Las limitaciones del TS derivan de fhit/PSF y de Pass versión (ver más abajo).
    

### 2.3.5 Pass 4 vs Pass 5 — mejoras y efectos

- Cambios introducidos por _Pass 5_ (resumen literal en tesis):
    - Mejor resolución energética <1 TeV (noise suppression), correcciones sistemáticas en dirección/ núcleo, mejora angular hasta factor ×4, mejor separación gamma/hadron, aumento de significancia hasta ×4 en algunos casos.
**Consecuencia hilada:**
- Análisis anteriores (Pass 4) tienen peor PSF y energy response → pueden **subestimar** TS de fuentes débiles o mezclar fuentes cercanas. El autor aplica Pass 4 a Cap.3 (M87) porque datos/tiempo de análisis coincidían, mientras Pass 5 se usó en Cap.4 y Cap.5 (survey y blazars) mejorando sensiblidad. Esto obliga a cautela al comparar resultados entre capítulos: diferencia en detección/índice puede deberse a Pass version y no sólo a física.
**Dónde se us:**
- Comparación entre survey antiguo y actualizado (Cap.4) y en la interpretación de detecciones marginales en Cap.5 (1ES/PG).
    

### 2.3.6 Tabla fhit (Tabla 2.1) — rango de bins → energías medianas

- La tesis ofrece la Tabla 2.1 comparando Pass4 vs Pass5 bins y las energías medianas (Crab on/off array) para B0–B10. Ejemplo: B3 ~0.83 TeV (Pass5 median on-array) hasta B10 ~30 TeV.
**Interpretación práctica:**
- Cada punto espectral HAWC se asocia a una «energía mediana del bin», pero la anchura energética efectiva puede ser grande. Al hacer fits (power-law con EBL), los modelos deben foldarse con respuesta por bin, no comparar directamente flux(Emedian) con modelo sin convolución. El autor trabaja con likelihood que incorpora respuesta (implícito en la metodología).
**Uso posterior:**
- Fittings spectrales en Cap.3–5 (p.ej. límites de energía, comparación con IACTs) usan esa mapeo fhit→Emed para construir puntos; pero el texto también advierte sobre incertidumbres y migración.
---

## Figuras y su papel explicativo (traducción + interpretación)

- **Fig. 2.1**: All-sky Fermi map (>1 GeV) — contextualiza concentración de blazares extragalácticos.  
    _Uso:_ justifica selección de fuentes 3FHL/4FGL como candidatos para HAWC survey (Cap.4).
    
- **Fig. 2.2**: Curvas de sensibilidad comparadas (HAWC, LHAASO, CTA, VERITAS, MAGIC, HESS).  
    _Uso:_ explica por qué HAWC detecta emisiones promedio/altas energías mientras IACTs dominan en sensibilidad cerca de 1 TeV en observaciones dirigidas; contextualiza por qué algunos objetos aparecen en surveys HAWC pero con menor detalle que IACT.
    
- **Fig. 2.3**: Ilustración de Fermi y configuración LAT/GBM — referencia técnica sobre capacidades.
    
- **Fig. 2.4 / 2.5 / 2.6**: Imagen del array HAWC, esquema de WCD y comparación visual de evento gamma vs hadrón (morfología de hits). Estas figuras son didácticas pero contienen información operativa crítica para entender compactness / PINCness y fhit.
    
 ***faltan 2.7: histogramas de los resultado de los srveys de galaxias activas.. 
2.8; los flujos normalizados y espectros de las 5 agns mas significantes.
2.9; espectros de Mkr 421 y Mkr 501 que se han recabado en 10 años del hawc
2.10; SED de Mkr421 y Mk501, un modelo SSc y los puntos de radio a gamma que fueron quasi-simultaneos.

---

## 2.4 Data products, catalogs y decisiones de selección

- La tesis explica uso de catálogos Fermi (3FHL, 4FGL) para construir muestras de AGN (ej. sample z<0.3 para survey HAWC) y criterios de selección (corte en zenith/declinación para cobertura HAWC).
**Consecuencia hilada:**
- Selección de muestra → afecta sensibilidad estadística y corrección EBL (fuentes con z>0.3 fuertemente atenuadas y por tanto excluidas). Esto reduce sesgos de no-detección por EBL.    
**Uso posterior:**
- En Cap.4 la sample de 138 AGN z<0.3 se analiza con 8 años de HAWC; la selección se basa en 3FHL y en la visibilidad desde HAWC.

---

## 2.5 Limitaciones experimentales y sistemáticas — resumen y su encadenamiento lógico

La tesis lista y discute explícitamente varias fuentes de incertidumbre que hay que propagar:
1. **Respuesta energética / migración de bin** (fhit) → afecta índice y normalización.
2. **PSF amplia en bins bajos** → cross-contamination entre fuentes cercanas (ej. 1ES 1215+303 vs PG 1218+304 separadas 0.88°). Esto requiere multisource fitting.
3. **Evolución Pass4→Pass5** → cambios en PSF/energy response obligan a cautela al comparar capítulos.
4. **Modelo de background** y selección de cuts gamma/hadron (compactness/PINCness) → puede introducir sesgos en TS y en flux.

**Interpretación hilada (por qué esto es importante para tu tesis / análisis):**
- Cualquier conclusión física (p.ej. necesidad de componente hadrónico, o predicción de neutrinos) extraída de un fit que usa puntos HAWC **debe** reportar y propagar estas incertidumbres instrumentales antes de comparar con límites IceCube u IACTs. El autor lo hace; yo te indicaré en cada capítulo si la propagación fue suficiente y dónde conviene replicar los cálculos.
    

---

# Resumen ejecutivo — ¿qué debes retener y por qué importa para analizar los capítulos 3–5?

1. **HAWC da espectros promedio por bins fhit**; cada punto es una energía mediana con anchos efectivos y migración. No tratar esos puntos como “medidas puntuales” de energía cuando hagas interpretaciones físicas.
2. **Compactness y PINCness** son las variables principales para separar γ/hadron; su eficacia determina s/n y nivel de fondo—esto afecta TS y upper limits. En fuentes próximas (≤1°) la PSF y la separación gamma/hadron controlan si puedes separar emisiones por fuente.
3. **Pass 4 vs Pass 5**: cuando compares resultados entre capítulos, verifica qué _pass_ fue usado. Cambios en Pass 5 pueden explicar aumentos de TS o mejor desambiguación de fuentes.
4. **Fermi-LAT** aporta la columna vertebral GeV; discrepancias entre LAT y HAWC suelen indicar problemas de simultaneidad, elección de forma espectral o limitaciones instrumentales (más que fallos teóricos directos).
5. **TS y likelihood**: entiende que la metodología de la tesis usa likelihood Poisson binned (ecuaciones 2.2–2.3) y que los fits espectrales se realizan foldando modelos con la respuesta por bin; por tanto, cuando vea un índice o normalización, esto ya incluye la respuesta instrumental (pero también incluye incertidumbre de migración).
    

---

# Mapas puntuales: dónde se usan conceptos de Cap.2 en Cap.3, Cap.4 y Cap.5 (vínculo directo)

- **Cap.3 (M87)**
    - Uso de 1523 días de HAWC (estado promedio) → análisis Pass 4 (ver nota sobre Pass). Interpretaciones lepto-hadrónicas vs SSC dependen de que HAWC representa un estado promedio y de la respuesta energética fhit. Ver cómo se comparan predicciones neutrínicas con IceCube; la robustez depende de la incertidumbre sistemática listada en Cap.2.
- **Cap.4 (HAWC AGN survey)**
    - Selección 138 AGN (z<0.3) desde 3FHL; uso de Pass 5 para mejorar detecciones y significancia; fitting power-law + EBL usando TS definido en 2.3.3. Atención especial a índices fijos vs libres (decisión estadística explicada en Cap.2).
- **Cap.5 (1ES 1215+303 & PG 1218+304)**
    - Caso de cross-contamination por separación 0.88°: se realizó **multisource fit** para separar emisiones; tabla fhit/Emedian y Pass5 se usan para construir SEDs quasi-simultáneas y ajustar modelos (two-zone SSC, etc.). Los límites de energía y las comparaciones con IACTs se interpretan con la advertencia sobre migración y PSF.
        

---

# Qué puedo hacer ahora...

Quieres que hilemos aún más: puedo entregarte **para cada figura y ecuación del Cap.2**:

- Traducción literal + comentario línea a línea (por ejemplo: descomponer la ecuación de TS, explicar cada término del sumatorio, cómo se discretiza en píxeles y bins en HAWC).
    
- Una tabla que liste **cada variable instrumental** (compactness, PINCness, fhit, GP, NN, PSF) con: definición literal, rango típico, efecto más importante en resultados, y el capítulo(s) donde impacta.
    
- Re-escribir la metodología (paso a paso) que el autor usó para producir los puntos HAWC (desde selección de data → cuts → construcción del mapa → likelihood → fit), pero ahora en formato “checklist reproducible” con las ecuaciones necesarias para replicar los números (útil si quieres replicar o modificar un análisis).

$$𝐹var=⟨𝑓2⟩−⟨𝑓⟩2√⟨𝑓⟩$$


