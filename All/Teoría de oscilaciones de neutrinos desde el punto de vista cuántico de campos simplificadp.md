
La exposición presenta la teoría de las oscilaciones de neutrinos desde un punto de vista cuántico de campos simplificado: los estados de sabor (electrón, muón, tau) no coinciden con los eigenestados de masa. Al propagarse, la diferencia de fases entre eigenestados de masa produce una probabilidad dependiente de la distancia y la energía para medir cada sabor, lo que se observa como “cambio de identidad” o oscilación de sabores.

---

### Formulación técnica resumida

- **Estados de sabor y masa**: se usan vectores en un espacio de Hilbert de dimensión 3. Los estados de sabor $|ν_α⟩ (α = e, μ, τ)$ se relacionan con los eigenestados de masa $|ν_i⟩ (i = 1,2,3)$ mediante una matriz de mezcla unitaria U (matriz de Pontecorvo–Maki–Nakagawa–Sakata, PMNS):

     $$|\nu_\alpha\rangle = \sum_{i=1}^{3} U_{\alpha i} , |\nu_i\rangle$$
    
- **Evolución en el tiempo/espacio**: cada eigenestado de masa acumula una fase al propagarse. En régimen relativista la fase relativa entre i y j es aproximadamente
     $$\Delta\phi_{ij} \simeq \frac{\Delta m_{ij}^2,L}{2E} $$
    
    donde ($\Delta m_{ij}^2 = m_i^2 - m_j^2$), L es la distancia de propagación y $E$ la energía del neutrino.
    
- **Probabilidad de transición**: la probabilidad de que un neutrino nacido con sabor α sea detectado con sabor β es
    
    $$P_{\alpha\to\beta}(L,E) = \left|\sum_{i} U_{\beta i} U_{\alpha i}^* e^{-i\frac{m_i^2 L}{2E}}\right|^2$$
    
    Expandiendo, aparecen términos oscilatorios con frecuencias proporcionales a ($\Delta m_{ij}^2/(2E)$) y amplitudes dependientes de los elementos de U.
    
- **Consecuencias físicas**: la presencia de oscilaciones implica ($\Delta m_{ij}^2 \neq 0$) para algún par i,j, por tanto al menos dos neutrinos tienen masa no nula; además, la mezcla U puede introducir CP-violación si contiene fases complejas.
    

---

### Analogy técnica con helados (cómo se ejemplifica)

El video usa una analogía donde:

- **Sabores de helado** representan los **estados de sabor** medibles (ν_e, ν_μ, ν_τ).
- **Marcas o recetas de helado** representan los **eigenestados de masa** (ν_1, ν_2, ν_3).
- Un helado “servido” con un sabor aparente puede ser en realidad una mezcla de recetas subyacentes; al recorrer distancia/tiempo las recetas interfieren entre sí y cambian la probabilidad de identificar un sabor concreto cuando se toma una muestra.

Elementos clave de la analogía y su propósito pedagógico:

- La misma bola visible de helado (estado de sabor) puede descomponerse en distintas “recetas” internas (combinación de eigenestados de masa), lo que ilustra la desalineación sabor–masa.
- Al dejar el helado “viajar” (propagación), las componentes de receta adquieren fases relativas (análogo a ($\Delta\phi_{ij})$) que cambian la mezcla efectiva; esto explica por qué el sabor medido varía con la distancia y la energía.
- Las alternativas de mezcla y la interferencia entre recetas muestran por qué la probabilidad de detectar cada sabor es oscilatoria y dependiente de parámetros físicos concretos.

---

### Mapeo directo entre la analogía y la teoría (tabla compacta)

