# Bloque IV – Métodos Bayesianos y Límites Superiores
[[Analisis Bayesiano]]

---
## 1. Motivación: ¿por qué necesitamos límites superiores?

En muchas búsquedas (ej. neutrinos de una supernova, rayos gamma de una galaxia, coincidencia multimessenger), el resultado es **no detección** o **exceso débil**. Es decir, la señal está inmiscuida en el fondo esperado. Entonces se establece un límite superior.

Responde a la pregunta:
- Dado lo que hemos observado, cual es el valor máximo de la señal que sigue siendo estadísticamente compatible con nuestros datos a un nivel de confianza (CL) determinado (al 95% o 90)? Es decir,
	- Si el flujo real fuera mayor que este límite las probabilidades de observar tan pocos eventos habrían sido extremadamente bajas, por lo que descartamos esa posibilidad.

En vez de decir simplemente “no hay señal”, los experimentos cuantifican:
$$N_\text{sig} \leq N_\text{UL}$$(con cierta confianza, ej. 90% o 95%)

Esto es, te puedo asegurar con un 95% de confianza que *no vas a encontrar un neutrino en esta población* o bajo esta cuestión pues **te puedo asegurar que en un rango de error determinado no vas a encontrar nada**, pues mi muestra debe progresar mas con su incertidumbre

donde $(N_\text{UL})$ es el número máximo de eventos compatibles con los datos.

Esto se traduce luego en un límite al **flujo** o **luminosidad** de la fuente.
#### El Problema del Fondo de Poisson
La estadística subyacente en el conteo de eventos se rige por la distribución de Poisson. Si esperas un número de eventos de fondo $b$ y una señal $s$, la probabilidad de observar $n$ eventos es:

$$P(n|s+b) = \frac{(s+b)^n e^{-(s+b)}}{n!}$$

Si observas una cantidad de eventos $n$ que es muy cercana al fondo $b$, necesitas encontrar el valor máximo de la señal $s$ que haga que tu observación (o un resultado menor) ocurra con una probabilidad de apenas el $5\%$ (para un límite al $95\%$ CL).


## 2. Métodos clásicos (frecuentistas)

### 2.1. Intervalos de confianza con cobertura

- En el enfoque frecuentista, un **intervalo de confianza del 95%** es un procedimiento que, repetido en muchos experimentos, contiene al valor real en el 95% de los casos.  
- Importante: esto **no significa** que la probabilidad de que el parámetro real esté dentro del intervalo sea 95% (esa es la interpretación bayesiana).

## 1. Construcción de Neyman y el Enfoque Feldman-Cousins

El enfoque frecuentista clásico puede generar un problema grave: cuando el número de eventos observados fluctúa _por debajo_ del fondo esperado ($n < b$), los cálculos pueden arrojar límites superiores negativos o intervalos de confianza vacíos, lo cual es físicamente imposible para un flujo o una sección eficaz.

Para solucionar esto, se usa el **enfoque unificado de Feldman-Cousins**. Este método utiliza una razón de verosimilitud como regla de ordenamiento. Esto permite una transición suave y automática entre establecer un límite superior (cuando hay solo fondo) y reportar un intervalo de confianza de dos lados (cuando hay un descubrimiento claro), garantizando que el límite siempre sea físicamente válido ($s \geq 0$).
#### 2.2. Feldman–Cousins (1998)

Problema: en experimentos de conteo con bajo número de eventos, los intervalos clásicos pueden dar resultados “no físicos” (ej. límite inferior negativo).  

Feldman y Cousins propusieron un método unificado:
- Se construye una **ordenación por razón de verosimilitudes** para decidir qué valores de \($N_\text{sig}$\) incluir en el intervalo.  
- Esto garantiza **cobertura exacta** y evita intervalos negativos.  
- En el caso de no detección, el intervalo se convierte automáticamente en un **límite superior**.

Ejemplo aplicado: IceCube reporta límites superiores al flujo de neutrinos de estallidos de rayos gamma cuando no detecta coincidencias.

### 2. Razón de Verosimilitud (Profile Likelihood) y el Método $CL_s$

Este método es el estándar actual en física de colisionadores y se usa extensamente en física de altas energías. Utiliza la razón de verosimilitud perfilada como estadístico de prueba para evaluar la compatibilidad de los datos con diferentes hipótesis de señal.

Para evitar excluir modelos reales simplemente porque el fondo fluctuó muy hacia abajo (una exclusión espuria donde el experimento en realidad no tiene sensibilidad para ver la señal), se utiliza el método $CL_s$:

$$CL_s = \frac{CL_{s+b}}{CL_b}$$

