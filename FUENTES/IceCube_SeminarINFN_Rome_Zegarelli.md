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


## Gráfica de Sección eficaz (Slide11)
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

# IceCube
Es un observatorio de neutrinos que esta moldeando bastante información al respecto 



