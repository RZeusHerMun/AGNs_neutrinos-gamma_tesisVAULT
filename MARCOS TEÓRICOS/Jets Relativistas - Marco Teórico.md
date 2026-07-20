---
fecha: 2026-07-16
tipo: marco-teorico
forma_nota: marco-teorico
seccion_destino: "[[II.ii Jets Relativistas]]"
tags:
  - tema/jets
  - proyecto/tesis-multimensajera
  - tesis/marco-teorico
  - estado/activo
---
> Un jet relativista es plasma magnetizado lanzado desde la vecindad inmediata de un agujero negro supermasivo a velocidades que difieren de la de la luz en menos de un uno por ciento. Este marco sigue la energía en su recorrido: de dónde sale (el espín del agujero negro), cómo se propaga (cinemática relativista y el factor Doppler $\delta$) y cómo termina depositada en partículas individuales de energías ultrarrelativistas. El resultado es la población no térmica que la sección [[II.iii Radiación y Mecanismos de Emisión]] convertirá en fotones gamma y, si hay protones, en neutrinos.

## Por qué este marco

La sección [[II.i Fenomenología de los AGNs]] cerró con una limitación física: la termodinámica del disco de acreción, por extrema que sea, tiene su techo en el ultravioleta y los rayos X. Los fotones de TeV que detecta HAWC y los neutrinos de TeV–PeV que registra IceCube exigen otra cosa: partículas individuales con energías comparables a las de los rayos cósmicos más energéticos, confinadas en un flujo que apunta hacia nosotros. Ese flujo es el jet. Aunque en el esquema de la tesis esta sección aparece separada, no es un tema aparte: es la continuación directa de la fenomenología de los AGNs —el mismo objeto, visto ahora desde el sistema de referencia del plasma— y el requisito para entender los mecanismos de emisión. Sin jet no hay blazar, y sin la física del jet no se puede justificar por qué buscamos neutrinos precisamente en las posiciones de las fuentes gamma.

![[Cascada conceptual - Jets Relativistas.svg]]
*Cascada conceptual del capítulo: los fundamentos del SMBH al centro, las capas II.i → II.iii creciendo hacia afuera, y la profundidad del recorrido desembocando en el caso explícito (TXS 0506+056) que motiva la correlación de esta tesis.*

## 1. El problema energético: el disco no alcanza

La primera pregunta es de contabilidad. Las potencias de los jets, estimadas de forma independiente a partir de la energética de los lóbulos de radio, de las cavidades que inflan en el gas intracúmulo y del modelado de sus espectros gamma, van de $10^{43}$ a $10^{48}$ erg s$^{-1}$ (Celotti & Ghisellini 2008). El análisis sistemático de los blazares de Fermi-LAT arrojó un resultado incómodo para el paradigma de acreción pura: la potencia del jet excede, de forma sistemática, la luminosidad del disco que lo alimenta, en promedio por un orden de magnitud (Ghisellini et al. 2014). Un mecanismo que solo recicle energía gravitacional del gas acretado no puede sostener ese balance.

El reservorio que falta lo señaló Penrose (1969) como posibilidad teórica: un agujero negro de Kerr almacena energía en su rotación, y esa energía es extraíble desde la ergosfera. La cantidad disponible es enorme. Para un agujero negro de masa $M$ y espín adimensional $a_*$,

$$E_{\rm rot} = M c^2\left[1-\sqrt{\tfrac{1}{2}\left(1+\sqrt{1-a_*^2}\,\right)}\right],$$

que alcanza el 29 % de $Mc^2$ para rotación máxima. En un SMBH de $10^9\ M_\odot$ eso equivale a $\sim 5\times10^{62}$ erg: suficiente para sostener un jet de $10^{45}$ erg s$^{-1}$ durante más que la edad del Universo. El problema deja de ser energético y pasa a ser mecánico: hace falta un agente que convierta rotación del espacio-tiempo en un flujo dirigido de plasma.

## 2. El lanzamiento: Blandford–Znajek, Blandford–Payne y los discos magnéticamente detenidos

