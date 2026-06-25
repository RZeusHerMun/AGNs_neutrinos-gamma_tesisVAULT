---
status: borrador
capitulo: 3
seccion: 3.2
tags: [tesis/escritura, tesis/datos, fermi-lat]
---
# III.ii Fermi-LAT (Large Area Telescope)

> **Estado:** 🟡 Borrador — necesita especificar catálogo definitivo (3FHL vs 4FHL)
> **Comentario del asesor:** [[Escritura/Comentarios del Asesor#Datos]] — "¿TIENES ALGÚN CATÁLOGO QUE ESTES USANDO?"

---

## Descripción del Observatorio

- Lanzamiento: 2008
- Rango energético: 20 MeV – >300 GeV
- Arquitectura: convertidores de tungsteno + tracker de silicio + calorímetro + anti-coincidencia
- Monitoreo all-sky cada ~3 horas
- Resolución angular mejora con la energía

## Principio de Detección

Fotones gamma se convierten en pares electrón-positrón en los convertidores de tungsteno. El tracker de silicio reconstruye la trayectoria, y el calorímetro mide la energía.

## Catálogos: 3FHL vs 4FHL

**Fernando usó el 3FHL**. Propuesta: migrar al **4FHL**.

### 3FHL (Third Fermi High-energy LAT catalog)
- 7 años de datos
- Rango: 10 GeV – 2 TeV
- Usado en la muestra original de Ureña

### 4FHL (Fourth Fermi High-energy LAT catalog)
**Beneficios:**
- Tiempo de observación extendido: 16 años vs 7
- Sensibilidad mejorada para E > 50 GeV
- Resolución angular mejorada con la energía
- Catálogo expandido: >700 fuentes arriba de 50 GeV
- Ref: [4FHL: The Deepest Fermi-LAT Catalog](https://ui.adsabs.harvard.edu/abs/2025AAS...24621302R/abstract) ==revisando==

**Desventajas:**
- Ventana energética modificada: 4FHL cubre 30 GeV – 2 TeV (HAWC: 300 GeV – 100 TeV) → menor traslape
- Espectros más "empinados" (índices espectrales mayores) para >10 GeV → complica extrapolaciones
- Dificultad para incorporar nuevas fuentes ==en progreso==
- Mayor riesgo de contaminación entre fuentes cercanas

### Catálogo 4FGL-DR4 (referencia general)
- LAT 14-year Source Catalog
- Formato: 4FGL JHHMM.m+DDMM
- Disponible en FITS, BROWSE table, XML
- Incluye DS9 Region Files con posiciones y elipses de error

## Criterios de selección para la muestra

- Fuentes asociadas o identificadas con AGNs conocidos
- $z \leq 0.3$
- Posición dentro de 40° del cenit de HAWC (optimizar respuesta del detector)

## Qué se obtiene del catálogo Fermi

- **Posición (RA, Dec)** y radio/elipse de incertidumbre → cruce espacial
- **Parámetros espectrales** (índice, curvatura, flujo en bandas) → modelar origen hadrónico
- **Flags de variabilidad y curvas de luz** → búsquedas temporales en ventanas de flaring

---

## 🔗 Conexiones
- Anterior: [[III.i HAWC]]
- Siguiente: [[III.iii IceCube]]
- Integración Fermi+HAWC+IceCube: [[Escritura/Flujo de Trabajo Multimensajero]]
- Hub: [[XCRITURA]]
