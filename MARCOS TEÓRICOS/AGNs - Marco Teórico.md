---
fecha: 2026-07-16
tipo: marco-teorico
forma_nota: marco-teorico
seccion_destino: "[[II.i Fenomenología de los AGNs]]"
tags:
  - tema/agn
  - proyecto/tesis-multimensajera
  - tesis/marco-teorico
  - estado/activo
---
> Un núcleo activo de galaxia es un centro galáctico que brilla más que todas las estrellas de su galaxia juntas, alimentado por la caída de materia sobre un agujero negro supermasivo. Este marco va de lo general a lo singular: del motor gravitacional que comparten todos los AGNs a su anatomía y el modelo unificado, hasta el caso extremo en que el jet apunta a la Tierra: el blazar, el objeto de estudio de esta tesis.

[[Cascada conceptual - Jets Relativistas.svg]]

## Por qué este marco

La tesis busca correlación espacial entre los neutrinos astrofísicos de IceCube y las fuentes de rayos gamma de HAWC y Fermi-LAT. Para eso hay que saber qué objeto puede acelerar protones a energías ultrarrelativistas y a la vez dominar el cielo en rayos gamma. La respuesta observacional son los blazares, pero un blazar no se entiende aislado: es un AGN visto desde un ángulo privilegiado. Este marco arma ese argumento y termina donde empieza [[II.ii Jets Relativistas]]: la física del plasma dentro del jet.

> [!note] Comentario del asesor atendido
> Este texto responde al comentario #8 ("este capítulo sobre los AGNs en general debe ir más cerca del principio"): el esquema de clasificación unificado aparece inmediatamente después del motor central, antes de cualquier mecanismo de emisión. Ver [[Escritura/Comentarios del Asesor]].

---

## 1. El motor central: gravedad convertida en luz

La historia de los núcleos activos comienza como una anomalía espectroscópica. Fath (1909) registró líneas de emisión inusualmente intensas en el núcleo de la "nebulosa espiral" NGC 1068, y Seyfert (1943) identificó una clase de galaxias espirales cuyos núcleos, puntuales y brillantes, exhibían líneas de emisión anchas imposibles de atribuir a poblaciones estelares. El problema se volvió cuantitativo con Schmidt (1963): al reconocer que las líneas de la fuente de radio 3C 273 eran líneas de hidrógeno corridas a $z = 0.158$, la "estrella" se convirtió en el objeto más luminoso conocido hasta entonces, con $L \sim 10^{46}\text{–}10^{47}$ erg s$^{-1}$ —cientos de veces la luminosidad de una galaxia entera— emergiendo de una región que la variabilidad temporal restringía a escalas menores que un parsec. Ninguna población estelar, por masiva que fuera, produce tanta energía en tan poco volumen. Eso define operacionalmente a un núcleo activo de galaxia (AGN, por sus siglas en inglés): una región nuclear compacta cuya emisión —un continuo no estelar que abarca del radio a los rayos gamma, líneas de emisión intensas y variabilidad rápida— no puede explicarse por estrellas, gas ni polvo de la galaxia anfitriona (Netzer 2015; Padovani et al. 2017).

Que los cuásares más luminosos estén casi siempre a distancias cosmológicas no es casualidad: la densidad espacial de cuásares alcanzó su máximo en $z \approx 2\text{–}3$, la llamada "época de los cuásares", y ha decaído desde entonces (Padovani et al. 2017). Hoy sabemos además que prácticamente toda galaxia masiva alberga un agujero negro supermasivo (SMBH) en su centro, con masas que correlacionan con las propiedades del bulbo galáctico (Kormendy & Ho 2013). La diferencia entre una galaxia "normal" y una activa no es la presencia del agujero negro sino su estado: un núcleo *activo* es un SMBH que está acretando materia a una tasa significativa. La actividad es una fase transitoria en la vida de las galaxias; del orden del 1 al 10 % de ellas la exhiben en el universo local, dependiendo del umbral de luminosidad (Ho 2008; Netzer 2015). La Vía Láctea, con Sgr A* prácticamente en ayuno, es el contraejemplo cercano.