Ese agente es el campo magnético. En el mecanismo de Blandford & Znajek (1977), el disco de acreción sostiene un campo poloidal que atraviesa el horizonte de sucesos. Dentro de la ergosfera, el arrastre del espacio-tiempo (*frame dragging*) obliga a las líneas de campo a rotar con el agujero; el retorcimiento de las líneas genera una diferencia de potencial y un circuito de corrientes que transporta energía hacia afuera como flujo de Poynting a lo largo del eje de rotación. El agujero negro funciona como un dinamo: pierde momento angular y alimenta un flujo electromagnético cuya potencia escala como

$$P_{\rm BZ} = \frac{\kappa}{4\pi c}\,\Phi_{\rm BH}^2\,\Omega_{\rm H}^2, \qquad \Omega_{\rm H} = \frac{a_*\,c}{2\,r_{\rm H}},$$

donde $\Phi_{\rm BH}$ es el flujo magnético que atraviesa el horizonte, $\Omega_{\rm H}$ la velocidad angular del horizonte de radio $r_{\rm H}$ y $\kappa \approx 0.05$ una constante que depende débilmente de la geometría del campo (Tchekhovskoy et al. 2011; Blandford, Meier & Readhead 2019). La dependencia cuadrática en $\Phi_{\rm BH}$ y en el espín contiene la física esencial: para un jet potente se necesita un agujero que rote rápido y un disco capaz de acumular mucho flujo magnético sobre él.

El caso límite de esa acumulación es el disco magnéticamente detenido (MAD, *magnetically arrested disk*): el flujo magnético se apila sobre el horizonte hasta que su presión obstruye la propia acreción (Narayan et al. 2003). Las simulaciones magnetohidrodinámicas en relatividad general de Tchekhovskoy et al. (2011) mostraron que, en ese régimen, la eficiencia del jet definida como $\eta = P_{\rm jet}/\dot{M}c^2$ alcanza $\sim 140\,\%$ para $a_* = 0.99$. Una eficiencia mayor que el cien por ciento solo es posible si el flujo saliente lleva más energía que la que entra por acreción, es decir, si está drenando el espín del agujero: fue la primera demostración numérica del mecanismo de Penrose–Blandford–Znajek operando de forma sostenida. La correlación observada entre potencia de jet y luminosidad de acreción en blazares es consistente con campos magnéticos en ese valor máximo saturado (Ghisellini et al. 2014). Del lado observacional, la interferometría de base muy larga ancla el lanzamiento a la escala prevista: en M87 la base del jet se ubica a decenas de radios gravitacionales del agujero negro (Hada et al. 2011), y las imágenes a 3.5 mm muestran de forma directa la conexión entre el flujo de acreción anular y la base del jet (Lu et al. 2023; EHT Collaboration 2019).

Existe un segundo mecanismo, complementario, que no involucra al agujero sino al disco: en el modelo de Blandford & Payne (1982), las líneas de campo ancladas al disco en rotación actúan como guías magnetocentrífugas que aceleran un viento de plasma desde la superficie del disco. La imagen contemporánea combina ambos: un núcleo interno (*spine*) electromagnético lanzado por Blandford–Znajek, envuelto por una capa (*sheath*) más lenta y cargada de masa lanzada por el disco (Blandford, Meier & Readhead 2019; Boccardi et al. 2017).

Lo que sale de esa máquina no es todavía el jet que observamos. Cerca de la base, el flujo está dominado por energía electromagnética: su magnetización $\sigma$ —el cociente entre flujo de Poynting y flujo de energía cinética— es mucho mayor que uno. A lo largo de la zona de aceleración y colimación, el gradiente de presión magnética empuja el plasma y convierte $\sigma \gg 1$ en $\sigma \lesssim 1$, con el factor de Lorentz creciendo hasta saturar en $\Gamma \sim 10\text{–}30$ a escalas de parsecs (Vlahakis & Königl 2004; Marscher et al. 2008). En M87, el único jet donde esta región se resuelve espacialmente, el perfil del flujo es parabólico (colimado por el medio externo) hasta $\sim 10^5$ radios de Schwarzschild y se vuelve cónico (expansión libre) a partir de ahí (Asada & Nakamura 2012). Esa transición marca el final de la fábrica y el inicio del canal de propagación que, en las radiogalaxias, termina depositando la energía en los lóbulos a escalas de kiloparsecs.

## 3. Cinemática relativista: la ilusión que gobierna los observables

