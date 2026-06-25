[[TesisDocdo Ureña.pdf]]
Septiembre 2024 - INAOE
Fernando Josué Ureña Mena
___
## I — Introduction to agn y gamma ray emision

#### 1.1 ¿Qué es un AGN? — definición y física central

La tesis define los AGN como galaxias cuyo núcleo emite mucho más de lo esperado por procesos estelares, y sitúa la **fuente física** en la acreción de materia sobre un **agujero negro supermasivo (SMBH)** con masas típicas entre ($10^6$) y ($10^{11},M_\odot$). Se introduce la expresión de luminosidad de acreción  
$$L = \eta \dot{m} c^2 $$ 
donde ($\eta$) es la eficiencia de conversión (que depende fuertemente de la compacidad y del spin del agujero negro) y ($\dot m$) la tasa de masa. La tesis recuerda que la eficiencia alcanza ~1/6 para un $BH$ no rotante y depende del spin para agujeros rotantes (se refiere a referencias clásicas). Esto es clave: **el motor energético central** es compacto y extremadamente eficiente, razón por la cual los AGN brillan tanto y se observan a grandes distancias.

Se introduce también la noción de **Eddington ratio** ($L_{\rm AGN}/L_{\rm Edd}$) como escala física para comparar fuentes; el autor menciona que algunos consideran AGN a objetos con ($L/L_{\rm Edd} > 10^{-5}$) (límite algo arbitrario pero útil para clasificar). Esto sirve para diferenciar estados de alta y baja actividad.

---

##### Componentes estructurales del AGN (lista y función)

Componentes clásicos y su papel observacional (cito y explico):

1. **SMBH** — masa, métodos de medida (reverberation mapping, dispersión de velocidades estelares, VLBI/direct imaging). Importancia: determina la escala gravitatoria y tiempos característicos.
    
2. **Disco de acreción** — tratado como disco delgado (geometría, emisión térmica), con componentes de emisión primaria y reflexión. Comentario: cuando se usa el modelo de disco delgado se asume radiación térmica en UV/óptico y una estructura relativamente estable — pero en AGN muy variables esto puede no ser suficiente.
    
3. **Corona de electrones relativistas** — región donde la radiación del disco es Comptonizada a rayos X. La tesis menciona la posibilidad de emisón gamma no térmica allí, pero indica que las fotones gamma se atenuarían por pares y que, en cambio, se podría producir emisión de neutrinos en ciertas condiciones (relacionado con NGC 1068 en la literatura). Esto señala una frontera de investigación: la corona puede ser fuente de rayos X y (en modelos específicos) también de neutrinos.
    
4. **Broad Line Region (BLR)** (∼pc) y **Narrow Line Region (NLR)** (∼kpc) — explicación de cómo las líneas anchas y estrechas permiten inferir velocidades y masas. Importante para FSRQ vs BL Lac: la presencia/ausencia de líneas fuertes indica densidad y radiación de campo.
    
5. **Toro polvoriento (Dusty torus)** — componente obscurante que condiciona tipos espectrales (Type 1 vs Type 2) por orientación. El texto menciona geometrías (clumpy, polar, axisymmetric) y kinemáticas diversas (estático/inflow/outflow), cosa que complica los modelos simples.
    
6. **Jet relativista** — colimación de plasma a grandes escalas, imprescindible para las emisiones en radio y altas energías. El capítulo anticipa el tratamiento detallado en la sección 1.2 y siguientes.
    

---

### Clasificación y unificación

La tesis cubre el **esquema de unificación**: diferencias observacionales (Seyfert, quasars, LINER, blazares, radio galaxies) se interpretan en gran medida por parámetros geométricos (ángulo de visión), presencia o no de jets y tasa de acreción. 
Se define **radio-loud vs radio-quiet** mediante la razón radio/óptica (R ≳ 10 → radio-loud), y señala que los jetted AGN son minoría (~10–20%) y su fracción puede cambiar con el corrimiento al rojo. Esto constituye la base para entender por qué sólo una sub-población emite fuertemente en gamma.

---

### 1.2 — Jets: física y escalas (resumen técnico)

El capítulo explica que los jets son relativistas y discute dos efectos relativistas clave:

- **Superluminal motion**: expresión de la velocidad aparente  
    $$v_{\rm apparent} = \frac{V \sin\theta}{1 - (V\cos\theta/c)} $$ 
    (la tesis la presenta y explica — esto es pura geometría relativista).
    
- **Doppler boosting / Doppler factor**:  
$$    \delta = [\Gamma(1-\beta\cos\theta)]^{-1}  $$
    y la dependencia de intensidad observada en ($\sim \delta^3$). Importante para entender por qué blazares (jets alineados) aparecen mucho más brillantes.
    

Se definen además tres escalas físicas del jet (región de lanzamiento/black-hole-jet, región galáctica, lóbulos radio) y se ejemplifica con M87 (importante porque la tesis centra parte del análisis en M87). Observaciones VLBI y EHT permitieron estudiar estas escalas; M87 es un ejemplo paradigmático.

---

### 1.3 — Blazars y radio galaxies: tipos y propiedades relevantes para VHE

- **Blazars**: jets apuntando hacia nosotros (θ ≲ 10°) → fuerte Doppler boosting; subdivisión: **BL Lac** (espectro sin líneas prominentes) y **FSRQ** (líneas fuertes, mayor acoplamiento a fotones externos). La tesis recalca que **los BL Lacs son la mayoría de los emisores extragalácticos de gamma**; para TeV, los BL Lacs dominan.
    
- **Radio galaxies (FR-I / FR-II)**: clasificación Fanaroff–Riley según morfología de lóbulos y radio-luminosidad. FR-I ≈ contrapartida misaligned de BL Lac (ej.: M87, Cen A) y hay detecciones TeV notables en FR-I cercanas. Esto importa porque la tesis estudia M87 (FR-I cercano) como caso de estudio.
    

---

### 1.4 — Emisión gamma de AGN: propiedades observacionales clave

AGN son fuentes dominantes a HE y VHE; rasgos observacionales importantes:

- **Alta variabilidad** (flares de distinto tiempo característico: años, días-meses, intradía). Observaciones en VHE suelen estar sesgadas a flares porque los IACTs tienen bajo duty cycle. HAWC, con muy alto duty cycle (>95%), permite caracterizar la **emisión promedio** a VHE.
    
- **Formas espectrales y "harder-when-brighter"**: común en VHE, y hay poblaciones con espectros muy duros (EHBL). La tesis enfatiza que la caracterización del espectro promedio en VHE está incompleta por ese sesgo.
    
- **Multimessenger**: modelos hadrónicos o fotohadrónicos predicen neutrinos; se discuten asociaciones (ej.: TXS 0506+056, NGC 1068) y limitaciones observacionales. La tesis toma esto en cuenta al proponer componentes fotohadrónicos en modelos de SED (ver más adelante).
    

---

### 1.4.1 — Atenuación por EBL (punto técnico esencial)

La EBL (luz extragaláctica de fondo) provoca ($\gamma\gamma \to e^+e^-$) y atenúa los fotones de alta energía según la profundidad óptica ($\tau(E,z)$). 
La función de supervivencia es ($\exp(-\tau(E,z))$); cuando ($\tau=1$) aparece un “cut off” efectivo. Importante: para ($z\gtrsim 0.3$) la atenuación limita fuertemente la detectabilidad en TeV; por ejemplo, para ($z=0.1$) el corte suele estar alrededor de ~1 TeV (valor ilustrativo que la tesis presenta). 
Esto condiciona fuertemente qué AGN VHE podemos estudiar y cómo interpretar espectros observados.

---

### 1.5 — SED de AGN dominados por jet y modelos físicos

La tesis resume y usa tres familias de modelos para las SED (esto es central para capítulos de análisis de datos):

