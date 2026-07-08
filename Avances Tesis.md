[[Data]] [[XCRITURA]] [[TheSis]]
### AVANCES REUNION DICIEMBRE 25
- [x] catalogo sloan digital sky survey
		- [ ] para checar los mapas y hacer algunas sobreposiciones de ubicaciones
		- [ ] plottear despues con DS9 
		- [ ]  se pueden descargar en FITS
	- [x]  meterle un analisis random a los distintas muestras q tengo (0.5, 1, 2, 5)
		- [ ]   checar con las  significantes a las identificadas
	- [x]  hacer un histograma de las distancias de las alertas a las fuentes de fermi cuando comienza a crecer la resolucion angular 
		- qué tan grande es el área del cielo donde IceCube cree que vino el neutrino
		- [ ] **ACT** Disminuir la escala para ver que tan grandes son o que tan
		- ![[Pasted image 20260218190742.png|290]]
		- distribución muy asimétrica.
		- contornos enormes, check.
		- [ ] Hacer una nueva grafica con un corte $error > 50 deg^2$
	- [ ] tabla con las distancias a las fuentes mas cercanas a las distintas alertas.
		- [ ]  comparar las estadísticas con las random.
		- [ ]  las distancias compararlas con las random solamente con las alertas de icecube.
	- [x]  con las random ubicar a mano fuentes random para q e codigo las marque.
	  
# Falta: 
	- RESUMEN-DESCRIPCIÓN DE LAS MEJORAS 
	- SACAR INFORMACION SOBRE LAS DETECCIONES ACTUALES
	- RE-HACER LOS SCRAMBLES SIN EL TXS. ANALIZAR
	- GRAFICO DE TODAS LAS FUENTES SOBRE TODAS LAS ALERTAS IC CON ERRORES.
		- CON 38 DIFERENCIADAS
		- CON 11 IMPORTANTES (0.5, 1 Y 1.5) MAS DIFERENCIADAS
		- 
![[Pasted image 20260121100023.png|300]]

Notas 19 d Feb:
- anotar la importancia de el random solo en la ar, eficiencia del IC cerca del ecuador
- explicar como va cambiando la cantidad de eficiencia con cada evz menos grados de error 
- poner mas positivos de control.
- sacar el plot original de los agn con la AR sin cambios, el q se superpone con los montecarlos x1000, etc. Es el que se pone en comparacion.
- Explicar como se encuentra la distncia efectiva para ver que variabilidad es la mas adecuada. Partiendo de la mediana del error para ver si una gaussiana puede ser un poco. Por que para no solo 1,2,3,4 o 5 siguen siendo los mismos. Como es son funcionales para salir de los errores de icecube
-
## mejoras
- se puede relacionar con la energia de los gamma con la energia probable siguiendo una ruta hadronica para los neutrinos, asi relacionar con las posibilidades que tenfo de encontrar en esos radios, como se descompone entre mas energia.

## pq - conclusion
- El catalogo estaba filtrado para ser estudiados como procesos leptonicos, la mayoria produce.
- las que conocemos y tenemos evidencia son la mayoria a fuentes hadronicas, entonces al estudiar las fuentes mas afines, tenemos menos posibilidad de encontrar. 
___
# ANALYSIS
al19 d feb d 2026
## SCRAMBLING 1, RA (datasets aleatorizados en el for)
- Dec fijo
- |b|>10$\degree$, *es necesario mantener el margen en la aleatorizacion?*
- RA_random = uniform(0, 360°)
	Preserva la distribución en latitud.
	## vectorización 
	- numpy broadcasting en lugar de iterows en cada iteracion
		- **Necesito hacer más iteraciones? 20k?**
	## Resultado Nulo
	Ejecución usando contornos de error elíptico d IceCube 
			- 38 vs 40.6 esperadas
				- Compatible con el azar, no hay exceso d neutrinos.
%% voy en la aleatorizacion 1, con elipses de error.%%
## SCRAMBLING 2. RA (vectorizado de las RA antes del ciclo)
Antes del ciclo:
- Posiciones aleatorias del tamaño del catalogo
- Dejamos fijos a los neutrinos, sus errores y demas valores
Despues, randomicé los AGN en su RA. (numpy broadcasting)
Errores elípticos. Criterio:
$$\left(\frac{\Delta \alpha \cos\delta}{\sigma_\alpha}\right)^2 + \left(\frac{\Delta \delta}{\sigma_\delta}\right)^2 \le 1$$

es una **aproximación estándar** para contornos tipo 90% cuando:
- IceCube reporta errores asimétricos
- no tengo la matriz de covarianza completa
    **SE DEBE EXPLICAR**?
    
    