Todo lo que medimos de un jet está filtrado por su velocidad. Para un flujo con $\beta = v/c$, el factor de Lorentz es

$$\Gamma = \frac{1}{\sqrt{1-\beta^2}},$$

y los valores inferidos para blazares ($\Gamma \sim 10\text{–}30$) implican que el plasma recorre un año luz quedando apenas unas horas o días por detrás de los fotones que emite. Esa persecución casi empatada entre fuente y señal produce el efecto más contraintuitivo de la disciplina: el movimiento superlumínico aparente. Rees (1966) lo predijo cuando aún no existía la técnica capaz de verlo; cinco años después, la interferometría de base muy larga lo confirmó en 3C 279 (Whitney et al. 1971). El cálculo es puramente geométrico: un nodo que se mueve con velocidad $\beta$ a un ángulo $\theta$ de la línea de visión casi alcanza a sus propios fotones, de modo que el intervalo entre dos posiciones observadas se comprime y la velocidad aparente proyectada en el cielo resulta

$$\beta_{\rm app} = \frac{\beta\,\sin\theta}{1-\beta\,\cos\theta},$$

que se maximiza en $\beta_{\rm app} = \beta\Gamma$ cuando $\cos\theta = \beta$. No hay violación de causalidad: hay un cronómetro engañado. El programa MOJAVE, tras dos décadas de monitoreo de cientos de jets a 15 GHz, encuentra velocidades aparentes de hasta $\sim 50c$, lo que fija de forma directa la cota $\Gamma \gtrsim 50$ para los flujos más rápidos (Lister et al. 2019).

El parámetro que condensa toda la cinemática para un observador es el factor Doppler,

$$\delta = \left[\Gamma\,(1-\beta\cos\theta)\right]^{-1},$$

que combina la dilatación temporal relativista con el efecto clásico de la fuente que se acerca. Para $\theta = 1/\Gamma$, $\delta = \Gamma$; para $\theta \to 0$, $\delta \to 2\Gamma$. En blazares toma valores típicos de 10 a 50. Tres observables se transforman con él. Las frecuencias se corren hacia arriba, $\nu_{\rm obs} = \delta\,\nu_{\rm em}$, desplazando la emisión hacia los rayos X y gamma. Los tiempos se comprimen, $\Delta t_{\rm obs} = \Delta t_{\rm em}/\delta$, lo que permite que regiones de tamaño considerable produzcan variabilidad de minutos. Y el flujo se amplifica como $F_{\rm obs} = \delta^{p}\,F_{\rm em}$, con $p = 3+\alpha$ para un nodo discreto y $p = 2+\alpha$ para un jet continuo de índice espectral $\alpha$ (Urry & Padovani 1995): para $\delta \sim 10$, un factor de $10^3$ a $10^4$. Es la razón por la que un blazar opaca a su propia galaxia y por la que el cielo gamma extragaláctico está dominado por la minoría de AGNs que nos apuntan.

Este beaming resuelve además dos anomalías que fueron históricamente incómodas. La primera es la temperatura de brillo: las fuentes compactas de radio parecen exceder el límite de $\sim 10^{12}$ K por encima del cual las pérdidas Compton inversas deberían apagar la fuente en la llamada catástrofe Compton (Kellermann & Pauliny-Toth 1969); con $T_{b,{\rm obs}} = \delta\,T_{b,{\rm int}}$, las temperaturas intrínsecas quedan bajo el límite. La segunda es la variabilidad extrema en el TeV: los flares de PKS 2155-304, con tiempos de duplicación de $\sim 200$ s (Aharonian et al. 2007), y los de Mrk 501, de pocos minutos (Albert et al. 2007), implican por causalidad regiones emisoras de radio $R \lesssim c\,\Delta t\,\delta/(1+z)$, comparables o menores que el horizonte del propio agujero negro si $\delta$ no es grande. La revisión de Hovatta & Lindfors (2019) resume el estado de estas restricciones. Para la tesis hay una consecuencia que conviene dejar explícita desde ahora: cualquier producto secundario del jet —incluidos los neutrinos— sale confinado al mismo cono relativista que los fotones. El beaming que selecciona a los blazares como fuentes gamma dominantes los selecciona también como los candidatos naturales a fuentes de neutrinos puntuales.

## 4. Aceleración de partículas: choques, reconexión y el límite de Hillas

