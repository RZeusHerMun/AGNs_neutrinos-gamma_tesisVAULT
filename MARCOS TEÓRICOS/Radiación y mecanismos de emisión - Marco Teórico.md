---
fecha: 2026-07-21
tipo: marco-teorico
forma_nota: marco-teorico
seccion_destino: "[[II.iii Radiación y Mecanismos de Emisión]]"
tags:
  - tema/emision
  - tema/multimensajero
  - proyecto/tesis-multimensajera
  - tesis/marco-teorico
  - estado/activo
---
 > 	Los mecanismos de emisión son el punto donde la física del jet se vuelve observable. La sección [[II.ii Jets Relativistas]] dejó una población de partículas no térmicas —electrones y, si el jet es hadrónico, protones— aceleradas hasta energías macroscópicas y confinadas en un flujo que apunta a la Tierra. Este marco sigue lo que esas partículas hacen con su energía: cómo los electrones la convierten en el continuo de sincrotrón y Compton inverso que domina el cielo gamma, cómo los protones abren un segundo canal que fabrica a la vez rayos gamma y neutrinos, y por qué solo ese segundo canal deja una huella que ningún modelo leptónico puede imitar. Ese es el argumento físico que justifica buscar neutrinos de IceCube en las posiciones de las fuentes gamma de HAWC.

%%
## Por qué este marco

La tesis mide una coincidencia espacial: neutrinos de IceCube contra posiciones de AGN detectados en rayos gamma. Para que esa medición signifique algo hay que responder antes una pregunta —¿por qué esperaríamos que un neutrino y un fotón gamma salieran del mismo objeto?— y la respuesta está entera en los mecanismos de emisión.

La sección anterior explicó de dónde sale la energía, el espín del agujero negro extraído por Blandford–Znajek, y cómo termina depositada en partículas individuales por los choques y la reconexión. Lo que no explicó es qué radiación producen esas partículas, y ahí está la bifurcación que ordena todo el capítulo. Una población de electrones radia fotones y nada más. Una población de protones radia fotones y neutrinos a la vez, porque unos y otros nacen del mismo decaimiento. El neutrino es, por eso, la única señal capaz de distinguir un jet que acelera hadrones de uno que solo acelera leptones, y distinguir eso —fuente por fuente— es exactamente lo que persigue la correlación multimensajera. Este marco cierra el bloque teórico entregando a los capítulos instrumentales dos cosas: el espectro que HAWC va a medir y la razón por la que una alerta de IceCube sobre la posición de una fuente gamma cuenta como evidencia y no como casualidad.
%%
## 1. Radiación térmica y no térmica: el techo del disco y el continuo del jet

Para definir la radiación que emite un cuerpo usamos los fundamentos de la radiación de cuerpo negro de Planck. Un cuerpo negro en equilibrio a temperatura $T$ emite un espectro de Planck cuyo máximo se corre con $T$ según la ley de Wien que dice: $\nu_{\rm pico}\propto T$ 

Todo cuerpo con temperatura radia. Un cuerpo negro en equilibrio a temperatura $T$ emite un espectro de Planck cuyo máximo se corre con $T$ según la ley de Wien, $\nu_{\rm pico}\propto T$: es la radiación de una estrella, de una brasa y también de un ser humano a $310$ K, cuyo pico cae en el infrarrojo. En un AGN, la componente térmica la produce el disco de acreción, que no es un anillo a una temperatura sino una superposición de anillos a temperaturas crecientes hacia el centro; integrados, forman el "gran bulto azul" con su máximo en el ultravioleta y su cola en rayos X blandos. Esa es la firma del gas caliente, y —como se estableció en [[II.i Fenomenología de los AGNs]]— es también su límite: la termodinámica de la acreción tiene un techo, y ese techo no llega ni de lejos al régimen del TeV.

