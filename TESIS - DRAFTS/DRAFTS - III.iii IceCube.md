---
status: borrador
capitulo: 3
seccion: 3.3
tags: [tesis/escritura, tesis/datos, icecube, neutrinos]
---
# III.iii IceCube Neutrino Observatory

> **Estado:** 🟡 Borrador — falta agregar más contenido
---

## Descripción del Observatorio

- 1 km³ en hielo antártico, 86 cuerdas colgantes %%STRINGS%%, 5160 DOMs %%DIGITAL OPTICAL MODULES%% 
- Profundidades: 1.45–2.45 km, separación triangular 125 m
- DeepCore: subarray denso, neutrinos hasta ~100 GeV (mínimo 10 GeV)
- IceTop: 82 pares de detectores Cherenkov en superficie, rayos cósmicos >300 TeV

## Principio de Detección
![[Pasted image 20260624113212.png|532]]
Cuando un neutrino interactúa con el hielo, puede producir un muón que viaja emitiendo luz Cherenkov. La dirección y tiempo de llegada permite reconstruir la trayectoria.
![[Pasted image 20260515124957.png]] 
## Tipos de eventos: Tracks vs Cascades

| Propiedad | Tracks | Cascades |
|-----------|--------|----------|
| Resolución angular | ~0.5°–1° (>1 TeV) | ~10° |
| Resolución energética | Moderada | Mejor |
| Uso en este estudio | **Sí (principal)** | No |

**¿Por qué tracks?** Se necesita resolución angular para asociar a fuentes puntuales.

## Justificación

Si un AGN produce neutrinos de alta energía, deberían aparecer correlacionados con episodios de actividad gamma. IceCube es el único instrumento capaz de detectar neutrinos astrofísicos >100 GeV con resolución angular suficiente para asociarlos con fuentes puntuales.

## Criterios de selección

- Eventos tipo "track" con resolución angular < 1.5°
- Rango temporal que cubra operación conjunta Fermi+HAWC
- Coincidencia direccional con las fuentes de la muestra

## Formato de datos (IceCat-1 CSV)

| Campo | Descripción |
|-------|-------------|
| NAME | Nombre único (ICYYMMDDA) |
| I3TYPE | gfu-gold, gfu-bronze, ehe-gold, hese-gold, hese-bronze |
| RA, DEC | Dirección J2000, errores asimétricos 90% CL |
| ENERGY [TeV] | Energía más probable (asumiendo E⁻²·¹⁹) |
| FAR [yr⁻¹] | Tasa de fondo esperada |
| SIGNAL | Probabilidad de origen astrofísico |
| *_SCR | Clasificadores CNN (THRGOING, START, CASCADE, SKIMMING, STOP) |
| CR_VETO | Actividad de rayos cósmicos en IceTop |

## Problema del fondo atmosférico

IceCube detecta un fondo considerable de neutrinos atmosféricos. Distinguir astrofísicos de atmosféricos requiere análisis estadísticos cuidadosos.

## Datos disponibles

- Archivo: `C:\Users\el_he\Documents\TESIS\data\icecube_copiaPRUEBAS.csv`
- IceCat-1: DOI 10.7910/DVN/SCRUCD

---

## Conexiones
- Anterior: [[DRAFTS - III.ii Fermi-LAT]]
- Siguiente: [[DRAFTS - IV. Análisis]]
- Catálogo: [[IceCat-1 -- TheIceCubeEventCatalogofAlertTracks]]
- Hub: [[XCRITURA]]