El motor que explica esta energética fue propuesto de forma casi simultánea por Salpeter (1964) y Zel'dovich (1964), y consolidado por Lynden-Bell (1969): la acreción de materia sobre un agujero negro supermasivo de $10^6\text{–}10^{10}\ M_\odot$. El argumento es termodinámico. La materia que cae hacia el SMBH conserva momento angular y forma un disco de acreción; la viscosidad del disco transporta momento angular hacia afuera y masa hacia adentro, disipando energía potencial gravitacional como calor que el disco radia térmicamente (Shakura & Sunyaev 1973). La eficiencia radiativa de este proceso, $L = \eta \dot{M} c^2$, va de $\eta \approx 0.057$ para un agujero negro de Schwarzschild hasta $\eta \approx 0.3$ para uno de Kerr en rotación máxima (Novikov & Thorne 1973): entre uno y dos órdenes de magnitud por encima del 0.7 % de la fusión del hidrógeno. Es el mecanismo más eficiente que se conoce para convertir masa en radiación de forma sostenida (Rees 1984). Para las masas involucradas, el disco alcanza temperaturas de $10^4\text{–}10^5$ K y emite un espectro térmico compuesto que domina en el óptico-ultravioleta, el llamado *big blue bump*.

La cota superior de esta luminosidad la impone la propia radiación. Cuando la presión de radiación sobre los electrones del plasma acretado iguala la atracción gravitacional sobre los protones, la acreción se autorregula; ese equilibrio define la luminosidad de Eddington (Eddington 1926),

$$L_{\rm Edd} = \frac{4\pi G M m_p c}{\sigma_T} \simeq 1.26 \times 10^{38} \left(\frac{M}{M_\odot}\right) \ \text{erg s}^{-1},$$

donde $\sigma_T$ es la sección eficaz de Thomson y $m_p$ la masa del protón. Invertir este argumento es lo que justifica las masas: las luminosidades observadas de $10^{44}\text{–}10^{48}$ erg s$^{-1}$ exigen $M \gtrsim 10^6\text{–}10^{10}\ M_\odot$ para no exceder el límite. Durante décadas ésta fue una inferencia indirecta; la imagen de la sombra de M87* obtenida por el Event Horizon Telescope, con $M = (6.5 \pm 0.7) \times 10^9\ M_\odot$ (EHT Collaboration 2019), la convirtió en una medición directa.

## 2. Anatomía de un AGN y el modelo unificado

Alrededor de ese motor común se organiza una estructura cuyas piezas modulan lo que finalmente observamos. De adentro hacia afuera: el disco de acreción (escalas de $\sim 10^{-3}$ pc) emite el continuo térmico óptico-UV; una corona de plasma caliente sobre el disco comptoniza fotones del disco y produce la ley de potencias en rayos X; a distancias de días-luz a meses-luz ($\sim 10^{-3}\text{–}10^{-1}$ pc), nubes densas ($n_e \gtrsim 10^9$ cm$^{-3}$) que orbitan el SMBH a $10^3\text{–}10^4$ km s$^{-1}$ reprocesan el continuo y generan las líneas de emisión anchas: la *Broad Line Region* (BLR). Envolviendo todo lo anterior, a escalas de $\sim 0.1\text{–}10$ pc, se extiende un toroide de gas y polvo —hoy entendido como una distribución grumosa más que como una dona sólida (Netzer 2015)— que absorbe la radiación del núcleo y la reemite en el infrarrojo. Mucho más afuera, a cientos de parsecs y hasta escalas de kiloparsec, gas menos denso y más lento ($\sim 10^2$ km s$^{-1}$) produce las líneas angostas de la *Narrow Line Region* (NLR), que al estar fuera del toroide es visible desde cualquier orientación. Finalmente, una fracción minoritaria de los AGNs —del orden del 10 %, los llamados *radio-loud* o, en la nomenclatura física propuesta por Padovani (2017), *jetted*— lanza jets bipolares relativistas perpendiculares al plano del disco (Kellermann et al. 1989; Blandford, Meier & Readhead 2019).

![[canvas agns.png|900]]
*Estructura interna de un AGN y clases observacionales según el ángulo de visión.*

La evidencia de que esta anatomía es universal —y no un catálogo de objetos intrínsecamente distintos— llegó por espectropolarimetría: Antonucci & Miller (1985) detectaron en NGC 1068, una Seyfert 2 "sin" líneas anchas, esas mismas líneas anchas reflejadas en luz polarizada. La BLR estaba ahí, oculta tras el toroide, visible solo en el espejo del gas circundante. Sobre esa base, Antonucci (1993) formuló el modelo unificado en su versión mínima: todos los AGNs comparten la misma estructura interna, y la dicotomía entre tipo 1 (con líneas anchas) y tipo 2 (sin ellas) es pura orientación del toroide respecto a la línea de visión. Urry & Padovani (1995) extendieron el esquema a los AGNs con jets, incorporando el segundo efecto geométrico: la amplificación relativista de la emisión del jet cuando éste apunta hacia el observador. La idea central es que el zoológico de los AGNs (Seyferts, radiogalaxias, cuásares, blazares) se reduce en primera aproximación a dos parámetros: la potencia intrínseca del sistema y el ángulo $\theta$ entre el eje de simetría —el eje de rotación del disco y del jet— y nuestra línea de visión.

