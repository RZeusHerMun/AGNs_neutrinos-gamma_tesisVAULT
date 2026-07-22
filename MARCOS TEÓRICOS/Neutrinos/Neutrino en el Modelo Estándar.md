---
fecha: 2026-06-16
tipo: nota-atomica
ia_usada: Claude (Opus 4.8)
forma_nota: marco-teorico
nodos_principales:
  - "[[Neutrinos - Marco Teórico]]"
notas_relacionadas:
  - "[[Neutrino - Descripción y Propiedades]]"
  - "[[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]"
  - "[[desintegracion_muon_icecube]]"
tags:
  - tema/neutrinos
  - tema/modelo-estandar
  - tema/fisica-de-particulas
  - proyecto/tesis-multimensajera
  - area/academia
---

# El Neutrino en el Modelo Estándar

> En el Modelo Estándar el neutrino es el miembro neutro del doblete leptónico, acoplado solo a los bosones $W$ y $Z$ de la fuerza débil, y siempre por su componente zurda. El Modelo lo construyó sin masa; que tenga masa es la primera grieta confirmada de la teoría.

## Dónde encaja

El Modelo Estándar organiza la materia en tres generaciones de fermiones y describe sus interacciones con el grupo de simetría gauge

$$SU(3)_C \times SU(2)_L \times U(1)_Y.$$

El neutrino no siente $SU(3)_C$ (no tiene color, así que ignora la fuerza fuerte) ni se acopla al fotón (no tiene carga). Su sitio está en el sector electrodébil, $SU(2)_L \times U(1)_Y$. Ahí, los leptones zurdos de cada generación se agrupan en **dobletes de isospín débil**:

$$L_\alpha = \begin{pmatrix} \nu_\alpha \\ \ell_\alpha \end{pmatrix}_L, \qquad \alpha = e,\ \mu,\ \tau$$

El leptón cargado tiene además una componente diestra, $\ell_{\alpha R}$, que vive sola como singlete. El neutrino no: en la versión mínima del Modelo Estándar **no existe un $\nu_R$**. El neutrino entra en la teoría únicamente por su mano izquierda. Esta asimetría, que parece arbitraria, es la que termina explicando por qué el Modelo lo deja sin masa.

## Cómo interactúa: corriente cargada y corriente neutra

Toda la física del neutrino en el Modelo Estándar pasa por dos vértices de la fuerza débil.

**Corriente cargada (CC), mediada por el $W^\pm$.** Convierte un neutrino en su leptón cargado y viceversa. Es el vértice que produce y detecta neutrinos:

$$\mathcal{L}_{CC} = -\frac{g}{\sqrt{2}} \sum_{\alpha} \bar{\nu}_{\alpha L}\,\gamma^\mu\,\ell_{\alpha L}\,W^+_\mu \;+\; \text{h.c.}$$

**Corriente neutra (NC), mediada por el $Z^0$.** Deja al neutrino como neutrino, pero le transfiere energía y momento:

$$\mathcal{L}_{NC} = -\frac{g}{2\cos\theta_W} \sum_{\alpha} \bar{\nu}_{\alpha L}\,\gamma^\mu\,\nu_{\alpha L}\,Z_\mu$$

Estos dos términos son el motor de [[desintegracion_muon_icecube]]: la desintegración del muón es una cascada de vértices CC, y la detección en IceCube es un vértice CC leído al revés ($\nu_\mu + N \to \mu + X$).

### La estructura V−A: solo cuenta la quiralidad izquierda

El detalle decisivo está en el subíndice $L$ de las fórmulas. La corriente débil tiene forma **V−A** (vectorial menos axial), lo que equivale a un proyector que se queda solo con la parte zurda del campo:

$$J^\mu \propto \bar{\psi}\,\gamma^\mu \frac{1-\gamma^5}{2}\,\psi.$$

Por eso la fuerza débil viola la paridad de forma máxima, y por eso solo interactúan neutrinos levógiros y antineutrinos dextrógiros (ver la helicidad en [[Neutrino - Descripción y Propiedades]]). No es una preferencia estadística: en el Modelo Estándar la componente diestra del neutrino sencillamente no figura.

## Números leptónicos

El Modelo Estándar asigna a cada generación un número leptónico ($L_e$, $L_\mu$, $L_\tau$) que se conserva en cada vértice. Esa contabilidad es la que obliga a que en la desintegración del muón aparezcan emparejados un $\nu_\mu$ por un lado y un $e^- + \bar\nu_e$ por otro. La oscilación de sabor viola esos números individuales —un $\nu_\mu$ puede llegar como $\nu_\tau$—, pero el número leptónico **total** sigue conservándose mientras el neutrino sea de tipo Dirac.

## El problema de la masa

Aquí está la grieta. Para dar masa a un fermión de Dirac hace falta un término que acople sus dos quiralidades:

$$\mathcal{L}_{\text{masa}} = -m\,\bar{\psi}\psi = -m\,(\bar{\psi}_L \psi_R + \bar{\psi}_R \psi_L).$$

El neutrino no puede tener un término así en el Modelo Estándar mínimo, por una razón simple: **no hay $\nu_R$** con qué emparejar a $\nu_L$. La alternativa, un término de masa de Majorana del tipo $\tfrac{1}{2}m\,\overline{\nu_L^c}\,\nu_L$, está prohibida a nivel renormalizable porque no respeta la simetría gauge (lleva isospín e hipercarga netos). Resultado: el Modelo Estándar mínimo predice $m_\nu = 0$, exactamente.

La naturaleza opina distinto. Las oscilaciones demuestran que al menos dos neutrinos tienen masa. Esa contradicción convierte al neutrino en la **primera evidencia de laboratorio de física más allá del Modelo Estándar**, y obliga a extenderlo: añadir neutrinos diestros (masa de Dirac con acoplos de Yukawa minúsculos), introducir masas de Majorana, o el popular mecanismo *see-saw*, que explica la pequeñez de la masa con estados pesados a escalas de gran unificación. El abanico de soluciones y sus consecuencias (jerarquía, fase CP, leptogénesis) está en [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]].

## Tres y solo tres (sabores ligeros)

Un dato experimental cierra el cuadro. La anchura de desintegración del bosón $Z^0$ medida en el colisionador LEP depende de cuántos tipos de neutrino ligero existan para que el $Z$ decaiga en ellos. El resultado,

$$N_\nu = 2.984 \pm 0.008,$$

fija en tres el número de sabores de neutrino ligeros que se acoplan a la fuerza débil. Cualquier cuarto neutrino tendría que ser "estéril" (sin interacción débil) o muy pesado.

## Conexiones

- Parte de: [[Neutrinos - Marco Teórico]]
- Propiedades de la partícula: [[Neutrino - Descripción y Propiedades]]
- Qué implica la masa no nula: [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp]]
- Los vértices CC/NC en acción: [[desintegracion_muon_icecube]]

## Fuente

- Estructura electrodébil estándar (Glashow–Weinberg–Salam) y datos del LEP sobre $N_\nu$.
- NuFIT-6.0 (2024) para los parámetros de oscilación — [arXiv:2410.05380](https://arxiv.org/html/2410.05380v1)
- Conversación de desarrollo del marco teórico, 2026-06-16