___
## tercara etapa. MEJORA DE ANAYLISIS
#### Mejora 1: Regresar a la Probabilidad, no al "Corte Duro"

Actualmente usas un corte binario: ¿Está dentro del círculo? (Sí/No) . Esto desperdicia información. Un neutrino a $0.1^\circ$ del AGN es mucho más valioso que uno a $1.4^\circ$, pero tu código actual los cuenta igual (como "1").

**Propuesta:** Implementa un **Stacking Likelihood**. En lugar de contar coincidencias ($N$), suma "pesos" ($TS$ o $\mathcal{L}$).

Asume que el error del neutrino es una Gaussiana 2D:

$$\Psi(\Delta r) = \frac{1}{2\pi\sigma^2} e^{-\frac{\Delta r^2}{2\sigma^2}}$$

En tu Monte Carlo, en lugar de sumar `+1` si cae dentro, suma el valor de esta Gaussiana. Esto dará mucho más peso a las alineaciones precisas.

#### Mejora 2: Incorporar "Pesos" Astrofísicos

Estás tratando a todos los AGNs por igual.

- _Problema:_ Un AGN brillante en rayos gamma (alto flujo en HAWC) tiene mucha más probabilidad de emitir neutrinos que un AGN débil.
    
- _Solución:_ Pondera tu suma.
    
    $$S = \sum_{i} w_i \times \text{coincidencia}_i$$
    
    Donde el peso $w_i$ puede ser el flujo de fotones del AGN o su `TS` (Test Statistic) de HAWC. _Si la correlación es real, esperaríamos que venga de los AGNs más potentes. Si mezclas los débiles (ruido), estás diluyendo tu propia señal._
    

#### Mejora 3: Recuperar la Elipticidad

Abandonaste las elipses por círculos en la segunda mitad.

- Los errores de IceCube **son elípticos**. Al usar círculos de $1.5^\circ$, estás incluyendo mucho fondo (ruido) en la dirección donde el error del neutrino es pequeño, y perdiendo señal donde el error es grande.
    
- _Acción:_ Vuelve a usar la función `is_inside_elliptical_contour` vectorizada o, mejor aún, usa la formulación Gaussiana 2D asimétrica:
    
    $$\chi^2 = \frac{\Delta RA^2}{\sigma_{RA}^2} + \frac{\Delta Dec^2}{\sigma_{Dec}^2}$$
    

### 4. Hoja de Ruta (Next Steps)

Para tu tesis, te sugiero la siguiente jerarquía de pasos:
1. **Inmediato (Fácil):** Vuelve a correr tu análisis de $1.5^\circ$ pero **pesando los AGNs por su TS de HAWC**.
    - _Hipótesis:_ Si el p-value baja (ej. de 0.04 a 0.01), la señal es robusta y viene de los objetos brillantes. Si sube, es probable que el exceso de 12 coincidencias que viste sea solo ruido de fondo.
2. **Intermedio (Necesario):** Implementa la **Suma de Gaussianas** en lugar del conteo binario. Esto es mucho más profesional para una tesis de maestría/licenciatura y aprovecha la precisión de los datos.
3. **Visualización:** Tu gráfica de "Distribución de coincidencias aleatorias" es buena. Agrega una línea vertical marcando el $3\sigma$ y $5\sigma$ teóricos para que el lector vea qué tan lejos estás del descubrimiento.
**Conclusión:**
Tu código está bien optimizado y tu estadística es correcta. Ese resultado de $2.4\sigma$ post-trials es **muy prometedor para una tesis**. No demuestra emisión de neutrinos, pero demuestra que hay "tensión" en los datos que merece más estudio.
¿Te gustaría que te ayude a escribir la función vectorizada para incluir el **peso por flujo (TS)** de los AGNs en tu Monte Carlo? Eso podría cambiar drásticamente tus resultados.

