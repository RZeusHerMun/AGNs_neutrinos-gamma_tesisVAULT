![[Pasted image 20260616212707.png]]
# La desintegración del muón y los neutrinos en IceCube

## 1. El proceso de desintegración

El muón (μ⁻) es un leptón cargado, una especie de "primo pesado" del electrón: tiene la misma carga negativa, pero unas 207 veces más masa. Es inestable y vive en promedio solo unos 2,2 microsegundos antes de desintegrarse a través de la **interacción débil**, casi siempre en un estado de tres partículas:

```
μ⁻  →  e⁻  +  ν̄ₑ  +  ν_μ
```

Es decir, produce **al menos tres partículas**: un **electrón** (e⁻), que conserva la carga negativa del muón original, y **dos tipos distintos de neutrino**, un **antineutrino electrónico** (ν̄ₑ) y un **neutrino muónico** (ν_μ).

### Leído como diagrama de Feynman

Si seguimos el proceso paso a paso (con el tiempo avanzando de izquierda a derecha):

1. El muón llega a un **vértice débil** y se transforma en un **neutrino muónico** (ν_μ).
2. En ese vértice emite un **bosón W⁻**, la partícula mediadora de la fuerza débil. El W⁻ se lleva la carga negativa.
3. El W⁻ es extremadamente inestable y se desintegra en un **electrón** (e⁻) y un **antineutrino electrónico** (ν̄ₑ).

Así se respetan todas las leyes de conservación: la carga eléctrica se conserva (la negativa pasa del muón al electrón a través del W), y los números leptónicos de cada familia también, gracias a la aparición emparejada de ν_μ por un lado y del par e⁻ / ν̄ₑ por otro. El electrón, al ser mucho más ligero, se lleva la mayor parte de la energía en forma de movimiento, mientras que los neutrinos escapan casi sin interactuar.

Este patrón —un fermión cargado que se convierte en su neutrino emitiendo un W, y el W decayendo en otro par leptón-neutrino— es la firma universal de la interacción débil, y es exactamente el mismo mecanismo (al revés) que permite **detectar** neutrinos.

## 2. Relación con los neutrinos que detecta IceCube

IceCube es un detector de un kilómetro cúbico de hielo instrumentado en el Polo Sur. No "ve" los neutrinos directamente —son casi indetectables—, sino la luz que producen las partículas cargadas que crean al chocar con el hielo. Aquí el muón aparece en el papel inverso al de la desintegración: en lugar de *desaparecer*, **se produce**.

Cuando un **neutrino muónico** cósmico (ν_μ) interactúa con un núcleo del hielo mediante la interacción débil, ocurre prácticamente el proceso inverso del diagrama: el ν_μ se convierte en un **muón**. Ese muón es muy energético, viaja varios kilómetros casi en línea recta y más rápido que la luz *en el hielo*, emitiendo un cono de luz azul llamado **radiación de Cherenkov**. Los miles de sensores ópticos de IceCube registran esa luz y reconstruyen la trayectoria.

La clave es la **dirección**: como el muón apenas se desvía respecto al neutrino que lo creó, su rastro (su "track") **apunta de vuelta hacia la fuente** en el cielo. Por eso los eventos de tipo *track* (canal ν_μ → muón) son los que dan la mejor resolución angular y los que permitieron, por ejemplo, asociar un neutrino con el blazar **TXS 0506+056** en 2017. Otros sabores de neutrino producen "cascadas" más difusas, con mucha peor puntería.

La desintegración del muón que muestra el diagrama es, además, la otra cara de la moneda: explica por qué los muones tienen una vida finita y por qué, gracias a la dilatación temporal relativista, los muones atmosféricos llegan hasta el detector. Distinguir esos muones atmosféricos (el "ruido") de los muones producidos por verdaderos neutrinos cósmicos es uno de los grandes retos del análisis de datos.

## 3. Importancia y mejoras del IceTracks-DR2