| Concepto clave         | En la teoría                                                                   | En la analogía del helado                                                                |            |                                                                |
| ---------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------- |
| Estado de sabor        |                                                                                | \|ν_α⟩ observable en interacción débil                                                   |            |                                                                |
| Estado de masa         |                                                                                | \|ν_i⟩ eigenestado con masa m_i                                                          |            |                                                                |
| Matriz de mezcla U     | Relaciona sabores con masas:                                                   | $\|\nu_α⟩ = Σ U_{αi}$                                                                    | $\|\nu_i⟩$ | Receta interna que determina la proporción de cada ingrediente |
| Evolución y fase       | fase ($e^{-i m_i^2 L/(2E)}$) acumulada por cada componente                     | Cada receta “cambia su nota” con el tiempo/distancia; las notas relativas interfieren    |            |                                                                |
| Oscilación             | Probabilidades $P_{α→β}(L,E)$ con términos oscilatorios ∝ $sin^2(Δm^2 L / 4E)$ | La probabilidad de que se perciba un sabor dado varía según cómo interfieren las recetas |            |                                                                |
| Parámetros mensurables | $Δm_{ij}^2$, ángulos de mezcla, fase CP                                        | Frecuencias y amplitudes de las variaciones de sabor observadas en distintos puntos      |            |                                                                |

---

### Notas finales para uso técnico o docente

- La analogía es eficaz porque convierte conceptos abstractos (bases no coincidentes y fases relativas) en objetos familiares y sensoriales; sin embargo, debe complementarse con las fórmulas anteriores para usos cuantitativos.
- Cuando se explique la analogía en un entorno técnico, conviene enfatizar que las “recetas” no son sabores distintos observables por sí mismos: son componentes matemáticas (autovectores de masa) que solo se infieren por medición estadística de muestras a distintas L/E.
- Para un público con formación, mostrar la ecuación de probabilidad junto con una gráfica de $P_{α→β}(L/E)$ y anclar cada término a la parte correspondiente de la analogía mejora la comprensión y evita malentendidos intuitivos.


### Contexto y por qué las oscilaciones son “el problema” de los neutrinos

Las oscilaciones de neutrinos revelaron que los neutrinos no se comportan como partículas de masa cero y que los estados que participan en la interacción débil (sabores) no son los mismos que los autovalores de masa. Eso plantea varias preguntas fundamentales: ¿cómo adquieren masa los neutrinos?, ¿qué es la estructura completa de mezcla y masas?, ¿son Dirac o Majorana?, y ¿qué implicaciones tienen para el Modelo Estándar y la cosmología? Resolver esas preguntas es precisamente el núcleo del “problema de los neutrinos”.

---

### Formalismo esencial (más profundo, pero conciso)

- **Relación sabor–masa**:  
    $$|\nu_\alpha\rangle=\sum_{i=1}^{3}U_{\alpha i},|\nu_i\rangle$$, con ($U$) la matriz PMNS unitaria y ($|\nu_i\rangle$) eigenestados de masa con masas ($m_i$).
    
- **Evolución relativista**: para partículas ultrarelativistas la fase relativa entre (i) y (j) tras propagación (L) es $$\Delta\phi_{ij}\simeq\frac{\Delta m_{ij}^2,L}{2E}$$ donde ($\Delta m_{ij}^2=m_i^2-m_j^2$) y ($E$) es la energía.
    
- **Probabilidad de transición**: $$P_{\alpha\to\beta}(L,E)=\Big|\sum_i U_{\beta i}U_{\alpha i}^* e^{-i\frac{m_i^2 L}{2E}}\Big|^2$$Al expandir aparecen términos de tipo ($\sin^2!\big(\tfrac{\Delta m_{ij}^2 L}{4E}\big)$) y factores de mezcla ($|U_{\alpha i}U_{\beta i}^*|$).
    

Estas ecuaciones encapsulan cómo parámetros medibles ($(\Delta m^2)$, ángulos de mezcla, fases) determinan el patrón de oscilaciones observado.

---

### Consecuencias físicas inmediatas

- **Existencia de masa**: ($\Delta m_{ij}^2\neq 0$) implica que al menos dos neutrinos tienen masa distinta de cero. Esto ya es una extensión del Modelo Estándar, que originalmente tenía neutrinos sin masa.
    
- **Jerarquía de masas**: los datos determinan valores de ($|\Delta m^2|$) pero no el orden absoluto; quedan dos posibilidades: jerarquía normal ($(m_1<m_2<m_3)$) o invertida (($m_3<m_1<m_2$)). La elección afecta señales en neutrinos de supernovas, ββ0ν y cosmología.
    
