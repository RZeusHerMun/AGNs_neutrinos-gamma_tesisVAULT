### Fase 2: Análisis de Coincidencias

**Criterios espaciales:**
- Distancia angular < θ_max (típicamente 0.5° - 2°, dependiendo de la PSF)
- Para IceCube tracks: usar error de reconstrucción reportado
- Para cascades: círculo de búsqueda más amplio

**Criterios temporales:**
- Ventana de coincidencia: ±Δt días (probar con Δt = 0.1, 1, 7, 14 días)
- Considerar variabilidad típica de AGNs (días a semanas)

**Análisis estadístico:**
- Calcular coincidencias observadas
- Generar distribución de fondo (scrambling de tiempos/posiciones)
- Significancia: ¿es consistente con fluctuaciones aleatorias?

### Fase 3: Clasificación y Caracterización

Por cada coincidencia:
- **Tipo de AGN**: BL Lac, FSRQ, radio galaxy
- **Energía del neutrino** (si disponible)
- **Flujo/significancia gamma en HAWC**
- **Separación angular**
- **Diferencia temporal**
- **Estado de actividad** (¿flare o emisión basal?)

### Fase 4: Integración con Fermi-LAT

- Verificar si hay detección en Fermi durante la ventana temporal
- Analizar comportamiento espectral (¿hay endurecimiento?)
- Construir curvas de luz multi-longitud de onda

Fernando usó la muestra del survey de 2021 *Third Catalog of HArd Fermi-LAT Sources (3FHL)*
- Cubre de 10 GeV a 2 Tev
- Observaciones de 4/ago/2008 al 2/ago/2015 (tiene 1556 fuentes; 79% identificadas)
	- Criterios:
		- Fuentes asociadas o identificadas con AGNs conocidos
		- redshift z<=0.3
		- fuentes observadas dentro de los 40 grados desde el zenith del hawc
		- objetos localizados a menos de 5 grados de fuentes detectadas en el *FOURTH hawc CATALOG (4HWC)*
- Da un total de 135 fuentes.