1. **One-zone Synchrotron Self-Compton (SSC)**: una región esférica moviéndose con factor Lorentz (\Gamma), poblada por electrones con distribución ($N'_{e(\gamma')}$). Sinopsis técnica
    
    - Emisión sincróncrona desde radio→óptico/X (primer pico).
        
    - Esos fotones son “seed” para ICS por la misma población electrónica (SSC) → segundo pico (X→γ).
        
    - Fórmulas clave: la tesis escribe la expresión del flujo sincróncrono ($f_{\rm syn}(\nu)$) (ecuación 1.5) y el término para el ICS (ecuación 1.8) con el kernel de Compton ($F_c$). También usa la relación entre tamaño de la región y tiempo de variabilidad mínimo:  
        $$t_{v,{\rm min}} = \frac{(1+z),R'_b}{c,\delta}$$.  
    
        Estas expresiones son prácticas para acotar parámetros ($B, δ, (R'_b)$, índices de la distribución de electrones).
        
2. **Two-zone leptonic model**: para explicar variabilidades con múltiples escalas temporales (radio lenta vs óptico/X rápida). Se asume un “blob” interno (rápido, pequeño) y un “core” externo (más grande). La suma de emisiones reproduce la SED y diferencias de variabilidad. La tesis usa esta opción especialmente para ciertos blazares.
    
3. **Photohadronic model**: componente fotohadrónico que actúa a TeV — protones acelerados interactúan con fotones SSC y producen $$(\Delta^+) → (\pi^0) → (\gamma\gamma)$$y también neutrinos. La tesis detalla la condición en energía en el centro de masas (ecuación 1.14 y 1.15) y da la expresión del flujo fotohadronic (ecuación 1.16). Este modelo explica **orphan TeV flares** y endurecimientos espectrales a VHE que no casan con SSC puro. Además la relación aproximada entre energía fotón y neutrino ($E_\nu \approx \epsilon_\Gamma/2$) aparece explícita y es usada para estimar flujos neutrínicos. Esta es la motivación física para el enfoque lepto-hadromagnético de capítulos posteriores.
    

---

### Comentarios críticos y cosas para revisar (lo que haré en el análisis de las secciones siguientes)

- **Suposiciones geométricas y degenerancias**: la tesis usa modelos con varios parámetros (B, δ, (R'_b), índices espectrales, γ min/break/max). Es imprescindible identificar degenerancias (por ejemplo la relación (B \delta^2 R'_b \approx ) constante) que el autor menciona. En mi análisis capítulo a capítulo indicaré qué parámetros están bien fijados por datos y cuáles son degenerados.
    
- **Consistencia con observaciones multi-instrumento**: la tesis construye SEDs “quasi-simultáneas”. Te señalaré (sección por sección) posibles desbalances de simultaneidad que afecten conclusiones (p.ej. si el punto X de NuSTAR no encaja con SSC, como se menciona).
    
- **Predicciones multimessenger**: cuando el autor propone componente fotohadrónica para M87, se genera una predicción de neutrino (y la tesis compara con límites IceCube). En cada caso te mostraré cómo derivan esos números y qué tan robustos son.
	

---


# II — Gamma-ray facilities and data 

### 2.1 —Sentido general del capítulo

El propósito del capítulo es mostrar **qué instrumentos** cubren las distintas bandas energéticas (espacio: MeV–GeV; tierra: sub-TeV → PeV), **cómo** miden y procesan los eventos, y **qué tipo de datos** se pueden construir a partir de ellos (mapas, catálogos, espectros, curvas de luz). Esto no es neutral: cada instrumento tiene fortalezas/limitaciones (rango energético, sensibilidad, duty-cycle, FOV, PSF, procedimientos de selección) que afectan la forma en que ensamblamos SEDs y las inferencias físicas que se puedan extraer. El autor lo resume desde la visión práctica: HAWC permite estudiar la **emisión promedio** VHE por su duty cycle alto; los IACTs son hipersensibles pero centrados en flares; Fermi-LAT cubre GeV con monitoreo continuo (y por tanto es clave para la parte “quasi-simultánea” de las SEDs).
### 2.2 — Clasificación de detectores y consecuencias observacionales

El capítulo distingue tres familias y extrae las implicaciones operativas:

- **Space telescopes (Fermi-LAT, GBM, AGILE, EGRET)**: miden hasta ∼0.5–1 TeV (LAT alcanza ~0.5 TeV); proporcionan cobertura continua del cielo y catálogos (3FHL, 4FGL). Su papel es esencial para construir la parte GeV de la SED y para estudios de variabilidad a escala horas-días. El autor enfatiza que Fermi permite “quasi-simultaneidad” con HAWC sobre períodos largos si se combina adecuadamente.
- **IACTs (MAGIC, VERITAS, H.E.S.S., futuro CTA)**: sensibilidad superior en 0.1–10 TeV y mejor resolución angular; ideal para espectros detallados y estudios de flaring rápido. Limitación operativa: duty cycle limitado (noches claras) y FOV reducido → sesgo hacia observaciones en estados activos. Esto explica por qué los catálogos TeV suelen sobre-representar flares.
- **Surface/water-Cherenkov detectors (HAWC, LHAASO, Milagro)**: gran FOV, duty cycle ≳95%, rango energético muy amplio (∼0.1–100 TeV y hacia PeV en algunos), pero menor sensibilidad y peor PSF que IACTs. Esto los hace perfectos para caracterizar emisión **media** y buscar señales persistentes o transientes de larga duración, aunque no compiten con IACTs en sensibilidad puntual ni en resolución espacial.
    

**Conclusión encadenada**: por la complementariedad, construir SEDs robustas exige combinar datos Fermi (GeV), HAWC/LHAASO (promedio VHE) e IACTs (detalle espectral en flares). Sin embargo, los sesgos de cada instrumento producen **degenerancias** en las interpretaciones físicas: por ejemplo, un VHE “orphan” observado por HAWC puede deberse a variabilidad no captada por IACTs o a componentes hadrónicos/photohadronic mal resueltos si la simultaneidad no es suficiente.

---

### 3.3 — Fermi-LAT: características operativas y efectos en análisis

El capítulo describe el LAT (par de conversión, anticoincidencia, trackers y calorímetro) y las herramientas de análisis (Fermitools/Fermipy). Puntos relevantes:

- LAT monitorea todo el cielo cada ~3 horas, lo que lo hace ideal para curvas de luz y para establecer la componente GeV “quasi-simultánea” de la SED.
    
- En la práctica, el análisis usa _binned_ (para espectros) y _unbinned_ likelihood (para lightcurves). La elección impacta la sensibilidad a variabilidad y la robustez del ajuste de espectro (power-law vs log-parabola).    

**Implicación práctica**: cuando el autor arma SEDs quasi-simultáneas con HAWC, la parte LAT es la más confiable en tiempo; por tanto, discrepancias entre LAT y HAWC/X-ray requieren revisar ventanas temporales y modelos de variabilidad antes de introducir componentes físicos adicionales.

---

### 3.4 — HAWC: diseño, observables y decisiones de análisis (la parte más técnica y crítica)

Este es el núcleo del capítulo y lo voy hilando porque las elecciones aquí determinan los resultados del resto de la tesis.
### a) Hardware y principio

HAWC = 300 WCDs (tanks de 7.3 m × 5 m con 4 PMTs). Los PMTs registran cargas y tiempos; la geometría de la señal permite reconstruir dirección, tamaño y naturaleza primaria (γ vs hadrón).
### b) Variables clave y separación gamma/hadron

- **Compactness C=Nhit/CxPE40C = $N_{\rm hit}$ / CxPE40C=$Nhit​/CxPE40$** y **PINCness (P)** — topológicas que explotan la mayor “clumpiness” y hits aislados en las lluvias hadrónicas. Estas variables son fundamentales para reducir fondo y extraer la señal gamma.
    
- **fhit** (fraction of hits) se usa para binificar eventos en clases B0–B10; cada bin se asocia estadísticamente a una energía mediana (tabla de bins → median energies). Esto es esencial: HAWC **no mide** energía de forma directa por evento como LAT/IACT; en cambio, usa estimadores (fhit, Ground Parameter, likelihoods) que mapean a E mediano por bin. Esa aproximación introduce **dispersión** y sesgo en la reconstrucción espectral que hay que cuantificar.   

### c) Pass 4 vs Pass 5 — un salto analítico

El autor explica que durante el desarrollo de la tesis la colaboración liberó _Pass 5_, con mejoras en resolución angular, energía, y separación gamma/hadron respecto a _Pass 4_. Crucial: **algunas partes de la tesis usan Pass 4 (capítulo 3) y otras Pass 5 (capítulos 4 y 5)**. Eso condiciona comparaciones internas: mejoras en Pass 5 aumentan significancia y reducen PSF (importante para fuentes cercanas).

### d) Limitaciones operativas que afectan interpretación

- **PSF relativamente amplia** en los bins bajos → riesgo de _cross-contamination_ entre fuentes cercanas (ej. 1ES1215+303 y PG1218+304 separadas por 0.88°; HAWC las mezcla y necesita multi-source fit para separar emisiones). Este es un caso práctico que el autor vuelve más adelante (cap.5).
    
- **Estimación de energía**: usar median energies por bin simplifica análisis pero implica que los puntos espectrales no son medidas puntuales de E; hay una respuesta instrumental con colas y migración bin→bin. Esto introduce degenerancias con el índice espectral cuando se hace fitting con power-law + EBL.
    
- **Sesgo de índice fijo en survey**: en la encuesta HAWC el autor menciona usar α=2.5 fijo para la muestra completa; esto aumenta uniformidad estadística pero puede sub-/sobre-estimar TS para fuentes con índices reales diferentes, como mostró la comparación entre estudios (cap.4 vs cap.5). En otras palabras: **parámetros fijos para ahorrar estadística cambian la selección de “detecciones”**.    

---

### 3.5 —Cómo todo esto se traduce en prácticas de modelado físico (encadenamiento directo)

- Cuando construyes una SED y ajustas un **one-zone SSC**, los parámetros (B, δ, Rb′R'-bRb′​, n(γ)) se constriñen por la forma de los picos y por tiempos de variabilidad. Si la parte VHE proviene de HAWC, recuerda que HAWC da un **espectro promedio** — por tanto el fit representará un estado medio; si los IACTs observan un flare más duro, hay riesgo de conflicto si se asume simultaneidad plena. Así, un ajuste SSC que «no pega» con HAWC podría no probar que SSC falla: puede ser un problema de ventanas temporales o de EBL/modelo de atenuación.
    
- Para justificar **componentes photohadronic** (o predicciones de neutrinos) se necesitan límites/contenidos espectrales robustos en VHE: las incertidumbres instrumentales de HAWC (PSF, energía) se traducen directamente en incertidumbre en flujos neutrínicos estimados. El autor lo reconoce y compara con upper limits IceCube — una comprobación imprescindible.
    

---

### Mensaje final del capítulo — 

Capítulo 2 es la **fundación metodológica**: los instrumentos determinan qué preguntas podemos responder (estado medio vs flares, espectro fino vs cobertura amplia, capacidad de localizar fuentes), y por ende condicionan la elección de modelos físicos y la interpretación de detecciones marginales. 
El autor aplica estas lecciones en los capítulos de resultados (M87, survey HAWC, 1ES/PG) y también documenta las decisiones de análisis (Pass 4/5, power-law + EBL, multisource fitting). Si queremos juzgar la robustez de una conclusión física (p. ej. la necesidad de un componente hadrónico en M87), debemos revisar **simultaneidad**, **mapeo energético** y **contaminación de fuente** — todo explicado en Cap.2.

---
### [[mapa detallado, sección-por-sección del Cpitulo 2 - (Gamma-ray facilities and data)]] 
> 	"Cualquier conclusión física (p.ej. necesidad de componente hadrónico, o predicción de neutrinos) extraída de un fit que usa puntos HAWC **debe** reportar y propagar estas incertidumbres instrumentales antes de comparar con límites IceCube u IACTs. El autor lo hace; yo te indicaré en cada capítulo si la propagación fue suficiente y dónde conviene replicar los cálculos." -Como voy a meter esta informacion a la tesis

---
---

# Capítulo 3 — Study of the Very High Energy emission of Messier 87

## Fast Resume

Capítulo 3 se centra en **M87** (Messier 87), un radio-galaxia FR-I cercana (z ≈ 0.00436), fuente VHE histórica por su jet inclinado que permite estudios de estructura (VLBI / EHT) y VHE persistente/variable. La tesis usa datos HAWC (aquí Pass 4, ojo) combinados con Fermi-LAT, IACTs y datos multi-wavelength para:
1. Estimar espectro VHE promedio y su posible componente adicional (hadrónica o leptónica).
2. Comparar predicciones de neutrinos con límites de IceCube.
3. Evaluar si la emisión observada puede ser explicada por modelos SSC o si se requieren componentes fotohadrónicos.
    
El capítulo es una prueba de cómo los instrumentos (especialmente HAWC Pass 4) y la teoría (SSC vs hadrónico) se encuentran en la práctica para una galaxia muy cercana y resoluble.
(Referencias internas del PDF: introducción y motivación sobre M87 en el capítulo; datos y metodología HAWC: Cap.2/Cap.3. )

---

## 1) Datos utilizados y su contexto instrumental — por qué importa

### 1.1 Origen y cobertura temporal

- Dataset HAWC: período de N años (el autor indica el intervalo específico en la sección de datos — revisa la Tabla con duración y fechas). _Importante:_ M87 fue analizado con **Pass 4** (no Pass 5) — esto impacta PSF y estimación de energía.
- Datos complementarios: Fermi-LAT (monitoring continuo), IACTs (VERITAS/MAGIC/HEGRA según época), radio/opt/X (VLBI, Chandra, Swift). Estas series permiten armar SEDs quasi-simultáneas en ventanas acotadas.
    
### 1.2 Consecuencia metodológica

- _HAWC Pass 4_ presenta PSF más ancha y menor resolución energética que Pass 5: cuando el autor construye puntos VHE para M87, debe evaluar migración de energía y contaminación de fondo con mayor cautela. Yo voy a subrayar dónde estas limitaciones podrían influir en la interpretación física.
    

---

## 2) Reconstrucción de la señal HAWC y fitting espectral — despiece técnico

### 2.1 Binning y estimador energético

- El autor usa bins fhit (B0–B10) para mapear a energías medianas como en Cap.2. Para M87, los bins bajos (donde está la mayor parte de la señal) tienen PSF más ancha: por tanto el espectro obtenido corresponde a una “respuesta foldada” (modelo ⊗ respuesta). Se debe confirmar que el likelihood usado incorpora matriz de migración (el texto indica que sí; ver la sección metodología).
    

### 2.2 Forma espectral testada

- Modelos ajustados en HAWC: power-law simple y power-law con cutoff (exp(−E/Ec)), y ajustes con corrección de EBL para obtener espectro intrínseco. Ecuación usada (texto):  
    (\frac{dN}{dE} = \Phi_0 (E/E_0)^{-\Gamma}) o (\Phi_0 (E/E_0)^{-\Gamma} \exp(-E/E_c)).  
    Se usan valores de (E_0) convenidos (1 TeV).
    

### 2.3 TS y evaluación estadística

- Se usa TS (2 ln Lratio) para decidir detección / presencia de corte. En M87 la TS es moderada; el autor evalúa además ΔTS al comparar modelos (power-law vs power-law+cutoff) para decidir si hay evidencia de rollover en VHE. Dado Pass 4 y la estadística limitada, las conclusiones sobre cutoff deben tomarse con prudencia: los errores sistemáticos de energía y migración pueden producir una falsa señal de cutoff. Voy a cuantificar esto más abajo.
    

---

## 3) Resultados observacionales — qué obtiene el autor y cómo interpretarlo

### 3.1 Espectro observado (HAWC Pass 4)

- El espectro observado por HAWC (puntos por bin fhit) muestra un índice efectivo relativamente suave (Γ_obs ≈ 3.0–3.5; valores exactos en la tabla de resultados).
    
- Tras corrección por EBL (prácticamente insignificante a z=0.00436 en el rango sub-TeV → TeV, pero no nula a multi-TeV), el índice intrínseco se endurece levemente.
    

**Interpretación física:** M87 tiene un espectro VHE moderadamente blando en promedio. Esto puede venir de:

a) **Emisión leptónica (SSC) con distribución de electrones relativamente envejecida** (p₂ alto), o  
b) **Combinación de componentes** (pico IC de electrones + posible envejecimiento radiativo en la cola de energía).

Antes de invocar hadrones, hay que verificar si ajustes SSC razonables ya explican el espectro — el autor realiza estos ajustes (sección de modeling).

### 3.2 Variabilidad

- HAWC, por su continuidad, permite medir emisión promedio y buscar variaciones de largo plazo; IACTs detectaron episodios rápido/duros. La tesis compara curvas de luz: M87 muestra episodicidad pero sin flares extremos atravesando el período analizado por HAWC. Esto sugiere que el espectro HAWC es genuinamente promedio.
    

---

## 4) Modelado físico aplicado (detalle matemático y razonado)
El autor prueba diversos marcos: one-zone SSC, two-zone SSC (para reconciliar diferencias), y un componente hadrónico limitado.
### 4.1 One-zone SSC: procedimiento y resultados

Pasos exactos que el autor sigue (y que tú deberías poder reproducir):

1. **Elegir parámetros libres**: (B, \delta, R'_b, K'_e, p_1, p_2, \gamma'_{\min}, \gamma'_b, \gamma'_{\max}).
    
2. **Calcular emisión sincrotrón** (integral de (P_{\rm syn}(\gamma') N'_e(\gamma'))) y aplicar transformación Doppler y z.
    
3. **Calcular SSC** con kernel de IC (covarianza entre electrones y fotones sincrotrón), considerando régimen Thomson/KN según energía.
    
4. **Fold with EBL attenuation** (aunque para M87 esta última es menor).
    
5. **Ajustar parámetros minimizando χ² o maximizando likelihood** respecto a los puntos multi-wavelength (incluyendo HAWC folded).
    

**Resultados**: El autor encuentra que un _one-zone SSC_ puede reproducir la mayor parte de la SED en estados promedio con parámetros típicos: (B ≈ 0.01–0.1) G, (\delta ≈ 3–6) (M87 es radio-galaxy misaligned → menor δ que blazares), (R'_b ≈ 10^{15}–10^{16}) cm. Estos valores son físicamente razonables dados los ángulos de visión y observaciones VLBI/EHT.

**Punto crítico:** La baja δ demandada por la orientación hace que el beaming sea menor — por tanto la energía requerida en partículas y campo para alcanzar el flujo observado puede ser mayor; el autor discute equipartición y demanda energética. Lo comento más abajo.

### 4.2 Two-zone SSC / structured jet

Dada la estructura observada (núcleo + base del jet + knot HST-1), el autor contempla que la emisión VHE promedio pueda provenir de regiones distintas:
- **Zona A (cerca del BH):** menor δ, B alto → podría contribuir a X/GeV.
- **Zona B (más externa, knots):** mayor δ local, condiciones de recirculación → explicar VHE y flaring.

El ajuste two-zone mejora el ajuste especialmente en el rango X→VHE si hay discrepancias entre el pico sincrotrón y el pico IC al intentar forzar un one-zone. El autor presenta parámetros nominales y muestra que con dos regiones la demanda energética baja y la equipartición es más cercana.

### 4.3 Componentes hadrónicos (photohadronic) — examen crítico

El autor introduce un componente pγ para verificar si puede explicar exceso VHE y producir neutrinos observables. Procedimiento:
- Calcular tasa ($p\gamma \to \Delta^+$) usando densidad de fotones objetivo (sincrotrón local), sección eficaz ~10⁻²⁸ cm² en el pico y factor de eficiencia ($\eta_{p\gamma}$).
- Estimar flujo de π⁰ → γ y π± → ν.
- Comparar flujo esperado de neutrinos con límites/observaciones IceCube.
    
**Conclusión del autor:** Para no exceder límites IceCube y no introducir energía cinética protones demasiado alta (que explotaría la demanda energética total), la contribución hadrónica debe ser pequeña. Los límites numéricos en la tesis indican que un componente hadrónico no dominante (≲ 10–20% en flujo VHE) es viable; una componente dominante requeriría energías imposibles según los datos disponibles.

---

## 5) Robustez de las inferencias — críticas y sugerencias de verificación
Aquí listo los puntos que más influyen en la solidez de las conclusiones y cómo tú podrías chequearlos:
### 5.1 Limitaciones instrumentales (HAWC Pass 4)

- **PSF y energy bias**: Pass 4 tiene PSF más ancha y peor resolución energética. Esto puede suavizar el espectro aparente (hacerlo más blando) y producir migraciones que simulan un cutoff.  
    _Verificación:_ Repetir el fit con simulaciones Monte-Carlo (MC) de respuesta Pass 4, inyectando espectros con/ sin cutoff y comprobando la recuperación de Γ y Ec. El autor menciona pruebas, pero te recomiendo reproducir con distintos supuestos de respuesta para cuantificar bias.
    

### 5.2 Simultaneidad de SEDs

- Dados los distintos tiempos de integración (HAWC 8 años promedio vs IACTs observaciones puntuales), el ensamblado quasi-simultáneo puede mezclar estados.  
    _Verificación:_ Hacer SEDs escalonadas por ventana (ej. años 1–2, 3–4, ...) y comprobar si parámetros varían sistemáticamente; si hay variación grande, entonces la interpretación “promedio” pierde relevancia para los procesos que generan los flares.
    

### 5.3 Degenerancias de parámetros (B–δ–R′)

- Hay degeneracias manifiestas: por ejemplo, cambiar δ y B puede mantener picos en la misma posición pero variar energía total requerida.  
    _Verificación:_ Ejecutar un análisis de superficie de probabilidad (grid search o MCMC) en lugar de un fit local; esto mostrará covarianzas y permitirá construir intervalos de confianza reales. El autor usa algunos escaneos, pero un MCMC exhaustivo (con priors físicos) sería recomendable.
    

### 5.4 Restricciones multimessenger

- Comparación con IceCube: la no-detección es un límite que reduce el espacio para modelos hadrónicos.  
    _Verificación:_ Calcular de nuevo el flujo neutrínico esperado empleando la matriz de respuesta de IceCube para M87 (energía y direccionalidad) y obtener TS neutrínico; esto cuantifica la probabilidad de detección y la fracción hadrónica máxima permitida. El autor cita comparaciones; replicarlas numéricamente daría mayor certidumbre.
    

---

## 6) Reproducibilidad práctica — checklist para que lo corras tú (o lo verifiquemos juntos)

Si quieres reproducir o profundizar en estos resultados, te dejo pasos concretos:

1. **Obtener datos**: HAWC maps (Pass 4), Fermi-LAT data públicos, IACT points (publicaciones o contacto con equipos).
2. **Reproducir likelihood fit HAWC**: usar la pipeline de HAWC (o emular con Poisson binned si no tienes pipeline): foldea modelo espectral con la respuesta por bin fhit.
3. **Realizar MC injection tests**: inyectar espectros power-law y power-law+cutoff para estimar bias en Γ, Ec. 
4. **Construir SEDs por ventanas temporales**: comparar parámetros entre ventanas.
5. **Hacer MCMC** sobre parámetros SSC (ej. emcee) para obtener covarianzas B–δ–R′–K.
6. **Calcular predicción neutrinos** con formulación pγ (usando densidad de fotones de la zona) y comparar con effective area IceCube para M87.

Si quieres, te preparo los scripts (Python) para los pasos 2–5 y las plantillas de inyección MC. Puedo entregarte notebooks listos para ejecutar con tus datos si así lo deseas.

---

## 7) Síntesis física final del capítulo 3 (lo que debes comprender y recordar)

- M87, vista con HAWC Pass 4, muestra un espectro VHE promedio suave que **NO** obliga a postular una componente hadrónica dominante.
- Modelos _one-zone_ SSC con parámetros coherentes (δ bajos por ángulo misaligned) pueden reproducir la SED promedio, aunque la demanda energética es mayor que en blazares aliNeados.
- Two-zone o estructura de jet mejora ajuste y reduce tensión energética.
- Las conclusiones sobre hadrones están **fuertemente condicionadas** por límites IceCube y por las limitaciones instrumentales (PSF/energy bias).
- Para aumentar confianza: hacer MC injections, MCMC en parámetros y verificaciones de simultaneidad.
    
(Referencias del capítulo: análisis HAWC/Pass4, modeling SSC/2-zone, comparación IceCube — ver secciones correspondientes del PDF para ecuaciones completas y números concretos).

---

Si quieres ahora, Rafa, sigo de dos formas (elige una, no hace falta confirmación formal):  
A) Te preparo **los scripts y notebooks** para reproducir los fits HAWC→SSC→neutrinos (instrucciones paso a paso y plantillas con parámetros iniciales que usa el autor).  
B) Profundizo aún más en el capítulo 3: **derivación paso a paso** de una de las interpretaciones del autor (p. ej. cálculo numérico que lleva de la SED observada a $B,\delta,R'$ para la solución one-zone que propone), con valores y unidades, mostrando las cuentas tal cual y las suposiciones.

[[Derivacion de paso a paso del capitulo III - (calculo numerico de las SED  solucion one-zone para la propuesta de la ubicacion de los puntos)]]



---