Los mensajeros de esta tesis viven por encima de ese techo. Su espectro no es una curva de Planck sino una ley de potencias, $F_\nu\propto\nu^{-\alpha}$, que se extiende sin máximo térmico a lo largo de decenas de órdenes de magnitud en frecuencia. Una ley de potencias es la firma inconfundible de un proceso no térmico: no hay una temperatura común, hay una población de partículas cuyas energías se distribuyen ellas mismas como ley de potencias —el $dN/dE\propto E^{-p}$ que la aceleración difusiva por choques dejó en el jet (sección [[II.ii Jets Relativistas]])— y cada partícula radia según su energía individual. El resto de este marco es, en el fondo, el diccionario que traduce esa distribución de partículas en la distribución de fotones y neutrinos que llega a los detectores.

## 2. La firma macroscópica: la distribución espectral de energía y sus dos jorobas

El resumen observacional de todo lo que un blazar radia es su distribución espectral de energía (SED), que se representa como $\nu F_\nu$ frente a $\nu$. Esta forma pone en el eje vertical la potencia por década de frecuencia, de modo que los máximos señalan dónde el objeto emite realmente su energía. La SED de un blazar tiene un perfil característico de doble joroba que ningún otro tipo de fuente reproduce, y ese perfil es el mapa que hay que explicar.

La primera joroba se extiende desde el radio hasta el óptico, el ultravioleta o los rayos X según la fuente, y su origen no está en disputa: es radiación de sincrotrón de electrones relativistas (§3). La posición de su máximo, $\nu_{\rm s}$, ordena a los blazares en una secuencia —de sincrotrón de baja, intermedia y alta frecuencia (LSP, ISP, HSP)— que Abdo et al. (2010) sistematizaron con el primer gran muestreo de Fermi-LAT y que sigue siendo la taxonomía operativa del campo. La segunda joroba cubre desde los rayos X duros hasta los gamma de muy alta energía (VHE, $\gtrsim 100$ GeV), y su origen es justamente el problema abierto que esta tesis ataca: puede ser obra de los mismos electrones (vía leptónica) o de protones acelerados (vía hadrónica). Desde la Tierra, las dos hipótesis producen jorobas gamma parecidas, y distinguirlas con el fotón solo es imposible; hace falta el neutrino. Las dos secciones siguientes desarrollan cada vía.

![[SED multimensajera - doble joroba.png]]
*Esquema de la SED de doble joroba de un blazar en clave multimensajera. La primera joroba es sincrotrón de electrones; la segunda, Compton inverso (leptónico) o decaimiento de $\pi^0$ (hadrónico), indistinguibles desde el fotón. La vía hadrónica arrastra además una joroba de neutrinos ($\pi^+$) hacia el PeV. Se marcan la atenuación de la cola VHE por la EBL y la cobertura de Fermi-LAT y HAWC (fotones) e IceCube (neutrinos), que se solapan en energía: ahí es donde vive la correlación de esta tesis.*

## 3. La vía leptónica: sincrotrón, Compton inverso y su techo

En el escenario leptónico, una única población de electrones —y positrones— relativistas produce las dos jorobas. Es el modelo de referencia porque es económico y ajusta la mayoría de las SED con pocos parámetros.

La primera joroba es sincrotrón. Un electrón de factor de Lorentz $\gamma$ que gira en un campo magnético $B$ radia una potencia

$$P_{\rm sinc}=\frac{4}{3}\,\sigma_T\,c\,\gamma^2\,U_B,\qquad U_B=\frac{B^2}{8\pi},$$

concentrada en torno a una frecuencia característica $\nu_{\rm s}\simeq\gamma^2\,(eB/2\pi m_e c)$. Como la energía radiada crece con $\gamma^2$, los electrones más rápidos dominan el extremo azul de la joroba; y como el jet mantiene una distribución $N(\gamma)\propto\gamma^{-p}$, el espectro resultante es también una ley de potencias, $F_\nu\propto\nu^{-(p-1)/2}$, lo que enlaza directamente el índice espectral observado con el índice de inyección $p$ de los choques. La radiación de sincrotrón está además fuertemente polarizada, y esa polarización es la evidencia empírica más directa de que la primera joroba es sincrotrón y no otra cosa.

La segunda joroba, en su versión leptónica, es Compton inverso. Los mismos electrones dispersan fotones de baja energía y los suben al régimen gamma. En el límite de Thomson, cada dispersión multiplica la energía del fotón por $\sim\gamma^2$,