Queda el último eslabón: pasar de un fluido rápido a partículas individuales de energías macroscópicas. Los espectros de los blazares son leyes de potencias, no cuerpos negros, y una ley de potencias pide un mecanismo que procese partículas de forma iterativa, sin escala de energía privilegiada. La idea fundacional es de Fermi (1949): partículas cargadas que rebotan contra irregularidades magnéticas en movimiento ganan energía en promedio, porque los choques frontales son más probables que los alcances. En su versión original el proceso es de segundo orden —la ganancia por ciclo escala como $(V/c)^2$, con $V$ la velocidad de las nubes magnéticas— y resulta demasiado lento para ser el acelerador principal.

La versión eficiente apareció al aplicar el mismo principio a un frente de choque (Axford et al. 1977; Krymskii 1977; Bell 1978; Blandford & Ostriker 1978). En la aceleración difusiva por choques (DSA), la partícula cruza el frente repetidamente, dispersada por turbulencia magnética a ambos lados, y en cada ciclo de ida y vuelta el salto de velocidades del fluido le aparece como una colisión frontal: la ganancia es de primer orden, $\langle\Delta E/E\rangle \propto \beta_{\rm ch}$. La competencia entre esa ganancia y la probabilidad de que la partícula sea arrastrada corriente abajo y escape produce, sin ajustes finos, el espectro

$$\frac{dN}{dE} \propto E^{-p}, \qquad p = \frac{r+2}{r-1},$$

donde $r$ es el cociente de compresión del choque (Drury 1983). Para un choque fuerte no relativista, $r = 4$ y $p = 2$; para choques relativistas, el valor de referencia es $p \approx 2.2$ (Kirk et al. 2000; Achterberg et al. 2001). Que los índices espectrales inferidos en blazares ronden estos valores es uno de los argumentos de consistencia del paradigma. Los sitios naturales para estos choques dentro del jet son las colisiones entre capas eyectadas con distinto $\Gamma$ —los choques internos (Rees 1978; Spada et al. 2001)— y los choques de recolimación donde el jet se reajusta contra el medio (Marscher et al. 2008). Esta identificación tiene una consecuencia observacional directa: los flares son los episodios de inyección. Cada fulguración marca el momento y el lugar donde una nueva población de partículas aceleradas entra en escena, y por eso los flares gamma funcionan como las ventanas temporales donde una contraparte de neutrinos es más probable.

La DSA no opera en cualquier condición: requiere que la energía del flujo sea cinética. En las regiones internas donde $\sigma \gtrsim 1$, los choques son débiles y el mecanismo pierde eficiencia; ahí el candidato es la reconexión magnética, que disipa el propio campo y transfiere su energía a las partículas. Las simulaciones cinéticas muestran que la reconexión relativista genera también leyes de potencias, tanto más duras cuanto mayor es $\sigma$ (Sironi & Spitkovsky 2014), y el modelo de "jets dentro del jet" —plasmoides de reconexión moviéndose relativísticamente dentro del flujo ya relativista— ofrece la explicación más natural de la variabilidad de minutos en el TeV (Giannios et al. 2009). Choques y reconexión no compiten: se reparten el jet, la reconexión cerca de la base magnetizada y los choques aguas abajo.

Sea cual sea el mecanismo, hay una cota geométrica superior que todo acelerador debe respetar: la partícula solo sigue ganando energía mientras su giro de Larmor quepa en la región aceleradora. Ese es el criterio de Hillas (1984),

$$E_{\max} \simeq Z\,e\,B\,R\,\beta \approx 3\times10^{18}\ \text{eV}\;Z\,\beta\left(\frac{B}{1\ \text{G}}\right)\left(\frac{R}{10^{16}\ \text{cm}}\right),$$

con $Z$ la carga, $B$ el campo magnético y $R$ el tamaño de la región. Con los valores típicos de la zona de emisión de un blazar ($B \sim 0.1\text{–}1$ G, $R \sim 10^{16}\text{–}10^{17}$ cm), los protones pueden alcanzar $10^{17}\text{–}10^{19}$ eV: los jets de AGN ocupan desde el trabajo original de Hillas la esquina del diagrama reservada a los candidatos a rayos cósmicos ultraenergéticos. Para la conexión multimensajera basta bastante menos. En las interacciones fotohadrónicas, cada neutrino se lleva del orden del 5 % de la energía del protón padre ($E_\nu \approx E_p/20$), de modo que los neutrinos de 0.1–1 PeV que IceCube atribuye a fuentes astrofísicas requieren protones de $10^{16}\text{–}10^{17}$ eV. Los jets de blazares cumplen ese requisito con margen holgado.

