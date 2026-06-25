![[IceCube_SeminarINFN_Rome_Zegarelli.pdf]]

## Diagrama de interacción de neutrinos 
Este diagrama ilustra el principio de funcionamiento de un **detector de neutrinos de Cherenkov** (como el observatorio IceCube en la Antártida o KM3NeT en el Mediterráneo). Muestra cómo se detecta indirectamente un neutrino de alta energía al interactuar con la materia.

Aquí tienes el desglose de los elementos del diagrama:

### 1. La Interacción Principal

- **El Neutrino Entrante ($\nu_\mu$):** La flecha azul representa un **neutrino muónico** que viaja a través del medio del detector (que suele ser hielo o agua). Los neutrinos son partículas fantasmales que rara vez interactúan con la materia.
    
- **La Colisión (Estrella amarilla):** Ocasionalmente, el neutrino choca de frente con el núcleo de un átomo en el medio (representado por $N$, un nucleón).
    
- **La Ecuación:** La fórmula describe esta colisión, conocida como interacción de corriente cargada (Deep Inelastic Scattering):
    
    $$\nu_\mu + N \rightarrow \mu + X$$
    
    Esto significa que el neutrino muónico ($\nu_\mu$) más un nucleón ($N$) se transforman en un muón ($\mu$) y una "cascada" de partículas secundarias o restos de la colisión ($X$).
    

### 2. La Señal Detectable (Cono Azul)

- **El Muón ($\mu$):** La flecha roja representa el muón resultante de la colisión. El muón es una partícula cargada similar al electrón, pero más masiva, y viaja en una línea casi recta a altísima velocidad.
    
- **Radiación de Cherenkov:** Debido a que el muón viaja a una velocidad superior a la velocidad de la luz _en ese medio específico_ (el hielo o el agua), emite un cono de luz direccional, similar al estampido sónico de un avión. Este es el **cono azul** en el diagrama.
    

### 3. Los Sensores

- **Módulos Ópticos:** Las esferas alineadas en cables verticales son tubos fotomultiplicadores (sensores de luz extremadamente sensibles).
    
- **Detección:** La flecha azul delgada que sale del cono hacia uno de los módulos indica que los fotones de la radiación de Cherenkov golpean estos sensores. Al medir exactamente cuándo y cuánta luz llega a diferentes sensores, los científicos pueden reconstruir la trayectoria exacta del muón.
    

### 4. El Recuadro Ampliado (Cinemática)

La parte inferior del diagrama amplía el punto de colisión para mostrar una relación matemática crucial:

- **El Ángulo ($\theta_{\nu\mu}$):** Es el ángulo de desviación entre la dirección original del neutrino (línea punteada) y la dirección en la que sale disparado el muón (flecha roja).
    
- **La Fórmula:**
    
    $$\theta_{\nu\mu} \simeq \frac{0.7^\circ}{[E_\nu(\text{TeV})]^{0.7}}$$
    
    Esta fórmula indica que **cuanta más energía tenga el neutrino ($E_\nu$), menor será el ángulo de desviación ($\theta_{\nu\mu}$)**. A energías de teraelectronvoltios (TeV) o superiores, el ángulo es minúsculo (menos de un grado). Esto es fundamental para la astronomía, ya que significa que la trayectoria del muón detectado apunta casi exactamente en línea recta hacia la fuente astrofísica original del neutrino en el espacio.


# Gráfica de Sección eficaz - Slide11
Esta diapositiva entra en la física de partículas subyacente a las detecciones, detallando la probabilidad de que un neutrino interactúe y cómo se manifiestan estas interacciones según su "sabor". Es fundamental para entender cómo se clasifican los eventos (las topologías) en los conjuntos de datos de observatorios como IceCube.

Aquí tienes el desglose técnico de los dos bloques principales:

### 1. La Gráfica: Sección Eficaz y la Resonancia de Glashow

La gráfica de la izquierda traza la **sección eficaz** ($\sigma$, medida en picobarns), que es esencialmente la probabilidad de interacción, frente a la **energía del neutrino** ($E$).