$$E_\gamma\simeq\frac{4}{3}\,\gamma^2\,E_{\rm sem},$$

de modo que un electrón que radia sincrotrón en el óptico puede llevar un fotón hasta el GeV o el TeV. La potencia Compton inversa tiene una forma gemela de la de sincrotrón, $P_{\rm IC}=\tfrac{4}{3}\sigma_T c\,\gamma^2 U_{\rm rad}$, con la densidad de fotones $U_{\rm rad}$ en lugar de la magnética; su cociente, $P_{\rm IC}/P_{\rm sinc}=U_{\rm rad}/U_B$, es la "dominancia Compton" que mide cuánta energía va a cada joroba. Según de dónde vengan los fotones semilla, el modelo se ramifica. En el Synchrotron Self-Compton (SSC) son los propios fotones de sincrotrón del jet, escenario que ajusta bien a los BL Lac, pobres en gas y en radiación externa. En el External Compton (EC) vienen de fuera —el disco, la región de líneas anchas, el toro de polvo— y ese aporte extra domina en los FSRQ, más luminosos. Böttcher et al. (2013) compararon sistemáticamente estos ajustes con sus alternativas hadrónicas y mostraron que ambos reproducen las SED gamma, lo que deja la degeneración sin resolver desde el lado del fotón.

La vía leptónica tiene, sin embargo, un techo, y vale la pena subrayarlo porque es una de las grietas por donde entra la alternativa hadrónica. A medida que la energía del fotón semilla vista por el electrón se acerca a su energía en reposo, $\gamma\,\epsilon\sim m_e c^2$, la dispersión Compton abandona el régimen de Thomson y entra en el de Klein–Nishina: la sección eficaz cae muy por debajo de $\sigma_T$ y la transferencia de energía se vuelve ineficiente. El resultado es que la producción leptónica de gamma de muy alta energía se suprime justo donde más se necesitaría, y sostener la joroba VHE observada exige entonces electrones aún más energéticos y condiciones de aceleración cada vez más extremas. En las fuentes más duras, esa exigencia empuja el modelo puramente leptónico hasta el límite de lo plausible.

Y el punto decisivo para esta tesis: por económica y exitosa que sea, la vía leptónica no produce neutrinos. Ninguno. Los electrones no tienen forma de generar piones cargados, que son la única fuente de neutrinos astrofísicos a estas energías. No se trata de un flujo pequeño o despreciable; es estrictamente cero. Por eso la mera detección de un neutrino de alta energía en la dirección de un blazar no "favorece" la interpretación hadrónica frente a la leptónica: la exige.

## 4. La vía hadrónica: fotoproducción de piones y el nacimiento de dos mensajeros

Para que un jet emita neutrinos tiene que acelerar protones —o núcleos—, no solo electrones. La sección [[II.ii Jets Relativistas]] ya mostró que puede hacerlo: los choques y la reconexión llevan a los protones hasta el criterio de Hillas, a $10^{17}$–$10^{19}$ eV, con margen de sobra para lo que sigue. La cuestión es qué ocurre cuando esos protones ultra-relativistas se cruzan con los densos campos de fotones del propio jet, los mismos fotones de sincrotrón que forman la primera joroba.

Por encima de un umbral de energía, la interacción protón-fotón ($p\gamma$) procede por resonancia, a través de la excitación de un barión $\Delta^+(1232)$, que decae casi instantáneamente en dos canales cinemáticos:

$$p+\gamma\;\longrightarrow\;\Delta^+\;\longrightarrow\;\begin{cases}\,p+\pi^0 & (\approx 2/3)\\[3pt]\,n+\pi^+ & (\approx 1/3)\end{cases}$$

El decaimiento reparte la energía entre un canal neutro y uno cargado, y ahí, literalmente en la razón de ramificación de una resonancia, nace la naturaleza multimensajera de la fuente.

Del canal neutro salen los rayos gamma. El pión neutro decae electromagnéticamente en unos $10^{-16}$ s en dos fotones,

