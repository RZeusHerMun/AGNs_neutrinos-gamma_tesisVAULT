---
status: borrador
capitulo: 3
seccion: 3.3
tags: [tesis/escritura, tesis/datos, icecube, neutrinos]
---
# III.iii IceCube Neutrino Observatory

> **Estado:** 🟡 Borrador — buen contenido disponible

---

## Descripción del Observatorio

- 1 km³ en hielo antártico
- 86 cadenas de detectores, 5160 DOMs (Digital Optical Modules)
- Profundidades: 1.45–2.45 km, separación triangular 125 m
- DeepCore: subarray denso, neutrinos hasta ~100 GeV (mínimo 10 GeV)
- IceTop: 82 pares de detectores Cherenkov en superficie, rayos cósmicos >300 TeV

## Principio de Detección

Cuando un neutrino de alta energía interactúa con el hielo o la roca bajo el detector, puede producir un muón que viaja distancias considerables emitiendo luz Cherenkov. La dirección y tiempo de llegada de esta luz permite reconstruir la trayectoria del muón y aproximadamente la del neutrino.

## Tipos de eventos: Tracks vs Cascades

| Propiedad | Tracks | Cascades |
|-----------|--------|----------|
| Resolución angular | ~0.5°–1° (>1 TeV) | ~10° |
| Resolución energética | Moderada | Mejor |
| Uso en este estudio | **Sí (principal)** | No |

**¿Por qué tracks?** Se necesita resolución angular para asociar a fuentes puntuales. Las cascades, aunque tienen mejor resolución energética, no permiten distinguir si el neutrino viene de una fuente específica.

## Justificación de su inclusión

Si un AGN produce neutrinos de alta energía, deberían aparecer correlacionados con episodios de actividad gamma. IceCube es el único instrumento capaz de detectar neutrinos astrofísicos >100 GeV con resolución angular suficiente para asociarlos con fuentes puntuales.

## Criterios de selección de eventos

- Eventos tipo "track" con resolución angular < 1.5°
- Rango temporal que cubra la operación conjunta de Fermi y HAWC
- Coincidencia direccional con las posiciones de las fuentes de la muestra
- Búsqueda de coincidencias durante flares de gammas

## Formato de datos (IceCat-1 CSV)

| Campo | Descripción |
|-------|-------------|
| NAME | Nombre único (ICYYMMDDA) |
| RUNID, EVENTID | Identificadores DAQ |
| I3TYPE | gfu-gold, gfu-bronze, ehe-gold, hese-gold, hese-bronze |
| RA, DEC [deg] | Dirección J2000, con errores asimétricos 90% CL |
| ENERGY [TeV] | Energía más probable (asumiendo E⁻²·¹⁹) |
| FAR [yr⁻¹] | Tasa de fondo esperada |
| SIGNAL | Probabilidad de origen astrofísico |
| *_SCR | Clasificadores CNN (THRGOING, START, CASCADE, SKIMMING, STOP) |
| CR_VETO | Actividad de rayos cósmicos en IceTop |

## Problema del fondo atmosférico

IceCube detecta un fondo considerable de neutrinos atmosféricos producidos por interacciones de rayos cósmicos. Distinguir neutrinos astrofísicos de este fondo requiere análisis estadísticos cuidadosos.

## Datos disponibles

- Archivo: `C:\Users\el_he\Documents\TESIS\data\icecube_copiaPRUEBAS.csv`
- IceCat-1: DOI 10.7910/DVN/SCRUCD (Harvard Dataverse)
- IceCat-2: catálogo actualizado

## Validación de la muestra

- Ajuste espectral de HAWC basado en B0/B1    
- Parámetros espectrales del 4FHL
- Distribución de energías reconstruidas en IceCube (para tracks)

---

## 🔗 Conexiones
- Anterior: [[III.ii Fermi-LAT]]
- Siguiente: [[IV. Análisis]]
- Catálogo IceCat-1: [[IceCat-1 -- TheIceCubeEventCatalogofAlertTracks]]
- Alertas GCN: en [[GENERAL reseach.canvas]] (nodo GCN)
- Hub: [[XCRITURA]]
