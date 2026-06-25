---
status: borrador
capitulo: 3
seccion: 3.1
tags: [tesis/escritura, tesis/datos, hawc]
---
# III.i HAWC (High-Altitude Water Cherenkov Observatory)

> **Estado:** 🟡 Borrador — contenido sustancial disponible
> **Comentario del asesor pendiente:** [[Escritura/Comentarios del Asesor#Datos]] — justificar uso exclusivo de B0/B1

---

## Descripción del Observatorio

- **Ubicación:** Sierra Negra, México, 4100 m s.n.m.
- **Rango energético:** ~300 GeV – 100 TeV
- **Instrumentación:** 300 tanques de agua con PMTs que detectan luz Cherenkov de cascadas atmosféricas
- **Cobertura:** Dec −26° a +64°, ~2/3 del cielo simultáneamente

## Principio de Detección

"Cuando un fotón gamma inicia un shower en la atmósfera, las partículas secundarias producen luz Cherenkov al atravesar los tanques. El patrón de señales permite reconstruir energía y dirección."

## Ventaja operacional

- Operación continua (~95% de ciclo útil)
- A diferencia de IACTs que requieren noches claras, HAWC monitorea 24/7
- Ideal para capturar flares transitorios impredecibles

## Pass 5 y Reconstrucción de Energía

- Pass 5 mejora resolución y calibración (×4 mejoras angulares en algunos casos)
- Método **fHit** ("Fraction of Hit PMTs") como estimador correlacionado con la energía
- Bines de energía B0–B10, mapeados a medianas de energía por bin
- Producción de nuevos bines B0 y B1: ~300 GeV – 10 TeV, contienen ~66% de la señal total
- **Separación γ/hadrón:** Compactness (C = N_hit/CxPE40) y PINCness (χ² morfológico)
- **TS = 2ln(L(S+B)/L(B))**, log-likelihood Poisson binado

> ⚠️ **NOTA:** Los puntos espectrales de HAWC son medianas de energía por bin, NO evento por evento. La migración y dispersión instrumental introducen sesgo en índice espectral y normalización — debe plegarse el modelo con la respuesta del bin.

## Muestra Seleccionada (base Fernando Ureña)

- **Criterios de selección:**
	- z < 0.3 (fuentes cercanas, menor atenuación EBL)
	- Uso preferente de bines B0 y B1 para maximizar traslape espectral con Fermi-LAT
		- Razón: AGNs extragalácticos tienen espectros blandos por atenuación EBL → poca señal a >10 TeV
	- Ajuste espectral con índice α = 2.5 y corrección EBL: $e^{-τ(E,z)}$ con modelo de Domínguez (2011 o 2019?) [CORREGIR CITA]
	- Fuentes dentro de 40° del cenit de HAWC

- **Construcción de la muestra:**
	- 3FHL con criterios → ~138 fuentes
	- Exclusiones por contaminación (3 fuentes muy cerca de Mrk 421/501):
		- 3FHL J1105.8+3944 (5BZG J1105+3946)
		- 3FHL J1100.3+4020 (RX J1100.3+4019) 
		- 3FHL J1652.7+4024 (SDSS J1652+4024)
	- **Muestra final: 135 AGNs**

## Datos disponibles

- Archivo: `C:\Users\el_he\Documents\TESIS\data\AGN_135 - copiaPRUEBAS.xlsx`
- Columnas: source | counterpart | class | redshift | TS | sqrt_TS_err | logK_inc | logk | K_2sigma | K | RA_deg | Dec_deg

---

## 🔗 Conexiones
- Anterior: [[II.iii Radiación y Mecanismos de Emisión]]
- Siguiente: [[III.ii Fermi-LAT]]
- Detalle técnico profundo: [[All/mapa detallado, sección-por-sección del Cpitulo 2 - (Gamma-ray facilities and data)]]
- Survey completo: [[A 9-Year TeV Gamma-Ray Survey of Active Galaxies by HAWC - FerJosue Ureña]]
- Composición muestra: [[DETECCIONES.canvas]]
- Hub: [[XCRITURA]]