$$\pi^0\longrightarrow\gamma+\gamma,$$

cada uno con la mitad de la energía del pión, es decir del orden del 10 % de la del protón padre. Estos fotones —de decenas de GeV a TeV— alimentan la segunda joroba de la SED, la misma que en la vía leptónica producía el Compton inverso. Vistos desde HAWC, un gamma pionico y un gamma Compton son indistinguibles: de ahí la degeneración.

Del canal cargado salen los neutrinos. El pión positivo decae por la fuerza débil en una cadena que termina en tres neutrinos y un positrón,

$$\pi^+\longrightarrow\mu^+ +\nu_\mu\longrightarrow e^+ +\nu_e+\bar\nu_\mu+\nu_\mu.$$

Cada neutrino se lleva aproximadamente un cuarto de la energía del pión, y el pión un quinto de la del protón, de modo que $E_\nu\approx E_p/20$: los neutrinos de $0{,}1$–$1$ PeV que IceCube atribuye a fuentes astrofísicas requieren protones de $10^{16}$–$10^{17}$ eV, exactamente el rango que el jet alcanza. El decaimiento fija además la composición de sabores en la fuente en $(\nu_e:\nu_\mu:\nu_\tau)\approx(1:2:0)$; tras oscilar durante miles de millones de años luz, la mezcla llega a la Tierra como $\approx(1:1:1)$, y es esa igualdad la que permite que IceCube detecte el flujo sobre todo por el canal muónico sin perder la información sobre su origen. Las distribuciones de energía precisas de los fotones y neutrinos secundarios producidos en $p\gamma$ están tabuladas en el trabajo de referencia de Kelner & Aharonian (2008).

Existe un segundo canal hadrónico, la colisión protón-protón ($pp$) contra gas denso, que produce las tres especies de pión en proporciones parecidas y, por tanto, gamma y neutrinos igual que $p\gamma$; domina en entornos ricos en materia —la corona o el disco de un Seyfert, un ambiente de brote estelar— más que en el jet limpio de un BL Lac. En cualquiera de las dos versiones la conclusión física es la misma, y es la que sostiene toda la estrategia multimensajera: los rayos gamma pionicos y los neutrinos se producen en la misma interacción, en la misma región, con luminosidades ligadas por la cinemática del decaimiento del pión. No son dos fenómenos que coincidan por azar; son dos salidas del mismo suceso. Que su presupuesto energético en fotones y en neutrinos sea del mismo orden es lo que convierte una coincidencia direccional en una predicción contrastable (Ahlers & Halzen 2018).

## 5. Por qué hace falta el neutrino: la degeneración que un fotón no resuelve

Conviene detenerse en el corazón lógico de la tesis, porque es lo que da sentido a todo el análisis posterior. La segunda joroba de la SED admite dos lecturas —Compton inverso de electrones o decaimiento de piones de protones— y desde el fotón gamma no hay forma limpia de decidir entre ellas: ambos modelos ajustan los datos con parámetros razonables (Böttcher et al. 2013). Es una degeneración genuina, no un problema de precisión que se arregle acumulando más estadística gamma.

El neutrino la rompe de un golpe porque es asimétrico respecto a las dos vías. Un rayo gamma puede ser leptónico o hadrónico; un neutrino de alta energía solo puede ser hadrónico. No existe mecanismo leptónico que lo produzca. Por eso el neutrino no es un mensajero más que aporta un dato adicional: es el único observable que responde directamente a la pregunta "¿se están acelerando protones aquí?". Cuando su dirección de llegada coincide con la posición de un AGN que brilla en gamma, esa coincidencia no confirma que el AGN emite —eso ya lo sabíamos por el fotón—, sino que emite hadrónicamente: que en ese jet se aceleran protones hasta energías de rayo cósmico. Ese es el salto cualitativo que ningún telescopio de fotones puede dar por sí solo, y es la razón de ser de cruzar los catálogos de IceCube con los de HAWC.

## 6. El viaje de regreso: atenuación por la luz de fondo extragaláctica