### TS ANALYSIS 
- Opcion 1. Usar el esquema de TS de Fernando
- Opcion 2. Esquema de pesos temporal (como https://doi.org/10.3847/1538-4357/acdfcb)
```
if Datos_temporales_HAWC:
    peso_AGN = flujo_en_mes_de_alerta_neutrino
else:
    peso_AGN = flujo_promedio_HAWC
```

Tengo posibilidad de realizar un test analisis (TS)
	$$TS_{total} = Σ TS_i$$(suma sobre todos los neutrinos)

Donde para cada neutrino **i**:
	- Se identifica el AGN más probable como contraparte (el que maximiza S_spatial × peso)
	- Se calcula TS_i para ese par neutrino-AGN
	
Para q? 
	- *SIGNIFICANCIA COMPROBABLE* en terminos de TS y de sigmas.
	- Serviría para *cuantificar* mis detecciones, ashora no solo diría que tengo coincidencias espaciales si no q estan relacionados por un analisis de de pesos-detccion.
	- Uso toda la informacion disponible, no solo coordenadas.
	- Jerarquizo las detecciones y comparación mas técnica


Que necesito?
- Del HAWC-Fermi-135
	- Posicion (RA, Dec) **TENGO**
	- Esquema de pesos (flujo, luminosidad, o uniforme). *FALTARIA*
		- Flujo promedio (?)
		- Flujo variable temporal.
- De las alertas IC (*LO TENGO*)
	- Posición reconstruida
	- PDF espacial (contornos de error)
	- Signalness (probabilidad de ser astrofísico)

Informacion Temporal que me serviría:
 **a) Mapas de significancia en diferentes períodos**
- Puedes dividir los datos en ventanas temporales (meses, años)
- Ver si la detección es persistente o variable
**b) Curvas de luz (si están disponibles)**
- Flujo vs tiempo para tus 135 AGN
- Similar a lo que Fermi hace con su Light Curve Repository
**c) Transit observations**
- HAWC observa fuentes cuando pasan por su campo de visión
- Puedes tener diferentes "transits" = diferentes períodos
**d) Información de flares**
- Si alguno de tus AGN tuvo un flare detectado por HAWC
- Fecha y duración del flare






___

# ESTADISTICA COMPLETA - 26 MARZO 2026

# Índice actual.
![[Pasted image 20251120105216.png]]


# Objetivos Centrales y Motivación

La presente investigación se centra en la caracterización fenomenológica observacional de núcleos galácticos activos (AGNs) emisores de rayos gamma, con el objetivo de identificar posibles correlaciones con detecciones de neutrinos de alta energía. **Este enfoque multimensajero busca aportar evidencia observacional que permitan discriminar entre los escenarios teóricos predominantes: el modelo leptónico (donde la emisión gamma proviene de Efecto Compton Inverso sobre electrones) y el modelo hadrónico (que involucra interacciones de protones relativistas y decaimiento de piones). La distinción es crítica, pues solo el segundo predice un flujo significativo de neutrinos.**

---

## I. Introducción: El Problema de los AGNs y la Astronomía Multimensajera

 - Astronomía multimensajera como ventana de investigación a los procesos más energéticos del univero.
- Planteamiento de el problema sobre la ambigua descripción de la naturaleza de los AGNs, sus emisiones de muy alta energía y la dificultad de encontrar un modelo (leptónico o hadrónico) que puedan explicarlos. 
- Importancia de correlacionar rayos gamma y neutrinos para poder dicernir entre modelos de generación de energía.

Objetivos centrales: 
- Analizar los AGNs que emiten rayos gamma, que son más propensas a producir neutrinos de alta energía. (muestra de 18 AGNs de Fernando Ureña)
- **Identificar y caracterizar los AGNs utilizando datos de HAWC y del catálogo 4FHL (Fourth Fermi-LAT Catalog of High-Energy Sources) de Fermi-LAT, para posteriormente correlacionarlos con las detecciones de IceCube**

La astronomía multimensajera ha emergido en las últimas décadas como una ventana privilegiada para investigar los procesos más energéticos del universo. A diferencia de la astronomía tradicional basada únicamente en fotones, esta nueva era permite correlacionar información proveniente de diferentes mensajeros cósmicos: radiación electromagnética en todo el espectro, neutrinos, rayos cósmicos y ondas gravitacionales. Esta complementariedad resulta especialmente valiosa al estudiar fenómenos extremos como los núcleos galácticos activos.

Los AGNs representan uno de los fenómenos más enigmáticos y energéticos del cosmos. Estos objetos, alimentados por agujeros negros supermasivos en proceso de acreción, generan emisiones que abarcan todo el espectro electromagnético y, potencialmente, producen neutrinos de muy alta energía. **Sin embargo, la descripción actual enfrenta retos. A las energías más altas (rango multi-TeV), los modelos puramente leptónicos enfrentan dificultades para explicar los flujos observados debido a la supresión de la sección eficaz de Klein-Nishina y la extrema eficiencia de aceleración requerida, lo que sugiere la necesidad de componentes hadrónicas.**

El problema central radica en la dificultad de encontrar un modelo unificado que explique satisfactoriamente las observaciones. Dos familias de modelos compiten actualmente: los **modelos leptónicos**, que postulan que las emisiones de alta energía provienen principalmente de procesos radiativos de electrones y positrones acelerados, y los **modelos hadrónicos**, que proponen que protones y núcleos acelerados juegan un papel dominante. La distinción entre ambos escenarios no es meramente académica, sino que tiene implicaciones profundas para nuestra comprensión de la aceleración de partículas en entornos astrofísicos extremos.