- **Fase CP leptónica**: la matriz PMNS puede contener una fase CP (o fases si son Majorana). CP violación en el sector leptónico impacta en probabilidad asimétrica ($P_{\alpha\to\beta}\neq P_{\bar\alpha\to\bar\beta}$) y tiene consecuencias para la generación del exceso de materia sobre antimateria (leptogénesis).
    
- **Naturaleza Dirac vs Majorana**: si los neutrinos son fermiones de Majorana, la masa viola número leptónico total (L) y permite procesos como la doble beta sin neutrinos ($ββ0ν$). Detectar $ββ0ν$ revelaría que la masa proviene de términos de Majorana.
    
- **Escala absoluta de masas**: oscilaciones dan diferencias de masa, no la suma ni la masa absoluta. Observaciones cosmológicas y experimentos de laboratorio (espectrometría β, ββ0ν) son necesarios para fijar la escala.
    

---

### Señales experimentales y cómo conectan con los parámetros

- Medidas en oscilación (solar, atmosférico, reactor, acelerador) fijan dos ($\Delta m^2$) y tres ángulos de mezcla principales ($(\theta_{12},\theta_{23},\theta_{13})$) y ya hay indicios de la fase de CP; falta determinar jerarquía y el signo de ($\Delta m_{31}^2$).
- Detecciones de ββ0ν indicarían Majorana y darían información sobre la combinación effective de masa: $$m_{\beta\beta}=\Big|\sum_i U_{ei}^2 m_i\Big|$$
- Límites cosmológicos sobre la suma de masas ($\sum_i m_i$) restringen la escala y descartan regiones de parámetros.

---

### Qué indican las posibles soluciones teóricas (interpretación física)

- **Mecanismo see-saw (tipo I, II, III)**: introduce estados pesados que generan masas pequeñas para los neutrinos ligeros por acoplamientos a escala alta; naturaliza por qué (m_\nu\ll m_{quarks}). Si cierto, sugiere nueva física a escalas muy altas (posible conexión con GUTs).
    
- **Dirac con Yukawas pequeñas**: requiere acoplamientos Yukawa extremadamente pequeños para generar masas tipo Dirac; conceptualmente posible pero menos natural y plantea la pregunta de por qué tales acoplamientos son minúsculos.
    
- **Modelos que violan número leptónico**: Majorana + violación de número leptónico podrían explicar la asimetría bariónica del universo vía leptogénesis si hay fases CP en desintegraciones de estados pesados.
    
- **Modelos con estados estériles**: añadir neutrinos “estériles” (sin interacciones débiles) cambiaría patrones de oscilación y afectaría cosmología; propuestas deben conciliar señales oscilatorias y límites cosmológicos.
    

Cada solución tiene firmas observables diferentes: ver ββ0ν favorece Majorana/violar número leptónico; ver nuevas resonancias o desviaciones energéticas podría indicar estados estériles; restricciones cosmológicas colocan límites en la suma de masas y por tanto en parámetros de modelos see-saw.

---

### Implicaciones más amplias para física y cosmología

- **Extensión del Modelo Estándar**: la existencia de masa neutrina obliga a introducir términos lógicos en el lagrangiano (masas de Dirac/Majorana), lo que abre la puerta a nuevas simetrías, campos y escalas energéticas.
    
- **Origen de la materia en el universo**: CP leptónico + violación de número leptónico puede dar el ingrediente necesario para leptogénesis y luego bariónogenesis.
    
- **Estructura a gran escala**: la suma de masas neutrinas afecta la formación de estructuras y las medidas del fondo cósmico de microondas y de distribución de galaxias.
    

---

### Resumen ejecutivo (qué resolvería “la solución” y por qué importa)

