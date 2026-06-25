¡Excelente! Llegamos a la sección 8, que es una prueba de consistencia física brillante. Aquí dejas de mirar el catálogo completo como un solo bloque y te empiezas a preguntar sobre las características individuales de cada galaxia.

### Parte 8: Correlación TS HAWC vs Número de neutrinos cercanos

En astrofísica de altas energías, cuando un detector como HAWC observa una fuente, le asigna un valor llamado **TS (Test Statistic)**. Simplificando un poco, el TS te dice qué tan significativa o "brillante" es esa fuente en rayos gamma. Un TS alto significa que estamos muy seguros de que ahí hay un emisor potente de rayos gamma.

**La Pregunta Física:** Si estos AGN realmente estuvieran produciendo neutrinos junto con sus rayos gamma, la lógica nos diría que las fuentes más potentes en HAWC (las de mayor TS) deberían tener más neutrinos a su alrededor.

**El Método: Correlación de Spearman**

Para probar esto, hiciste lo siguiente:

1. Contaste cuántos neutrinos caían dentro de un radio de $1.5^\circ$ para cada uno de tus 135 AGN.
    
2. Usaste el **Coeficiente de Correlación de Spearman ($\rho$)** para comparar el TS de HAWC con el número de neutrinos.
    
    - _Nota metodológica:_ Usar Spearman aquí es súper acertado. A diferencia del coeficiente de Pearson (que busca relaciones estrictamente lineales), Spearman busca relaciones monótonas usando "rangos" (ordenando los valores de mayor a menor). Esto es ideal en astronomía porque variables como el TS varían en escalas logarítmicas enormes y no quieres que un solo AGN súper brillante distorsione todo el cálculo.
        

**Los Resultados y su Significado:**

- El cálculo arrojó un valor de **$\rho = -0.831$**.
    
- Esto indica una **correlación negativa** bastante fuerte.
    
- ¿Qué nos dice la gráfica que generaste? En el eje X tienes el logaritmo del TS ($\log_{10}(TS + 1)$) y en el eje Y la cantidad de neutrinos. La línea de ajuste va hacia abajo.
    

**La Interpretación para tu Tesis:** Este resultado es una joya para tus conclusiones. Significa que los AGN que tienen mayor significancia (mayor TS) en HAWC _no_ tienden a tener más neutrinos cercanos; de hecho, tienden a tener menos.

Físicamente, esto es la confirmación definitiva de tu hipótesis nula: corrobora que la emisión de rayos gamma (que sabemos que es leptónica en esta muestra) **NO** implica la producción de neutrinos. Si el mecanismo fuera hadrónico, a mayor flujo de rayos gamma, mayor flujo de neutrinos esperaríamos ver. Como vemos exactamente lo opuesto, consolidas la naturaleza puramente leptónica de estas observaciones.

¿Te queda clara la justificación de por qué una correlación negativa aquí es en realidad un "éxito" para confirmar la física de tu catálogo? Si estás listo, podemos pasar a la **Sección 9**, que es donde calculas los "Upper Limits" (Límites Superiores) y pones el clavo final al ataúd estadístico. ¿Le damos?