Hasta aquí, la física de la fuente. Falta el trayecto, y el trayecto trata a los dos mensajeros de manera radicalmente distinta —una asimetría que, lejos de estorbar, refuerza el argumento.

El neutrino cruza el universo casi sin interactuar: su sección eficaz débil es tan pequeña que el camino libre medio contra los fondos cósmicos supera con holgura el tamaño del universo observable a estas energías. Llega, por tanto, como salió, apuntando a su fuente y con su espectro intacto. El rayo gamma de muy alta energía no tiene esa suerte. En su viaje se topa con la luz de fondo extragaláctica (EBL) —el tenue baño de fotones ópticos e infrarrojos acumulado por todas las estrellas y el polvo de la historia cósmica— y sufre producción de pares,

$$\gamma_{\rm VHE}+\gamma_{\rm EBL}\longrightarrow e^+ + e^-,$$

posible siempre que el producto de las energías supere el umbral $E_\gamma\,\epsilon_{\rm EBL}\gtrsim (m_e c^2)^2$. Para un fotón de $1$ TeV el blanco óptimo es un fotón EBL óptico o infrarrojo, justo la banda más poblada, así que la absorción es severa. Su efecto se describe con una profundidad óptica $\tau(E,z)$ que crece con la energía del fotón y con la distancia a la fuente, y que atenúa el flujo observado por un factor $e^{-\tau(E,z)}$. El lugar geométrico $\tau=1$ define un "horizonte gamma": más allá de él el universo se vuelve opaco al TeV. El modelo estándar de esta atenuación, y el que usan las colaboraciones de HAWC y Fermi, es el de Domínguez et al. (2011).

De aquí sale una consecuencia práctica que gobierna la muestra de esta tesis. Como $\tau$ crece con $z$, las fuentes lejanas tienen su joroba VHE recortada o directamente borrada, lo que sesga la luminosidad reconstruida y complica cualquier ajuste espectral. Por eso la muestra de AGN se restringe a $z<0{,}3$: a bajo corrimiento al rojo la atenuación es moderada, la corrección $e^{-\tau}$ es fiable y el espectro que mide HAWC —concentrado en los bines de menor energía, donde la señal sobrevive— se puede recuperar con confianza. La cercanía de las fuentes no es una casualidad de la muestra; es un requisito impuesto por la EBL, y es lo que da pie a describirla aquí, además de motivar el corte en $z$ que se detalla en [[III.i HAWC]].

Y el cierre del argumento: donde la EBL apaga al fotón, el neutrino sigue llegando. En las fuentes cuya emisión VHE está parcialmente absorbida, el neutrino es una sonda sin atenuación de las entrañas del jet, capaz de revelar aceleración hadrónica que el fotón, atenuado, ocultaría. La correlación espacial entre ambos mensajeros no solo confirma el origen; en las fuentes más lejanas de la muestra, es la única vía para verlo.

## 7. Cierre: de los mecanismos a los instrumentos

El andamiaje de este marco es una sola cadena. La energía que el jet extrajo del espín del agujero negro terminó en una población no térmica de partículas; esas partículas radian; si son electrones, producen sincrotrón y Compton inverso, y nada más; si hay protones, producen además —por la fotoproducción de piones— rayos gamma y neutrinos atados por la misma cinemática. El fotón gamma es ambiguo entre las dos vías, y encima viaja atenuado por la EBL; el neutrino es inequívocamente hadrónico, y viaja intacto. De esa doble asimetría nace toda la estrategia: buscar, en la posición de las fuentes gamma, la llegada de un neutrino que delate a los protones.

Que esa estrategia no es un ejercicio teórico lo demuestran dos hitos. El primero es el blazar TXS 0506+056, cuya dirección coincidió con el neutrino IceCube-170922A (IceCube Collaboration et al. 2018a) y que, al revisar el archivo, mostró un exceso de neutrinos independiente y significativo al $3{,}5\sigma$ desde esa misma posición del cielo (IceCube Collaboration 2018b): la primera identificación de un blazar como fuente de neutrinos. El segundo, y más cercano al método de esta tesis, es la galaxia activa NGC 1068, de la que IceCube reportó un exceso estacionario de unos $79$ neutrinos con una significancia global de $4{,}2\sigma$, coincidente con la posición de una fuente gamma conocida (IceCube Collaboration 2022). NGC 1068 importa aquí por una razón concreta: su señal es una acumulación espacial, no un estallido —una correlación de posiciones, no de tiempos—, exactamente el tipo de evidencia que este trabajo busca al cruzar catálogos. Como ambos mensajeros nacen juntos en el mismo choque hadrónico, su coincidencia en el cielo es, en sí misma, la firma; el análisis temporal conjunto queda como una extensión natural para más adelante, cuando las curvas de luz de la muestra estén disponibles.

