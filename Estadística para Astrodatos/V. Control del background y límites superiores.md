## Bloque V – Métodos Monte Carlo y Simulación Estadística

---

## 1. Motivación: ¿por qué Monte Carlo?

Los métodos analíticos (Poisson, verosimilitud, Wilks) funcionan bajo **aproximaciones asintóticas**.  
Pero en la práctica:
- Los detectores son complejos (resolución angular, energía, eficiencia de disparo, fondos irreducibles).  
- Los datos son limitados (pocos eventos en búsquedas transitorias).  
- La estadística puede ser muy no-Gaussiana.  

👉 La única forma de cuantificar bien la distribución de los estadísticos de prueba es mediante **simulación Monte Carlo (MC)**.

---

## 2. Fundamentos teóricos

### 2.1. Definición

Un algoritmo de **Monte Carlo** genera muchas realizaciones aleatorias de un experimento según un modelo probabilístico, y estima cantidades estadísticas sobre esas realizaciones.

Formalmente, para una variable aleatoria \($X$\) con distribución \($p(x)$\):
$$\mathbb{E}[f(X)] \approx \frac{1}{N} \sum_{i=1}^N f(x_i), \quad x_i \sim p(x)$$

El error de la aproximación decrece como \($1/\sqrt{N}$\).

---

### 2.2. Tipos de Monte Carlo en astrofísica

- **MC físicos**: simulan la física de cascadas (CORSIKA en HAWC, IceCube).  
- **MC detector**: propagan partículas a través del detector → obtienen respuesta en PMTs, calorímetros.  
- **MC estadísticos (pseudo-experimentos)**: generan datasets sintéticos bajo \(H_0\) o \(H_1\) para estimar distribuciones de \(TS\), p-values globales, cobertura, etc.

---

## 3. Generación de pseudo-experimentos

### 3.1. Caso general

1. Definir hipótesis \($H_0$\) (fondo) y \($H_1$\) (señal + fondo).  
2. Generar muchos datasets sintéticos de conteos o eventos.  
3. Para cada dataset, calcular el estadístico de prueba (ej. \($TS$\)).  
4. Construir la distribución empírica de \($TS$\).  

Esto permite:
- Estimar el p-value **sin asumir Wilks**.  
- Evaluar la **cobertura real** de intervalos de confianza.  
- Aplicar corrección por **ensayos múltiples (trial factor)**.

---

### 3.2. Ejemplo: IceCube

- Hipótesis nula: neutrinos atmosféricos isotrópicos.  
- Método: **scrambling en ascensión recta** (se rota aleatoriamente el RA de cada evento, preservando declinación y energía).  
- Se calcula un mapa de \(TS\) para cada realización → se obtiene la distribución global.  
- Esto permite corregir significancias locales → globales.  

---

## 4. Técnicas avanzadas de Monte Carlo

### 4.1. Importance sampling

En lugar de muestrear directamente de \($p(x)$\), se muestrea de \($q(x)$\) y se reponderá:

$$\mathbb{E}[f(X)] = \int f(x) p(x)\, dx = \int f(x)\, \frac{p(x)}{q(x)} q(x)\, dx$$

Usado en simulación de cascadas donde ciertas regiones de fase-espacio son raras.

---

### 4.2. Re-sampling (bootstrap, jackknife)

- **Bootstrap**: generar pseudo-datasets por remuestreo con reemplazo.  
- Usado para estimar la varianza de parámetros ajustados.  
- Ejemplo: en análisis espectrales de fuentes débiles.  

---

### 4.3. MCMC (Markov Chain Monte Carlo)

Cuando la dimensionalidad es alta, se usan cadenas de Markov para explorar la distribución posterior (Bayes).  

- Algoritmo Metropolis-Hastings.  
- Hamiltonian Monte Carlo (NUTS, usado en PyMC3/Stan).  
- Aplicación: estimación de parámetros espectrales con priors físicos (ej. cutoff exponencial).  

---

## 5. Validación y “data challenge”

Los experimentos no solo usan MC para p-values, sino para todo el ciclo:

1. **Optimización del análisis**: cortes, selección de eventos.  
2. **Estimación de sensibilidad**: qué flujo mínimo puede detectarse a 5σ en 50% de los casos.  
3. **Cross-checks**: generar datasets ciegos para evitar sesgos (“blinding”).  
4. **Systematics**: variar parámetros (atmósfera, eficiencia detectora) para estudiar robustez.  

Ejemplo:  
- IceCube define su **sensibilidad** a GRBs mediante miles de MC de estallidos sintéticos.  
- HAWC publica mapas de sensibilidad all-sky basados en MC bajo distintas duraciones de observación.

---

## 6. Aplicaciones directas

### HAWC
- Simulación de cascadas atmosféricas con **CORSIKA**.  
- MC de detector con **GEANT4**.  
- Pseudo-experimentos estadísticos para determinar distribución de \(TS\) en mapas.  

### IceCube
- MC de propagación de muones y neutrinos.  
- Scrambling en RA para pruebas all-sky.  
- MCMC para ajuste de espectros de neutrinos astrofísicos.  

### CTA (Cherenkov Telescope Array, futuro)
- Uso intensivo de MC para optimizar diseño de telescopios.  
- Data challenges basados en MC para preparar análisis de comunidad.  

---

## 7. Limitaciones y desafíos

- **Costo computacional**: simular cascadas atmosféricas es extremadamente caro.  
- **Dependencia de modelos**: incertidumbre en interacción hadrónica, atmósfera, campo geomagnético.  
- **Convergencia estadística**: se necesitan millones de pseudo-experimentos para estimar colas extremas de distribución (ej. 5σ → p ~ 10⁻⁷).  

---

## 8. Resumen

- Monte Carlo es **la herramienta central** en astrofísica de altas energías.  
- Permite validar teorías estadísticas (Wilks, cobertura) y corregir efectos de pocos datos.  
- Se aplica en todo: sensibilidad, intervalos de confianza, significancia global, systematics.  
- Métodos avanzados como MCMC conectan con inferencia bayesiana en espacios de parámetros altos.  
- Sin MC, experimentos como HAWC e IceCube no podrían reportar resultados con rigor.

---