## 5. Cierre: la población que va a radiar

El balance de este marco es una cadena causal completa. El espín del agujero negro, extraído electromagnéticamente vía Blandford–Znajek en regímenes de acreción magnéticamente saturada, carga un flujo de Poynting que la zona de aceleración y colimación convierte en plasma con $\Gamma \sim 10\text{–}30$. Visto casi de frente, ese flujo se observa amplificado por $\delta^{3\text{–}4}$, acelerado en apariencia hasta $\sim 50c$ y comprimido en el tiempo. Dentro de él, choques internos y reconexión magnética mantienen poblaciones de partículas con espectros $dN/dE \propto E^{-2}$ a $E^{-2.2}$, con protones —si los hay— hasta energías que sobran para alimentar el flujo de neutrinos astrofísicos.

Lo que este marco deja pendiente, deliberadamente, es la radiación. Una población de electrones acelerados emite sincrotrón y Compton inverso: esa es la vía leptónica, que no produce ningún neutrino. Una población de protones acelerados, interactuando con los campos de fotones del propio jet ($p\gamma$) o con gas ($pp$), produce piones cuyo decaimiento genera a la vez rayos gamma ($\pi^0 \to \gamma\gamma$) y neutrinos ($\pi^\pm \to \mu\nu_\mu \to e\,\nu_e\nu_\mu\bar{\nu}_\mu$): esa es la vía hadrónica, la única que convierte a un blazar en fuente de neutrinos. Distinguir cuánto pesa cada vía en cada fuente es exactamente lo que hace valiosa la correlación espacial y temporal entre ambos mensajeros: la coincidencia del neutrino IceCube-170922A con un flare gamma de TXS 0506+056 (IceCube Collaboration et al. 2018a) y el exceso de neutrinos de 2014–2015 desde la misma dirección (IceCube Collaboration et al. 2018b) son, hasta ahora, la evidencia más directa de que la vía hadrónica opera en al menos un jet. La física de estos dos canales de emisión, y la atenuación que el fondo de luz extragaláctica impone a los fotones en su viaje, es el contenido de [[II.iii Radiación y Mecanismos de Emisión]].

---

## Referencias

