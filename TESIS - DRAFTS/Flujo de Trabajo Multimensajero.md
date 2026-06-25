---
status: referencia
tags: [tesis/escritura, tesis/metodologia, multimensajero]
---
# Pipeline completo del análisis gamma–neutrino.

```
Fermi-LAT (3FHL/4FHL)          HAWC (Pass 5, B0/B1)
       ↓                              ↓
  Catálogo GeV                   Survey TeV AGNs
       ↓                              ↓
  Selección: z<0.3, AGN        Ajuste espectral (α=2.5)
       ↓                              ↓
       └──────── Muestra combinada ────┘
                      ↓
              135 AGNs con posiciones,
              espectros GeV–TeV, TS
                      ↓
              IceCube (IceCat-1)
              Tracks, >100 GeV
                      ↓
         ┌─── Búsqueda de coincidencias ───┐
         │                                  │
    Espacial                          Temporal
    (ventanas angulares,             (flares gamma,
     contornos 90% CL,               curvas de luz)
     Vincenty)                        [futuro]
         │                                  │
         └──────── Tests estadísticos ──────┘
                      ↓
    ┌─────────────────────────────────────────┐
    │ • Scrambling (isotrópico vs banda HAWC) │
    │ • KS distancias angulares               │
    │ • Ponderado signalness / energía        │
    │ • Spearman TS vs neutrinos              │
    │ • Upper limits 95% CL                   │
    │ • Corrección post-trials                │
    └─────────────────────────────────────────┘
                      ↓
              Resultado: sin correlación
              → Consistente con emisión leptónica
```

## Justificación del enfoque multimensajero

La astronomía multimensajera combina información de diferentes "mensajeros cósmicos" (fotones, neutrinos, ondas gravitacionales, rayos cósmicos) para obtener una imagen más completa de las fuentes astrofísicas. Estas nuevas observaciones tienen mas que ver con las posibilidades que sean astrofísicas que con las nuevas detecciones, queremos asignarles una probabilidad de que sean o no provenientes de las distintas fuentes astrofísicas que tenemos a disposición, no solo un

En esta tesis:
- **Fotones gamma** (Fermi-LAT + HAWC): identifican fuentes con emisión de alta energía
- **Neutrinos** (IceCube): discriminan entre mecanismos leptónicos y hadrónicos
- La **correlación espacial** (y eventualmente temporal) entre ambos mensajeros es la prueba directa

## Ventajas del enfoque estadístico de población

A diferencia de estudios de fuentes individuales (como TXS 0506+056), este trabajo analiza una **población completa** de 135 AGNs, permitiendo:
- Establecer límites superiores globales
- Identificar tendencias estadísticas
- Reducir sesgos de selección

## Archivos de datos

| Instrumento | Archivo | Contenido |
|-------------|---------|-----------|
| HAWC | `AGN_135 - copiaPRUEBAS.xlsx` | 135 AGNs, TS, posiciones, espectros |
| IceCube | `icecube_copiaPRUEBAS.csv` | Eventos track, posiciones, energías, signalness |
| Fermi-LAT | Catálogo 3FHL/4FHL | Parámetros espectrales GeV |

---

## Conexiones
- Análisis completo: [[DRAFTS - IV. Análisis]]
- Muestra HAWC: [[DRAFTS - III.i HAWC]]
- Datos Fermi: [[DRAFTS - III.ii Fermi-LAT]]
- Datos IceCube: [[DRAFTS - III.iii IceCube]]
- Resultados y tests: [[Modelo nulo de banda HAWC]], [[Prueba KS de distancias angulares]], [[Tests ponderados]], [[Correlación TS vs neutrinos]]
- Hub: [[XCRITURA]]
