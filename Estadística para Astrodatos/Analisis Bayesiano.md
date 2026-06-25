tags: [astrofísica, estadística, bayes, python, análisis-datos]
aliases: [análisis_bayesiano_astrofísica]
___
# 📊 Análisis Bayesiano en Astrofísica

## 📈 Distribuciones de Probabilidad:
### 🔹 Distribución Binomial
**Aplicación:** Eficiencia instrumental, detección de fotones

$$P(k; n, p) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Parámetros:**
- $n$: número total de ensayos (fotones incidentes)
- $p$: probabilidad de éxito (eficiencia de detección)
- $k$: número de éxitos (fotones detectados)

**Ejemplo:** Telescopio con 85% de eficiencia, 100 fotones incidentes:
```python
from scipy.stats import binom
n, p = 100, 0.85
prob_90_detectados = binom.pmf(90, n, p)  # ≈ 0.049
```

### 🔹 Distribución de Poisson
**Aplicación:** Conteo de eventos raros (fotones, rayos cósmicos)

$$P(k; \lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$$

**Propiedades:**
- Media = $\lambda$, Varianza = $\lambda$
- $\sigma = \sqrt{\lambda}$ (error estándar)

**Ejemplo HAWC:** Espera 5 eventos/s del Crab:
```python
from scipy.stats import poisson
lambda_ = 5
prob_7_eventos = poisson.pmf(7, lambda_)  # ≈ 0.104
prob_al_menos_7 = 1 - poisson.cdf(6, lambda_)  # ≈ 0.238
```

### 🔹 Distribución Normal
**Aplicación:** Fluctuaciones de fondo cuando $\lambda$ es grande

$$f(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/(2\sigma^2)}$$

**Límite de Poisson:** $\lambda > 20$ → Normal($\mu=\lambda$, $\sigma=\sqrt{\lambda}$)

```python
from scipy.stats import norm
mu, sigma = 1000, np.sqrt(1000)  # ≈ 31.6
prob_menos_900 = norm.cdf(900, mu, sigma)  # ≈ 0.0008
```

## ⚙️ Técnicas Computacionales Bayesianas

### 🔹 MCMC (Markov Chain Monte Carlo)
**Para:** Estimación de parámetros en modelos complejos

**Librerías Python:**
```python
import pymc3 as pm
import numpyro
import emcee
```

**Ejemplo básico:
```python
with pm.Model() as model:
    # Prior: tasa de señal (must be positive)
    mu_s = pm.Exponential('mu_s', lam=1.0)
    
    # Likelihood: Poisson para conteos
    observations = pm.Poisson('obs', mu=mu_s + alpha*mu_b, observed=N_on)
    
    # MCMC sampling
    trace = pm.sample(2000, tune=1000, chains=4)
```

### 🔹 Nested Sampling
Calcular evidencias $P(D)$ y distribuciones posteriores

**Librerías:**
```python
import dynesty
import ultranest
```

**Ventaja:** Calcula directamente la evidencia para comparación de modelos.

### 🔹 ABC (Approximate Bayesian Computation)
**Para:** Cuando la likelihood es intratable pero podemos simular datos

```python
def abc_rejection(simulator, prior, distance, data, epsilon, n_samples):
    posterior = []
    for i in range(n_samples):
        theta = prior.rvs()
        sim_data = simulator(theta)
        if distance(sim_data, data) < epsilon:
            posterior.append(theta)
    return posterior
```

## 🐍 Implementación Python Completa

### 📦 Setup del Entorno
```python
# Librerías esenciales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Bayesian libraries
import pymc3 as pm
import arviz as az

# Configuración
plt.style.use('seaborn-whitegrid')
np.random.seed(42)
```

### Exceso de Señal (Ejemplo HAWC)
```python
def analyze_excess_bayesian(N_on, N_off, alpha, prior_strength=1.0):
    """
    Análisis bayesiano de exceso de señal
    
    Parameters:
    - N_on: Conteo en región ON
    - N_off: Conteo en región OFF  
    - alpha: Factor de normalización
    - prior_strength: Fuerza del prior (1.0 = débil)
    """
    
    # Fondo esperado en región ON
    mu_b_expected = alpha * N_off
    
    with pm.Model() as model:
        # Prior para la señal (Exponential para parámetro positivo)
        mu_s = pm.Exponential('mu_s', lam=1.0/prior_strength)
        
        # Likelihood Poisson
        obs_on = pm.Poisson('obs_on', mu=mu_s + mu_b_expected, observed=N_on)
        
        # MCMC sampling
        trace = pm.sample(2000, tune=1000, chains=4, return_inferencedata=True)
    
    return trace, model

# Ejemplo con datos realistas
N_on, N_off, alpha = 1200, 10000, 0.1
trace, model = analyze_excess_bayesian(N_on, N_off, alpha)
```

### 📊 Visualización de Resultados
```python
def plot_posterior_analysis(trace):
    """Visualización de resultados MCMC"""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Trace plot
    az.plot_trace(trace, axes=axes[0, :])
    axes[0, 0].set_title('Traza de mu_s')
    
    # Posterior distribution
    az.plot_posterior(trace, var_names=['mu_s'], ax=axes[1, 0])
    axes[1, 0].set_title('Distribución Posterior de mu_s')
    
    # HDI (Highest Density Interval)
    hdi = az.hdi(trace, var_names=['mu_s'])
    axes[1, 0].axvline(hdi['mu_s'][0], color='red', linestyle='--')
    axes[1, 0].axvline(hdi['mu_s'][1], color='red', linestyle='--')
    
    # Probability of signal existence
    mu_s_samples = trace.posterior['mu_s'].values.flatten()
    prob_signal = np.mean(mu_s_samples > 0)
    axes[1, 1].text(0.5, 0.5, f'P(mu_s > 0) = {prob_signal:.4f}', 
                   ha='center', va='center', fontsize=14)
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    return fig

plot_posterior_analysis(trace)
```

### 📉 Análisis de Significancia Clásica + Bayesiana
```python
def comprehensive_analysis(N_on, N_off, alpha):
    """Análisis completo frequentista + bayesiano"""
    
    # Análisis clásico (Li & Ma style)
    excess = N_on - alpha * N_off
    sigma_excess = np.sqrt(N_on + alpha**2 * N_off)
    significance_classic = excess / sigma_excess
    
    # Análisis bayesiano
    trace, model = analyze_excess_bayesian(N_on, N_off, alpha)
    mu_s_samples = trace.posterior['mu_s'].values.flatten()
    prob_signal = np.mean(mu_s_samples > 0)
    
    return {
        'excess': excess,
        'significance_classic': significance_classic,
        'prob_signal_bayesian': prob_signal,
        'mu_s_mean': np.mean(mu_s_samples),
        'mu_s_hdi': az.hdi(trace, var_names=['mu_s'])['mu_s']
    }

results = comprehensive_analysis(1200, 10000, 0.1)
print(f"Exceso: {results['excess']:.1f}")
print(f"Significancia clásica: {results['significance_classic']:.2f}σ")
print(f"Probabilidad bayesiana de señal: {results['prob_signal_bayesian']:.4f}")
```

## Datos 

### 📋 Formato de Datos 
```python
# DataFrame para análisis astrofísico
data = pd.DataFrame({
    'source_id': ['Crab', 'Crab', 'Background'],
    'region_type': ['ON', 'OFF', 'OFF'],
    'counts': [1200, 10000, 15000],
    'exposure_time': [3600, 3600, 3600],  # segundos
    'energy_min': [1000, 1000, 1000],     # MeV
    'energy_max': [10000, 10000, 10000]   # MeV
})
```

### 🎯 Parámetros Clave para Análisis
| Parámetro | Descripción | Valores típicos |
|-----------|-------------|-----------------|
| `N_on` | Conteo región fuente | 100-10^6 |
| `N_off` | Conteo región fondo | 1000-10^7 |
| `alpha` | Razón de normalización | 0.01-1.0 |
| `exposure_time` | Tiempo de exposición | 1000-10^6 s |
| `energy_bins` | Bines energéticos | 8-12 bins log |

## 🚀 Workflow Completo de Análisis

1. **Preprocesamiento:**
   - Limpieza de datos
   - Corrección por eficiencia instrumental
   - Normalización de exposiciones

2. **Análisis Exploratorio:**
   - Histogramas de conteos
   - Cálculo de significancias simples
   - Identificación de candidatos

3. **Modelado Bayesiano:**
   - Definición de priors informativos
   - Sampling MCMC
   - Validación de convergencia

4. **Interpretación:**
   - Cálculo de probabilidades posteriores
   - Estimación de flujos
   - Evaluación de systemáticas

## 📚 Referencias Rápidas

### 🔗 Librerías Python Esenciales
- `pymc3`: MCMC para modelos probabilísticos
- `arviz`: Visualización y diagnóstico de resultados Bayesianos  
- `emcee`: MCMC puro y eficiente
- `dynesty`: Nested sampling
- `scipy.stats`: Distribuciones estadísticas

### 📖 Conceptos Clave
- **HDI**: Intervalo de mayor densidad (credible interval)
- **R-hat**: Estadístico de convergencia MCMC (<1.1 = buen sampling)
- **ESS**: Tamaño de muestra efectivo (>200 por chain)

---

**Nota:** Este framework se adapta a HAWC, Fermi-LAT, HESS, MAGIC, etc. Solo ajustar priors y modelos de likelihood según el instrumento.