El **IceCube Second Track Data Release (IceTracks-DR2)**, titulado *"Data from 2008-2022 for Neutrino Source Searches"*, es la publicación pública más reciente del catálogo de eventos de tipo *track* de IceCube (arXiv:2605.19040, mayo de 2026, enviado a *The Astrophysical Journal Supplements*). Está disponible para la comunidad en el repositorio dataverse.harvard.edu.

Como acabamos de ver, el canal de *tracks* es precisamente el de los muones generados por neutrinos muónicos: el más valioso para localizar fuentes en el cielo. Por eso este conjunto de datos es central para la astronomía de neutrinos.

### Qué aporta y qué mejora respecto a versiones anteriores

**Más tiempo de observación.** Extiende el conjunto anterior, de 10 años, a **14 años de datos** (del 6 de abril de 2008 al 23 de mayo de 2022). Cuatro años adicionales significan más estadística y, por tanto, mayor sensibilidad para detectar fuentes débiles y eventos transitorios.

**Mejor calibración del detector.** Incorpora una calibración actualizada para los datos tomados después del 1 de junio de 2010, lo que mejora simultáneamente la **resolución en energía**, la **resolución angular** y la **clasificación de eventos**.

**Mejor puntería angular.** Tras aplicar toda la selección, la separación angular *mediana* entre el neutrino original y el muón reconstruido baja de **1 grado** para energías superiores a 10 TeV, y esto se logra **en ambos hemisferios** (norte y sur). Una mejor resolución angular es exactamente lo que se necesita para señalar fuentes concretas en el cielo. Las configuraciones más completas del detector (con 86 y 79 cuerdas) rinden mejor que las temporadas iniciales con menos instrumentación.

**Selección de eventos actualizada.** Usa criterios de selección revisados que producen una muestra más limpia y mejor caracterizada.

**Funciones de respuesta del instrumento y áreas efectivas.** Incluye *instrument response functions* (IRF) binned y áreas efectivas, lo que permite a cualquier grupo de investigación externo realizar búsquedas sensibles de fuentes de neutrinos, tanto estables como transitorias, usando herramientas internas y públicas documentadas.

**Es la referencia recomendada.** El propio equipo señala que IceTracks-DR2 representa el conjunto de datos de *tracks* de muones de cielo completo **más sensible y completo disponible públicamente hasta la fecha**, y que debe usarse en lugar de las versiones anteriores.

### En síntesis

El muón conecta dos mundos: su **desintegración** es un ejemplo de manual de la interacción débil (un leptón, un electrón y dos sabores de neutrino), y su **producción** por neutrinos muónicos es lo que convierte a IceCube en un telescopio capaz de apuntar a fuentes cósmicas. El IceTracks-DR2 mejora justamente la calidad de ese canal —más años, mejor calibración y resolución angular por debajo del grado— y lo pone a disposición de toda la comunidad, consolidándose como el mejor catálogo público de *tracks* de neutrinos hasta ahora.

## 4. El recorrido completo: del AGN al hielo

Para entender el valor del muón en IceCube conviene ver la historia entera, en tres etapas secuenciales, como una sola cadena de procesos de Feynman.

### Etapa 1 — Producción en el AGN

En el entorno de un núcleo galáctico activo (AGN) hay un agujero negro supermasivo que lanza un **chorro relativista** (jet). Dentro de ese chorro, los **protones** se aceleran hasta energías altísimas y chocan con la radiación presente, es decir, con **fotones** (γ):

```
p + γ  →  Δ⁺  →  n + π⁺
```

La colisión genera **piones** cargados. El pión positivo es inestable y decae por interacción débil:

```
π⁺  →  μ⁺ + ν_μ
```

Aquí nace el **neutrino muónico** (ν_μ). El muón que lo acompaña a su vez decae (μ⁺ → e⁺ + ν_e + ν̄_μ), generando todavía más neutrinos. Lo importante: el neutrino sale del AGN sin carga, casi sin masa y prácticamente sin interactuar con nada.

### Etapa 2 — Viaje cósmico

El neutrino atraviesa **miles de millones de años luz** hasta llegar a la Tierra. Tiene dos propiedades que lo hacen un mensajero único:

Como **no tiene carga eléctrica**, los campos magnéticos del espacio no lo desvían: viaja en línea recta y conserva la dirección de su fuente. Y como **apenas interactúa**, atraviesa nubes, estrellas y polvo sin ser absorbido, trayendo información directa de regiones que la luz no puede escapar.

Durante el trayecto ocurre la **oscilación de sabor**: el neutrino cambia de identidad entre los tres tipos (ν_μ ↔ ν_e ↔ ν_τ). Por eso, aunque en la fuente se producen sobre todo neutrinos muónicos y electrónicos, la mezcla que llega a la Tierra está repartida de forma más equilibrada entre los tres sabores.

### Etapa 3 — Detección en IceCube (la "degradación" en muón)

Al llegar al hielo de la Antártida, el neutrino muónico interacciona con un **núcleo** (N) del hielo mediante la **interacción débil de corriente cargada**: intercambia un **bosón W** y se transforma en un **muón** detectable, mientras el núcleo se rompe en una lluvia de **hadrones** (X):

```
ν_μ + N  →  μ⁻ + X
```

Este es exactamente el **proceso inverso** al de la primera etapa: allí un pión "fabricaba" un neutrino emitiendo un muón; aquí el neutrino se "convierte" de nuevo en un muón. Ese muón, muy energético, recorre varios kilómetros de hielo casi en línea recta y más rápido que la luz _en ese medio_, emitiendo un cono de **luz Cherenkov** (un destello azulado). Los miles de sensores ópticos (DOM) de IceCube registran ese destello y reconstruyen la trayectoria del muón, que **apunta de vuelta** hacia el neutrino y, por tanto, hacia el AGN que lo originó.

### Por qué este recorrido importa para el IceTracks-DR2

Toda esta cadena termina en un único dato observable: la **traza (track)** del muón. El IceTracks-DR2 es precisamente el catálogo de esas trazas a lo largo de 14 años. Cada mejora de la que hablamos en la sección anterior —más años de datos, mejor calibración y una resolución angular mediana por debajo de 1° sobre 10 TeV— hace que esa flecha final apunte con más precisión, permitiendo retroceder por todo el recorrido y señalar la fuente cósmica. El muón es, así, el eslabón final que convierte un neutrino casi invisible en una dirección concreta del cielo.
#### Se usan en imagenología muónica
![[Pasted image 20260616221922.png]]

---

## 🔗 Conexiones con el Marco Teórico de Neutrinos

Esta nota es el caso aplicado, paso a paso, de varias piezas del marco teórico:

- Hub: [[Neutrinos - Marco Teórico]]
- La desintegración del muón como ejemplo de manual de la interacción débil → [[Neutrino en el Modelo Estándar]]
- El nacimiento del neutrino en el AGN (cadena de piones) → [[Producción de Neutrinos]]
- El trayecto completo fuente → detector → [[Ciclo de Vida del Neutrino]]
- La oscilación de sabor en ruta (1:2:0 → 1:1:1) → [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]
- El muón como señal detectable (Cherenkov, *tracks*) → [[Detección de Neutrinos]]
- Por qué los rayos gamma y los neutrinos salen del mismo choque → [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]

---

### Fuentes

- [IceCube Second Track Data Release IceTracks-DR2 — página de datos (IceCube)](https://icecube.wisc.edu/data-releases/2026/05/icecube-second-track-data-release-icetracks-dr2-data-from-2008-2022-for-neutrino-source-searches/)
- [IceCube's 14-year data release for neutrino source searches (noticia IceCube)](https://icecube.wisc.edu/news/research/2026/05/icecubes-14-year-data-release-for-neutrino-source-searches/)
- [arXiv:2605.19040 — IceTracks-DR2 (abstract)](https://arxiv.org/abs/2605.19040)
- [arXiv:2605.19040 — versión HTML completa](https://arxiv.org/html/2605.19040)
- [IceCube Neutrino Observatory — Data Releases](https://icecube.wisc.edu/science/data-releases/)
- https://unlp.edu.ar/investiga/cienciaenaccion/radiografiar-volcanes-con-un-telescopio-de-muones-20438-25438/
