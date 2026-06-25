---
status: referencia
tags: [tesis/escritura, tesis/metodologia, workflow]
---
# **[[XCRITURA]]**
# Flujo de Trabajo Multimensajero (Fermi + HAWC + IceCube)

> **Estado:** 📘 Notas de referencia para la metodología

---

## ¿Por qué Fermi-LAT ayuda?

1. **Referencia sistemática de fuentes gamma**: los catálogos 4FGL listan posiciones, errores, espectros, índices de variabilidad y curvas de luz para miles de fuentes (50 MeV–~1 TeV). [Ref: fermi.gsfc.nasa.gov](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/12yr_catalog/)
2. **Cobertura complementaria a HAWC**: HAWC opera en TeV, Fermi en sub-TeV. Comparar ambos ayuda a construir SEDs y ver si hay continuidad espectral consistente con emisión hadrónica.
3. **Multi-mensajería ya probada**: hay campañas que usan Fermi-LAT para seguir blazares relacionados con alertas IceCube (ej: 4FGL J0658).

## Qué se obtiene del catálogo Fermi

- **Posición (RA, Dec) + elipse de incertidumbre** → cruce espacial
- **Parámetros espectrales** (índice, curvatura, flujo en bandas) → modelar origen
- **Flags de variabilidad y curvas de luz** → búsquedas temporales

## Pipeline de integración

1. **Descarga y preprocesa catálogos** (4FGL DR3/DR4, 3HWC, IceCat-1/2)
2. **Búsqueda espacial**: para cada neutrino track, buscar fuentes Fermi/HAWC dentro del contorno 90% CL. Priorizar por Δθ/σθ
3. **Búsqueda temporal**: curvas de luz Fermi para actividad alrededor del tiempo del neutrino (±days/weeks)
4. **Criterios espectrales**: extrapolación Fermi→TeV compatible con HAWC? ¿Requiere nueva componente?
5. **Análisis estadístico**: scrambles (randomizar RA manteniendo Dec), pruebas likelihood, stacking, p-values post-trials
6. **Stacking poblacional**: si no hay coincidencias individuales significativas, apilar todas las fuentes de un tipo

## Herramientas recomendadas

- **Fermitools / Fermipy**: curvas de luz, espectros, likelihood LAT
- **Gammapy**: análisis gamma-ray
- **Astropy / healpy**: posiciones, mapas, scrambles
- **Scipy / PyMC**: pruebas estadísticas, modelado bayesiano

## Ejemplos concretos para la tesis

- Script/pipe: ingestión catálogos → cruce espacial+temporal → test estadístico → catálogo de coincidencias con ranking
- Caso de estudio: análisis de eventos IceCube Gold con búsqueda de contrapartidas Fermi/HAWC

## Riesgos / Limitaciones

- Diferente rango energético (LAT no llega a TeV, y viceversa)
- Resolución posicional de IceCube → privilegiar track-like events
- Trials factor: múltiples ventanas y fuentes → controlar con scrambles o correcciones

## Referencias

- [Fermi LAT 4FGL](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/12yr_catalog/)
- [4LAC AGN catalog](https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermilac.html)
- [HAWC 3HWC](https://ui.adsabs.harvard.edu/abs/2020ApJ...905...76A/abstract)
- [IceCube real-time alerts](https://icecube.wisc.edu/science/real-time-alerts/)

---

## 🔗 Conexiones
- Relacionado: [[III.ii Fermi-LAT]], [[III.i HAWC]], [[III.iii IceCube]]
- Código Python: [[All/HAWC+IceCube- Fuentes multimensajero]]
- Hub: [[XCRITURA]]