## 3. El filtro geométrico: la perspectiva del observador

Tomarse en serio el modelo unificado significa que clasificar AGNs es, en buena medida, medir ángulos. Con visión cercana al plano ecuatorial ($\theta \to 90°$), el toroide intercepta la línea de visión: el disco y la BLR quedan ocultos y observamos objetos tipo 2 (Seyfert 2, radiogalaxias de líneas angostas). A ángulos intermedios, el núcleo queda expuesto y aparecen las Seyfert 1 y los cuásares tipo 1, cuyo espectro está dominado por la emisión térmica del disco y las líneas de la BLR. Si el AGN posee jets y lo vemos de lado, la emisión extendida de los lóbulos domina en radio y hablamos de radiogalaxias, cuya morfología separó Fanaroff & Riley (1974) en las clases FR I (de baja potencia, brillo decreciente hacia afuera) y FR II (de alta potencia, con *hotspots* terminales). Para esta tesis la consecuencia práctica es que la gran mayoría de los AGNs, vistos desde estas orientaciones, están dominados por procesos térmicos (disco, líneas, polvo) cuyo techo energético está en el ultravioleta y los rayos X. La termodinámica del disco, por violenta que sea, no produce fotones de TeV ni neutrinos de PeV. Para eso se necesita el ingrediente no térmico: los jets bipolares de plasma relativista que los AGNs *jetted* expulsan a lo largo del eje de rotación (Blandford & Königl 1979; Blandford, Meier & Readhead 2019), y se necesita, además, mirarlos casi de frente.

La geometría hace de esa condición un filtro severo. La fracción de cielo que subtiende un cono de semiapertura de $10°$ es $1 - \cos 10° \approx 1.5\,\%$ por jet: aun contando ambos jets, solo unos pocos por ciento de los AGNs con jets tienen uno apuntando aproximadamente hacia la Tierra. De la población total de AGNs, los que combinan tener jet y tenerlo alineado son del orden del 1 %. Esa rareza juega a favor: el cielo extragaláctico de altas energías queda dominado por una subclase pequeña, bien definida y catalogada.

## 4. Blazares: el laboratorio multimensajero

Esa subclase son los blazares: AGNs con jets cuyo ángulo de visión tiende a cero ($\theta \lesssim 10°$, y típicamente $\theta \sim 1/\Gamma$, con $\Gamma \sim 10$ el factor de Lorentz del flujo). Comprenden dos familias espectroscópicas. Los FSRQs (*Flat Spectrum Radio Quasars*) conservan líneas de emisión anchas e intensas (ancho equivalente $> 5$ Å en reposo) y discos luminosos; los objetos BL Lac presentan continuos casi sin rasgos, con líneas débiles o ausentes (Stickel et al. 1991; Urry & Padovani 1995). En el esquema unificado, unos y otros son las contrapartes alineadas de las radiogalaxias FR II y FR I, respectivamente, y la secuencia continua de propiedades espectrales entre ambas familias —la "secuencia blazar"— traza en última instancia la potencia de acreción del sistema (Fossati et al. 1998; Ghisellini et al. 2017).

Bajo esta geometría el sistema cambia de régimen: la emisión térmica del disco, las líneas y el toroide quedan opacadas por el continuo no térmico del jet. La razón es relativista y se cuantifica con el factor de amplificación Doppler,

$$\delta = \left[\Gamma\,(1 - \beta \cos\theta)\right]^{-1},$$

cuya derivación cinemática se desarrolla en [[II.ii Jets Relativistas]]; aquí basta enunciar sus consecuencias. Para $\theta \to 0$, $\delta \sim 2\Gamma$: el flujo observado se amplifica por factores de $\delta^{3\text{–}4}$ (hasta $10^{3}\text{–}10^{4}$ para $\delta \sim 10$), las energías de los fotones se corren hacia arriba por $\delta$ y las escalas de tiempo se comprimen por $\delta^{-1}$ (Urry & Padovani 1995). Este *beaming* explica de golpe las tres firmas fenomenológicas de los blazares: su dominio absoluto del cielo gamma extragaláctico —en el catálogo 4LAC de Fermi-LAT, el 98 % de los AGNs detectados son blazares, y los blazares constituyen más de la mitad de todas las fuentes del 4FGL (Ajello et al. 2020, 2022)—, su variabilidad extrema en escalas de minutos a semanas (que por causalidad, $R \lesssim c\,\Delta t\,\delta/(1+z)$, acota regiones emisoras compactas), y sus movimientos aparentemente superlumínicos en radio.

