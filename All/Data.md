# Fuentes de Datos
___
### DataSet
3FHL Source	Counterpart	Class	Redshift	TS	±√TS	K ± ΔK	K_2σ
J0007.9+4711	RX J0007.9+4711	bll	0.28	9.4	-3.07	-18.4 ± 5.99	2.59




### HAWC (High Altitude Water Cherenkov)

- **Catálogo principal**: 3HWC (Third HAWC Catalog)
- **Energías**: ~300 GeV - 100 TeV
- **Cobertura**: -26° < Dec < 64°
- **Ventana de observación**: continua (~90% uptime)
## 3HWC Survey

[Details](https://data.hawc-observatory.org/datasets/3hwc-survey/index.php)    [Catalog](https://data.hawc-observatory.org/datasets/3hwc-survey/catalog.php)    [**Maps**](https://data.hawc-observatory.org/datasets/3hwc-survey/fitsmaps.php)    [Interactive Tool](https://data.hawc-observatory.org/datasets/3hwc-survey/coordinate.php)

### Downloadable 3HWC Maps

You can download the skymaps with significance/flux information (healpix format in FITS files) used in the creation of the 3HWC catalog here:

- [Point source search](https://data.hawc-observatory.org/datasets/3hwc-survey/aerie-apps_bin1-9__allsky_1024_i2.5_r0.0_p1.0_fc2Flux_negSigMap.fits.gz)
- [0.5o extended source search](https://data.hawc-observatory.org/datasets/3hwc-survey/aerie-apps_bin1-9__allsky_1024_i2.5_r0.5_p1.0_fc2Flux_negSigMap.fits.gz)
- [1.0o extended source search](https://data.hawc-observatory.org/datasets/3hwc-survey/aerie-apps_bin1-9__allsky_1024_i2.5_r1.0_p1.0_fc2Flux_negSigMap.fits.gz)
- [2.0o extended source search](https://data.hawc-observatory.org/datasets/3hwc-survey/aerie-apps_bin1-9__allsky_1024_i2.5_r2.0_p1.0_fc2Flux_negSigMap.fits.gz)

If you use these files, please reference the following publication:

- A. Albert et al. 2020: [3HWC: The Third HAWC Catalog of Very-High-Energy Gamma-ray Sources](https://iopscience.iop.org/article/10.3847/1538-4357/abc2d8), ApJ 905 76

### Map-making

We provide here the results of a putative point and extended source searches, described in more detail in the 3HWC catalog paper. For each pixel in HEALPix binning (NSIDE=1024) in celestial coordinates (RA/Dec, J2000), we perform an independent fit to HAWC event counts, using events recorded within (1o + source exension) of the pixel center. For the point (extended) source searches, the source model consists of a point source (extended, disk-like source) with a power-law energy spectrum with a spectral index of -2.5, convolved with HAWC's instrument response function. The only fit parameter is the flux normalization. The best-fit source+background model is compared to a background-only model to calculate the test statistic, TS = 2 log( Ls+b / Lb ).

Additionally, for each pixel, we calculate the value of the flux norm that maximixes the likelihood function, under the constraint that the flux norm must be greater or equal to 0 (as sources with negative flux would be considered unphysical), and the 2 sigma confidence level [Feldman-Cousins confidence interval](https://link.aps.org/pdf/10.1103/PhysRevD.57.3873). For locations with a large TS, as the sources in the catalog, these intervals are equivalent to central confidence intervals; for lower TS location the bounds become asymmetric around the flux best estimate and the flux upper bound can be regarded as an upper limit.

### Content of the FITS files

The FITS files contain the following columns:

- Column 0: significance = +-sqrt(TS), as defined above. The negative sign is used when the unconstrained best-fit flux norm is negative.
- Column 1: Best-fit flux norm at the pivot energy of 7 TeV in TeV-1cm-2s-1.
- Column 2: 2 sigma lower limit on the flux norm (same units).
- Column 3: 2 sigma upper limit on the flux norm (same units).

Pixels with invalid values (failed fit, outside the field of view) are set to -1.63yy
75e30, the default value of healpy.UNSEEN.

### Accessing the FITS files

The following code snippet provides an example for how to obtain the signifiance and best-fit flux at a given position on the sky:

import numpy as np
import healpy as hp

file="aerie-apps_bin1-9__allsky_1024_i2.5_r0.0_p1.0_fc2Flux_negSigMap.fits.gz"
sigmap, fluxmap, fluxmap_lower, fluxmap_upper = hp.read_map(file, (0, 1, 2, 3))
NSIDE = hp.get_nside(sigmap)

lon, lat = 83.63, 22.02 # Crab coordinates in degrees, J2000 RA/Dec
th, ph = np.deg2rad([90.0-lat, lon])
pixel = hp.ang2pix(NSIDE, th, ph)

sig = sigmap[pixel]
flux_best = fluxmap[pixel]
flux_lower = fluxmap_lower[pixel]
flux_upper = fluxmap_upper[pixel]

print (sig, flux_best, flux_lower, flux_upper)

Check out the [healpy documentation](https://healpy.readthedocs.io/en/latest/) for more information about how to use and display healpix-format maps within python.

# IceCube

- **Alertas en tiempo real**: IceCube Realtime Alert System
- **Catálogos**:
    - Track events (mejor resolución angular: ~0.5°)
    - Cascade events (resolución ~10°, mejor energía)
- **Base de datos**: [https://gcn.gsfc.nasa.gov/amon_icecube_gold_bronze_events.html](https://gcn.gsfc.nasa.gov/amon_icecube_gold_bronze_events.html)

# Fermi-LAT (para futuro)

- **Catálogo**: 4FGL (Fourth Fermi-LAT catalog)
- **Energías**: 50 MeV - 1 TeV
- **Ventaja**: monitoreo continuo de todo el cielo


====

Identificar AGNs en el campo de visión común (~-26° < Dec < 64°)