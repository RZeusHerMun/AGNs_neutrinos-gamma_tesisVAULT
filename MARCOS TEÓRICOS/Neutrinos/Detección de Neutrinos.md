---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[desintegracion_muon_icecube]]"
  - "[[III.iii IceCube]]"
  - "[[Ciclo de Vida del Neutrino]]"
tags:
  - tema/neutrinos
  - tema/deteccion
  - tema/icecube
  - proyecto/tesis-multimensajera
  - area/academia
---

# Detección de Neutrinos

> No se detecta el neutrino, sino el rastro de la partícula cargada que crea al interactuar. Como interactúa poquísimo, hace falta instrumentar volúmenes enormes —un kilómetro cúbico de hielo, en el caso de IceCube— y leer la luz Cherenkov que deja esa partícula secundaria.

## El problema de fondo

La sección eficaz del neutrino es del orden de $10^{-44}$ cm² a energías de MeV (ver [[Neutrino - Descripción y Propiedades]]). Eso significa que la inmensa mayoría de los neutrinos atraviesan cualquier detector sin tocar nada. La única forma de cazar unos pocos es aumentar dos factores: la **masa del blanco** (más átomos, más oportunidades de choque) y el **tiempo de exposición**. De ahí que los telescopios de neutrinos no sean aparatos de laboratorio, sino kilómetros cúbicos de hielo o agua natural instrumentados con sensores.

Ayuda que la sección eficaz crece con la energía: los neutrinos astrofísicos de TeV–PeV son bastante más detectables que los solares, aunque sigan siendo escasos.

## Principio: detección indirecta

El neutrino es invisible, pero la partícula que produce al interactuar no lo es. La secuencia es siempre la misma:

1. El neutrino interactúa con un núcleo del medio por fuerza débil.
2. Nace una partícula cargada (un leptón y/o una lluvia de hadrones).
3. Esa partícula cargada emite luz que los sensores registran.
4. Con los tiempos y posiciones de llegada de la luz se reconstruye energía y dirección.

### Dos canales de interacción

- **Corriente cargada (CC):** $\nu_\ell + N \to \ell^- + X$. El neutrino se convierte en su leptón cargado ($e$, $\mu$ o $\tau$), lo que **identifica el sabor** y, en el caso del muón, da una dirección precisa.
- **Corriente neutra (NC):** $\nu + N \to \nu + X$. El neutrino sobrevive pero sacude el núcleo; se ve la lluvia hadrónica, pero no el sabor ni una buena dirección.

### Luz Cherenkov

La señal estrella es la **radiación Cherenkov**: cuando una partícula cargada viaja por un medio más rápido que la luz *en ese medio*, emite un cono de luz, análogo al estampido sónico. El ángulo del cono cumple

$$\cos\theta_c = \frac{1}{n\,\beta},$$

donde $n$ es el índice de refracción del medio y $\beta = v/c$. En agua o hielo ($n\approx 1.33$) y para partículas ultrarrelativistas ($\beta\approx 1$), el cono se abre a unos $41°$. Esa luz azulada es lo que ven los miles de módulos ópticos.

## Topologías de evento: tracks y cascades

Lo que el detector "dibuja" depende del sabor y del canal. Hay dos morfologías, y la distinción es central para esta tesis:

|                            | Tracks                        | Cascades                           |
| -------------------------- | ----------------------------- | ---------------------------------- |
| Origen                     | $\nu_\mu$ por CC → muón largo | $\nu_e$, $\nu_\tau$ y todas las NC |
| Forma                      | traza recta de km             | lluvia casi esférica               |
| Resolución angular         | $\lesssim 1°$ (> TeV)         | $\sim 10°$–$15°$                   |
| Resolución en energía      | moderada                      | mejor                              |
| Uso para fuentes puntuales | **sí, principal**             | limitado                           |

La razón de fondo es geométrica: el muón de un *track* viaja varios kilómetros casi en línea recta y apunta de vuelta a la fuente; una *cascade* es un destello compacto sin una dirección clara. Por eso los análisis de correlación con AGN usan *tracks*. Esta es justo la física que desarrolla [[desintegracion_muon_icecube]] (el muón como eslabón final) y que aplica [[III.iii IceCube]].

## Los detectores

- **IceCube** (Polo Sur): 1 km³ de hielo antártico instrumentado con 5160 módulos ópticos en 86 cadenas, entre 1.45 y 2.45 km de profundidad. Es el instrumento de referencia para neutrinos astrofísicos de TeV–PeV y la fuente de datos de esta tesis. Detalle completo en [[III.iii IceCube]].
- **KM3NeT** (Mediterráneo): el equivalente en agua marina, con dos bloques (ARCA para astronomía, ORCA para oscilaciones). En 2025 registró KM3-230213A, el neutrino más energético jamás observado ($\sim 220$ PeV).
- **Super-Kamiokande** (Japón): 50 000 toneladas de agua ultrapura; dominó la física de neutrinos solares y atmosféricos y confirmó las oscilaciones.
- **Pioneros**: el experimento de cloro de Homestake (que destapó el déficit solar), Kamiokande y SNO (que lo resolvió midiendo el flujo total por corriente neutra).
- **Radiodetección** (ANITA, ARA, y proyectos futuros): para el rango EeV se buscan los pulsos de radio (efecto Askaryan) de las cascadas en hielo, donde el volumen necesario supera lo viable con sensores ópticos.

## El fondo y cómo se combate

El mayor enemigo son los **muones y neutrinos atmosféricos** producidos por rayos cósmicos (ver [[Producción de Neutrinos]]). Dos estrategias clásicas:

- **Usar la Tierra como filtro.** Los muones atmosféricos solo llegan desde arriba; ningún muón cruza el planeta. Seleccionar eventos *ascendentes* (que vienen de "abajo", tras atravesar la Tierra) elimina ese fondo de un plumazo.
- **Espectro y vetos.** Los neutrinos atmosféricos tienen un espectro más blando que los astrofísicos, y la actividad coincidente en la superficie (IceTop) ayuda a vetar eventos de origen atmosférico.

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- El detector de la tesis: [[III.iii IceCube]]
- El muón como eslabón final, con diagramas: [[desintegracion_muon_icecube]]
- Dónde encaja la detección en el trayecto: [[Ciclo de Vida del Neutrino]]

## Fuente

- Parámetros de IceCube según [[III.iii IceCube]].
- KM3NeT Collaboration (2025), evento KM3-230213A (~220 PeV) — [km3net.org](https://www.km3net.org/observation-of-an-ultra-high-energy-cosmic-neutrino-with-km3net/)
- Conversación de desarrollo del marco teórico, 2026-06-16