![[BZCAT_ait_transparent.gif]]
*Distribución en el cielo de los blazares del catálogo Roma-BZCAT (Massaro et al. 2015).*

Para la astrofísica multimensajera, el mismo beaming que amplifica los fotones amplifica cualquier producto secundario emitido por el jet. Si el jet acelera protones además de electrones, las interacciones hadrónicas ($p\gamma$, $pp$) producen piones cuyo decaimiento genera simultáneamente rayos gamma (vía $\pi^0$) y neutrinos (vía $\pi^\pm$), con direcciones confinadas al mismo cono relativista que la luz (véase [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]). Los blazares son así los candidatos naturales a fuentes de neutrinos astrofísicos: máxima luminosidad gamma aparente, geometría favorable y reservorio energético suficiente. La evidencia empírica llegó en septiembre de 2017, cuando el neutrino IceCube-170922A ($\sim 290$ TeV) coincidió con un flare de rayos gamma del blazar TXS 0506+056, con significancia de $3\sigma$ (IceCube Collaboration et al. 2018). Fue la primera asociación multimensajera de una fuente extragaláctica de altas energías y es el antecedente directo del análisis de correlación que desarrolla esta tesis.

## 5. Cierre: del disco al jet

El disco de acreción y su termodinámica explican por qué existen los AGNs y fijan su presupuesto energético, pero no producen las señales que registran HAWC, Fermi-LAT o IceCube. En un blazar, todo lo que llega a esos detectores —fotones de GeV-TeV y, potencialmente, neutrinos de TeV-PeV— nace en el plasma relativista del jet y está modulado por su cinemática. El paso siguiente es abandonar el sistema de referencia del disco y trabajar en el del jet: derivar el factor de Lorentz $\Gamma$, el movimiento superlumínico aparente y la forma exacta del factor Doppler $\delta$ ([[II.ii Jets Relativistas]]), para después poblar ese jet con los mecanismos de radiación leptónicos y hadrónicos que compiten por explicar su espectro ([[II.iii Radiación y Mecanismos de Emisión]]).

---

## Referencias

