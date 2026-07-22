---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[Neutrino en el Modelo Estándar]]"
  - "[[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]"
tags:
  - tema/neutrinos
  - tema/fisica-de-particulas
  - proyecto/tesis-multimensajera
  - area/academia
---

# Neutrino — Descripción y Propiedades

> El neutrino es un fermión elemental sin carga eléctrica, de masa minúscula, que solo interactúa por la fuerza débil y la gravedad. Esa indiferencia ante casi todo es justo lo que lo vuelve un mensajero astrofísico único.

## Qué es

El neutrino es una partícula elemental: no está hecho de nada más pequeño, hasta donde sabemos. Pertenece a la familia de los leptones, igual que el electrón, y comparte con él dos rasgos —espín $1/2$ (es un fermión) y carácter puntual— pero le falta lo que define al electrón: la carga eléctrica. Tampoco tiene carga de color, así que la fuerza fuerte tampoco lo toca. Le quedan dos formas de interactuar con el resto del universo: la fuerza débil y la gravedad. Ambas son extraordinariamente tenues a escala de partícula, y de ahí viene todo lo demás.

Hay tres tipos, o **sabores**, uno por cada leptón cargado: el neutrino electrónico ($\nu_e$), el muónico ($\nu_\mu$) y el tauónico ($\nu_\tau$). Cada uno tiene su antipartícula ($\bar\nu_e$, $\bar\nu_\mu$, $\bar\nu_\tau$). Que son exactamente tres —ni dos ni cuatro— no es una suposición: la anchura de desintegración del bosón $Z^0$ medida en el LEP fija el número de sabores ligeros en $N_\nu = 2.984 \pm 0.008$.

## Propiedades clave

| Propiedad | Valor / carácter |
|-----------|------------------|
| Espín | $1/2$ (fermión) |
| Carga eléctrica | $0$ |
| Carga de color | ninguna |
| Interacciones | débil y gravitatoria |
| Sabores | $\nu_e,\ \nu_\mu,\ \nu_\tau$ (+ antineutrinos) |
| Masa | no nula pero diminuta: $m_\nu < 0.45$ eV (KATRIN, 2024) |
| Helicidad observada | levógira (los antineutrinos, dextrógiros) |

### Masa: pequeña, pero distinta de cero

Durante décadas se asumió que el neutrino no tenía masa. El descubrimiento de la oscilación de sabor lo desmintió: para que un neutrino cambie de identidad en el camino hace falta que al menos dos de los estados de masa sean distintos, y eso exige masa. Lo que miden las oscilaciones son diferencias de masas al cuadrado, no la masa en sí:

$$\Delta m^2_{21} = 7.41\times10^{-5}\ \text{eV}^2, \qquad \Delta m^2_{3\ell} = 2.514\times10^{-3}\ \text{eV}^2$$

La escala absoluta se acota por otras vías. La medida directa más precisa, del experimento KATRIN (2024), sitúa el límite en $m_\nu < 0.45$ eV con 90 % de confianza. Para hacerse una idea: eso es más de un millón de veces menos que la masa del electrón. El desarrollo formal de las oscilaciones, con la matriz PMNS y las jerarquías de masa, está en [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]].

### Sección eficaz: por qué casi nunca choca

La probabilidad de que un neutrino interactúe se mide por su sección eficaz, y es ridículamente pequeña. Para un neutrino de unos pocos MeV ronda

$$\sigma \sim 10^{-44}\ \text{cm}^2,$$

unas veinte órdenes de magnitud por debajo de una sección eficaz nuclear típica. Dicho de otro modo: un neutrino solar podría atravesar un año luz de plomo y tener apenas una probabilidad del orden del 50 % de chocar con algo. La consecuencia práctica es doble: por un lado, un neutrino escapa de los entornos más densos del universo sin inmutarse; por otro, detectarlo obliga a construir detectores del tamaño de un kilómetro cúbico (ver [[Detección de Neutrinos]]).

La sección eficaz **crece con la energía**, aproximadamente de forma lineal en un amplio rango, lo que ayuda: los neutrinos astrofísicos de TeV–PeV son mucho más "atrapables" que los solares, aunque siguen siendo escurridizos.

### Helicidad: solo participan los zurdos

La fuerza débil es selectiva con la quiralidad. Los neutrinos que interactúan son siempre **levógiros** (helicidad negativa: el espín apunta en sentido contrario al movimiento) y los antineutrinos, **dextrógiros**. Lo confirmó el experimento de Goldhaber en 1958. Esta asimetría no es un detalle técnico: es la huella de que la interacción débil viola la paridad, y está en el corazón de cómo el neutrino encaja en el Modelo Estándar (ver [[Neutrino en el Modelo Estándar]]).

### Abundancia: están por todas partes

Lo escurridizo no significa raro. Todo lo contrario: el neutrino es una de las partículas más abundantes del universo.

- El **fondo cósmico de neutrinos**, reliquia del Big Bang, llena el espacio con unos 336 neutrinos por cm³ a una temperatura de 1.95 K.
- El **Sol** baña la Tierra con un flujo de unos $6\times10^{10}$ neutrinos por cm² y segundo. Mientras lees esto, billones de ellos te atraviesan sin dejar rastro.

## Un poco de historia

El neutrino nació como una idea desesperada. En 1930, Wolfgang Pauli lo postuló para salvar la conservación de la energía en la desintegración beta, donde el espectro del electrón emitido parecía no cuadrar. Lo llamó "remedio desesperado" porque proponía una partícula que, sospechaba, jamás podría detectarse. Enrico Fermi le dio el nombre —*neutrino*, "pequeño neutro" en italiano— y construyó la teoría de la interacción débil a su alrededor. La detección directa tardó 26 años: llegó en 1956, con el experimento de Frederick Reines y Clyde Cowan junto a un reactor nuclear.

## Cuestiones abiertas

- **¿Dirac o Majorana?** No se sabe si el neutrino es su propia antipartícula (Majorana) o no (Dirac). La respuesta cambiaría la física más allá del Modelo Estándar y se busca en la desintegración doble beta sin neutrinos.
- **Escala y jerarquía de masas.** Conocemos las diferencias de masa, no los valores absolutos ni el orden (jerarquía normal o invertida).

## Por qué importa para la tesis

Las dos propiedades que parecen un estorbo —no tiene carga y casi no interactúa— son precisamente las que lo convierten en el mensajero ideal. Sin carga, los campos magnéticos galácticos no lo desvían: llega apuntando a su fuente. Y como casi no interactúa, escapa de los núcleos densos de los AGN, opacos incluso para los rayos gamma. Ese argumento se desarrolla en [[Importancia del Neutrino como Mensajero Cósmico]].

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- Su papel en la física de partículas: [[Neutrino en el Modelo Estándar]]
- El cambio de sabor en el camino: [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]
- Cómo se detecta lo que casi no interactúa: [[Detección de Neutrinos]]

## Fuente

- KATRIN Collaboration (2024), cota de masa $m_\nu < 0.45$ eV — [arXiv:2406.13516](https://arxiv.org/abs/2406.13516)
- NuFIT-6.0 (2024), parámetros de oscilación — [arXiv:2410.05380](https://arxiv.org/html/2410.05380v1)
- Conversación de desarrollo del marco teórico, 2026-06-16