Resolver el problema de los neutrinos consiste en determinar: la escala absoluta de masa, la jerarquía, la naturaleza Dirac/Majorana y la presencia de CP en el sector leptónico. Cada respuesta orienta hacia distintas extensiones del Modelo Estándar (see-saw/estados pesados, simetrías nuevas, neutrinos estériles) y tiene consecuencias directas en cosmología (suma de masas, formación de estructura) y en el origen del exceso de materia. En términos prácticos, detectar ββ0ν o medir la fase CP con precisión serían hitos decisivos que transformarían nuestra comprensión de la física fundamental.

Si quieres, preparo una derivación detallada de la probabilidad de oscilación en el caso de 3 sabores, con expansión en términos de (\sin^2) y fases, y ejemplos numéricos que muestren cómo cambian las probabilidades para valores reales de (\Delta m^2) y ángulos de mezcla.

---

### Objetivo de investigación

Diseñar y ejecutar un programa integrado (teoría + análisis + experimento/tecnología) para avanzar en la comprensión de la naturaleza de la masa neutrino y sus implicaciones: determinar señales discriminantes entre mecanismos de masa (see‑saw vs Dirac pequeño Yukawa vs estados estériles) y buscar firmas observables que conecten oscilaciones, violación de número leptónico y efectos en detectores ópticos/eléctricos dedicados.

---

### Motivación y aporte del equipo

- Teoría de partículas y relatividad: formulación precisa de escenarios extendidos del Modelo Estándar (mecanismos see‑saw, acoplamientos de Dirac reducidos, modelos con neutrinos estériles) y predicción de observables (Δm2, mezclas, mββ, señales en ββ0ν y cambios en espectros).
- Experimentos con bosones W: experiencia en calibración de detectores, análisis de fondo y modelado de interacción débil; transferencia metodológica a detectores de neutrinos y a control sistemático de señales débiles.
- Óptica y polinomios de cernite: aporte en diseño de sensores ópticos, modelado de respuesta energética y desarrollo de filtros polinómicos (cernite) para extracción de señal en presencia de ruido y distorsiones instrumentales.
- Habilidades computacionales y matemáticas: implementación numérica de simulaciones Monte Carlo, ajuste bayesiano de parámetros de oscilación y evaluación de sensibilidad experimental.

---

### Preguntas científicas concretas (hipótesis verificables)

1. ¿Qué rango de parámetros mββ y combinaciones de fases Majorana/CP son compatibles con escenarios see‑saw naturales vs Dirac con Yukawas pequeñas, dados límites cosmológicos actuales?
2. ¿Existen configuraciones experimentales de detectores ópticos/sensores con filtrado cernite que aumenten la sensibilidad a ββ0ν en rangos de mββ alcanzables en próximas generaciones?
3. ¿Cómo afectarían neutrinos estériles con masas ~eV a patrones de oscilación en experimentos a corto y media distancia, y cuáles son las firmas inequívocas frente a sistemáticas instrumentales?
4. ¿Qué combinación de medidas (oscilaciones de acelerador, ββ0ν, espectrometría β, cosmología) optimiza la determinación de jerarquía y naturaleza Majorana/Dirac?

---

### Trabajo propuesto: paquetes de tareas (6–12 meses fase 1)

1. Teoría y simulación (líder: teoría)
    
    - Formalizar 4 escenarios modelo: (A) see‑saw tipo I con escala Mheavy variable; (B) Dirac clásico con Yukawas pequeñas; (C) mezcla con 1–2 estériles; (D) variantes con fases CP/Mayorana.
    - Calcular predicciones para: Δm2, ángulos mezcla, mββ, señales esperadas en ββ0ν y espectros de electrones.
    - Generar conjuntos de «truth» Monte Carlo para cada escenario en rangos de parámetros.
2. Análisis de sensibilidad e interfase con detectores (líder: experimental W)
    
    - Mapear respuesta de detectores existentes y próximos (reactor, acelerador, ββ0ν) a las señales predichas.
    - Modelar backgrounds y sistemáticas transferidas desde experiencia en W (calibración, falsos positivos).
    - Definir métricas de sensibilidad y requerimientos de exposición/ruido para discriminar escenarios.
