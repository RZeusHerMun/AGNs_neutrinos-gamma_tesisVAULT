> **Contexto**: detectores tipo HAWC/IceCube/Fermi trabajan con conteo discreto de eventos (fotones/neutrinos/rayos cósmicos) afectado por fluctuaciones de **fondo**. El modelo base es **Poisson**; a grandes números, **Gauss**; para ensayos con dos resultados, **Binomial**.

# Probabilidad en astrofísica. Conceptos
##  **Evento**

Un **evento** es un resultado posible de un experimento.
**Ejemplo:**  
	Que un tanque del observatorio **HAWC** registre un fotón en un intervalo de 1 segundo.

---

### **Espacio muestral**

El **espacio muestral** es el conjunto de todos los eventos posibles.
**Ejemplo:**  
$$\Omega = \{0, 1, 2, 3, \dots\}$$
Número de fotones detectados en un segundo.

---
### **Probabilidad**
La **probabilidad** mide la frecuencia relativa esperada de un evento.

$$P(A) = \frac{\text{número de casos favorables}}{\text{número de casos posibles}}$$
**Ejemplo astrofísico:**  
Si en promedio se detectan 5 fotones por segundo, ¿cuál es la probabilidad de detectar exactamente 3?  
Esto se modela con una **distribución de Poisson**:

$$P(K=k;λ) = \frac{\lambda^k e^{-\lambda}}{k!}$$
donde:
- \($k = 3$\)
- \($\lambda = 5$\) tasa×tiempo
---
##   **Probabilidad condicional**

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$**Ejemplo:**  
Probabilidad de que un evento detectado sea un **fotón gamma** dado que vino de la dirección del **Crab Nebula**.

---

##  **[[Teorema de Bayes]]**
$$P(H \mid D) = \frac{P(D \mid H) \cdot P(H)}{P(D)}$$
Se usa para **actualizar la credibilidad de una hipótesis** ($H$) (ej. “la fuente es real”) dado un conjunto de datos ($D$).

**Ejemplo astrofísico:**  
- \(H\): “El exceso de eventos proviene de una fuente puntual”.
- \(D\): “Se detectaron 50 fotones en la región del cielo asociada al Crab”.

Bayes permite combinar:
- **Prior**: conocimiento previo (catálogos de fuentes, modelos de fondo).
- **Likelihood**: probabilidad de los datos dado el modelo.
- **Evidence**: normalización.

---

##  **Contexto astrofísico relevante**

- **Conteo de fotones:** sigue típicamente una **distribución de Poisson**.
- **Rayos cósmicos:** constituyen el **fondo dominante** en detectores como HAWC.
- **Fluctuaciones de fondo:** se modelan estadísticamente para estimar la significancia de un exceso (ej. método **Li & Ma** para detección de fuentes).
---

###  **Distribución de Poisson en astrofísica**

$$P(k; \lambda) = \frac{\lambda^k e^{-\lambda}}{k!}
$$
- \(k\): número de eventos observados.
- \(\lambda\): número esperado de eventos (tasa × tiempo).

**Ejemplo:**  
Si el fondo esperado es \($\lambda = 20$\) y observamos \(4\), ¿es significativo?  
Se calcula la probabilidad de observar ≥30 dado \($\lambda = 20$\).

---

###  **Significancia estadística**

En astrofísica de rayos gamma, se usa:
$$S = \sqrt{2} \left[ N_{\text{on}} \ln \left( \frac{1+\alpha}{\alpha} \frac{N_{\text{on}}}{N_{\text{on}}+N_{\text{off}}} \right) + N_{\text{off}} \ln \left( (1+\alpha) \frac{N_{\text{off}}}{N_{\text{on}}+N_{\text{off}}} \right) \right]^{1/2}$$

**Fórmula de Li & Ma**, donde:
- \($N_{\text{on}}$\): eventos en la región de la fuente.
- \($N_{\text{off}}$\): eventos en la región de fondo.
- \($\alpha$\): factor de normalización.

---

##  **Resumen rápido**
- **Evento:** resultado posible.
- **Espacio muestral:** conjunto de todos los resultados.
- **Probabilidad:** frecuencia relativa esperada.
- **Probabilidad condicional:** \(P(A|B)\).
- **Teorema de Bayes:** actualiza hipótesis con datos.
- **Distribución de Poisson:** modelo para conteo de fotones.
- **Significancia:** mide si un exceso es real o fluctuación.

---

# **Ejercicios prácticos**

#### **Ejercicio 1: Distribución de Poisson**

Un detector registra en promedio \($\lambda = 4$\) fotones por segundo. 
**Pregunta:** ¿Cuál es la probabilidad de detectar exactamente 6 fotones en un segundo?
**Solución:**
$$P(6; 4) = \frac{4^6 e^{-4}}{6!} \approx 0.104$$
#### **Ejercicio 2: Probabilidad condicional**

Supón que el 70% de los eventos son rayos cósmicos y el 30% son fotones gamma. 
Si un evento proviene de la dirección del Crab, la probabilidad de que sea gamma es 0.9, y si no, es 0.1. 
**Pregunta:** ¿Cuál es la probabilidad de que un evento detectado sea gamma dado que vino del Crab?
**Solución:**
$$P(\text{gamma}|\text{Crab}) = 0.9$$
#### **Ejercicio 3: Teorema de Bayes**

Usando el mismo escenario: 
- \($P(H) = 0.3$\) (evento gamma) 
- \($P(D|H) = 0.9$\) (dirección Crab dado gamma) 
- \($P(D|\neg H) = 0.1$\) (dirección Crab dado rayo cósmico) 

$$P(H|D) = \frac{0.9 \cdot 0.3}{0.9 \cdot 0.3 + 0.1 \cdot 0.7} \approx 0.794$$
#### **Ejercicio 4: Significancia Li & Ma**

Se observa:
- \($N_{\text{on}} = 50$\)
- \($N_{\text{off}} = 200$\)
- \($\alpha = 0.2$\)
**Pregunta:** Calcula la significancia \(S\). 
**Solución:** Sustituir en la fórmula de Li & Ma.

  

---

  [[Analisis Bayesiano]]
