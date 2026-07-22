---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[Producción de Neutrinos]]"
  - "[[Detección de Neutrinos]]"
  - "[[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]"
  - "[[desintegracion_muon_icecube]]"
tags:
  - tema/neutrinos
  - tema/ciclo-de-vida
  - proyecto/tesis-multimensajera
  - area/academia
---

# Ciclo de Vida del Neutrino

> A diferencia del muón, que vive microsegundos y se desintegra, el neutrino es estable: no "muere", viaja. Su ciclo de vida es en realidad un trayecto de cuatro etapas —nace, se propaga, oscila y por fin interactúa—, y es el hilo que conecta todas las demás notas de este marco.

## Una aclaración: el neutrino no decae

Hablar de "ciclo de vida" para un neutrino es un poco engañoso, y vale la pena dejarlo claro de entrada. El muón tiene un ciclo de vida en sentido literal: aparece, vive unos 2.2 µs y se desintegra (es el tema de [[desintegracion_muon_icecube]]). El neutrino, no. Los neutrinos más ligeros son estables: no hay casi nada en qué decaer, y la interacción débil es tan tenue que cualquier proceso de desintegración sería absurdamente lento. Así que un neutrino producido en el universo temprano sigue por ahí hoy.

Lo que sí tiene es una **historia**: un recorrido con un principio (su producción) y un final observable (la interacción que lo delata). Eso es lo que organiza esta nota, en cuatro etapas.

## Etapa 1 — Nacimiento

El neutrino se crea en un proceso de fuerza débil: una desintegración beta, el decaimiento de un pión, una colisión de protones. En el contexto de la tesis, nace en el chorro de un AGN cuando un protón acelerado choca y produce piones cargados que decaen ($\pi^+ \to \mu^+ + \nu_\mu$, y luego $\mu^+ \to e^+ + \nu_e + \bar\nu_\mu$). Sale con un sabor definido y con una fracción —en torno al 5 %— de la energía del protón original. El catálogo completo de orígenes está en [[Producción de Neutrinos]].

## Etapa 2 — Propagación

Aquí es donde el neutrino se gana su fama de mensajero. Dos propiedades gobiernan el viaje:

- **No tiene carga**, así que los campos magnéticos del espacio interestelar e intergaláctico no lo desvían. Viaja en línea recta y conserva la dirección de su fuente. Un protón de la misma energía, en cambio, llegaría con la trayectoria completamente revuelta.
- **Casi no interactúa**, así que no lo absorben ni el gas, ni el polvo, ni la luz de fondo. Atraviesa regiones opacas incluso para los rayos gamma y recorre distancias cosmológicas —miles de millones de años luz— sin atenuarse.

Como es ultrarrelativista, viaja prácticamente a la velocidad de la luz y, desde su propio marco, apenas transcurre tiempo propio. Llega, en esencia, tan "joven" como salió.

## Etapa 3 — Oscilación (durante el viaje)

Mientras se propaga, el neutrino cambia de identidad. Los estados de sabor con que interactúa ($\nu_e, \nu_\mu, \nu_\tau$) no coinciden con los estados de masa que se propagan ($\nu_1, \nu_2, \nu_3$); la diferencia de fases que acumulan estos últimos hace que el sabor medido oscile con la distancia y la energía:

$$P_{\alpha\to\beta}(L,E) = \left|\sum_i U_{\beta i}\,U_{\alpha i}^*\,e^{-i\,m_i^2 L/2E}\right|^2.$$

Para la tesis, la consecuencia práctica es directa: una fuente que produce sabores en proporción $(\nu_e:\nu_\mu:\nu_\tau) = (1:2:0)$ entrega en la Tierra una mezcla casi igualada, $(1:1:1)$, tras promediar las oscilaciones sobre distancias astronómicas. El desarrollo formal (matriz PMNS, $\Delta m^2$, jerarquías) está en [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]].

## Etapa 4 — Interacción (el final observable)

El viaje termina cuando el neutrino, por fin, interactúa: en un detector, o absorbido por la materia. Por corriente cargada se convierte en su leptón cargado, y ese leptón sí es visible. Para un $\nu_\mu$:

$$\nu_\mu + N \rightarrow \mu^- + X.$$

Ese muón emite luz Cherenkov y reconstruye la dirección del neutrino. Es exactamente el proceso inverso al de su nacimiento —antes un pión "fabricaba" un neutrino emitiendo un muón; ahora el neutrino se "convierte" de vuelta en un muón— y es el eslabón que estudia [[desintegracion_muon_icecube]]. Cómo se traduce esa interacción en una señal medible se trata en [[Detección de Neutrinos]].

## El recorrido de un vistazo

```
NACE              VIAJA                 OSCILA              INTERACTÚA
(AGN)        (línea recta, sin        (1:2:0 → 1:1:1)      (ν_μ + N → μ + X)
 │            absorberse)                 │                     │
 ▼                 ▼                      ▼                     ▼
proceso        sin carga →           cambia de             luz Cherenkov
débil          sin desvío            sabor en ruta         → dirección
               casi sin masa →                              → fuente
               sin absorción
```

La fuerza de este recorrido es que cada flecha es reversible en la lógica: como el neutrino no se desvió ni se absorbió, la dirección del muón final apunta de vuelta, etapa por etapa, hasta el AGN que lo originó. Esa es, en una frase, la razón por la que un neutrino sirve para hacer astronomía.

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- Etapa 1 en detalle: [[Producción de Neutrinos]]
- Etapa 3 en detalle: [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]
- Etapa 4 en detalle: [[Detección de Neutrinos]] y [[desintegracion_muon_icecube]]
- Por qué este trayecto lo hace valioso: [[Importancia del Neutrino como Mensajero Cósmico]]

## Fuente

- Conversación de desarrollo del marco teórico, 2026-06-16
- Cadena fuente→detección desarrollada en [[desintegracion_muon_icecube]]
