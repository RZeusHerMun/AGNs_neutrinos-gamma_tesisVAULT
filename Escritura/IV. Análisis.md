---
status: en-proceso
capitulo: 4
tags: [tesis/escritura, tesis/analisis, estadistica]
---
# IV. Análisis y Resultados

> **Estado:** 🟠 En proceso — resultados estadísticos completos, falta redacción formal
> **Subnota con resultados detallados:** ver notas individuales abajo

---

## Estrategia Analítica

El análisis se estructura en componentes que se retroalimentan:

### Caracterización espectral

#### HAWC
- Ajustes con B0/B1
- Reconstrucción de SEDs TeV
- Corrección EBL

#### Fermi-LAT
- Parámetros del 4FHL
- SEDs GeV
- Análisis de variabilidad cuando exista curva de luz

#### SED combinada (GeV–TeV)
- Comparación directa entre Fermi y HAWC
- Evaluación de consistencia del espectro

### Búsqueda de coincidencias con IceCube
- Definir ventanas espaciales basadas en resolución combinada
- Buscar neutrinos dentro de esa región
- Corridas temporales centradas en flares gamma

### Significancia estadística
- Comparación con fondo atmosférico
- Número de coincidencias vs esperadas
- Corrección por búsquedas múltiples

---

## Resultados Estadísticos (resumen)

| Test | Resultado | p-value | Interpretación |
|------|-----------|---------|----------------|
| Scrambling isotrópico 3° | 39 vs 23.6 | 0.0007 | ⚠️ ARTEFACTO del modelo |
| **Scrambling banda HAWC 3°** | 39 vs 38.2 | **0.4723** | No significativo |
| Contornos elípticos 90% CL | 32 vs 34.9 | 0.75 | Compatible con azar |
| Corrección empírica post-trials | — | 0.7673 | No significativo |
| KS distancias angulares | D=0.072 | 0.4725 | Distribuciones idénticas |
| Ponderado signalness | 5.12 vs 5.49 | 0.5674 | Sin señal (z=−0.23σ) |
| Ponderado energía | 22.9 vs 26.3 | 0.6728 | Sin señal (z=−0.47σ) |
| Spearman TS vs neutrinos | **ρ=−0.831** | — | Correlación negativa → leptónico |
| Upper limit 95% CL | ~8 coinc. / ~5.9% | — | Límite superior |

> **Conclusión global:** Ningún test muestra evidencia de correlación. Resultados consistentes con emisión leptónica para esta muestra.

## Detalles de cada análisis

Para el desarrollo completo de cada test, consultar las notas dedicadas:

- [[Modelo nulo de banda HAWC]] — Modelo isotrópico vs banda HAWC (la revelación clave)
- [[geometría de detecciones]] — Fórmula de Vincenty para distancias angulares
- [[Correccion de Bonferroni o Empirica]] — Look-Elsewhere Effect y correcciones post-trials
- [[Prueba KS de distancias angulares]] — Test de Kolmogorov-Smirnov
- [[Tests ponderados]] — Ponderación por signalness y energía
- [[Correlación TS vs neutrinos]] — Spearman ρ = −0.831
- [[All/Problemas]] — Log de issues y correcciones aplicadas

## Mejoras propuestas (no implementadas)

1. **Stacking Likelihood**: Gaussiana 2D en vez de corte binario → $\Psi(\Delta r) = \frac{1}{2\pi\sigma^2} e^{-\Delta r^2/2\sigma^2}$
2. **Pesos astrofísicos**: por flujo/TS de HAWC → $S = \sum_i w_i \times \text{coincidencia}_i$
3. **Elipticidad completa**: Gaussiana 2D asimétrica → $\chi^2 = \Delta RA^2/\sigma_{RA}^2 + \Delta Dec^2/\sigma_{Dec}^2$
4. **Análisis TS formal**: $TS_{total} = \sum TS_i$ sobre todos los neutrinos
5. **Información temporal**: curvas de luz HAWC, flares, ventanas temporales

---

## 🔗 Conexiones
- Anterior: [[III.iii IceCube]]
- Siguiente: [[V. Catálogo de Coincidencias]]
- Avances de reuniones: [[Avances Tesis]]
- Estadística de soporte: [[Estadística para Astrodatos/Estadística para Astrodatos]]
- Hub: [[XCRITURA]]