Aquí es donde la correlación entre rayos gamma y neutrinos se vuelve crucial. Los modelos hadrónicos predicen naturalmente la producción de neutrinos de alta energía a través de interacciones hadrónicas (principalmente mediante la desintegración de piones cargados y neutros), mientras que los modelos leptónicos puros no generan flujos significativos de neutrinos. Por lo tanto, la detección de neutrinos asociados espacial y temporalmente con brotes de rayos gamma en AGNs constituiría una evidencia contundente a favor de escenarios hadrónicos.![[Pasted image 20251204005426.png]]
 
### Objetivos Específicos

Este trabajo se propone analizar una muestra de 18 AGNs emisores de rayos gamma, inicialmente identificada en **[Paper de Ureña, Año]**, que presentan características favorables para la posible emisión de neutrinos de alta energía. Los objetivos específicos incluyen:

1. **Caracterización multifrecuencia**: Identificar y caracterizar detalladamente los AGNs de la muestra, utilizando datos de rayos gamma provenientes de HAWC y Fermi-LAT.
2. **Análisis espectral integrado**: Comparar y relacionar las mediciones espectrales obtenidas por HAWC (en el régimen de TeV) y Fermi-LAT (en el régimen de GeV), construyendo distribuciones espectrales de energía (SEDs) coherentes para cada fuente.
3. **Búsqueda de coincidencias con neutrinos**: Contrastar las posiciones y tiempos de emisiones intensas (flares) de rayos gamma con el catálogo de eventos de neutrinos de IceCube, buscando coincidencias espaciales y temporales que puedan indicar una conexión física.

---

## II. Marco Teórico y Fenomenología

Quiero centrar la descripción en su fenomenología observacional:
- Explicación de la estructura básica de los AGNs
- Descripción del esquema de clasificación unificado (para detallar sobre las diferencias de los AGNs). Aquí los clasifico dependiendo de sus características.
- Variabilidad rápida y sesgo observacional que esta causa, descripción que el uso de datos del HAWC presentan beneficio al tener más tiempo de observación.
### II.i Fenomenología de los AGNs
![[AGNs|1000]]
Los núcleos galácticos activos son sistemas complejos caracterizados por la presencia de un agujero negro supermasivo central (con masas entre 10⁶ y 10¹⁰ masas solares) rodeado por un disco de acreción. La materia que cae hacia el agujero negro libera muy grandes cantidades de energía gravitacional, convirtiéndola en radiación electromagnética. En una fracción significativa de los AGNs, se observan chorros (jets) relativistas de plasma que emergen perpendicularmente al disco de acreción, extendiéndose por distancias que pueden alcanzar millones de años luz.

Estos jets son los responsables de las emisiones más energéticas observadas en AGNs. Cuando uno de estos chorros apunta aproximadamente hacia la Tierra, observamos lo que se denomina un blazar (subclase de AGN caracterizada por emisiones extremadamente variables y luminosas en todo el espectro electromagnético, incluyendo rayos gamma de muy alta energía).

#### La Radiación Electromagnética: Fundamentos y Procesos
![[LuzRadiacionEspectroElectromagnetico|5000]]
Para comprender las emisiones de los AGNs, es fundamental revisar la naturaleza de la radiación electromagnética. La luz es una forma de radiación electromagnética que exhibe una dualidad onda-partícula: se propaga como una onda descrita por las ecuaciones de Maxwell, pero interactúa con la materia como partículas cuantizadas (fotones). Esta radiación no requiere un medio material para propagarse y viaja a la velocidad constante $c ≈ 300,000 km/s$ en el vacío.

La radiación electromagnética se clasifica mediante su espectro, ordenándose por:

- Frecuencia (_f_): medida en Hertz (Hz = ciclos/segundo)
- Longitud de onda (*λ*): distancia física entre dos picos sucesivos de la onda

Estas propiedades están relacionadas por la ecuación fundamental: _$c = λf$_

La energía transportada por un fotón está dada por la relación de Planck: _$E = hf$_, donde _h_ es la constante de Planck. Esta ecuación revela que a mayor frecuencia (y menor longitud de onda), mayor es la energía del fotón. Los rayos gamma, situados en el extremo de alta frecuencia del espectro, son por tanto la forma más energética de radiación electromagnética, con energías que pueden superar los TeV (10¹² electronvoltios) en fuentes astrofísicas.

