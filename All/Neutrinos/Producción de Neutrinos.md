---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[Neutrinos y Rayos Gamma - Conexión Hadrónica]]"
  - "[[Ciclo de Vida del Neutrino]]"
  - "[[desintegracion_muon_icecube]]"
  - "[[6. Interacciones y Producción de Mensajeros]]"
tags:
  - tema/neutrinos
  - tema/produccion
  - proyecto/tesis-multimensajera
  - area/academia
---

# Producción de Neutrinos

> Un neutrino nace cada vez que ocurre un proceso de fuerza débil. Eso pasa en el Big Bang, en el centro del Sol, en una supernova, en la alta atmósfera y —lo que importa para esta tesis— cuando un protón acelerado choca en el chorro de un AGN.

## La regla general

Donde hay interacción débil, hay neutrinos. Casi siempre aparecen como subproducto de una desintegración o una colisión que cambia el sabor de un fermión. La energía con que nacen abarca más de quince órdenes de magnitud, desde los micro-electronvoltios del fondo cósmico hasta los cientos de PeV del neutrino más energético jamás detectado. Conviene ordenarlos por origen.

## Fuentes naturales, de baja a alta energía

### Reliquias del Big Bang (fondo cósmico de neutrinos)

Cuando el universo tenía alrededor de un segundo, se enfrió lo bastante para que los neutrinos dejaran de interactuar y se desacoplaran del resto de la materia. Esos neutrinos siguen ahí, formando el **fondo cósmico de neutrinos** (CνB): unos 336 por cm³ a una temperatura de 1.95 K. Son tan fríos (energías de micro-eV) que aún no se han detectado de forma directa, pero su existencia deja huella en la abundancia de elementos ligeros y en el fondo de microondas.

### Sol y estrellas

En el núcleo del Sol, la fusión del hidrógeno produce neutrinos electrónicos. El primer paso de la cadena protón-protón es

$$p + p \rightarrow d + e^+ + \nu_e,$$

y otras ramas (Be, B, el ciclo CNO) añaden contribuciones a mayor energía. El resultado es un flujo de unos $6\times10^{10}$ neutrinos por cm² y segundo llegando a la Tierra, con energías de MeV. La discrepancia histórica entre los neutrinos solares predichos y los detectados —el "problema de los neutrinos solares"— fue lo que destapó las oscilaciones de sabor.

### Supernovas con colapso de núcleo

Cuando el núcleo de una estrella masiva colapsa, casi toda la energía gravitatoria liberada —del orden de $3\times10^{53}$ erg, un 99 % del total— escapa en forma de neutrinos de todos los sabores, en una ráfaga de unos diez segundos. La supernova SN1987A confirmó el mecanismo: detectores como Kamiokande-II e IMB registraron unas dos docenas de eventos, la primera detección de neutrinos de una fuente astrofísica fuera del Sol.

### Neutrinos atmosféricos

Los rayos cósmicos que golpean la alta atmósfera generan cascadas de piones y kaones que decaen produciendo neutrinos:

```
p + núcleo  →  π± , K±  + X
π+  →  μ+ + ν_μ
μ+  →  e+ + ν_e + ν̄_μ
```

A bajas energías esto da una proporción aproximada de dos neutrinos muónicos por cada electrónico. Estos neutrinos (de escala GeV) fueron la otra pieza que confirmó las oscilaciones, al verse que faltaban $\nu_\mu$ según la dirección de llegada. Para un telescopio de neutrinos como IceCube son **ruido de fondo**, y separarlos de los astrofísicos es uno de los grandes retos del análisis (ver [[desintegracion_muon_icecube]]).

## Fuentes artificiales

- **Reactores nucleares.** Las desintegraciones beta de los fragmentos de fisión emiten un flujo intenso de antineutrinos electrónicos ($\bar\nu_e$) de pocos MeV. Fueron la fuente del descubrimiento de Reines y Cowan y siguen siendo clave para medir parámetros de oscilación.
- **Aceleradores.** Haces de protones que golpean un blanco producen piones que, al decaer en vuelo, generan haces dirigidos de $\nu_\mu$. Permiten experimentos de oscilación de línea base larga con energía y dirección controladas.

## Neutrinos astrofísicos de alta energía — el caso de la tesis

Esta es la fuente que da sentido al trabajo. En los aceleradores cósmicos —los chorros relativistas de los AGN, entre otros— los protones se aceleran hasta energías extremas y luego interactúan con la materia y la radiación del entorno. Hay dos canales hadrónicos:

```
p + p   →  π± , π0  + X          (colisión protón-protón)
p + γ   →  Δ+  →  n + π+         (fotoproducción, vía resonancia Δ)
              →  p + π0
```

Los piones cargados son los que fabrican neutrinos, siguiendo la misma cadena que arriba:

```
π+  →  μ+ + ν_μ
μ+  →  e+ + ν_e + ν̄_μ
```

De aquí salen dos hechos centrales:

- **Proporción de sabores en la fuente.** Cada pión cargado produce dos neutrinos de tipo muónico y uno de tipo electrónico, una proporción $(\nu_e : \nu_\mu : \nu_\tau) = (1:2:0)$. Tras oscilar durante el viaje cósmico, la mezcla que llega a la Tierra se reparte casi a partes iguales, $(1:1:1)$.
- **Energía heredada.** Cada neutrino se lleva en torno al 5 % de la energía del protón que lo originó. Un protón de PeV produce neutrinos de decenas de TeV: justo el rango que detecta IceCube.

El pión neutro ($\pi^0$) no produce neutrinos, sino rayos gamma ($\pi^0 \to \gamma\gamma$). Que los dos tipos de pión nazcan del mismo choque es la raíz física de la correlación neutrino–gamma que persigue la tesis, y se desarrolla en [[Neutrinos y Rayos Gamma - Conexión Hadrónica]].

## Resumen por fuente

| Fuente | Energía típica | Sabor dominante | Papel en la tesis |
|--------|---------------|-----------------|-------------------|
| Fondo cósmico (CνB) | µeV | todos | contexto cosmológico |
| Sol / estrellas | MeV | $\nu_e$ | — |
| Supernovas | decenas de MeV | todos | mensajero transitorio |
| Atmosféricos | GeV | $\nu_\mu$ (2:1) | **fondo a eliminar** |
| Reactores / aceleradores | MeV–GeV | $\bar\nu_e$ / $\nu_\mu$ | calibración, oscilaciones |
| **Astrofísicos (AGN)** | **TeV–PeV** | **1:1:1 en la Tierra** | **señal buscada** |

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- Qué pasa después de nacer: [[Ciclo de Vida del Neutrino]]
- La coproducción con rayos gamma: [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]
- La cadena completa AGN → detector: [[desintegracion_muon_icecube]]

## Fuente

- Mecanismos estándar de producción (cadena pp solar, colapso de supernova, cascadas atmosféricas, fotoproducción $p\gamma$ vía resonancia $\Delta$).
- Conversación de desarrollo del marco teórico, 2026-06-16
