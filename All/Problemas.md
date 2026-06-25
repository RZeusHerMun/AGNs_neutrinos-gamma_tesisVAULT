# check rapido
###### 1.  que *error angular* usamos? 
**IC: error_ang=max(RA_ERR_PLUS, RA_ERR_MINUS, DEC_ERR_PLUS, DEC_ERR_MINUS)**
	- Supuestamente el icecat lo que nos da son en realidad rectángulos de error que yo los hago elipses. *pero, eso está bien?*
	- Buscamos un error eliptico con SkyCord (PENDIENTE)
###### 2.  tengo q librar el plano galáctivo en las coincidencias con IC?
![[Pasted image 20260218191228.png]]Tengo objetos dentro de esa zona, pero los filtro para q no confunda con fuentes locales, **ESTOY EN LO CORRECTO?** o estoy desperdiciando señales?

###### 3. por que uso solo AGN sin redshift asociado. 
- El FHIFT tiene mejoras en los bines de muy baja energía, entonces, mejora cuando los AGN tienen muy poco redshift. Esto ayudaría a mostrar los AGN que necesitan más investigacion. **no?** FUENTE: ![[A 9-Year TeV Gamma-Ray Survey of Active Galaxies by HAWC - FerJosue Ureña#^a2b573]]
- catalogo de fenando es hwc3 o hwc4?
	- Usa el 4HWC, HAWC fhit Pass 5 data set which comprises nine years of HAWC121 data acquired from 2014 November 26 to 2024 January 1 (3339 días. 9años, 1 mes y 22 días).
	- Del HAWC se ocupa el método FHIT (divide los eventos en 11 bins basados en la fraccion de PMTs activados durante cada evento, ahora con acceso a los bines de baja energía (B1 yB0)) 
	- Ocupa el 3FHL con nueve años de el HAWC (2014-2024)
		-  10 GeV and 2 TeV
		  
	- **Criterios** de uso de la muestra: 
		- Del Third Catalog of Hard Fermi-LAT Sources (3FHL) de 4/Ago/2008 al 2/Ago/2015. 1556 fuentes de las cuales 79% son identificadas o asociadas a objetos extragalácticos.
			- Fuentes asociadas (coincidencia posicional) o identificadas (confirmadas por variabilidad) cn AGNs.
			- Fuentes localizadas a redshift $z \leq 0.3$, (límite establecido por la atenuación del EBL). Tambien excluye fuentes sin redshift.
			- Fuentes observadas dentro de los 40° desde el cenit del HAWC.
	- Se buscaron las fuentes que estuvieran a menos de 5° (cerca de dos veces la resolucion angular del HAWC en sus bines de energia mas bajos). Solo se quitaron las fuentes que estuvieran a menos de 2.5°![[Pasted image 20260121102511.png]]- **Muestra inicial de 3FHL (con criterios z<0.3, cenit<40°):** ~138 fuentes **Exclusiones por contaminación:** 3 fuentes 
		- 3FHL J1105.8+3944 (5BZG J1105+3946) → muy cerca de Mrk 421
		- 3FHL J1100.3+4020 (RX J1100.3+4019) → muy cerca de Mrk 421
		- 3FHL J1652.7+4024 (SDSS J1652+4024) → muy cerca de Mrk 501
		- **LA MUESTRA FINAL CONTIENE SOLO 135 AGNs.** o 136 si agrego el *TXS*



---------
------
---
/////////////////////////////////////////////////////////////////////////////////////////////////////////
____
# 26 DE MARZO 
%% PONER LA SOLUCION O RESPUESTA EN COMENTARIOS %% 
%% AGREGAR LOS TXS Y LA M87 COMO LAS %%
#### catalogo agns con zooms individuales. 
- [ ] Sirve de algo tener la banda optica? (solo ROJA)
		- SDSS Y DSS, solo en banda roja (filtro 'r'). Proyeccion TAN (Gnomónica) para no distorsionar con filtro cmap='gray_r' - *falló la compu al recoger los 3 colores y juntarlos*
	- [ ] Pero no se ven las galaxias, entonces debo detallar los objetos que aparecen en los mapas optics? %% SI, IR NMBRANDO LOS VECINDARIOS PARA ELIMINAR DETALLES %%
		- [ ] %% COMPROBAR LAS COORDENADAS CON PUNTOS VERDADEROS %%.
		- [ ] %% SI NO ESTAN EN EL SLOAN, EN LUGAR DE DSS, MEJOR TUMAS %%.
-  Objetos dentro del margen de error:
	- SDSS, MKN 421 y b2.2
		- [ ] Van a necesitar evidencia para esclarecer un caso individual?
		- [ ] Agregar investigacion por flares o bandas elesctromagneticas?
			- %% NECESARIO PARA INVESTIGAR MAS PROFUNDA EN LOS ESPECIFICOS, VERLOS %%
		- [x] TXS no hubo exceso poblacional, fue temporal. ANALISIS TEMPORAL?
- Objetos lejanos:
	- J1449.5+2745 ($z = 0.227$) y J0211.2+1051 ($z = 0.200$);
		- [ ] EBL atenua los rayos gamma; entonces se deben analizar otras bandas de energía? (ejemplo ovro,caz, HAWC?, etc) %% DESCRIPCION MEDIANA%%
		- [x]  J0211.2+>: Este objeto no tenía los errores de IceCube capturados, y el código activó el parche de seguridad asignándole un error default de . Matemáticamente, a un  de confianza, IceCube dice que el neutrino no vino de ese AGN.
- [ ] Description de los reportes del [Fermi-LAT follow-up of IceCube realtime alerts](https://multimessenger.ua.edu/fermi/)
	- [ ] Tienen varios mapas en muchas bandas, pero solo del 2019 hacia acá. Que mapas agregar o hacer parecidos para su analisis?
	- [ ] %% PONER LAS EXTRAS QUE NO ESTOY CONSIDERANDO EN MI MUESTRA%%
- [ ] Difuminar el área de IceCube?
	- [ ] Agregar otras galaxias que estén dentro del radio de error del icecube?
	- [ ] %% SOMBREADO EN LAS AREAS DENTRO DE EL ERROR DEL ICECUBE%%
##### HAWC: Requiere analisis de cada uno por si llegó a ser un flare?
- Al ser 1523 dias el flujo diluido en promedio pudo haber discriminado un flare?
- La falta de señal en gamma en la produccion de neutrinos podría deberse a que sean aceleradores ocultos. DEBO PROPONERLO COMO UNA CAUSA?
	- [Hidden Cosmic-Ray Accelerators as an Origin of TeV-PeV Cosmic Neutrinos](https://arxiv.org/pdf/1509.00805)
	- Siento que esto se va hacia analizar desde donde se producen los neutrinos y particulas, investigacion a fondo sobre la corona y lo compacto que son.
- [ ] Falta All-Sky Map en proyección Mollweide con AGNs. En fondo optico o en blanco(?)
	      
---

El scrip **SCRAMBLIN-FEBRERO**, tenía ciertos *problemas*:
- MC isotrópico (distribuyendo fuentes uniformemente en toda la esfera), lo cual produce excesos a radios grandes (2°-3°). 
	- Disperso fuentes fuera de la banda de HAWC, compardo reales en la banda del HAWC contra un fondo q diluye efectividad, entonces refleja el sesgo geométrico compartido e infla mi p-value global (0.0171)
	- [[Modelo nulo de banda HAWC]]
- Al realizar las correciones por p-trials invalidaba la [teoria](https://staff.fnwi.uva.nl/c.weniger/data/stats1/slides3.pdf) al usar poca población y solo 3 enfoques (0.5,1,1.5)
#### **MEJORAS aplicadas**:
- Mas radios de búsqueda para relacionar ese incremento en radios más grandes, y como me nubla los resultados.
- Dos modelos nulos:
		- Fondo isotrópico (identico en todas direcciones)
		- Analisis de la banda de declinación del HAWC.
			- Dec fija, y scrambles en RA
			- Comparacion da p-values >0.47 (no significativos)
				- *CONCLUIMOS* el exceso contra la isotropía se da pq ICECUBE y HAWC comparten la banda de declinación, no hay correlación física.  
				- %% TENER LO SUFICIENTE  %%
- Test elíptico con contornos al 90% CL
	- Se calibró correctamente: 32 coincidencias reales vs. 34.9 esperadas → p = 0.75, sin exceso.
	- - [[Correccion de Bonferroni o Empirica]]
- [[Prueba KS de distancias angulares]]:
	- Compara la distribución de distancias mínimas AGN→neutrino contra la distribución isotrópica. D = 0.30, p ≈ 10⁻¹¹. Los AGNs tienden a estar más cerca de neutrinos que lo esperado por azar.
	- %% ANALIZAR ESTOS Y AGREGARLOS %%
- [[Tests ponderados]]: 
	- Ponderan las coincidencias por signalness (probabilidad astrofísica del neutrino) y por energía. Resultados: 1.43σ y 1.21σ — indicios débiles, no significativos.
- Corrección look-elsewhere más formal:
	- p_global = 0.0171 con 3 trials. 
	- p_global = 0.0018 con corrección Bonferroni p = 0.0035, pero con 5 radios.
- [[Correlación TS vs neutrinos]]: 
	- El Spearman ρ = −0.83 es nuevo. Muestra que AGNs con mayor TS en HAWC no tienen más neutrinos cercanos — contraintuitivo y importante de discutir.
- Límites superiores:
	- Si no hay señal, COTA SUPERIOR: máximo ~8 coincidencias elípticas o ~5.9% de la muestra podría tener correlación real al 95% CL.
- %% TENER LOS ANALISIS QUE MUESTRAN EL MISMO RESULTADO PERO %%
### **MEJORAS PROPUESTAS**
- Debo profundizar en el desarrrollo de la [[geometría de detecciones]] de las detecciones?
- 
### Conclusiones
- Pq hacerlo si era esperado q no hubiera relación? confirma que las clasificaciones actuales de HAWC se sostienen frente a los datos de IceCube.