# Estadística para Astrodatos
Repaso con el chatgpt
[[Probabilidad y Estadística]]
___

## [[Analisis Estadistico Completo.pdf]]
- Uso 
## [[I. Fundamentos de probabilidad y estadística]]
- **Conceptos básicos de probabilidad**||[[Chapter 3.- Basic Probability Concepts]]
    - Espacio muestral, eventos, probabilidad condicional.
    - [[Teorema de Bayes]] y su importancia en inferencia.
- **Distribuciones fundamentales**[[]]
    - Binomial.
    - Poisson (clave para conteo de fotones/partículas).
    - Gaussiana (límite de Poisson a grandes números).
- **Errores y propagación de incertidumbres**
    - Varianza, desviación estándar, error cuadrático medio.
    - Propagación lineal de errores.
    [[Analisis Bayesiano]]

---

## [[II. Estadística de conteo de eventos]] (el corazón del tema)
- **Procesos de Poisson y detección de fotones/gamma**.
- **Señal vs. fondo**
    - Definición de regiones ON/OFF.
    - Normalización con el parámetro α\alphaα.
- **Cálculo de significancia**
    - Aproximaciones simples ($$S=N_{exceso}BS = \frac{N_\text{exceso}}{\sqrt{B}}S=B​N_{exceso}$$​​).
    - Fórmula de **Li & Ma (1983)**.
    - Comparación entre métodos.
        

---

## [[III. Métodos frecuentistas en astrofísica]]

- **Estimación de parámetros**    
    - Máxima verosimilitud (MLE).
    - Intervalos de confianza.
- **Tests de hipótesis**
    - p-values.
    - Neyman–Pearson lemma (decisión entre hipótesis).
- **Métodos de binned/unbinned likelihood**
    - Aplicados a espectros y mapas de cielo.
    - Ejemplo: detección de exceso en mapas de HAWC.
        

---

## [[IV. Métodos bayesianos en astrofísica]]

- **Inferencia bayesiana**
    - Prior, verosimilitud, posterior.
- **Estimación de parámetros y credibilidad**.
- **Comparación de modelos**
    - Factor de Bayes (Bayes Factor).
- **Aplicaciones en IceCube, HAWC, Fermi**
    - Ejemplo: búsqueda de señales transitorias con priors astrofísicos.
    #### [[Analisis Bayesiano]]

---

## [[V. Control del background y límites superiores]]

- **Métodos de exclusión estadística**
    - Cálculo de upper limits cuando no se alcanza 5σ.
    - Métodos de Feldman–Cousins (1998).
    - Métodos bayesianos para límites de flujo.
        
- **Corrección por “trials factor”**
    - El problema de búsquedas múltiples (penalización por mirar muchas fuentes o muchas posiciones en el cielo).
    - Bonferroni, False Discovery Rate, etc.
        

---

## VI. Técnicas más avanzadas en uso actual
#### [[VI. Incertidumbres sistemáticas y parámetros de “nuisance”]]

- **Análisis de máxima verosimilitud en mapas de cielo**
    - Funciones de respuesta del detector (PSF, área efectiva, tiempo de exposición).
- **Estadística para transitorios y alertas rápidas**
    - Métodos “real-time” (burst searches).
    - Estadística bayesiana secuencial.
- **Métodos no paramétricos y machine learning**
    - Separación gamma/hadrón (clasificación supervisada en HAWC e IceCube).
- **Métodos multimensajero**
    - Coincidencias estadísticas entre fotones, neutrinos, ondas gravitacionales.
    - Métodos de correlación angular.
        

---

## VII. Bibliografía clave

- **Li & Ma (1983), ApJ 272, 317** [1983ApJ...272..317L](https://articles.adsabs.harvard.edu/pdf/1983ApJ...272..317L)→ Biblia para significancia en astrofísica de rayos gamma.
- [**Cowan, “Statistical Data Analysis”**](https://www.sherrytowers.com/cowan_statistical_data_analysis.pdf) → libro estándar en física de partículas.
- **James, “Statistical Methods in Experimental Physics”**.
- **Barlow, “Statistics: A Guide to the Use of Statistical Methods in the Physical Sciences”**.
- **Lectures de IceCube y Fermi-LAT (material público en línea)**.