- **Dispersión Inelástica Profunda (DIS):** Las líneas que suben constantemente (verde turquesa para Corriente Cargada - CC, y naranja para Corriente Neutra - NC) muestran las colisiones $\nu + N$ (neutrino contra nucleón). Nota que a mayor energía, mayor es la sección eficaz.
    
- **La Necesidad de Hielo:** El cuadro de la izquierda compara la sección eficaz de los neutrinos ($\sigma_{\nu N}$) con la de los protones ($\sigma_{pp}$). La del neutrino es $\sim 10^{-8}$ veces menor. Esto justifica el recuadro explicativo del centro: debido a esta bajísima probabilidad, se requiere instrumentar volúmenes gigantescos de materia (como el kilómetro cúbico de hielo en la Antártida) para tener una tasa de detección estadísticamente significativa.
    
- **El Pico Morado (Resonancia de Glashow):** Esta es una firma importantísima. Ese pico agudo alrededor de los $6.3 \times 10^{14}$ eV (o $6.3$ PeV) ocurre exclusivamente cuando un **antineutrino electrónico ($\bar{\nu}_e$)** interactúa con un electrón en reposo del hielo para producir un bosón $W^-$. Identificar eventos en este rango de energía ayuda a discriminar el flujo de antineutrinos del de neutrinos y estudiar los mecanismos de producción en las fuentes astrofísicas.
    

### 2. Los Diagramas: Corrientes y Topologías

La parte derecha muestra los diagramas de Feynman (simplificados) de los diferentes canales, que en el análisis de datos se traducen en topologías muy distintas:

- **Corriente Cargada (CC):** El neutrino intercambia un bosón $W$ con el nucleón y se transforma en su leptón cargado correspondiente.
    
    - **CC $\nu_\mu \rightarrow \mu$:** Produce un muón y una cascada hadrónica. El muón viaja grandes distancias dejando una **traza (track)** recta. Esta topología es la que vimos en el diagrama anterior y es la que ofrece la mejor resolución angular para apuntar a correlaciones espaciales con fuentes de rayos gamma.
        
    - **CC $\nu_e \rightarrow e$:** Produce un electrón. El electrón pierde energía rápidamente, creando una **cascada (shower)** electromagnética densa y casi esférica en el detector. Ofrece excelente resolución de energía, pero pobre resolución angular.
        
    - **CC $\nu_\tau \rightarrow \tau$:** Produce un leptón tau. El tau decae casi inmediatamente. A energías muy altas ($> 100$ TeV), esto puede producir una firma de "Double Bang" (una cascada inicial de la colisión, un pequeño rastro del tau, y una segunda cascada de su decaimiento).
        
- **Corriente Neutra (NC - todos los sabores):** Intercambio de un bosón $Z$. El neutrino entra, transfiere parte de su impulso al nucleón rompiéndolo (creando una cascada hadrónica) y el neutrino se aleja perdiéndose. Para cualquier observatorio óptico, un evento NC de cualquier sabor se verá idéntico a una cascada de CC $\nu_e$, complicando la separación de sabores pero contribuyendo al conteo total del flujo difuso.


>para los drafts
>
Esta es la razón por la cual le damos más peso a las muestras que usamos del catálogo IceCat-1, pues le damos prioridad a las alertas que provienen de los tracks (tracks events) que son (en su mayoría) desencadenados por colisiones de corriente cargada (CC) de neutrinos muónicos que proporcionan una mejor resolución de las trayectorias. 
Usamos los tracks de colisiones de corriente cargada de la colisión de neutrinos muónicos puesto que es uno de los canales ideales para fuentes puntuales, puesto que la resolución angular es de $0.5\degree$ para eventos con energia $E>10 \:\; TeV$ y se tiene una resolución de energía estimada de un $20\%$ del logaritmo de la energía del muón entrante al detector.
En cambio, los eventos denominados como *cascades* son desencadenados por neutrinos de todos los sabores en una interacción de corriente cargada

