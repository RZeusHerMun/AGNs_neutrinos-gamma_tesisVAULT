
- **La ruta de Miniforge** (`C:\Users\el_he\miniforge3\...`) es **"La Cocina"**. Ahí viven los cocineros (Python), los cuchillos (Numpy) y las ollas (Astropy). **Tú no debes guardar tu comida ahí.** Si un día remodelamos la cocina (borramos el entorno), se iría tu comida a la basura.
    
- **Tu carpeta en Documentos** (`C:\Users\...\Documents\Tesis`) es **"Tu Mesa"**. Ahí es donde pones tus platos (datos), tus recetas (scripts) y tus fotos.
    

**La forma correcta de empezar a trabajar cada día es esta:**

1. Abres la terminal negra.
2. Activas el entorno:    
    ```
    conda activate multi
    ```
3. Navegas a tu carpeta de tesis (Aquí está el truco):
    ```
    cd Documents\TESIS
    ```
    _(El comando `cd` significa "Change Directory")._
4. **Ahora** lanzas Jupyter:
    ```
    jupyter lab
    ```
### . organizacion tesis
```
Documentos/
└── Tesis_Proyecto/
    ├── data/             <-- Aquí pones los archivos FITS de Fermi/HAWC
    ├── notebooks/        <-- Aquí tus .ipynb (Analisis1.ipynb)
    ├── plots/            <-- Aquí guardas las imágenes que generes
    ├── scripts/          <-- Aquí scripts .py sueltos
    └── entorno_tesis.yml <-- El archivo de respaldo que creamos
```
Y en tu código, cuando cargues datos, lo haces así:
```
dat = fits.open('../data/archivo_hawc.fits') # ".." significa "baja una carpeta"
```
salir
```
    conda deactivate multi
    exit
```