#### Mecanismos de Emisión: Térmicos vs No Térmicos
___
- En esta parte pienso explicar ambos modelos de producción de altas energías. 
	- Modelo leptónico estándar 
	- Modelos Hadrónico
	Como es q los dos modelos predicen las relaciones energéticas que estarían (hadrónico), o no (leptónico), produciendo los neutrinos. 
	(No se si aqui agregar algo relacionado con el problema q representa tener el EBL de fondo y como es que en esa radiación de fondo perdemos mucha información) **al hablar de las fuentes (q son cercanas) dará pie a hablar del EBL**
___
Las emisiones electromagnéticas en astrofísica se clasifican en dos categorías fundamentales según su mecanismo de producción:

**Emisión Térmica**: Cuando un objeto se calienta, sus moléculas y átomos se agitan debido a la energía térmica. Estas partículas cargadas, al oscilar, generan campos eléctricos cambiantes que producen radiación electromagnética. Este proceso genera un espectro continuo de emisión que sigue la distribución de Planck. Las características principales incluyen:

- La potencia total emitida sigue la ley de Stefan-Boltzmann: $P = σT⁴$
- La longitud de onda del pico de emisión está determinada por la ley de Wien: _$λ_{max} T = b$_
- Ejemplos incluyen estrellas (como el Sol), filamentos incandescentes y **cualquier cuerpo (incluyéndonos a 36 grados)**desde objetos cotidianos hasta estrellas. En el contexto de los AGNs, esta emisión domina en el disco de acreción.

En AGNs, la emisión térmica domina en el disco de acreción, particularmente en las bandas óptica, ultravioleta y de rayos X blandos.

**Emisión No Térmica**: Los jets relativistas de los AGNs generan radiación mediante procesos no térmicos, donde partículas individuales aceleradas a velocidades relativistas producen fotones de alta energía. Los mecanismos principales incluyen:

- **Radiación sincrotrón**: Electrones relativistas girando en espiral alrededor de líneas de campo magnético emiten radiación polarizada en un amplio rango de frecuencias, típicamente desde radio hasta rayos X.
- **Dispersión Compton inversa**: Fotones de baja energía (por ejemplo, del disco de acreción o radiación sincrotrón) son dispersados por electrones relativistas, ganando energía en el proceso y alcanzando frecuencias de rayos gamma.
- **Bremsstrahlung**: Electrones que se frenan al interactuar con iones emiten radiación.

Ejemplos de fuentes dominadas por emisión no térmica incluyen púlsares y, crucialmente, los jets de AGNs.

#### Variabilidad y Flares en AGNs
---
Se explica la naturaleza de los chorros energéticos que provienen de los AGNs, su lugar en el espectro electromagnético. 

Se presenta a detalle la variación en los flares de los AGNs y como es que los flares son los precedentes de las correlaciones de las señales multimensajero
___
Algo distintivo de los blazares es su extrema variabilidad temporal. Las emisiones de rayos gamma pueden aumentar dramáticamente en escalas de tiempo que van desde minutos hasta semanas (flares). Esta variabilidad rápida proporciona información crucial sobre las dimensiones de la región emisora: si una fuente varía significativamente en un tiempo _$Δt$_, su tamaño no puede ser mucho mayor que $c·Δt$ (de lo contrario, los efectos de propagación de luz suavizarían las variaciones).

Los flares son particularmente relevantes para este estudio porque representan los momentos de mayor actividad en los jets, cuando la aceleración de partículas alcanza su máxima eficiencia. Si los AGNs producen neutrinos, es razonable esperar que lo hagan con mayor intensidad durante estos episodios de alta actividad. Por tanto, los flares de rayos gamma constituyen ventanas temporales privilegiadas para buscar coincidencias con detecciones de neutrinos.

Sin embargo, la variabilidad rápida también introduce un **sesgo observacional**: telescopios con tiempos de exposición limitados pueden perder eventos importantes que ocurren cuando no están observando la fuente. Aquí es donde los datos de HAWC presentan una ventaja significativa. A diferencia de telescopios con observaciones programadas, HAWC opera continuamente, monitoreando simultáneamente una gran fracción del cielo. Esto permite capturar flares inesperados y construir curvas de luz más completas.

#### Esquema de Clasificación Unificado **llevar este capitulo más al inicio**
**Conectar el corte de redshift $z < 0.3$ con la absorción EBL.**
*Propuesta de orden:
*- 2.1 Fenomenología de los AGNs (Aquí explicas qué son, Clasificación Unificada, Blazares).*
*- 2.2 Mecanismos de Emisión (Térmicos/No térmicos).*
*- 2.3 Modelos Leptónicos vs Hadrónicos.*

