---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[Producción de Neutrinos]]"
  - "[[Importancia del Neutrino como Mensajero Cósmico]]"
  - "[[desintegracion_muon_icecube]]"
  - "[[6. Interacciones y Producción de Mensajeros]]"
tags:
  - tema/neutrinos
  - tema/rayos-gamma
  - tema/procesos-hadronicos
  - tema/agn
  - proyecto/tesis-multimensajera
  - area/academia
---

# Neutrinos y Rayos Gamma — La Conexión Hadrónica

> Es el núcleo físico de la tesis. En un acelerador cósmico, los piones cargados producen neutrinos y los piones neutros producen rayos gamma, y ambos nacen del mismo choque de protones. Por eso un neutrino que coincide con una fuente de gammas es la prueba de que ahí se aceleran protones.

## El acelerador hadrónico

En el chorro relativista de un AGN, los protones se aceleran hasta energías enormes. Cuando uno de esos protones choca —contra otro protón (proceso $pp$) o contra un fotón del entorno (fotoproducción $p\gamma$)—, produce piones. Y los piones son el cruce de caminos entre las dos señales que persigue esta tesis:

```
p + p  →  π0 , π+ , π−  + X
p + γ  →  Δ+  →  p + π0      (≈ 2/3)
              →  n + π+      (≈ 1/3)
```

A partir de aquí, los dos tipos de pión siguen destinos distintos:

```
π0  →  γ + γ                         (rayos gamma)
π+  →  μ+ + ν_μ ; μ+ → e+ + ν_e + ν̄_μ   (neutrinos)
```

El pión neutro decae en dos fotones gamma. El cargado arranca la cadena de neutrinos que ya conoces de [[Producción de Neutrinos]] y de [[desintegracion_muon_icecube]]. La clave es que **los dos salen del mismo proceso**: no se puede acelerar protones y producir piones cargados sin producir también neutros. Gammas y neutrinos son las dos caras de una misma moneda hadrónica.

## El reparto de energía

Las dos señales heredan, de forma ordenada, la energía del protón:

- El pión se lleva alrededor del 20 % de la energía del protón en la fotoproducción.
- El $\pi^0$ reparte su energía entre dos fotones: $E_\gamma \approx E_{\pi^0}/2$.
- El $\pi^+$ la reparte entre cuatro leptones de la cadena: $E_\nu \approx E_{\pi^+}/4$.

De ahí sale la regla práctica que usa toda la astronomía multimensajera:

$$E_\nu \;\approx\; \frac{1}{2}\,E_\gamma, \qquad E_\nu \;\approx\; 0.05\,E_p.$$

Un protón de PeV produce gammas de $\sim$0.1 PeV y neutrinos de $\sim$50 TeV. Como la cantidad de piones cargados y neutros es comparable (idéntica en $pp$, sesgada hacia los neutros en $p\gamma$), la potencia que se va en gammas y en neutrinos es del mismo orden. Esto permite predecir un flujo de neutrinos a partir de un flujo de gammas medido, y al revés.

## El neutrino como prueba decisiva (el "smoking gun")

Aquí está el argumento que justifica la tesis entera. Un AGN puede emitir rayos gamma por dos rutas muy distintas:

- **Ruta leptónica.** Electrones relativistas que radian por sincrotrón y dispersan fotones por Compton inverso (modelos SSC). Produce gammas, pero **ni un solo neutrino**.
- **Ruta hadrónica.** Protones que producen piones, como arriba. Produce gammas **y** neutrinos.

Con rayos gamma solos, distinguir las dos rutas es difícil: ambos modelos ajustan el espectro electromagnético con parámetros razonables. Esta es la famosa degeneración leptónico/hadrónica. El neutrino la rompe de un golpe: **solo la ruta hadrónica los produce**. Detectar un neutrino en coincidencia con una fuente de gammas es, por tanto, la prueba directa —no inferida— de que ahí se aceleran protones, y de paso señala a los AGN como candidatos a fuentes de los rayos cósmicos de alta energía.

## Un matiz crucial: los gammas se absorben, los neutrinos no

La correlación no siempre es uno a uno, y entender por qué es importante para no malinterpretar los datos. Los rayos gamma de muy alta energía se absorben:

$$\gamma + \gamma \rightarrow e^+ + e^-,$$

al chocar con la luz de fondo (dentro de la fuente densa y durante el viaje, contra la luz extragaláctica de fondo, EBL). Esa energía absorbida se reprocesa hacia energías más bajas. Los neutrinos, en cambio, escapan intactos. La consecuencia es que existen fuentes **"oscuras en gamma pero ruidosas en neutrinos"**.

El caso de **NGC 1068** lo ejemplifica: IceCube midió un flujo de neutrinos más de un orden de magnitud por encima del límite superior de su emisión gamma de TeV. La interpretación es que los neutrinos se producen muy cerca del agujero negro, en una corona tan densa que los rayos gamma quedan atrapados y no escapan. Es un acelerador "calorimétrico", oculto a los telescopios gamma pero brillante para IceCube.

Frente a él, **TXS 0506+056** es un blazar con el chorro apuntando a la Tierra: ahí los gammas sí escapan y la coincidencia gamma–neutrino fue clara. Dos paradigmas opuestos —fuente transparente vs. fuente oculta— que conviene tener presentes al diseñar y leer una búsqueda de correlaciones.

## Qué implica para la metodología de la tesis

- Buscar **coincidencia espacial y temporal** entre neutrinos de IceCube y fuentes/flares de gammas (HAWC, Fermi-LAT) es buscar, en el fondo, la firma hadrónica común.
- La relación $E_\nu \approx E_\gamma/2$ orienta en qué bandas de energía esperar la contraparte.
- La absorción de gammas obliga a contemplar que algunas fuentes neutrino-brillantes tengan emisión gamma débil o desplazada a baja energía: ausencia de gammas de TeV no es ausencia de aceleración hadrónica.

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- Cómo se producen los piones y neutrinos: [[Producción de Neutrinos]]
- Los hitos observacionales (NGC 1068, TXS 0506+056): [[Importancia del Neutrino como Mensajero Cósmico]]
- La cadena de Feynman en detalle: [[desintegracion_muon_icecube]]
- Producción de mensajeros en las fuentes: [[6. Interacciones y Producción de Mensajeros]]

## Fuente

- IceCube Collaboration (2022), *Evidence for neutrino emission from NGC 1068*, Science — [DOI](https://www.science.org/doi/10.1126/science.abg3395)
- IceCube Collaboration (2018), *Multimessenger observations of TXS 0506+056*, Science — [DOI](https://www.science.org/doi/10.1126/science.aat1378)
- Relaciones de producción hadrónica $pp$ / $p\gamma$ (resonancia $\Delta$) y reparto de energía $E_\nu \approx E_\gamma/2$, estándar en astronomía multimensajera.
- Conversación de desarrollo del marco teórico, 2026-06-16
