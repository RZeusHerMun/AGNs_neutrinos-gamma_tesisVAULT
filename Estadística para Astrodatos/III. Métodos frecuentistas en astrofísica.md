# 📘 Estadística en Astrofísica de Altas Energías  
## Bloque III – Métodos Frecuentistas e Inferencia Estadística

---

## 1. Introducción: del conteo al modelo estadístico

En Bloques I y II vimos el caso de detección basada en **conteo de eventos** (Poisson, ON/OFF, significancia).  

Sin embargo, los experimentos modernos no se limitan a contar:  
- La señal se distribuye en **energía, dirección, tiempo**.  
- El fondo tiene distribuciones distintas.  
- Se necesitan métodos generales para extraer parámetros físicos: **flujo, espectro, localización, variabilidad**.  

La herramienta central aquí es la **inferencia estadística frecuentista** basada en **funciones de verosimilitud**. (likelihood)

---

## 2. Función de verosimilitud

La **verosimilitud** es la probabilidad de observar los datos \(D\) dados unos parámetros \($\theta$\):
$$\mathcal{L}(\theta) = P(D|\theta)$$
En práctica, se suele trabajar con el **logaritmo de la verosimilitud**:
$$\ln \mathcal{L}(\theta) = \sum_i \ln P(d_i|\theta)
$$

donde los datos se asumen independientes.

**Ejemplo HAWC**:  
- Cada evento tiene variables reconstruidas: dirección \(($\alpha,\delta$)\), energía estimada, parámetros de discriminación gamma/hadrón.  
- La verosimilitud modela la probabilidad de cada evento dado un modelo de flujo gamma + fondo.  

**Ejemplo IceCube**:  
- Cada neutrino candidato tiene dirección, energía, calidad de reconstrucción.  
- La verosimilitud combina la distribución espacial y energética para separar señal de fondo atmosférico.

---

## 3. Estimación por máxima verosimilitud (MLE)

El estimador de máxima verosimilitud es el valor de \($\theta$\) que maximiza \($\mathcal{L}(\theta)$\):
$$\hat{\theta} = \arg \max_\theta \mathcal{L}(\theta)$$

Propiedades:
- **Consistencia**: \($\hat{\theta} \to \theta_\text{real}$\) cuando \($N \to \infty$\).  
- **Invarianza**: si \($\hat{\theta}$\) maximiza \($\mathcal{L}$\), entonces \($g(\hat{\theta})$\) maximiza \($\mathcal{L}$\) para la función transformada.  
- **Distribución asintótica**: para grandes \($N$\), \($\hat{\theta}$\) es aproximadamente Gaussiana con varianza dada por la **matriz de Fisher**:
$$\text{Var}(\hat{\theta}) \approx \left[ -\frac{\partial^2 \ln \mathcal{L}}{\partial \theta^2} \bigg|_{\hat{\theta}} \right]^{-1}$$

---

## 4. Intervalos de confianza: método de perfil de verosimilitud

Se define la razón de verosimilitud:
$$\lambda(\theta) = \frac{\mathcal{L}(\theta)}{\mathcal{L}(\hat{\theta})}$$
La estadística de prueba es:
$$TS(\theta) = -2 \ln \lambda(\theta) = -2 \ln \frac{\mathcal{L}(\theta)}{\mathcal{L}(\hat{\theta})}$$
Por el **teorema de Wilks**, \($TS(\theta)$\) sigue una ($\chi^2$) con grados de libertad igual al número de parámetros.  

Un intervalo de confianza al 95% para un parámetro corresponde a los valores de \($\theta$\) con:
$$TS(\theta) \leq 3.84$$
---

## 5. Test estadísticos y detección de señal

La prueba clásica es comparar:
- \($H_0$\): hipótesis nula (solo fondo).  
- \($H_1$\): hipótesis alternativa (fondo + señal).  
Definimos:
$$TS = -2 \ln \frac{\mathcal{L}(H_0)}{\mathcal{L}(H_1)}
$$
Si \($H_0$\) es verdadera, \($TS \sim \chi^2$\) con 1 g.l.  
→ entonces la **significancia estadística** es:
$$Z = \sqrt{TS}$$

---

### Ejemplo aplicado: IceCube

- \($H_0$\): todos los eventos son neutrinos atmosféricos.  
- \($H_1$\): hay una fuente astrofísica puntual en dirección \(($\alpha,\delta$)\).  
- Construyen una verosimilitud combinada de energía y dirección.  
- El **TS** se calcula para cada punto del cielo → se genera un **mapa de significancias**.  

---

## 6. p-values y corrección por ensayos múltiples

- **p-value**: probabilidad de observar un resultado igual o más extremo bajo \(H_0\).  
- Convención en física de partículas:  
  - \($p \approx 2.7\times10^{-3})$ → $(3\sigma)$.  
  - \($p \approx 5.7\times10^{-7}$\) → \($5\sigma$\).  

### Trials factor
Cuando se hacen muchas pruebas (ej. búsqueda de fuentes en todo el cielo), el p-value local se sobreestima.  

- **p-value global**: probabilidad de encontrar al menos una fluctuación igual o mayor en todo el conjunto de pruebas.  
- Se corrige mediante simulaciones Monte Carlo del cielo isotrópico.  

---

## 7. Aplicaciones en astrofísica de altas energías

### HAWC
- Usa MLE para ajustar el flujo espectral $(dN/dE = N_0 (E/E_0)^{-\gamma}$).  
- Los intervalos de confianza de $(N_0$) y ($\gamma$) se obtienen por perfil de verosimilitud.  
- El **TS** se usa para generar mapas de significancia (fuentes extendidas, variabilidad).  

### IceCube
- Método de máxima verosimilitud en búsqueda de fuentes puntuales y correlaciones multimessenger.  
- \(TS\) convertido en p-values locales y globales tras corrección por número de fuentes y posiciones.  
- Ejemplo: detección del blazar TXS 0506+056 (2017).  

### Fermi-LAT
- Uso extensivo de **Likelihood Analysis** en el paquete `gtlike`.  
- Significancia reportada como **Test Statistic (TS)**, con \$(TS = 25 \approx 5\sigma$\).  

---

## 8. Limitaciones y puntos avanzados

- El teorema de Wilks falla si los parámetros están en el borde del espacio permitido (ej. señal ≥ 0).  
- Para conteos muy bajos, los métodos asintóticos no son válidos → se requieren intervalos de confianza “exactos” (ej. **Feldman–Cousins**).  
- Métodos bayesianos ofrecen alternativas, especialmente para límites superiores (Bloque IV).  

---

## 9. Resumen

- La **máxima verosimilitud** es el estándar para estimar parámetros de fuentes astrofísicas.  
- Los **tests de razón de verosimilitud** permiten cuantificar significancia de detección.  
- El **TS → Z** conecta directamente con la convención de “5σ = descubrimiento”.  
- Correcciones por ensayos múltiples son críticas en estudios “all-sky”.  
- Estos métodos forman el núcleo de la estadística aplicada en HAWC, IceCube, Fermi-LAT, VERITAS, CTA, etc.

---