# Tracks vs Cascades - Slide 14
Esta diapositiva es una de las más importantes para comprender el análisis de datos en observatorios de neutrinos como IceCube, ya que explica la dicotomía fundamental en la detección: **el compromiso entre la resolución espacial y la resolución energética**.
Para tu tesis, debes enfocar esta explicación en cómo la física subyacente de la interacción determina la firma macroscópica (topología) en el detector, y cómo esto dicta el tipo de ciencia que se puede hacer con cada evento.
Aquí tienes una explicación detallada y fundamentada:
### Topologías de Eventos: Trazas (Tracks) vs. Cascadas (Cascades)

En un detector de volumen masivo (como el hielo de IceCube), no observamos al neutrino directamente, sino el patrón espacial y temporal de la luz de Cherenkov emitida por las partículas secundarias creadas tras la colisión. Estos patrones se agrupan en dos topologías principales:
#### 1. Trazas (Tracks) - El Canal Astronómico
- **Física (Origen):** Se originan casi exclusivamente por **interacciones de Corriente Cargada (CC) de neutrinos muónicos ($\nu_\mu$)**. Como se ve en el diagrama de Feynman superior izquierdo, el neutrino intercambia un bosón W con un nucleón y se convierte en un muón ($\mu$).
- **Morfología:** El muón es una partícula cargada altamente penetrante. A energías astrofísicas (TeV - PeV), el muón puede viajar varios kilómetros a través del hielo antes de desintegrarse. A su paso, emite luz de Cherenkov continuamente, dejando una **traza (track) larga y direccional** que ilumina los sensores (DOMs) a lo largo de una línea recta (representado por los puntos iluminados alineados en la imagen 3D).
- **Resolución Angular (Excelente):** Debido a que la "palanca" geométrica (la longitud de la traza) es inmensa (cientos de metros a kilómetros), la dirección de la traza se puede reconstruir con extrema precisión geométrica. La diapositiva indica una resolución de **$0.5^\circ$ para energías > 10 TeV**. Por esto, las trazas son el **"Canal principal para apuntar a fuentes"**. Son esenciales para la astronomía multimensajero.
- **Resolución de Energía (Pobre):** Es de aproximadamente el **20% (en escala logarítmica)**. Esto se debe a que el muón generalmente no se origina ni se detiene completamente dentro del volumen instrumentado del detector. Al ver solo un segmento de su viaje, el detector no actúa como un calorímetro total; en su lugar, la energía original del neutrino debe inferirse a partir de la tasa de pérdida de energía ($dE/dx$) del muón, lo cual conlleva gran incertidumbre.
#### 2. Cascadas (Cascades / Showers) - El Canal Calorimétrico
- **Origen físico:** Se producen por dos vías principales:
    1. **Interacciones de Corriente Neutra (NC) de todos los sabores:** El neutrino choca, rompe el núcleo (creando una cascada hadrónica) y escapa sin dejar rastro. Se crea una onda de choque parecida a una burbuja por su relación esférica que impide la orientación fina de el precursor. Por esta razón las cascades pueden no ser los mejores rastros para estas partículas.
    2. **Interacciones de Corriente Cargada (CC) de neutrinos electrónicos ($\nu_e$):** El neutrino se convierte en un electrón. A diferencia del muón, el electrón interactúa inmediatamente con el hielo, generando una densa lluvia electromagnética (Bremsstrahlung y producción de pares).