- Ajello, M., et al. (2020), *The Fourth Catalog of Active Galactic Nuclei Detected by the Fermi-LAT*, ApJ 892, 105 — [arXiv:1905.10771](https://arxiv.org/abs/1905.10771)
- Ajello, M., et al. (2022), *The Fourth LAT AGN Catalog — Data Release 3*, ApJS 263, 24 — [arXiv:2209.12070](https://arxiv.org/abs/2209.12070)
- Antonucci, R. (1993), *Unified models for active galactic nuclei and quasars*, ARA&A 31, 473 — [ADS](https://ui.adsabs.harvard.edu/abs/1993ARA%26A..31..473A)
- Antonucci, R., & Miller, J. S. (1985), *Spectropolarimetry and the nature of NGC 1068*, ApJ 297, 621 — [ADS](https://ui.adsabs.harvard.edu/abs/1985ApJ...297..621A)
- Blandford, R., & Königl, A. (1979), *Relativistic jets as compact radio sources*, ApJ 232, 34 — [ADS](https://ui.adsabs.harvard.edu/abs/1979ApJ...232...34B)
- Blandford, R., Meier, D., & Readhead, A. (2019), *Relativistic jets from active galactic nuclei*, ARA&A 57, 467 — [arXiv:1812.06025](https://arxiv.org/abs/1812.06025)
- Eddington, A. S. (1926), *The Internal Constitution of the Stars*, Cambridge University Press
- EHT Collaboration (2019), *First M87 Event Horizon Telescope Results. I. The Shadow of the Supermassive Black Hole*, ApJL 875, L1 — [DOI](https://doi.org/10.3847/2041-8213/ab0ec7)
- Fanaroff, B. L., & Riley, J. M. (1974), *The morphology of extragalactic radio sources of high and low luminosity*, MNRAS 167, 31P — [ADS](https://ui.adsabs.harvard.edu/abs/1974MNRAS.167P..31F)
- Fath, E. A. (1909), *The spectra of some spiral nebulae and globular star clusters*, Lick Obs. Bull. 5, 71 — [ADS](https://ui.adsabs.harvard.edu/abs/1909LicOB...5...71F)
- Fossati, G., et al. (1998), *A unifying view of the spectral energy distributions of blazars*, MNRAS 299, 433 — [arXiv:astro-ph/9804103](https://arxiv.org/abs/astro-ph/9804103)
- Ghisellini, G., et al. (2017), *The Fermi blazar sequence*, MNRAS 469, 255 — [arXiv:1702.02571](https://arxiv.org/abs/1702.02571)
- Ho, L. C. (2008), *Nuclear activity in nearby galaxies*, ARA&A 46, 475 — [arXiv:0803.2268](https://arxiv.org/abs/0803.2268)
- IceCube Collaboration, et al. (2018), *Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A*, Science 361, eaat1378 — [DOI](https://doi.org/10.1126/science.aat1378)
- Kellermann, K. I., et al. (1989), *VLA observations of objects in the Palomar Bright Quasar Survey*, AJ 98, 1195 — [ADS](https://ui.adsabs.harvard.edu/abs/1989AJ.....98.1195K)
- Kormendy, J., & Ho, L. C. (2013), *Coevolution of supermassive black holes and their host galaxies*, ARA&A 51, 511 — [arXiv:1304.7762](https://arxiv.org/abs/1304.7762)
- Lynden-Bell, D. (1969), *Galactic nuclei as collapsed old quasars*, Nature 223, 690 — [ADS](https://ui.adsabs.harvard.edu/abs/1969Natur.223..690L)
- Massaro, E., et al. (2015), *The 5th edition of the Roma-BZCAT*, Ap&SS 357, 75 — [arXiv:1502.07755](https://arxiv.org/abs/1502.07755)
- Netzer, H. (2015), *Revisiting the unified model of active galactic nuclei*, ARA&A 53, 365 — [arXiv:1505.00811](https://arxiv.org/abs/1505.00811)
- Novikov, I. D., & Thorne, K. S. (1973), *Astrophysics of black holes*, en *Black Holes (Les Astres Occlus)*, ed. C. DeWitt & B. DeWitt, p. 343
- Padovani, P. (2017), *On the two main classes of active galactic nuclei*, Nature Astronomy 1, 0194 — [arXiv:1707.08069](https://arxiv.org/abs/1707.08069)
- Padovani, P., et al. (2017), *Active galactic nuclei: what's in a name?*, A&ARv 25, 2 — [arXiv:1707.07134](https://arxiv.org/abs/1707.07134)
- Rees, M. J. (1984), *Black hole models for active galactic nuclei*, ARA&A 22, 471 — [ADS](https://ui.adsabs.harvard.edu/abs/1984ARA%26A..22..471R)
- Salpeter, E. E. (1964), *Accretion of interstellar matter by massive objects*, ApJ 140, 796 — [ADS](https://ui.adsabs.harvard.edu/abs/1964ApJ...140..796S)
- Schmidt, M. (1963), *3C 273: a star-like object with large red-shift*, Nature 197, 1040 — [ADS](https://ui.adsabs.harvard.edu/abs/1963Natur.197.1040S)
- Seyfert, C. K. (1943), *Nuclear emission in spiral nebulae*, ApJ 97, 28 — [ADS](https://ui.adsabs.harvard.edu/abs/1943ApJ....97...28S)
- Shakura, N. I., & Sunyaev, R. A. (1973), *Black holes in binary systems. Observational appearance*, A&A 24, 337 — [ADS](https://ui.adsabs.harvard.edu/abs/1973A%26A....24..337S)
- Stickel, M., et al. (1991), *The complete sample of 1 Jy BL Lacertae objects. I.*, ApJ 374, 431 — [ADS](https://ui.adsabs.harvard.edu/abs/1991ApJ...374..431S)
- Urry, C. M., & Padovani, P. (1995), *Unified schemes for radio-loud active galactic nuclei*, PASP 107, 803 — [arXiv:astro-ph/9506063](https://arxiv.org/abs/astro-ph/9506063) — PDF local: [[AGNs Urry & Padovani (1995).pdf]]
- Zel'dovich, Ya. B. (1964), *The fate of a star and the evolution of gravitational energy upon accretion*, Sov. Phys. Dokl. 9, 195

## 🔗 Conexiones

- Sección de escritura destino: [[II.i Fenomenología de los AGNs]] / [[DRAFTS - II.i Fenomenología de los AGNs]]
- Continúa en: [[II.ii Jets Relativistas]] (cinemática, derivación de $\delta$) y [[II.iii Radiación y Mecanismos de Emisión]]
- Marco hermano: [[Neutrinos - Marco Teórico]] — el otro mensajero de la correlación
- Conexión física central: [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]
- Muestra observacional: [[Catalogo de Coincidencias Multimensajero.  AGN vs Neutrino]]
- Seguimiento de correcciones: [[Escritura/Comentarios del Asesor]]
- Hub: [[XCRITURA]]