Los AGNs presentan una diversidad morfológica aparente que inicialmente llevó a una nomenclatura compleja: cuásares, radiogalaxias, Seyferts, BL Lacs, FSRQs, etc. Sin embargo, el **modelo de unificación** postula que muchas de estas diferencias observacionales son consecuencia de efectos de orientación y propiedades intrínsecas relacionadas.

El esquema unificado se basa en dos factores principales:

1. **Ángulo de visión**: La orientación del jet respecto a nuestra línea de visión determina efectos de relatividad especial (beaming) que amplifican o atenúan la emisión observada.
2. **Oscurecimiento por el toro**: Un toro de polvo y gas rodea el disco de acreción, obscureciendo nuestra visión directa del núcleo en ciertas orientaciones.

Para este estudio, nos enfocamos en AGNs con jets apuntando aproximadamente hacia nosotros (blazares), ya que estos presentan las emisiones más intensas de rayos gamma y, potencialmente, las mejores oportunidades para detectar neutrinos asociados. Pero no dejamos fuera a los demás AGNs.

---

### II.ii Jets Relativistas


[No se si agregar esta sección para detallar la física de los jets, su formación, estructura y mecanismos de aceleración de partículas. O solo agregarlo en los mecanismos de emisión]

---

### II.iii Modelos de Emisión

La naturaleza de las partículas responsables de las emisiones de muy alta energía en AGNs es uno de los problemas abiertos más importantes en astrofísica de altas energías. Al día de hoy se mantienen dos modelos válidas para la producción de estas partículas.

#### Modelo Leptónico Estándar

En este escenario, las emisiones observadas son generadas exclusivamente por poblaciones de leptones (principalmente electrones y positrones) acelerados en el jet. El espectro de fotones se explica mediante una combinación de:
- Radiación sincrotrón en la banda de baja energía
- Dispersión Compton inversa en la banda de alta energía (rayos gamma)
Este modelo tiene la ventaja de su relativa simplicidad y ha tenido éxito explicando muchas observaciones. Sin embargo, **no predice** flujos de neutrinos.

#### Modelos Hadrónicos

Los modelos hadrónicos postulan que protones (y posiblemente núcleos más pesados) son acelerados a energías ultrarelativistas en el jet. Estos hadrones pueden interactuar mediante:

- Colisiones protón-fotón (_pγ_)
- Colisiones protón-protón (_pp_)

Estas interacciones producen piones cargados y neutros. Los piones neutros decaen en pares de fotones gamma, mientras que los piones cargados decaen en muones y neutrinos, estableciendo una conexión directa entre emisiones de rayos gamma y neutrinos.

**Predicción clave**: Los modelos hadrónicos predicen relaciones energéticas específicas entre el flujo de rayos gamma y el flujo de neutrinos. La detección (o no detección) de neutrinos asociados a flares de rayos gamma proporciona una prueba observacional directa de estos modelos.

Un desafío adicional es la presencia de la **radiación de fondo extragaláctica** (EBL, por sus siglas en inglés), que atenúa los rayos gamma de muy alta energía mediante interacciones fotón-fotón durante su viaje cosmológico. Esta atenuación debe ser modelada cuidadosamente para reconstruir los espectros intrínsecos de las fuentes.

---

## III. Datos y Metodología

### Observatorios y Capacidades Instrumentales

#### HAWC (High-Altitude Water Cherenkov Observatory)

HAWC es un observatorio de rayos gamma ubicado a 4,100 metros sobre el nivel del mar en el volcán Sierra Negativa, México. Su arquitectura consiste en un arreglo de 300 detectores de agua que cubren un área de 22,000 m². Cada detector contiene agua purificada instrumentada con tubos fotomultiplicadores (PMTs) que registran la luz Cherenkov producida por las cascadas de partículas secundarias iniciadas por rayos gamma de muy alta energía en la atmósfera.

**Principios de detección**: Cuando un rayo gamma de energía > 100 GeV interactúa con la atmósfera, produce una cascada electromagnética. Las partículas cargadas de esta cascada, al atravesar el agua de los detectores a velocidades superiores a la velocidad de la luz en ese medio, generan radiación Cherenkov, detectada por los PMTs.

**Ventajas operacionales**: A diferencia de telescopios Cherenkov atmosféricos que requieren observaciones nocturnas programadas, HAWC opera continuamente, las 24 horas del día, monitoreando simultáneamente aproximadamente 2/3 del cielo. Esta operación continua es ideal para capturar eventos transitorios impredecibles como los flares de AGNs.