- **Morfología:** Toda la energía se deposita en una región espacial muy reducida (unos pocos metros a decenas de metros). La luz se difunde en el hielo, creando en los sensores una señal casi esférica, un **estallido o cascada (cascade)** de luz concentrada (representado por el cúmulo denso de puntos en la imagen 3D derecha).    
- **Resolución Angular (Pobre):** Al carecer de un vector direccional largo, reconstruir la trayectoria original es muy complejo y depende de sutiles asimetrías en la distribución del tiempo de llegada de los fotones. Su resolución es mucho peor, **$\lesssim 5^\circ$ para energías > 50 TeV**. No son ideales para encontrar el punto exacto de origen en el cielo.    
- **Resolución de Energía (Excelente):** Es **$< 10\%$ para energías > 10 TeV**. Como toda la energía de las partículas secundarias se disipa _dentro_ del volumen del detector, IceCube actúa como un calorímetro casi perfecto. La cantidad total de luz medida es directamente proporcional a la energía del neutrino original. Este canal es vital para medir el espectro de energía difuso del universo y buscar anomalías fundamentales (como la resonancia de Glashow que vimos en la diapositiva anterior).
**En resumen para tu defensa:** Las Trazas actúan como "telescopios" que nos dicen _de dónde_ viene el neutrino, mientras que las Cascadas actúan como "calorímetros" que nos dicen exactamente _cuánta energía_ tenía.
Para ayudarte a visualizar la diferencia espacial y temporal de cómo el detector registra estas dos topologías, he creado el siguiente modelo interactivo.
# IceCube
Es un observatorio de neutrinos que esta nos esta proporcionando información de punto en diversas áreas de la investigación de la física como lo son: simetrías fundamentales, ciencias de la tierra, modelo estándar, materia oscura, astrofísica y física de neutrinos. Dentro de la astrofísica tenemos 3 ramas principales: aceleradores cósmicos, astronomía multimensajera y dentro de la física de neutrinos podemos hablar de las investigaciones sobre los radios de sabor, su oscilación, las apariencias tau, neutrinos estériles, producción de quarks pesados y decaimiento de neutrinos. Estas mismas son las que han tenido mayor relevancia. 

# Aceleradores cósmicos - slide 24

Los núcleos activos de galaxias son aceleradores de partículas. Estos son sistemas astrofísicos muy violentos que pueden acelerar partículas cerca del motor de dicha fuente, aquí es donde se forman los [[Rayos Cósmicos]] y hace que interactúen con los fotones y materia circundante. 
Cuando se acelera la materia en núcleos activos de galaxias se puede predecir la aceleración de protones, cuando se acelera un protón tenemos que 

 *justifica la existencia de observatorios como IceCube*. 
 Introduce el paradigma de la **Astronomía Multimensajero**: la idea de que para entender los fenómenos más violentos del universo, no basta con mirar la luz (fotones); debemos combinar la información de todas las partículas que nos llegan desde el cosmos.
Para tu tesis, esta diapositiva es perfecta para explicar el "modelo de producción" (cómo se crean los neutrinos en las fuentes astrofísicas) y por qué están indisolublemente ligados a los rayos cósmicos y los rayos gamma.
Aquí tienes el desglose técnico y fundamentado:

### 1. El Enfoque Multimensajero (Esquema Central)
El diagrama con los cuatro círculos muestra los mensajeros cósmicos y cómo están interconectados:
- **Rayos Cósmicos (CR - Rojo):** Son partículas cargadas (principalmente protones y núcleos atómicos) aceleradas a velocidades relativistas en las fuentes astrofísicas. El problema es que, al tener carga eléctrica, los campos magnéticos galácticos y extragalácticos desvían su trayectoria. Cuando llegan a la Tierra, ya no apuntan a su lugar de origen.
- **Fotones / Rayos Gamma ($\gamma$ - Azul claro):** Viajan en línea recta, pero a muy altas energías (TeV-PeV) pueden ser absorbidos por la luz de fondo extragaláctica (interactuando y creando pares electrón-positrón).
- **Neutrinos ($\nu$ - Verde):** Al no tener carga eléctrica ni color, viajan en línea recta sin ser desviados por campos magnéticos y rara vez interactúan con la materia, escapando intactos de los entornos más densos.    
- **Ondas Gravitacionales (GWs - Azul oscuro):** Son perturbaciones en el espacio-tiempo producidas por el movimiento de masas extremas (como la fusión de agujeros negros o estrellas de neutrones).  
La premisa es: un mismo "motor astrofísico" (como el agujero negro supermasivo ilustrado arriba a la derecha) puede emitir todos estos mensajeros simultáneamente.

