---
tags: [tesis/hub, tesis/escritura]
---
# 🔬 Tesis — Hub de Escritura

**Título:** Correlación de Emisiones de Alta Energía en Núcleos Galácticos Activos: Un Enfoque Multimensajero  
**Asesor:** Dr. Daniel Rosa González — INAOE  
**Colaboración:** HAWC — IceCube

---
## Índice de Capítulos

| Cap. | Sección | Estado | Nota |
|------|---------|--------|------|
| I | [[DRAFTS - I. Introducción\|Introducción]] | 🟡 Borrador | Falta especificar modelos, dar refs sólidas |
| II.i | [[DRAFTS - II.i Fenomenología de los AGNs\|Fenomenología de AGNs]] | 🟡 Borrador | Mover clasificación al inicio (asesor) |
| II.ii | [[DRAFTS - II.ii Jets Relativistas\|Jets Relativistas]] | 🔴 Esqueleto | ¿Sección propia o integrar? |
| II.iii | [[DRAFTS - II.iii Radiación y Mecanismos de Emisión\|Radiación y Mecanismos]] | 🟡 Borrador | Correcciones leptónico/hadrónico hechas |
| III.i | [[DRAFTS - III.i HAWC\|HAWC]] | 🟡 Borrador | Justificar B0/B1 pendiente |
| III.ii | [[DRAFTS - III.ii Fermi-LAT\|Fermi-LAT]] | 🟡 Borrador | Definir 3FHL vs 4FHL |
| III.iii | [[DRAFTS - III.iii IceCube\|IceCube]] | 🟡 Borrador | Buen contenido |
| IV | [[DRAFTS - IV. Análisis\|Análisis y Resultados]] | 🟠 En proceso | Resultados completos, falta redacción |
| V | [[DRAFTS - V. Catálogo de Coincidencias\|Catálogo Multimensajero]] | 🟡 Datos listos | Falta presentación |
| VI | [[DRAFTS - VI. Discusión y Conclusiones\|Discusión y Conclusiones]] | 🔴 Esqueleto | Se escribe al final |

---

## Panel de Control

### ✏️ Comentarios del Asesor
→ [[TESIS - DRAFTS/Comentarios del Asesor]] — 5 resueltos, 6 pendientes, 1 por aclarar

### 🔧 Metodología y Workflow
→ [[TESIS - DRAFTS/Flujo de Trabajo Multimensajero]] — Pipeline Fermi+HAWC+IceCube

### Analisis Estadístico Completo [[Analisis Estadistico Completo.pdf|pdf]]

### 📊 Resultados Estadísticos (Quick View)

| Test                 | p-value  | Conclusión                   |
| -------------------- | -------- | ---------------------------- |
| Banda HAWC 3°        | 0.4723   | No significativo             |
| KS distancias        | 0.4725   | Distribuciones idénticas     |
| Ponderado signalness | 0.5674   | Sin señal                    |
| Ponderado energía    | 0.6728   | Sin señal                    |
| Spearman TS          | ρ=−0.831 | Anti-correlación → leptónico |

> **Veredicto:** Sin evidencia de correlación AGN-neutrino. Emisión consistente con modelo leptónico.

---

## Notas de Investigación (vault original)
Creamos notas nuevas con los cambios que se realizan y por que es que se estan tomando estas decisiones. Después actualizamos la nota citada al hub de xcritura. Así las referencias pueden estar en la nota maestra de cada parte de la tesis.

### Datos y catálogos
- [[All/Data]] — Estructura de datos HAWC, Fermi, IceCube
- [[All/Criterios]] — Fases del análisis, criterios de selección
- [[DETECCIONES.canvas]] — Muestra de 135 AGNs
- [[AGN DETECCIONES - Sloan digital sky survey]] — Detecciones SDSS

### Análisis estadístico
- [[Modelo nulo de banda HAWC]] — Isotrópico vs banda HAWC
- [[geometría de detecciones]] — Fórmula de Vincenty
- [[Correccion de Bonferroni o Empirica]] — Correcciones post-trials
- [[Prueba KS de distancias angulares]] — Test KS
- [[Tests ponderados]] — Signalness y energía
- [[Correlación TS vs neutrinos]] — Spearman
	- [[Corrección de Análisis - Spearman]]
	

### Canvas y mapas mentales
- [[GENERAL reseach.canvas]] — Mapa general del proyecto
- [[TITULACION.canvas]] — Proceso de titulación

### Avances y reuniones
- [[Avances Tesis]] — Reuniones, scrambling, mejoras propuestas
- [[All/Problemas]] — Issues y correcciones
- [[Inicio Diario - Launch Jupy - versionsGIT]] — Workflow diario (conda, Jupyter)

### Papers y síntesis
- [[Síntesis de Tesis - Multifrequency study of Very High Energy emitter Active Galactic Nuclei observed with HAWC - FerJosue Umeña|Síntesis Tesis Ureña]]
- [[A 9-Year TeV Gamma-Ray Survey of Active Galaxies by HAWC - FerJosue Ureña|Survey 9 años Ureña]]
- [[SINTESIS -- Multi-messenger observations of a flaring blazar coincident with a high energy neutrino IceCube-170922A|TXS 0506+056 / IceCube-170922A]]
- [[Catalogo de Coincidencias Multimensajero.  AGN vs Neutrino|Catálogo de coincidencias]]
- [[cORRELACION cO ESPACIAL DE NEURTINOS Y FUENTES GAMMA - UNAM.pdf]]
- [[A multimessenger search for ultra high energy gamma rays in coincidence with neutrinos]]

### Estadística de soporte
- [[Estadística para Astrodatos/Estadística para Astrodatos|Curso de Estadística para Astrodatos]]
- [[Analisis Bayesiano|Guía Bayesiana (Python)]]

### Teoría complementaria
- [[Teoría de oscilaciones de neutrinos desde el punto de vista cuántico de campos simplificadp|Oscilaciones de Neutrinos]]
- [[Rayos_Cosmicos_y_Campos_Magneticos|Rayos Cósmicos]]


___

- ESCRIBIR BORRADORES DE UN PAR DE MARCOS TEÓRICOS 
	- MAÑANA REPASARLOS
	- ENVIAR AVANCES
 - USAR UNOS POMODOROS
	 - NO DESPERDICIAR EL PEAK DE MI CEREBRO
- 
# ACCIONA Y DESPUES PERFECCIONA

- HACER EL VAULT EN GIT
- 