Se establece el límite superior en el valor de la señal donde $CL_s \leq \alpha$ (con $\alpha = 0.05$ para el $95\%$ CL). Matemáticamente, esto penaliza el límite, haciéndolo más conservador cuando el poder estadístico del experimento es débil.


---

## 3. Métodos bayesianos

### 3.1. Principios
En el marco bayesiano, se calcula la distribución de probabilidad a posteriori para la señal $s$ dado el número de observaciones $n$, marginando los parámetros de molestia (como las incertidumbres sistemáticas en el modelo de fondo o la eficiencia del detector).
En Bayes se interpreta la probabilidad como **grado de creencia**.  

Se define la **posterior** para el parámetro \($\theta$\):
$$p(\theta|D) = \frac{p(D|\theta)\,\pi(\theta)}{p(D)}$$


- \($p(D|\theta)$\): verosimilitud.  
- \($\pi(\theta)$\): prior (conocimiento previo).  
- \($p(D)$\): normalización (evidencia).  

El límite superior al 95% se define como:
$$\int_0^{\theta_\text{UL}} p(\theta|D)\, d\theta = 0.95$$Esto requiere definir una distribución a priori (prior), que por lo general se asume plana o uniforme para valores donde $s \geq 0$.

Visualiza cómo interactúan estas variables para definir el límite de sensibilidad estadística:

---

### 3.2. Elección del prior

- **Uniforme en señal**: \($\pi(N_\text{sig}) = \text{cte}$\).  
- **Jeffreys prior**: \($\pi(\theta) \propto \sqrt{I(\theta)}$\), donde \($I(\theta)$\) es la información de Fisher.  
- En astrofísica, la elección del prior es crítica → puede afectar fuertemente el límite reportado.

Ejemplo: HAWC a veces asume prior uniforme en flujo, lo que da límites más conservadores.

---

## 4. Comparación de enfoques

| Método | Interpretación | Pros | Contras |
|--------|---------------|------|---------|
| Frecuentista (Feldman–Cousins) | Cobertura garantizada, independiente de priors | Objetivo, aceptado en física de partículas | Puede ser complicado de implementar numéricamente |
| Bayesiano | Probabilidad de que el parámetro esté en un rango dado | Intuitivo, flexible, útil con pocos eventos | Dependencia fuerte del prior, debates filosóficos |

---

## 5. Aplicaciones prácticas en astrofísica

### 5.1. HAWC
- Si no se detecta una fuente puntual, se reporta un límite superior al flujo gamma en cierto rango de energía.  
- Ejemplo: búsqueda de emisión gamma de GRBs.  

### 5.2. IceCube
- En búsquedas transitorias, a menudo no se detecta señal → se reporta un límite al número de neutrinos asociados al evento.  
- Luego se traduce en un límite a la **fluencia** (energía por unidad de área).  

### 5.3. Fermi-LAT
- Cuando un blazar no se detecta en cierto estado, se publican límites superiores al flujo por bin energético.  
- Uso rutinario de análisis bayesiano en `gtlike`.

## Aplicación Práctica en Astrofísica

En el contexto de detectores astrofísicos, la señal teórica $s$ depende directamente de la integral del flujo diferencial incidente, que suele modelarse como una ley de potencias:

$$\Phi(E) = \Phi_0 \left(\frac{E}{E_0}\right)^{-\gamma}$$

Cuando calculas el límite superior estadístico para $s$, este valor se traduce matemáticamente para restringir la constante de normalización $\Phi_0$. Geométricamente, el resultado final se reporta en las publicaciones como "curvas de sensibilidad" (sensitivity curves) o áreas de exclusión, que marcan la frontera superior del flujo máximo posible en diferentes bandas de energía.

---

## 6. Métodos avanzados

- **CLs method** (usado en CERN): evita excluir modelos demasiado rápido en casos de baja sensibilidad.  
- **Bayesian model comparison**: en vez de dar solo límites, se compara \(H_0\) vs \(H_1\) vía evidencia bayesiana.  
- **Hierarchical Bayes**: modela poblaciones de fuentes (ej. distribución de blazares).

---

## 7. Resumen

- Los **límites superiores** son esenciales cuando no se detecta señal.  
- El enfoque **frecuentista (Feldman–Cousins)** asegura cobertura y evita intervalos negativos.  
- El enfoque **bayesiano** da una interpretación directa en términos de probabilidad, pero depende del prior.  
- En astrofísica de altas energías (HAWC, IceCube, Fermi, CTA), ambos enfoques se usan y suelen reportarse en paralelo.  
- Los límites son tan importantes como las detecciones, pues permiten descartar modelos teóricos.

---