### 2. Aceleración Hadrónica y Producción de Partículas
El recuadro ampliado ("HADRON acceleration") y las ecuaciones inferiores describen exactamente _cómo_ se generan estos mensajeros. Este es el escenario **hadrónico** (involucra protones), en contraposición al leptónico (solo involucra electrones).
En las cercanías del motor astrofísico, un protón ($p$) es acelerado a energías extremas. Este protón colisiona con el material circundante, que puede ser gas (otro protón, interacción $p \gamma$) o campos de radiación/luz (fotones, interacción $p \gamma$).
Estas colisiones inelásticas producen mesones, predominantemente **piones ($\pi$)**, de los cuales hay neutros y cargados:
- **Canal de Piones Neutros ($\pi^0$):** $$p + p/\gamma \rightarrow X + \pi^0$$
    El pion neutro es muy inestable y decae casi inmediatamente en dos rayos gamma de muy alta energía:  $$\pi^0 \rightarrow \gamma + \gamma$$
    _(Este es el origen de los rayos gamma astrofísicos en modelos hadrónicos)._
- **Canal de Piones Cargados ($\pi^\pm$):**   $$p + p/\gamma \rightarrow X + \pi^\pm$$
    Los piones cargados decaen en un muón ($\mu$) y un neutrino muónico ($\nu_\mu$):  $$\pi^\pm \rightarrow \mu^\pm + \nu_\mu (\bar{\nu}_\mu)$$Posteriormente, el muón también decae en un electrón/positrón, un neutrino electrónico y otro neutrino muónico:    $$\mu^\pm \rightarrow e^\pm + \nu_e (\bar{\nu}_e) + \bar{\nu}_\mu (\nu_\mu)$$    _(Este es el origen de los neutrinos astrofísicos)._
    

### 3. La Cinemática y el Reparto de Energía 
El último recuadro es fundamental para el análisis de datos. Muestra cómo se reparte la energía original del protón ($E_p$) entre las partículas secundarias:
$$\langle E_\nu \rangle \simeq \frac{1}{2} \langle E_\gamma \rangle \simeq \frac{1}{20} E_p$$

**¿Qué significa esto para tu tesis?**
1. **Regla de dedo de 1/20:** En promedio, un neutrino astrofísico se lleva aproximadamente el 5% (1/20) de la energía del protón que lo originó. Si detectamos un neutrino de $100$ TeV, sabemos que la fuente debe estar acelerando protones a al menos $2$ PeV.
2. **Relación Neutrino-Gamma:** La energía del neutrino es, en promedio, la mitad de la energía del rayo gamma emitido en el mismo proceso.
El IceCube tiene como objetivo detectar los neutrinos producidos para identificar estos aceleradores cósmicos.
#### Potenciales aceleradores cósmicos y fuentes astrofísicas de neutrinos
- Starbust galaxies
- Explosiones de Supernovas (CBD)
- Nucleos activos de galaxias
- Eventos de disrupcion de marea
- burst de rayos gamma
- Nuestra galaxia
**Conclusión clave:**
Detectar rayos gamma de una fuente espacial no nos asegura que se estén acelerando protones, ya que los electrones también pueden producir rayos gamma (mediante efecto Compton Inverso o Bremsstrahlung). Sin embargo, **los neutrinos SOLO se producen mediante colisiones hadrónicas (protones)**. Por lo tanto, detectar una coincidencia espacial y temporal de rayos gamma y neutrinos procedentes del mismo objeto es la "prueba irrefutable" (smoking gun) de que estamos observando un acelerador cósmico de protones.

# Neutrinos como mensajeros cósmicos ideales - Slide 29

- Los *RAYOS CÓSMICOS* son sensibles a campos magnéticos, por lo que su dirección puede ser modificada en su viaje interestelar. Nuestras detecciones no apuntan específicamente hacia su origen.
- Los *RAYOS GAMMA* se pueden trackear hacia su origen pero la mayoría en el nivel de $TeV-\gamma$ son absorbidos por la radiación de fondo del universo. Estos se pueden producir en fuentes hadrónicas y leptónicas
- Los *NEUTRINOS*, por sus propiedades (eléctricamente neutros, estables y casi nula interacción de fuerza débil), no son desviados ni absorbidos. Además que se producen solamente en fuentes hadrónicas, y esto los vuelve mensajeros cósmicos ideales y smoking-gun (prueba irrefutable) de fuentes de aceleradores de rayos cósmicos.

# Discriminación entre neutrinos astrofísicos y atmosféricos - Slide 35 y 36



# Mecanismo de producción de neutrinos para su diversificación de sabor