- Achterberg, A., Gallant, Y. A., Kirk, J. G., & Guthmann, A. W. (2001), *Particle acceleration by ultrarelativistic shocks: theory and simulations*, MNRAS 328, 393 — [ADS](https://ui.adsabs.harvard.edu/abs/2001MNRAS.328..393A)
- Aharonian, F., et al. (H.E.S.S. Collaboration) (2007), *An exceptional very high energy gamma-ray flare of PKS 2155-304*, ApJL 664, L71 — [arXiv:0706.0797](https://arxiv.org/abs/0706.0797)
- Albert, J., et al. (MAGIC Collaboration) (2007), *Variable very high energy gamma-ray emission from Markarian 501*, ApJ 669, 862 — [ADS](https://ui.adsabs.harvard.edu/abs/2007ApJ...669..862A)
- Asada, K., & Nakamura, M. (2012), *The structure of the M87 jet: a transition from parabolic to conical streamlines*, ApJL 745, L28 — [arXiv:1110.1793](https://arxiv.org/abs/1110.1793)
- Axford, W. I., Leer, E., & Skadron, G. (1977), *The acceleration of cosmic rays by shock waves*, Proc. 15th ICRC (Plovdiv) 11, 132 — [ADS](https://ui.adsabs.harvard.edu/abs/1977ICRC...11..132A)
- Bell, A. R. (1978), *The acceleration of cosmic rays in shock fronts. I.*, MNRAS 182, 147 — [ADS](https://ui.adsabs.harvard.edu/abs/1978MNRAS.182..147B)
- Blandford, R. D., & Königl, A. (1979), *Relativistic jets as compact radio sources*, ApJ 232, 34 — [ADS](https://ui.adsabs.harvard.edu/abs/1979ApJ...232...34B)
- Blandford, R. D., & Ostriker, J. P. (1978), *Particle acceleration by astrophysical shocks*, ApJL 221, L29 — [ADS](https://ui.adsabs.harvard.edu/abs/1978ApJ...221L..29B)
- Blandford, R. D., & Payne, D. G. (1982), *Hydromagnetic flows from accretion discs and the production of radio jets*, MNRAS 199, 883 — [ADS](https://ui.adsabs.harvard.edu/abs/1982MNRAS.199..883B)
- Blandford, R. D., & Znajek, R. L. (1977), *Electromagnetic extraction of energy from Kerr black holes*, MNRAS 179, 433 — [ADS](https://ui.adsabs.harvard.edu/abs/1977MNRAS.179..433B)
- Blandford, R., Meier, D., & Readhead, A. (2019), *Relativistic jets from active galactic nuclei*, ARA&A 57, 467 — [arXiv:1812.06025](https://arxiv.org/abs/1812.06025)
- Boccardi, B., Krichbaum, T. P., Ros, E., & Zensus, J. A. (2017), *Radio observations of active galactic nuclei with mm-VLBI*, A&ARv 25, 4 — [arXiv:1711.07548](https://arxiv.org/abs/1711.07548)
- Celotti, A., & Ghisellini, G. (2008), *The power of blazar jets*, MNRAS 385, 283 — [arXiv:0711.4112](https://arxiv.org/abs/0711.4112)
- Drury, L. O'C. (1983), *An introduction to the theory of diffusive shock acceleration of energetic particles in tenuous plasmas*, Rep. Prog. Phys. 46, 973 — [ADS](https://ui.adsabs.harvard.edu/abs/1983RPPh...46..973D)
- EHT Collaboration (2019), *First M87 Event Horizon Telescope Results. I. The shadow of the supermassive black hole*, ApJL 875, L1 — [DOI](https://doi.org/10.3847/2041-8213/ab0ec7)
- Fermi, E. (1949), *On the origin of the cosmic radiation*, Phys. Rev. 75, 1169 — [DOI](https://doi.org/10.1103/PhysRev.75.1169)
- Ghisellini, G., Tavecchio, F., Maraschi, L., Celotti, A., & Sbarrato, T. (2014), *The power of relativistic jets is larger than the luminosity of their accretion disks*, Nature 515, 376 — [arXiv:1411.5368](https://arxiv.org/abs/1411.5368)
- Giannios, D., Uzdensky, D. A., & Begelman, M. C. (2009), *Fast TeV variability in blazars: jets in a jet*, MNRAS 395, L29 — [arXiv:0901.1877](https://arxiv.org/abs/0901.1877)
- Hada, K., et al. (2011), *An origin of the radio jet in M87 at the location of the central black hole*, Nature 477, 185 — [ADS](https://ui.adsabs.harvard.edu/abs/2011Natur.477..185H)
- Hillas, A. M. (1984), *The origin of ultra-high-energy cosmic rays*, ARA&A 22, 425 — [ADS](https://ui.adsabs.harvard.edu/abs/1984ARA%26A..22..425H)
- Hovatta, T., & Lindfors, E. (2019), *Relativistic jets of blazars*, New Astron. Rev. 87, 101541 — [arXiv:1909.04977](https://arxiv.org/abs/1909.04977)
- IceCube Collaboration, et al. (2018a), *Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A*, Science 361, eaat1378 — [DOI](https://doi.org/10.1126/science.aat1378)
- IceCube Collaboration (2018b), *Neutrino emission from the direction of the blazar TXS 0506+056 prior to the IceCube-170922A alert*, Science 361, 147 — [DOI](https://doi.org/10.1126/science.aat2890)
- Kellermann, K. I., & Pauliny-Toth, I. I. K. (1969), *The spectra of opaque radio sources*, ApJL 155, L71 — [ADS](https://ui.adsabs.harvard.edu/abs/1969ApJ...155L..71K)
- Kirk, J. G., Guthmann, A. W., Gallant, Y. A., & Achterberg, A. (2000), *Particle acceleration at ultrarelativistic shocks: an eigenfunction method*, ApJ 542, 235 — [ADS](https://ui.adsabs.harvard.edu/abs/2000ApJ...542..235K)
- Krymskii, G. F. (1977), *A regular mechanism for the acceleration of charged particles on the front of a shock wave*, Dokl. Akad. Nauk SSSR 234, 1306 — [ADS](https://ui.adsabs.harvard.edu/abs/1977DoSSR.234.1306K)
- Lister, M. L., et al. (2019), *MOJAVE. XVII. Jet kinematics and parent population properties of relativistically beamed radio-loud blazars*, ApJ 874, 43 — [ADS](https://ui.adsabs.harvard.edu/abs/2019ApJ...874...43L)
- Lu, R.-S., et al. (2023), *A ring-like accretion structure in M87 connecting its black hole and jet*, Nature 616, 686 — [arXiv:2304.13252](https://arxiv.org/abs/2304.13252)
- Marscher, A. P., et al. (2008), *The inner jet of an active galactic nucleus as revealed by a radio-to-gamma-ray outburst*, Nature 452, 966 — [ADS](https://ui.adsabs.harvard.edu/abs/2008Natur.452..966M)
- Narayan, R., Igumenshchev, I. V., & Abramowicz, M. A. (2003), *Magnetically arrested disk: an energetically efficient accretion flow*, PASJ 55, L69 — [ADS](https://ui.adsabs.harvard.edu/abs/2003PASJ...55L..69N)
- Penrose, R. (1969), *Gravitational collapse: the role of general relativity*, Riv. Nuovo Cimento 1, 252 — [ADS](https://ui.adsabs.harvard.edu/abs/1969NCimR...1..252P)
- Rees, M. J. (1966), *Appearance of relativistically expanding radio sources*, Nature 211, 468 — [ADS](https://ui.adsabs.harvard.edu/abs/1966Natur.211..468R)
- Rees, M. J. (1978), *The M87 jet: internal shocks in a plasma beam?*, MNRAS 184, 61P — [ADS](https://ui.adsabs.harvard.edu/abs/1978MNRAS.184P..61R)
- Sironi, L., & Spitkovsky, A. (2014), *Relativistic reconnection: an efficient source of non-thermal particles*, ApJL 783, L21 — [arXiv:1401.5471](https://arxiv.org/abs/1401.5471)
- Spada, M., Ghisellini, G., Lazzati, D., & Celotti, A. (2001), *Internal shocks in the jets of radio-loud quasars*, MNRAS 325, 1559 — [ADS](https://ui.adsabs.harvard.edu/abs/2001MNRAS.325.1559S)
- Tchekhovskoy, A., Narayan, R., & McKinney, J. C. (2011), *Efficient generation of jets from magnetically arrested accretion on a rapidly spinning black hole*, MNRAS 418, L79 — [arXiv:1108.0412](https://arxiv.org/abs/1108.0412)
- Urry, C. M., & Padovani, P. (1995), *Unified schemes for radio-loud active galactic nuclei*, PASP 107, 803 — [arXiv:astro-ph/9506063](https://arxiv.org/abs/astro-ph/9506063)
- Vlahakis, N., & Königl, A. (2004), *Magnetic driving of relativistic outflows in active galactic nuclei. I.*, ApJ 605, 656 — [ADS](https://ui.adsabs.harvard.edu/abs/2004ApJ...605..656V)
- Whitney, A. R., et al. (1971), *Quasars revisited: rapid time variations observed via very-long-baseline interferometry*, Science 173, 225 — [ADS](https://ui.adsabs.harvard.edu/abs/1971Sci...173..225W)

## 🔗 Conexiones

- Sección de escritura destino: [[II.ii Jets Relativistas]] / [[DRAFTS - II.ii Jets Relativistas]]
- Viene de: [[AGNs - Marco Teórico]] — el motor central y el filtro geométrico que define al blazar
- Continúa en: [[II.iii Radiación y Mecanismos de Emisión]] — sincrotrón, Compton inverso, procesos hadrónicos y EBL
- Conexión física central: [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]
- Complemento: [[Rayos_Cosmicos_y_Campos_Magneticos]] — el criterio de Hillas visto desde los rayos cósmicos
- Marco hermano: [[Neutrinos - Marco Teórico]]
- Seguimiento de correcciones: [[Escritura/Comentarios del Asesor]]
- Hub: [[XCRITURA]]
