La **distancia angular** en una esfera es la medida del ángulo entre dos puntos vistos desde el centro de esa esfera. Geométricamente, representa el camino más corto entre esos dos puntos a lo largo de la superficie de la esfera, lo que se conoce como un arco de círculo máximo (great-circle distance).

Cuando escuchas el término **"Vincenty, esfera"**, se refiere a una fórmula matemática muy específica (y computacionalmente robusta) para calcular esa distancia angular.

Thaddeus Vincenty es famoso por desarrollar algoritmos de alta precisión para medir distancias sobre un elipsoide (que representa la forma real de la Tierra). Sin embargo, su fórmula también tiene un caso especial aplicado a una **esfera perfecta**.

### ¿Por qué usar la fórmula de Vincenty en una esfera?

En la programación y el análisis de datos, existen tres fórmulas principales para calcular la distancia angular:

1. **Ley de los cosenos esféricos:** Es la más simple, pero sufre de graves errores de redondeo computacional cuando los puntos están muy juntos.
    
2. **Fórmula del Haversine:** Es la más popular y soluciona el problema de las distancias cortas, pero pierde precisión cuando los puntos están en lados exactamente opuestos de la esfera (puntos antipodales).
    
3. **Fórmula de Vincenty (caso esférico):** Utiliza la función arcotangente de dos parámetros (`atan2` en muchos lenguajes de programación), lo que la hace matemáticamente precisa y estable para **todas** las distancias, ya sean microscópicas o antípodales.
    

Demostraci'on:

Si tienes dos puntos en una esfera con coordenadas $(\lambda_1, \phi_1)$ y $(\lambda_2, \phi_2)$ —que representan longitud y latitud, o ascensión recta y declinación— y la diferencia de longitud es $\Delta\lambda = \lambda_2 - \lambda_1$, la distancia angular central $\Delta\sigma$ (en radianes) se calcula así:

$$\Delta\sigma = \arctan\left(\frac{\sqrt{(\cos\phi_2 \sin\Delta\lambda)^2 + (\cos\phi_1 \sin\phi_2 - \sin\phi_1 \cos\phi_2 \cos\Delta\lambda)^2}}{\sin\phi_1 \sin\phi_2 + \cos\phi_1 \cos\phi_2 \cos\Delta\lambda}\right)$$

Para implementarla en código de manera segura y manejar correctamente todos los cuadrantes, se utiliza la función $\text{arctan2}(y, x)$ donde el numerador de la fracción es $y$ y el denominador es $x$.

Las correlaciones espaciales que se buscan cruzando datos de catálogos de neutrinos como IceCat-1 con las posiciones de AGNs detectados por observatorios como HAWC o Fermi-LAT, un error de redondeo en tu script de Python podría hacerte perder una coincidencia multimensajero o generar un falso positivo. La fórmula de Vincenty garantiza que la separación angular que calculas entre la fuente de rayos gamma y el evento del neutrino es computacionalmente exacta en todos los escenarios.

¿Te gustaría que te comparta una función vectorizada en Python (usando NumPy) que aplique esta fórmula para que puedas procesar listas largas de coordenadas rápidamente?