3. Desarrollo óptico y procesamiento (líder: óptico/polinomios cernite)
    
    - Diseñar esquema de readout óptico y filtros de señal basados en polinomios de cernite que optimicen relación señal/ruido en la banda de interés.
    - Implementar prototipo de filtro digital y medir su capacidad para separar señales neutrino‑like en datos sintéticos contaminados.
    - Evaluar viabilidad de integrar cadena óptica propuesta en detectores de próxima generación.
4. Integración y estadística (líder: matemáticas/estadística)
    
    - Construir pipeline de inferencia bayesiana que combine oscilación, ββ0ν y datos cosmológicos para estimar parámetros y probabilidad de modelos.
    - Pruebas de robustez frente a desviaciones instrumentales y sesgos de modelado.
5. Gestión, documentación y difusión (líder: coordinación)
    
    - Plantilla Notion/bitácora para registrar datos, versionado de códigos, pruebas y resultados; configuración de repositorio y políticas reproducibles.
    - Plan de publicaciones y presentaciones en 12–24 meses.

---

### Hitos y entregables (12 meses)

- Mes 3: Informe de modelos teóricos con predicciones numéricas y conjuntos Monte Carlo básicos.
- Mes 6: Evaluación de sensibilidad para detectores actuales; documento que cuantifica requisitos experimentales para distinguir modelos.
- Mes 9: Prototipo de filtro cernite funcional y reporte de reducción de ruido en señales sintéticas.
- Mes 12: Pipeline combinado de inferencia y primer paper interno con escenarios excluibles/compatibles; plan técnico para un prototipo experimental a escala.

---

### Recursos y colaboraciones necesarias

- Computación: cluster para Monte Carlo y muestreo bayesiano (GPUs opcionales).
- Laboratorio óptico: banco óptico, fotodetectores (SiPM/PMT), electrónica de adquisición.
- Acceso a datos: colaboración con experimentos de oscilación/ββ0ν o uso de datasets públicos para validación.
- Financiamiento modesto inicial para personal (1–2 posdocs/estudiantes), prototipos de sensores y viajes de colaboración.

---

### Riesgos principales y mitigaciones

- Riesgo: modelos alternativos degenerados dentro de incertidumbres instrumentales. Mitigación: diseñar métricas de discriminación que combinen múltiples observables (no depender de una sola medida).
- Riesgo: filtros ópticos no mejoran S/N en condiciones reales. Mitigación: pruebas tempranas con datos reales/sintéticos, iteración rápida de diseño; considerar enfoques híbridos (óptico + análisis estadístico avanzado).
- Riesgo: dependencias externas (acceso a detectores/datos). Mitigación: asegurar acuerdos de colaboración o concentrarse en escenarios de «pathfinder» con componentes de bancada.

---

### Resultados esperados y contribuciones científicas

- Conjuntos de predicción que marquen regiones de parámetros donde ββ0ν o nuevas oscilaciones son esperables.
- Evaluación clara de la viabilidad de técnicas ópticas basadas en polinomios de cernite para mejorar sensibilidad experimental.
- Pipeline público reproducible que combine datos de distintas técnicas para restringir la naturaleza de la masa neutrino.
- Al menos una publicación de referencia y un prototipo demostrador que pueda presentarse a convocatorias para avanzar a fase experimental mayor.

---

### Primeros pasos concretos (iniciar inmediatamente)

1. Reunir al equipo y asignar roles por tarea.
2. Crear la bitácora Notion con templates para modelos, MC, experimentos y resultados (yo puedo ayudar a diseñarla).
3. Lanzar trabajo teórico para generar muestras MC simplificadas (3 escenarios, 10^5 eventos cada uno) en 4 semanas.
4. Paralelizar diseño óptico con pruebas de filtros en datos sintéticos en 6 semanas.

Si quieres, preparo: (a) el esquema de la bitácora Notion con plantillas para cada paquete de trabajo; (b) el primer Jupyter notebook que genera los Monte Carlo simplificados para los 4 escenarios y ejemplos numéricos comparativos. ¿Cuál prefieres que entregue primero?