**Reconstrucción de energía y Pass 5**: La energía de los rayos gamma incidentes se estima mediante el método de "Fraction of Hit PMTs" (fHit)—la fracción de PMTs que registran señal en el evento. El análisis Pass 5 introduce mejoras en resolución angular y dependencia energética. Particularmente relevante para este estudio es la producción de nuevos **bines de energía** B0 y B1, que corresponden a eventos de menor energía (≈ 300 GeV - 10 TeV) y contienen aproximadamente el 66% de la señal total. Estos bines de baja energía son cruciales para maximizar el traslape espectral con Fermi-LAT.
%%Estamos usando una muestra de núcleos activos de galaxias que tienen una mejor resolución y mejoras en las dependencias energéticas dado que el Pass 5 usa nuevos bines de energía  (B0 y B1). Estos bines tienen sensibilidad mejorada a eventos de menor energía (desde los 10 hasta casi los 300 GeV). Con estas mejoras, podemos maximizar el área de traslape espectral con, por ejemplo el telescopio Fermi-LAT%%
Por otra estaremos usando una muestra previamente seleccionada de Fernando Ureña, en este caso aplicó los sigiuentes criterios específicos:

**Muestra seleccionada**: La muestra de Fernando Ureña aplica criterios específicos:

- Redshift z < 0.3 (fuentes relativamente cercanas)
- Uso preferente de bines B0 y B1 
		- La razón es que los AGNs extragalácticos tienen espectros blandos (soft spectra) debido a la atenuación EBL; casi no llega señal a energías más altas (10 TeV+).
		- Traslape con Fermi: Estos bines corresponden a las energías más bajas de HAWC, maximizando la continuidad espectral con el rango de alta energía de Fermi-LAT."
- Ajuste espectral con índice α = 2.5 y corrección por absorción EBL usando el modelo de Domínguez (2011 o 2019)

#### Fermi-LAT (Large Area Telescope)

El telescopio espacial Fermi-LAT, lanzado en 2008, detecta rayos gamma en el rango de 20 MeV a más de 300 GeV. Su arquitectura incluye detectores de silicio para rastrear la trayectoria de pares electrón-positrón producidos por rayos gamma, un calorímetro para medir energía, y detectores anti-coincidencia para rechazar el fondo de rayos cósmicos.

**Catálogos 3FHL vs 4FHL**: Fernando Ureña utilizó el catálogo 3FHL (Third High-Energy Catalog), que cubre 7 años de datos en el rango 10 GeV - 2 TeV. Para esta investigación, propongo migrar al **catálogo 4FHL** (Fourth High-Energy Catalog), que ofrece varias ventajas:

**Beneficios del 4FHL**:
- Tiempo de observación extendido: 16 años vs 7 años
- Sensibilidad mejorada para E > 50 GeV
- Resolución angular mejorada con la energía
- Catálogo expandido: más de 700 fuentes detectadas por encima de 50 GeV

**Consideraciones y desventajas**:
- Ventana energética modificada: El 4FHL cubre 30 GeV - 2 TeV, mientras HAWC cubre 300 GeV - 100 TeV. Esto reduce el rango de traslape espectral
- Espectros más "empinados" (índices espectrales mayores) para fuentes observadas por encima de 10 GeV, complicando extrapolaciones
- Dificultad para incorporar nuevas fuentes a la muestra (análisis en progreso)
- Mayor riesgo de contaminación entre fuentes cercanas debido a la mejor resolución angular

**Criterios de selección para la muestra**:
- Fuentes asociadas o identificadas con AGNs conocidos
- Redshift z ≤ 0.3
- Posición dentro de 40° del cenit de HAWC (para optimizar la respuesta del detector)

#### IceCube Neutrino Observatory

IceCube es un telescopio de neutrinos de un kilómetro cúbico ubicado en el hielo de la Antártida. Consiste en 86 cadenas de detectores instrumentadas con más de 5,000 módulos ópticos que registran la luz Cherenkov producida por muones generados en interacciones de neutrinos.

**Principios de detección**: Cuando un neutrino de alta energía interactúa con el hielo o la roca bajo el detector, puede producir un muón que viaja distancias considerables emitiendo luz Cherenkov. La dirección y tiempo de llegada de esta luz permite reconstruir la trayectoria del muón (y por ende, aproximadamente la del neutrino).

**Resolución angular**: IceCube puede reconstruir la dirección de neutrinos con precisión de ~1° para eventos de tipo "track" (muones que atraviesan el detector), aunque la resolución empeora para energías menores.

**Justificación de su inclusión**: IceCube es actualmente el único instrumento capaz de detectar neutrinos astrofísicos de energías > 100 GeV con resolución angular suficiente para asociarlos con fuentes puntuales. La posible detección de neutrinos coincidentes espacial y temporalmente con flares de rayos gamma en AGNs proporcionaría evidencia crucial para discriminar entre modelos leptónicos y hadrónicos.

