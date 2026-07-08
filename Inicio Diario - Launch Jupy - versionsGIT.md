
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
###  organizacion tesis
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

# Control de versiones en git

### Fase 1: Preparar tu Vault y GitHub

Dado que Obsidian guarda todo en archivos Markdown locales, lo trataremos como cualquier otro proyecto de código.

**1. Crea el repositorio en GitHub**

- Ve a tu cuenta de GitHub y crea un nuevo repositorio.
    
- Llámalo como prefieras (por ejemplo, `tesis-vault`).
    
- **Importante:** Déjalo completamente vacío. No marques la opción de añadir un archivo `README`, ni `.gitignore`, ni licencia.
    

**2. .gitingnore**

```
# Ignorar el estado del espacio de trabajo de Obsidian
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# Ignorar caché
.obsidian/cache
.trash/
.DS_Store
```

**3. 1errimer "push"**

```bash
git init
git add .
git commit -m "Commit inicial: Estructura de la tesis"
git branch -M main
git remote add origin https://github.com/tu-usuario/tesis-vault.git
git push -u origin main
```

### Fase 2: Uso del pliggin del obsidian-git

**1. Instala el plugin "Obsidian Git"**
**2. Configura los respaldos automáticos (Opcional pero recomendado)**

- Ve a las opciones de **Obsidian Git** en la barra lateral izquierda de la Configuración.
- Aquí puedes establecer que el plugin haga un _commit_ y un _push_ de forma automática cada cierto tiempo.
- Busca la opción **Vault backup interval (minutes)** y pon un valor, por ejemplo, `30` (para que guarde cada media hora) o `0` si prefieres hacerlo siempre manualmente.
- También puedes configurar el **Commit message** por defecto para que sea algo como `backup: {{date}}`.

**3. Uso manual desde la Paleta de Comandos**
Si prefieres tener el control total de cuándo se envían las actualizaciones a tu repositorio (ideal si quieres poner mensajes de commit específicos detallando tus avances), puedes usar la paleta de comandos de Obsidian (`Ctrl + P` o `Cmd + P`):

- Escribe `Git: Commit all changes` para preparar y confirmar tus avances (te pedirá un mensaje).
- Escribe `Git: Push` para enviar los cambios a GitHub.
- Escribe `Git: Pull` para descargar cambios si has editado tu vault desde otro dispositivo.