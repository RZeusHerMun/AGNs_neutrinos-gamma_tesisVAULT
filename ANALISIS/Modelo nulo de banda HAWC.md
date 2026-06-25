## El problema que queremos resolver

La pregunta fundamental es: "¿Los AGNs de HAWC están más cerca de neutrinos de IceCube de lo que esperaríamos por puro azar?"

Para responder eso necesitas un modelo nulo — una simulación de cómo se verían las coincidencias si **no hubiera ninguna relación física** entre AGNs y neutrinos. Comparas tus datos reales contra ese modelo nulo, y si hay un exceso significativo, tienes evidencia de correlación.

El problema es que "azar" no significa lo mismo dependiendo de qué modelo nulo uses.

## Modelo isotrópico: qué hace y por qué falla

En tu análisis previo, el modelo nulo decía: "si los AGNs estuvieran distribuidos aleatoriamente por toda la esfera celeste, ¿cuántas coincidencias habría?"

Entonces en cada iteración MC generabas 135 posiciones con RA uniforme en [0°, 360°] y Dec uniforme en coseno (toda la esfera). Pero piensa en lo que pasa: muchos AGNs simulados caen en declinación −60°, −80°, en el hemisferio sur profundo... donde IceCube tiene muy pocos tracks y donde HAWC no tiene sensibilidad. Esos AGNs simulados básicamente nunca van a coincidir con un neutrino, así que arrastran la media MC hacia abajo.

Tus 135 AGNs reales, en cambio, están todos en la banda de HAWC (aproximadamente −26° a +64° en declinación), que se traslapa fuertemente con la zona donde IceCube detecta más tracks. Entonces tus AGNs reales tienen una "ventaja geométrica" sobre los simulados — no porque estén correlacionados con neutrinos, sino simplemente porque están en la misma franja del cielo.

El exceso que encontrabas (p = 0.0171) medía en parte correlación física real, pero mezclada con este sesgo de cobertura que no podías separar.

## Modelo de banda HAWC: qué hace y por qué es correcto

El modelo de banda HAWC dice algo diferente: "si los AGNs estuvieran distribuidos aleatoriamente **dentro de la misma franja de declinación donde HAWC puede detectarlos**, ¿cuántas coincidencias habría?"

En la práctica, lo que se hace en cada iteración MC es mantener la declinación de cada AGN exactamente igual (la Dec real del catálogo) y solo aleatorizar la ascensión recta uniformemente en [0°, 360°].

Esto preserva toda la estructura en declinación: la distribución de sensibilidad de HAWC, el traslape con la zona eficiente de IceCube, los efectos de exposición. Lo único que destruyes es la correlación en RA — es decir, la posición específica en el cielo donde está cada AGN.

Imagínalo así: tomas tu mapa del cielo con los 135 AGNs y "giras" cada uno aleatoriamente en RA como si estuvieran en anillos de declinación fija. Si un AGN real está en Dec = +20°, su versión simulada también está en Dec = +20° pero en una RA al azar. Esto garantiza que el fondo simulado "ve" los mismos neutrinos disponibles en esa banda de declinación.

## Por qué la diferencia es tan dramática

Déjame ponerte un ejemplo concreto para que quede claro. Supón que a Dec = +20° hay una concentración de neutrinos de IceCube (que la hay, porque IceCube tiene buena eficiencia ahí). Tu catálogo tiene, digamos, 15 AGNs en esa banda de declinación.

Con el **modelo isotrópico**, de tus 135 AGNs simulados, quizá solo 8–10 caen cerca de Dec = +20° (el resto se va al hemisferio sur, a los polos, etc.). Entonces el modelo predice pocas coincidencias en esa banda → tus 15 AGNs reales parecen un exceso.

Con el **modelo de banda HAWC**, esos mismos 15 AGNs simulados siguen en Dec ≈ +20°, solo cambian de RA. Ahora el modelo predice correctamente cuántas coincidencias esperas por azar dado que tienes 15 AGNs y X neutrinos en esa franja → y resulta que el número real no es especial.

Revisando tus resultados concretos, esto queda clarísimo. A 3°, por ejemplo:

- **Isotrópico:** media MC = 23.6, real = 39, p = 0.0007 (3.59σ — parece muy significativo)
- **Banda HAWC:** media MC = 38.2, real = 39, p = 0.47 (no significativo en absoluto)

La media del modelo de banda es casi el doble que la del isotrópico. Esas ~15 coincidencias "extra" que parecían señal eran simplemente el efecto de que HAWC e IceCube comparten la misma ventana de declinación.

## ¿Cuál es el modelo nulo "correcto"?

Depende de la pregunta que quieras responder:

Si preguntas "¿los AGNs de HAWC coinciden con neutrinos más de lo esperado para fuentes distribuidas por todo el cielo?", la respuesta es sí, y el isotrópico es el modelo adecuado. Pero esta pregunta es poco interesante porque la respuesta trivial es "claro, porque HAWC e IceCube ven la misma parte del cielo."

Si preguntas "dado que los AGNs de HAWC están donde están en declinación, ¿sus posiciones específicas en RA coinciden con neutrinos más de lo esperado?", esa es la pregunta físicamente relevante. Y el modelo de banda HAWC es el adecuado para responderla. La respuesta, con los datos actuales, es que no.

Para tu tesis, lo más robusto es presentar ambos modelos y explicar exactamente esta distinción. Muestra que el isotrópico da un exceso aparente, explica por qué está sesgado, y muestra que el modelo de banda (más conservador y correcto) no confirma el exceso. Esto demuestra rigor metodológico, que es exactamente lo que un comité de tesis quiere ver.
![[ancho de banda hawc.png]]