**Criterios de selección de eventos**:

- Eventos tipo "track" con resolución angular < 1.5°
- Rango temporal que cubra la operación conjunta de Fermi y HAWC
- Coincidencia direccional con las posiciones de las fuentes de la muestra
- Validación mediante comparación con el espectro completo esperado

For each event, the CSV table contains:  
- NAME: Unique name given to each alert, in form ICYYMMDDA - RUNID,EVENTID: Unique RunID and EventID combination from IceCube DAQ system  
- START,EVENTMJD: Date/time of event detection  
- I3TYPE: Identification of event selection type (see supporting paper publication for details). gfu-gold, gfu-bronze, ehe-gold, hese-gold, or hese-bronze types  
- OTHER_I3TYPES: List of other I3TYPE event selection types this event additionally passed.  
: - RA,DEC [deg] (and _ERR): Best fit direction in J2000 equatorial coordinates, with asymmetric 90% CL error rectangle boundaries.  
- ENERGY:[TeV] Most probable neutrino energy that would have produced this event. Calculated assuming an E^(-2.19) astrophysical neutrino power law flux.  
- FAR: [yr^(-1)] Rate of background events expected for alert events at this energy and sky location.  
- SIGNAL: Probability event is of astrophysical origin, calculated assuming an E^(-2.19) astrophysical neutrino power law flux.  
- *_SCR: Probabilities from post-alert convolutional neural network based classifier applied to each event to better distinguish each events topological signal in the detector  
-- THRGOING_SCR: Primary event vertex outside is the detector and a muon-like track is observed passing through the instrumented volume  
-- START_SCR: Primary event vertex is inside the instrumented volume and a muon-like track is seen  
-- CASCADE_SCR: Primary event vertex is inside the instrumented volume and a shower (non-muon-like track) is observed  
-- SKIMMING_SCR: Primary event vertex outside is the detector and little or no energy deposited within instrumented volume  
-- STOP_SCR: Primary event vertex outside is the detector and a muon-like track is observed stopping in the instrumented volume  
- CR_VETO [Bool]: Significant in-time cosmic-ray shower activity detected in the surface IceTop array, indicating this event is likely a background event.

---

## IV. Análisis Propuesto

### Estrategia Analítica
El análisis se estructurará en tres componentes principales que se retroalimentan entre sí:
#### 1. Caracterización Espectral Multi-Instrumento

**Para HAWC**:

- Ajuste espectral basado en los bines de energía B0 y B1
- Determinación de índices espectrales y flujos normalizados
- Construcción de SEDs en el régimen TeV

**Para Fermi-LAT (4FHL)**:

- Extracción de parámetros espectrales del catálogo
- Construcción de SEDs en el régimen GeV
- Análisis de variabilidad temporal cuando esté disponible

**Integración**:

- Combinación de espectros HAWC + Fermi para obtener SEDs de banda ancha (GeV-TeV)
- Corrección por absorción EBL para reconstruir espectros intrínsecos
- Identificación de características espectrales (picos, quiebres) que puedan distinguir modelos

#### 2. Análisis de Eventos de Neutrinos

**Problema del fondo atmosférico**: Un desafío fundamental es que IceCube detecta un fondo considerable de neutrinos atmosféricos producidos por interacciones de rayos cósmicos en la atmósfera terrestre. Distinguir neutrinos astrofísicos de este fondo requiere análisis estadísticos cuidadosos. El beneficio que tenemos al usar las nuevas modelos de el IceCube es que opodemos plotear los nuevos puntos en las distintos modelos que tenemos al alcance de estos observatorios. 



**Distribución de energías reconstruidas**: Para eventos tipo "track", se analizará la distribución de energías reconstruidas buscando excesos sobre el fondo esperado en las direcciones de las fuentes de la muestra.

#### 3. Búsqueda de Coincidencias

**Coincidencia espacial**: Dada la resolución angular de IceCube (~1°) y las incertidumbres posicionales de fuentes HAWC, se definirá una ventana de búsqueda apropiada (típicamente círculos de 2-3° de radio) alrededor de cada AGN.

**Coincidencia temporal**: Los flares de rayos gamma identificados en las curvas de luz de HAWC y Fermi-LAT definirán ventanas temporales de interés. Se buscará si eventos de neutrinos ocurren durante o poco después de estos periodos de alta actividad gamma.

**Análisis estadístico**: La significancia de cualquier coincidencia detectada se evaluará considerando:

- El número de coincidencias observadas vs esperadas por azar (trials factor)
- La distribución espacial y temporal de eventos de fondo
- Correcciones por búsquedas múltiples (múltiples fuentes y ventanas temporales)

---


