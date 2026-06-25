# AGNs y Blazares Multimensajeros (HAWC + IceCube)
____
## 1. Introducción y Marco Teórico

### 1.1. Núcleo activo de galaxia (AGN)
Las **AGN** son regiones extremadamente luminosas en los centros de ciertas galaxias, impulsadas por la acreción de un **agujero negro supermasivo (SMBH)**. Históricamente, los objetos Seyfert fueron identificados en 1943, mientras que los cuásares aparecieron como los núcleos más potentes y compactos alrededor de 1963. La emisión radia desde radio hasta rayos gamma mediante acreción, chorros relativistas, y discos de acreción.

### 1.2. Blazares: BL Lac y FSRQ
- **Blazares**: AGNs con un jet dirigido casi directamente a la Tierra, lo que provoca un **boosting relativista** que intensifica la luminosidad y acelera la variabilidad.
	- **BL Lac**: Espectro pobre en líneas de emisión, generalmente con picos de sincrotrón en energías más altas.
	- **FSRQ (Flat-Spectrum Radio Quasar)**: Espectro con líneas prominentes, picos de sincrotrón más bajos, y luminosidad mayor.

### 1.3. Astrofísica Multimensajero
La combinación **gamma-ray (emisión EM)** y **neutrinos** abrevent into el proceso de aceleración de rayos cósmicos. Se cree que la interacción foto-hadónica produce piones que decaen en neutrinos y rayos gamma. HAWC:
	 - gammas TeV (0.1–100 TeV) 
	 - amplio campo de visión 
	 - alta disponibilidad; 
IceCube:
	- detecta neutrinos de TeV–PeV con resolución celeste variable (~0.5° track, ~10° cascada).

## HAWC e IceCube

- **HAWC** (High Altitude Water Cherenkov): monitorea el cielo norte en TeV gamma, generando catálogos como 3HWC con posiciones y espectros de ~65 fuentes.

- **IceCube**: emite alertas “Gold” (~>50 % probabilidad astrofísica) y “Bronze” (~30–50 %) tras captar eventos de alta energía, mediante GCN/AMON 

- Un caso emblemático: **TXS 0506+056**, blazar BL Lac con *z* ≈ 0.336, identificado tras la alerta IC-170922A.

## 3. Observables Iniciales

- **Coordenadas célestes**: RA (°), Dec (°).
- **Redshift (z)**: para datos cosmológicos y absorción EBL.
- **Clasificación**: BL Lac, FSRQ, etc.
- **Flujo gamma/TeV**: medido por HAWC.
- **Absorción por EBL**: importante a *z* ≳ 0.2.

## 4. Catálogo Base (≈ 15 fuentes)

| Fuente             | Catalogo         | RA (°)  | Dec (°)  | z      | Tipo     | Notas                                      |
|-------------------|------------------|---------|----------|--------|----------|--------------------------------------------|
| Mrk 421           | 3HWC J1104+381   | 166.10  | +38.21   | 0.031  | BL Lac   | Extremadamente brillante en TeV            |
| Mrk 501           | 3HWC J1653+397   | 253.47  | +39.76   | 0.034  | BL Lac   | Fuente persistente de TeV                   |
| TXS 0506+056      | IceCube Alert    | 77.36   | +5.69    | 0.3365 | BL Lac   | Confirmado con neutrino (IC-170922A)       :contentReference[oaicite:4]{index=4} |
| NGC 1068          | IceCube Stack    | ~40.67  | −00.01   | 0.0038 | Seyfert II | Identificado como fuente de neutrinos :contentReference[oaicite:5]{index=5} |
| 3HWC J0534+220    | Crab Nebula      | 83.63   | +22.01   | —      | PWN      | Fuente calibradora, usado como referencia   |
| 3HWC J1427–605    | —                | 216.75  | –60.87   | —      | —        | —                                          |
| 3HWC J1953+294    | —                | 298.25  | +29.40   | —      | —        | —                                          |
| 3HWC J1930+188    | —                | 292.50  | +18.80   | —      | —        | —                                          |
| 3HWC J1852+013    | —                | 283.00  | +1.30    | —      | —        | —                                          |
| 3HWC J1814–173    | —                | 273.50  | –17.30   | —      | —        | —                                          |
| 3HWC J1908+063    | —                | 287.00  | +6.30    | —      | —        | —                                          |
| 3HWC J2019+368    | —                | 304.75  | +36.80   | —      | —        | —                                          |
| 3HWC J2031+415    | —                | 307.75  | +41.50   | —      | —        | —                                          |
| 3HWC J2016+352    | —                | 304.00  | +35.20   | —      | —        | —                                          |

> **Nota**: Las últimas fuentes son representativas del catálogo 3HWC (~65 fuentes) detección general en TeV. Faltaría agregar los demás datos en cuento se tengan la base de datos completa: RA/Dec precisos y asociar redshift/clasificación según Fermi-LAT 3LAC/4LAC.

## 5. Gráficas 

1. **Mapa celeste RA–Dec**: posicionar estas ~15 fuentes; resaltar con símbolos distintos los AGN/neutrino vs. otras fuentes.
2. **Histograma de redshifts**: mostrar distribución de *z* (solo para las fuentes con redshift conocido, ej. Mrk 421, Mrk 501, TXS 0506+056, NGC 1068).
3. **Gráfica RA vs. Dec**: visualización de densidad y posibles coincidencias espaciales.

## 6. Aplicación *actual* al Proyecto

1. agregar la informacion de los datos que se usaron el principio y los scripts (HWC3)
2. sacar datos de el icecat1
3. acotar los graficos de el ultimo paper


- Base sólida para mañana: tabla + mapa de posiciones.
- Luego: agregar flujos TeV de HAWC, realizar análisis de stacking o correlación estadística.
- Bloque II puede incluir diagramas de flujo, absorción EBL, modelo de emisión neutrino–gamma, etc.

---
### 7. Detalles para agregar

-  agregar histograma sobre las 18 galaxias que tienen, su respectivo redshift.  por que quedan tan pocas de fermi a hawc. (factor ubicacion en el espacio)
- agregarle los labels de las nuevas graficas a las 
- checar cuales son los que no son agn que son starbust.
- diferenciar los detectores de fermi y hawc, cuales son y por q sucede.
- quitar unos 10 grados del centro de la galaxia, detallar descarte

- descripcion historica, desarrollo de nuetrinos.
	- Origenes:- 
		- Reacciones nucleares en el Sol
		- Supernovas
		- Colisiones de estrellas de neutrones
		- Núcleos galácticos activos (como NGC 1068)
    
- Rayos cósmicos interactuando con la atmósfera
- ngc 1068, el txs y como se van a ir asociando a los valores que tenemos.
- difereniacion de probabilidad del gold y bronze en el amon.
  - emision de energia; radiacion, compton, no térmica, etc.
  - 