Con esto, el bloque teórico entrega a los capítulos siguientes todo lo que necesitan. Se sabe qué mide cada instrumento y por qué: HAWC muestrea la segunda joroba —los gamma de la fotoproducción o del Compton inverso— en la ventana de energía donde la EBL todavía deja pasar la señal; IceCube atrapa los neutrinos muónicos del canal cargado, cuya resolución angular permite asignarlos a una fuente puntual. Y se sabe qué significa que sus posiciones coincidan. Los mecanismos ya están sobre la mesa; lo que sigue —secciones [[III.i HAWC]] y [[III.iii IceCube]]— es cómo se detecta cada mensajero y cómo se mide, estadísticamente, si esas coincidencias son reales.

---

## Referencias

- Abdo, A. A., et al. (Fermi-LAT Collaboration) (2010), *The spectral energy distribution of Fermi bright blazars*, ApJ 716, 30 — [DOI](https://doi.org/10.1088/0004-637X/716/1/30)
- Ahlers, M., & Halzen, F. (2018), *Opening a new window onto the universe with IceCube*, Prog. Part. Nucl. Phys. 102, 73 — [DOI](https://doi.org/10.1016/j.ppnp.2018.05.001)
- Böttcher, M., Reimer, A., Sweeney, K., & Prakash, A. (2013), *Leptonic and hadronic modeling of Fermi-detected blazars*, ApJ 768, 54 — [arXiv:1304.0605](https://arxiv.org/abs/1304.0605)
- Domínguez, A., et al. (2011), *Extragalactic background light inferred from AEGIS galaxy-SED-type fractions*, MNRAS 410, 2556 — [arXiv:1007.1459](https://arxiv.org/abs/1007.1459)
- IceCube Collaboration, Fermi-LAT, MAGIC, et al. (2018a), *Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A*, Science 361, eaat1378 — [DOI](https://doi.org/10.1126/science.aat1378)
- IceCube Collaboration (2018b), *Neutrino emission from the direction of the blazar TXS 0506+056 prior to the IceCube-170922A alert*, Science 361, 147 — [DOI](https://doi.org/10.1126/science.aat2890)
- IceCube Collaboration (2022), *Evidence for neutrino emission from the nearby active galaxy NGC 1068*, Science 378, 538 — [DOI](https://doi.org/10.1126/science.abg3395)
- Kelner, S. R., & Aharonian, F. A. (2008), *Energy spectra of gamma-rays, electrons, and neutrinos produced at interactions of relativistic protons with low energy radiation*, Phys. Rev. D 78, 034013 — [arXiv:0803.0688](https://arxiv.org/abs/0803.0688)

## 🔗 Conexiones

- Sección de escritura destino: [[II.iii Radiación y Mecanismos de Emisión]]
- Viene de: [[II.ii Jets Relativistas]] — la población no térmica que este marco convierte en fotones y neutrinos
- Continúa en: [[III.i HAWC]] y [[III.iii IceCube]] — los instrumentos que detectan cada mensajero
- Conexión física central: [[Neutrinos y Rayos Gamma - Conexión Hadrónica]]
- Marco hermano: [[Neutrinos - Marco Teórico]]
- Caso empírico: [[SINTESIS -- Multi-messenger observations of a flaring blazar coincident with a high energy neutrino IceCube-170922A]]
- Seguimiento de correcciones: [[Escritura/Comentarios del Asesor]]
- Hub: [[XCRITURA]]
- ![[SED multimensajera - doble joroba.svg]]