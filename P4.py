#!/usr/bin/env python
# coding: utf-8

# ---
# 
# ## Universidad de Costa Rica
# ### Escuela de Ingeniería Eléctrica
# #### IE0405 - Modelos Probabilísticos de Señales y Sistemas
# 
# ---
# 
# * Estudiante: **Yeikko Valverde Jiménez**
# * Carné: **B47216**
# * Grupo: **1**
# 
# ---
# # `P4` - *Modulación digital IQ*
# 
# > La modulación digital es una de las aplicaciones del análisis de procesos estocásticos, y es parte de los sistemas digitales de comunicación. Este proyecto presenta una introdución a tópicos fundamentales de la ingeniería de comunicaciones para simular un sistema de transmisión de imágenes de baja resolución.
# 
# ---
# * Elaboración de nota teórica y demostración: **Jeaustin Sirias Chacón**, como parte de IE0499 - Proyecto Eléctrico: *Estudio y simulación de aplicaciones de la teoría de probabilidad en la ingeniería eléctrica*.
# * Revisión y edición: **Fabián Abarca Calderón**

# <span id="Chapter1"></span>
# 
# ## 1. - Una introducción a los sistemas de comunicaciones
# 
# La ingeniería de comunicaciones es la rama de la ciencia y la tecnología que busca establecer sistemas de transmisión de información entre emisores y receptores separados espacial o temporalmente. 
# 
# El modelo más generalizado de un sistema de comunicaciones incluye una fuente de información, un transmisor que codifica la información, un esquema de modulación que adapta la señal al medio, un canal de transmisión, un receptor que decodifica la información y un destino. El siguiente es un ejemplo de envío de imágenes: 
# 
# <img align='center' src='https://i.imgur.com/ZqQ9Psh.png' width ='450'/>
# 
# Un sistema de comunicaciones completo implica etapas altamente complejas y detalladas, tales como la multiplexación de múltiples usuarios, compresión de la información, así como corrección de datos erróneos. En esta actividad se estudiará solamente **los esquemas de modulación digital y el canal ruidoso**, que corresponde a dos de las etapas más relevantes.

# ### 1.1. - La modulación digital
# 
# Supóngase, por ejemplo, la tramisión inalámbrica de una imagen a largas distancias, ¿cómo es posible enviar sus pixeles (que se asumen como "algo digital") de un punto a otro, a través de un medio físico que es esencialmente "analógico"?
# 
# La *modulación* en ingeniería de comunicaciones consiste en depositar la información de una **señal moduladora** (fuente de información) en una **señal portadora** que está diseñada para el medio físico de transmisión. En el caso específico de la modulación *digital*, la fuente de información es, precisamente, *digital* (discreta en el tiempo y la amplitud).
# 
# <img align='center' src='https://i.imgur.com/eVnhbbG.png' width ='400'/>
# 
# La modulación sirve dos propósitos importantes:
# 
# * La señal portadora está **adaptada al medio** por el que se va a transmitir o a las tecnologías que se utilizan para ello. Por ejemplo: una señal de audio, en sus frecuencias originales, no puede ser transmitida eficientemente con antenas pequeñas y portables. Otro ejemplo: las señales digitales cuadradas (transiciones entre 0 y 1) sufrirían graves distorsiones y atenuación si se transmiten tal cual a grandes distancias por un conductor eléctrico.
# * Como la señal portadora puede modificarse a conveniencia, es posible crear esquemas de **acceso al medio** para múltiples usuarios. Por ejemplo: la modulación FM (*frequency modulation*) utiliza distintas franjas del espectro radioeléctrico para acomodar distintas emisiones ("radioemisoras").
# 
# La modulación digital presenta ventajas adicionales:
# 
# * Un esquema de modulación con técnicas de codificación apropiadas es capaz de reconstruir señales distorsionadas.
# * El flujo de información (bits por unidad de tiempo) es adaptativo, según las condiciones del canal.

# ### 1.2. - La demodulación
# 
# Si una señal ha atravesado un canal físico y se encuentra en el receptor: *¿cómo pueden los bits ser reconstruidos nuevamente a partir de la señal modulada $s(t)$ que fue recibida?*, *¿qué ocurrirá si esta señal fue distorsionada por cierto ruido durante su travesía por el medio de transmisión?* Estas son preguntas claves para el diseño de sistema de comunicación.
# 
# Algunas de las técnicas de procesamiento de señales para extraer la información de la señal son:
# 
# * Demodulación por **detección de envolvente**
# * Demodulación por **detección de energía**
# * Demodulación por **mínima distancia euclidiana**
# * Demodulación por **detección de lazo de seguimiento de fase**
# * Demodulación por **detección de fuerza en recepción**
# 
# ### 1.3. - Sobre canales ruidosos
# 
# > El ruido en un medio de transmisión generalmente se debe a variables físicas de comportamiento aleatorio. Por ejemplo: los fenómenos atmosféricos, las vibraciones, la interferencia entre señales y la temperatura.
# 
# En particular, los sistemas eléctricos y electrónicos son comúnmente afectados por el denominado **ruido aditivo blanco gaussiano** (AWGN, por las siglas en inglés de *Additive White Gaussian Noise*).
# 
# * Es **aditivo** porque la perturbación se "adhiere" o se "suma" a la señal viajera $s(t)$ al atravesar un determinado canal. De forma genérica, la señal resultante es la original más ruido, es decir, $\hat{s}(t) = s(t) + n(t)$.
# * Es **blanco** porque tiene una [densidad espectral de potencia](https://es.wikipedia.org/wiki/Densidad_espectral) aproximadamente constante dentro del ancho de banda de interés, es decir, está presente en todos los componentes de frecuencia. ¿Por qué entonces "blanco"?, podrían preguntarse ustedes.
# * Es **gaussiano** porque la función de densidad probabilística (PDF) de la **amplitud** del ruido es precisamente una distribución normal, con parámetros tales que la media es típicamente cero (lo que implica que tiene valores positivos y negativos) y la varianza tiene un valor relacionado con la potencia del ruido.
# 
# <img align='center' src='https://i.imgur.com/gtiM5SJ.png' width='850'/>

# ### 1.4 -  La relación señal-a-ruido
# 
# La relación señal-a-ruido (**SNR**, *Signal-to-Noise Ratio*) es una medida de la proporción entre la potencia $P_s$ de una señal $s(t)$ y la potencia $P_n$ del ruido $n(t)$ que la corrompe. Su magnitud suele ser especificada en decibel (dB). Un SNR alto indica que la presencia de una señal es más fuerte que la presencia del ruido, mientras que un SNR bajo indica lo contrario. Por ejemplo: el audio de un disco de vinilo tiene un SNR de unos 60 dB mientras que un disco compacto tiene 90 dB.
# 
# Su relación se expresa de la siguiente manera:
# 
# $$
# \mathrm{SNR}_{\mathrm{dB}} = 10\log(\mathrm{SNR}) = 10\log\left ( \frac{P_s}{P_n} \right )
# $$
# 
# Dado lo anterior, 60 dB implica una señal un millón de veces más potente que el ruido, y 90 dB mil millones de veces más grande. Hay que notar en el caso del audio que la percepción humana de la audición no es lineal, y por eso se prefiere una medida logarítmica como el dB.
# 
# ### 1.5 - Tasa de error binario
# 
# La tasa de error de bit (**BER**, *Bit Error Rate*) es una medida del error $p(\epsilon)$ que contiene un medio de transmisión no ideal (ruidoso). Según la definición estadística de la probabilidad, la probabilidad de ocurrencia de un suceso es la razón de los casos favorables entre los casos posibles:
# 
# $$
# \displaystyle
# p(\epsilon) = \frac{\text{bits fallidos}}{\text{bit totales}}
# $$
# 
# En sistemas de comunicaciones usuales, las tasas de error aceptables son de $10^{-5}$ o menores (un error por cada cien mil bits).

# ---
# ## 2. - Conceptos básicos del procesamiento de imágenes
# 
# 
# ### 2.1 - Los píxeles
# 
# Una imagen digital es un conjunto de pixeles (unidad mínima de color) en un plano. La sinergia de sus colores permite visualizar una imagen con sentido para el ojo humano.
# 
# <img align='center' src='https://i.imgur.com/ohBErgV.jpg' width='350'/>
# 
# ### 2.2 - El modelo de colores *RGB*
# 
# El modelo RGB (por las siglas en inglés de *Red, Green, Blue*) es el esquema de colores digitales más tradicional. Es "aditivo" en el sentido de que los colores se forman por la combinación de los componentes R, G, y B. Algunos ejemplos son: 
# 
# | Color             |                       Tripleta RGB                         | 
# |-----------------------|----------------------------------------------------------------|
# | <img src="https://i.pinimg.com/564x/2c/c6/2e/2cc62efc5998bc3bfdec089acf1e12c4.jpg" width="30"></img>                  |          `(255, 0, 0)`         |
# | <img src="https://i.pinimg.com/564x/ad/2f/b5/ad2fb5dd9b658483cb5c4f6120fe528b.jpg" width="30"></img> |          `(0, 0, 255)`         |
# | <img src="https://i.pinimg.com/564x/26/8b/2c/268b2c4f2742bfdc73dfbc8154ef5d11.jpg" width="30"></img> |          `(0, 0, 255)`         |
# | <img src="https://i.pinimg.com/564x/e5/be/78/e5be78c8312fd6ce650408abb87bd0ce.jpg" width="30"></img>                  |          `(0, 0, 0)`         |
# | <img src="https://i.pinimg.com/564x/a2/73/09/a27309683bfcaaf152864a0e19e79fd9.jpg" width="30"></img>                  |          `(0, 0, 128)`         |
# 
# A cada color se le denomina **canal**, de forma que un pixel RGB tiene tres canales. El modelo RGB es un esquema de colores discreto: cada canal tiene un rango de libertad entre 0 y 255, es decir, 256 tonos posibles por canal. La cantidad de memoria necesaria para almacenar un canal es de 8 bits, lo que significa que un pixel RGB tiene 8 $\times$ 3 = 24 bits. De aquí viene el comentario "*este televisor tiene 16 millones de colores, las imágenes se verán buenísimas*", un número obtenido por la regla de la multiplicación:
# 
# $$
# 256 \times 256 \times 256 = 2^{24} = 16\,777\,216 \,\text{combinaciones de colores}
# $$
# 
# ### 2.3 - El formato de compresión de imágenes *JPG*
# 
# Las imágenes digitales con formato JPG poseen un modelo de colores **RGB** y se trata de un "formato con compresión", en el que la imagen ha sido sometida a un proceso de reducción de información redundante para "aligerar" su peso en memoria.
# 
# Por ejemplo, la imagen mostrada anteriormente es de 198 $\times$ 89 pixeles, lo que implicaría un tamaño total de 198 $\times$ 89 $\times$ 24 bit / 8 = 52,87 kB, sin embargo el tamaño del archivo de la compresión es de solamente 8,58 kB. El nivel de compresión depende de cada imagen, pero alcanza típicamente la relación 10:1.

# ---
# 
# ## 3. - Simulando un sistema de comunicaciones 
# 
# Para utilizar los conocimientos adquiridos, se procederá a simular un **sistema de comunicaciones para la transmisión de imágenes de baja resolución**. 
# 
# El objetivo es transmitir la siguiente imagen (o cualquiera de baja resolución de su elección):
# 
# <img align='center' src='https://i.imgur.com/ohBErgV.jpg' width='250'/>
# 
# Las condiciones iniciales para el sistema de comunicaciones serán las siguientes:
# 
# * Una onda portadora banda base con **frecuencia $f_s$ = 5 kHz.**
# * Una frecuencia de muestreo de **20 muestras por período**.
# * Una relación señal/ruido de **5 dB**.
# 
# ### 3.1. - Funciones implementadas
# 
# A continuación se especificarán las funciones desarrolladas en la simulación del sistema (considerar que en telecomunicaciones se utiliza **Tx** para referirse a transmisión y **Rx** a recepción):
# 
# 1. `fuente_info(imagen)`: Extrae en un `array` de NumPy los pixeles contenidos en la imagen.
# * `rgb_a_bit(vector_pixel)`: Convierte los pixeles del 'array' de NumPy en una cadena `bits_Tx` continua de tamaño $(1 \times k)$, en donde $k$ es la cantidad total de bits de la imagen.
# * `modulador(bits_Rx, FS, MPP)`: Convierte la señal de información (arreglo de `bits_Tx`) en una señal modulada bajo un esquema **BPSK**.
# * `canal_ruidoso(senal_Tx, Pm, SNR)`: Simula un canala ruidoso con **AWGN** para `senal_Tx`.
# * `demodulador(senal_Rx, carrier, MPP)`: Demodula a `senal_Rx` (señal recibida) y determina los bits recibidos usando el criterio de demodulación por detección de energía.
# * `bits_a_rgb(bits_Rx, dims)`: Reconstruye los bits recibidos en `bits_Rx` en una imagen.
# 
# Las bibliotecas de Python de interés para este proyecto son:
# 
# ```python
# # Para manipular imágenes (Python Imaging Library)
# from PIL import Image
# 
# # Para manipular 'arrays' de pixeles y bits, señales y operaciones
# import numpy as np
# 
# # Para visualizar imágenes y señales
# import matplotlib.pyplot as plt
# 
# # Para medir el tiempo de simulación
# import time
# ```

# #### 3.1.1 - Extracción de los pixeles de una imagen (fuente de información)

# In[9]:


from PIL import Image
import numpy as np

def fuente_info(imagen):
    '''Una función que simula una fuente de
    información al importar una imagen y 
    retornar un vector de NumPy con las 
    dimensiones de la imagen, incluidos los
    canales RGB: alto x largo x 3 canales

    :param imagen: Una imagen en formato JPG
    :return: un vector de pixeles
    '''
    img = Image.open(imagen)
    
    return np.array(img)


# Es relevante considerar la forma de la salida de la función anterior.
# 
# ```python
# >>> pixeles = fuente_info('imagen.jpg')
# >>> print('Dimensiones: ', pixeles.shape, '\n')
# >>> print(pixeles)
# 
# Dimensiones: (300, 300, 3)
#     
# [[[132 123 118]
#   [133 124 119]
#   [136 127 122]
#   ...
#   [  8   2   2]
#   [ 10   1   4]
#   [ 10   1   2]]
# 
#  [[143 134 129]
#   [145 136 131]
#   [144 135 130]
#   ...
#   [ 13   3   1]
#   [ 15   5   3]
#   [ 15   7   5]]]
# ```
# 
# * Las dimensiones de la imagen elegida son (300, 300, 3); esto es su resolución: 300 px $\times$ 300 px. 
# * La tercera entrada del vector de dimensiones se refiere a las tres "capas" o canales R, G y B que componen aditivamente cada uno de los pixeles de esta imagen. 
# * En este caso específico hay $300 \times 300 = 90\,000$ pixeles por canal. 
# * ¿Puede estimarse cuántos bits tiene la imagen? Puesto que un solo canal tiene 8 bits de profundidad (256 niveles) por pixel, entonces la imagen en transmisión tiene, *antes de la compresión*:
# 
# $$
# 90\,000 \times 8 \times 3 = 2\,160\,000 \,\text{bit}
# $$

# #### 3.1.2. - Codificación de pixeles a una base binaria (bits)

# In[10]:


import numpy as np

def rgb_a_bit(array_imagen):
    '''Convierte los pixeles de base 
    decimal (de 0 a 255) a binaria 
    (de 00000000 a 11111111).

    :param imagen: array de una imagen 
    :return: Un vector de (1 x k) bits 'int'
    '''
    # Obtener las dimensiones de la imagen
    x, y, z = array_imagen.shape
    
    # Número total de elementos (pixeles x canales)
    n_elementos = x * y * z

    # Convertir la imagen a un vector unidimensional de n_elementos
    pixeles = np.reshape(array_imagen, n_elementos)

    # Convertir los canales a base 2
    bits = [format(pixel, '08b') for pixel in pixeles]
    bits_Rx = np.array(list(''.join(bits)))
    
    return bits_Rx.astype(int)


# #### 3.1.3. - Esquema de modulación BPSK
# 
# El esquema de modulación o "codificación" por desplazamiento de fase o [PSK](https://es.wikipedia.org/wiki/Modulaci%C3%B3n_por_desplazamiento_de_fase) (de *phase shift keying*) consiste, como lo sugiere su nombre, en **variar la fase** de la onda portadora $c(t)$ a partir grupos de bits codificados en símbolos discretos. El caso **BPSK** hace referencia a la modulación bi-fase, con dos símbolos disponibles. En general hay $M = 2^k$ símbolos, con $k$ la cantidad de bits para representarlos. Por tanto, con BPSK y despejando para $k$ con $M = 2$:
# 
# $$
# \log_2(2) = 1 \quad \text{bit/símbolo}
# $$
# 
# Puede haber un `0` o un `1` por cada símbolo. Puesto que el esquema se basa en el desplazamiento de fase entonces es conveniente asignar valores angulares de fase en radianes, como 0 y $\pi$:
# 
# $$
# s(t) = A_c \cdot \sin(2\pi f_c t - \theta_c), \quad \text{con}\, \theta_c \in \{0, \pi\}
# $$
# 
# Por la identidad trigonométrica $\sin(\alpha - \pi) = \sin(-\alpha) = -\sin(\alpha)$, implícitamente $s(t)$ puede manipular su desplazamiento de fase desde la óptica de la amplitud $A_c$:
# 
# $$
# A_c= 
# \begin{cases}
#              1, &   \text{si} \quad \theta_c = 0 \\
#              -1, &  \text{si} \quad \theta_c = \pi \\
# \end{cases}
# $$
# 
# A través de este "artificio" la modulación **BPSK** (pero solo BPSK) pasa de ser un asunto de fases a un tema de amplitud. Esto simplifica en gran medida la programación del esquema, puesto que si el bit entrante es cero, entonces la fase de la portadora se invierte con solo tomar $A_c = -1$. En el caso contrario (si el bit entrante es un uno), entonces $A_c = 1$ y ya no es necesario lidiar con las fases en términos del ángulo $\theta_c$. A continuación se muestra una implementación de esta modulación.

# In[11]:


import numpy as np

def modulador(bits, fc, mpp):
    '''Un método que simula el esquema de 
    modulación digital BPSK.

    :param bits: Vector unidimensional de bits
    :param fc: Frecuencia de la portadora en Hz
    :param mpp: Cantidad de muestras por periodo de onda portadora
    :return: Un vector con la señal modulada
    :return: Un valor con la potencia promedio [W]
    :return: La onda portadora c(t)
    :return: La onda cuadrada moduladora (información)
    '''
    # 1. Parámetros de la 'señal' de información (bits)
    N = len(bits) # Cantidad de bits

    # 2. Construyendo un periodo de la señal portadora c(t)
    Tc = 1 / fc  # periodo [s]
    t_periodo = np.linspace(0, Tc, mpp)  # mpp: muestras por período
    portadora = np.sin(2*np.pi*fc*t_periodo)

    # 3. Inicializar la señal modulada s(t)
    t_simulacion = np.linspace(0, N*Tc, N*mpp) 
    senal_Tx = np.zeros(t_simulacion.shape)
    moduladora = np.zeros(t_simulacion.shape)  # (opcional) señal de bits
 
    # 4. Asignar las formas de onda según los bits (BPSK)
    for i, bit in enumerate(bits):
        if bit == 1:
            senal_Tx[i*mpp : (i+1)*mpp] = portadora
            moduladora[i*mpp : (i+1)*mpp] = 1
        else:
            senal_Tx[i*mpp : (i+1)*mpp] = portadora * -1
            moduladora[i*mpp : (i+1)*mpp] = 0
    
    # 5. Calcular la potencia promedio de la señal modulada
    P_senal_Tx = (1 / (N*Tc)) * np.trapz(pow(senal_Tx, 2), t_simulacion)
    
    return senal_Tx, P_senal_Tx, portadora, moduladora  


# #### 3.1.4. - Construcción de un canal con ruido AWGN

# In[12]:


import numpy as np

def canal_ruidoso(senal_Tx, Pm, SNR):
    '''Un bloque que simula un medio de trans-
    misión no ideal (ruidoso) empleando ruido
    AWGN. Pide por parámetro un vector con la
    señal provieniente de un modulador y un
    valor en decibelios para la relación señal
    a ruido.

    :param senal_Tx: El vector del modulador
    :param Pm: Potencia de la señal modulada
    :param SNR: Relación señal-a-ruido en dB
    :return: La señal modulada al dejar el canal
    '''
    # Potencia del ruido generado por el canal
    Pn = Pm / pow(10, SNR/10)

    # Generando ruido auditivo blanco gaussiano (potencia = varianza)
    ruido = np.random.normal(0, np.sqrt(Pn), senal_Tx.shape)

    # Señal distorsionada por el canal ruidoso
    senal_Rx = senal_Tx + ruido

    return senal_Rx


# #### 3.1.5. - Esquema de demodulación

# In[13]:


import numpy as np

def demodulador(senal_Rx, portadora, mpp):
    '''Un método que simula un bloque demodulador
    de señales, bajo un esquema BPSK. El criterio
    de demodulación se basa en decodificación por 
    detección de energía.

    :param senal_Rx: La señal recibida del canal
    :param portadora: La onda portadora c(t)
    :param mpp: Número de muestras por periodo
    :return: Los bits de la señal demodulada
    '''
    # Cantidad de muestras en senal_Rx
    M = len(senal_Rx)

    # Cantidad de bits (símbolos) en transmisión
    N = int(M / mpp)

    # Vector para bits obtenidos por la demodulación
    bits_Rx = np.zeros(N)

    # Vector para la señal demodulada
    senal_demodulada = np.zeros(senal_Rx.shape)

    # Pseudo-energía de un período de la portadora
    Es = np.sum(portadora * portadora)

    # Demodulación
    for i in range(N):
        # Producto interno de dos funciones
        producto = senal_Rx[i*mpp : (i+1)*mpp] * portadora
        Ep = np.sum(producto) 
        senal_demodulada[i*mpp : (i+1)*mpp] = producto

        # Criterio de decisión por detección de energía
        if Ep > 0:
            bits_Rx[i] = 1
        else:
            bits_Rx[i] = 0

    return bits_Rx.astype(int), senal_demodulada


# #### 3.1.6. - Reconstrucción de la imagen

# In[14]:


import numpy as np

def bits_a_rgb(bits_Rx, dimensiones):
    '''Un blque que decodifica el los bits
    recuperados en el proceso de demodulación

    :param: Un vector de bits 1 x k 
    :param dimensiones: Tupla con dimensiones de la img.
    :return: Un array con los pixeles reconstruidos
    '''
    # Cantidad de bits
    N = len(bits_Rx)

    # Se reconstruyen los canales RGB
    bits = np.split(bits_Rx, N / 8)

    # Se decofican los canales:
    canales = [int(''.join(map(str, canal)), 2) for canal in bits]
    pixeles = np.reshape(canales, dimensiones)

    return pixeles.astype(np.uint8)


# ### 3.2. - Simulación del sistema de comunicaciones con modulación BPSK
# 
# **Nota**: esta simulación tarda un poco y quizá hay que hacerla dos veces.

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import time

# Parámetros
fc = 5000  # frecuencia de la portadora
mpp = 20   # muestras por periodo de la portadora
SNR = -5   # relación señal-a-ruido del canal

# Iniciar medición del tiempo de simulación
inicio = time.time()

# 1. Importar y convertir la imagen a trasmitir
imagen_Tx = fuente_info('arenal.jpg')
dimensiones = imagen_Tx.shape

# 2. Codificar los pixeles de la imagen
bits_Tx = rgb_a_bit(imagen_Tx)

# 3. Modular la cadena de bits usando el esquema BPSK
senal_Tx, Pm, portadora, moduladora = modulador(bits_Tx, fc, mpp)

# 4. Se transmite la señal modulada, por un canal ruidoso
senal_Rx = canal_ruidoso(senal_Tx, Pm, SNR)

# 5. Se desmodula la señal recibida del canal
bits_Rx, senal_demodulada = demodulador(senal_Rx, portadora, mpp)

# 6. Se visualiza la imagen recibida 
imagen_Rx = bits_a_rgb(bits_Rx, dimensiones)
Fig = plt.figure(figsize=(10,6))

# Cálculo del tiempo de simulación
print('Duración de la simulación: ', time.time() - inicio)

# 7. Calcular número de errores
errores = sum(abs(bits_Tx - bits_Rx))
BER = errores/len(bits_Tx)
print('{} errores, para un BER de {:0.4f}.'.format(errores, BER))

# Mostrar imagen transmitida
ax = Fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(imagen_Tx)
ax.set_title('Transmitido')

# Mostrar imagen recuperada
ax = Fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(imagen_Rx)
ax.set_title('Recuperado')
Fig.tight_layout()

plt.imshow(imagen_Rx)


# In[16]:


import matplotlib.pyplot as plt

# Visualizar el cambio entre las señales
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, sharex=True, figsize=(14, 7))

# La onda cuadrada moduladora (bits de entrada)
ax1.plot(moduladora[0:600], color='r', lw=2) 
ax1.set_ylabel('$b(t)$')

# La señal modulada por BPSK
ax2.plot(senal_Tx[0:600], color='g', lw=2) 
ax2.set_ylabel('$s(t)$')

# La señal modulada al dejar el canal
ax3.plot(senal_Rx[0:600], color='b', lw=2) 
ax3.set_ylabel('$s(t) + n(t)$')

# La señal demodulada
ax4.plot(senal_demodulada[0:600], color='m', lw=2) 
ax4.set_ylabel('$b^{\prime}(t)$')
ax4.set_xlabel('$t$ / milisegundos')
fig.tight_layout()
plt.show()


# ### 3.3. - Modulación IQ
# 
# Obsérvese que en la modulación BPSK anterior existe una única portadora (*carrier*) sinusoidal, dada por
# 
# $$
# c(t) = A_c \sin(2\pi f_c t - \theta_c)
# $$
# 
# La propiedad de la **ortogonalidad** entre las funciones $\sin(\omega t)$ y $\cos(\omega t)$ permite utilizar dos portadoras en lugar de una, de forma tal que es posible crear una señal modulada del tipo:
# 
# $$
# s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
# $$
# 
# Esta señal ocupa el mismo ancho de banda que una sola portadora sinusoidal, pero puede transportar el doble de la información, codificada en $A_1$ y $A_2$. Debido a que las ondas seno y coseno están separadas por un desfase de 90 grados, a este tipo de modulación se le llama "en fase" (**I**, *in phase*) y "en cuadratura" (**Q**, *quadrature*), o **modulación IQ**.
# 
# #### 3.3.1. - Ortogonalidad
# 
# La prueba de ortogonalidad de dos funciones del tiempo está dada por el producto interno:
# 
# $$
# \begin{aligned}
# (f * g) (t) & = \langle f(t), g(t)\rangle \\
# & = \int f(t) g(t) \, \mathrm{d}t            
# \end{aligned}
# $$
# 
# Y en el caso de las dos portadoras sinusoidales:
# 
# $$
# \begin{aligned}
# (f * g) (t) & = \langle f(t), g(t)\rangle \\
# & = \int f(t) g(t) \, \mathrm{d}t \\
# & = \int \cos(2\pi f_c t) \, \sin(2\pi f_c t) \, \mathrm{d}t \\
# & = 0 
# \end{aligned}
# $$
# 
# > Podría decirse, coloquialmente, que las portadoras viajan "juntas pero no revueltas". 
# 
# Este resultado es útil para la *demodulación coherente (en fase)* de señales IQ, porque permite "separar" una portadora de otra.
# 
# #### 3.3.2. - Modulación QPSK
# 
# La modulación BPSK tiene dos símbolos posibles (`0`, `1`) lo que implica un bit $b$ por símbolo, mientras que la modulación QPSK (*Quadrature Phase-Shift Keying*) tiene cuatro símbolos posibles (`00`, `01`, `10`, `11`), con dos bits $b_1 b_2$ por símbolo. La codificación para un símbolo $b_1 b_2$ es ahora:
# 
# $$
# s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
# $$
# 
# donde
# 
# $$
# A_1 = 
# \begin{cases}
#              -1, &   \text{si} \quad b_1 = 0 \\
#              1, &  \text{si}   \quad b_1 = 1 \\
# \end{cases}
# $$
# 
# y
# 
# $$
# A_2 = 
# \begin{cases}
#              -1, &   \text{si} \quad b_2 = 0 \\
#               1, &   \text{si} \quad b_2 = 1 \\
# \end{cases}
# $$
# 
# <img src="https://www.analog.com/-/media/analog/en/landing-pages/technical-articles/low-power-iq-modulator-for-digital-communications/iqmodulator.png?h=270&hash=868F3CDB85D7842D27627F7A12099156E9729935&la=en" width="400">
# 
# Si se grafica la amplitud $A_1$ y $A_2$ de cada portadora en una gráfica donde el eje $x$ representa al coseno (en fase, $I$) y el eje $y$ al seno (en cuadratura, $Q$), se obtiene lo que se conoce como un "diagrama de constelación" de la modulación:
# 
# <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/QPSK_Gray_Coded.svg/800px-QPSK_Gray_Coded.svg.png' width='200'>
# 
# Ahí es posible verificar la correspondencia de los bits $b_1 b_2$ (`00`, `01`, `10`, `11`) con los puntos de la constelación.
# 
# > La modulación QPSK es utilizada en el estándar Wi-Fi IEEE 802.11 (una de sus posibles modulaciones), en comunicaciones satelitales, y en 5G, entre otros.
# 
# #### 3.3.3. - Modulación QAM
# 
# La modulación de amplitud en cuadratura (**QAM**, *Quadrature Amplitude Modulation*) es otro tipo de modulación IQ que ahora utiliza más posibles amplitudes de las dos portadoras para crear una constelación como la siguiente:
# 
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/16QAM_Gray_Coded.svg/1280px-16QAM_Gray_Coded.svg.png" width="250">
# 
# en donde se aprecian dos valores positivos y dos valores negativos para cada portadora. Este es el caso 16-QAM, en tanto que tiene 16 símbolos de 4 bits cada uno ($2^4 = 16$).
# 
# La codificación para un símbolo $b_1 b_2 b_3 b_4$ es:
# 
# $$
# s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
# $$
# 
# donde
# 
# $$
# A_1 = 
# \begin{cases}
#              -3, &   \text{si} \quad b_1 b_2 = 00 \\
#              -1, &   \text{si} \quad b_1 b_2 = 01 \\
#              1, &  \text{si}   \quad b_1 b_2 = 11 \\
#              3, &  \text{si}   \quad, b_1 b_2 = 10 \\
# \end{cases}
# $$
# 
# y
# 
# $$
# A_2 = 
# \begin{cases}
#              3, &   \text{si} \quad b_3 b_4 = 00 \\
#              1, &   \text{si} \quad b_3 b_4 = 01 \\
#              -1, &  \text{si}   \quad b_3 b_4 = 11 \\
#              -3, &  \text{si}   \quad b_3 b_4 = 10 \\
# \end{cases}
# $$
# 
# > La modulación QAM es también utilizada en el estándar Wi-Fi IEEE 802.11 de forma adaptativa, por lo que puede ir desde 16-QAM (4 bits/símbolo) hasta 512-QAM (9 bits/símbolo) cuando las condiciones del canal son óptimas.

# ---
# ## 4. - Asignaciones del proyecto
# 
# ### 4.1. - Modulación 16-QAM
# 
# * (50%) Realice una simulación del sistema de comunicaciones como en la sección 3.2., pero utilizando una modulación **16-QAM** en lugar de una modulación BPSK. Deben mostrarse las imágenes enviadas y recuperadas y las formas de onda.
# 
# ### 4.2. - Estacionaridad y ergodicidad
# 
# * (30%) Realice pruebas de estacionaridad y ergodicidad a la señal modulada `senal_Tx` y obtenga conclusiones sobre estas.
# 
# ### 4.3. - Densidad espectral de potencia
# 
# * (20%) Determine y grafique la densidad espectral de potencia para la señal modulada `senal_Tx`.
# 
# \begin{equation}
# \displaystyle
# \mathcal{S}_{XX}(\omega) = \lim_{T \rightarrow \infty}\frac{E[\vert X_{T}(\omega) \vert^2]}{2T}
# \end{equation}

# In[17]:


# 4.1. - Modulación 16-QAM

import numpy as np  # Se importa la librería numpy
import matplotlib.pyplot as plt  # Se importa la libreía matplotlib
import time  # Se importa la librería time


def modulador_n(bits, fc, mpp):

    # 1. Parámetros de la 'señal' de información (bits)
    N = len(bits) # Cantidad de bits
    c = np.array(bits).reshape(105732, 4).tolist()  # Obtención de las parejas de bits
    newListC = []
    newListD = []
    newListE = []

    for element in c:
        newListC.append(str(element[0])+str(element[1])+str(element[2])+str(element[3]))
            
    for element in newListC:
        newListD.append(element[0]+element[1])
        newListE.append(element[2]+element[3])
        
    
    # 2. Construyendo un periodo de la señal portadora c(t)
    Tc = 1 / fc  # periodo [s]
    t_periodo = np.linspace(0, Tc, mpp)  # mpp: muestras por período
    port_I = np.sin(2*np.pi*fc*t_periodo)  # Portadora I
    port_Q = np.cos(2*np.pi*fc*t_periodo)  # Portadora Q
    

    # 3. Inicializar la señal modulada s(t)
    t_simulacion = np.linspace(0, N*Tc, N*mpp) 
    senal_Tx_I = np.zeros(t_simulacion.shape)
    mod_I = np.zeros(t_simulacion.shape)  # Moduladora I
    senal_Tx_Q = np.zeros(t_simulacion.shape)
    mod_Q = np.zeros(t_simulacion.shape)  # Moduladora Q
    

    # 4. Asignar las formas de onda según los bits (16-QAM)
    for i, element in enumerate(newListD):
        if element == '00':
            senal_Tx_I[i*mpp : (i+1)*mpp] = port_I*-3
            mod_I[i*mpp : (i+1)*mpp] = 0
        elif element == '01':
            senal_Tx_I[i*mpp : (i+1)*mpp] = port_I*-1
            mod_I[i*mpp : (i+1)*mpp] = 0
        elif element == '11':
            senal_Tx_I[i*mpp : (i+1)*mpp] = port_I
            mod_I[i*mpp : (i+1)*mpp] = 1
        else:
            senal_Tx_I[i*mpp : (i+1)*mpp] = port_I*3  
            mod_I[i*mpp : (i+1)*mpp] = 1

    for i, element in enumerate(newListE):
        if element == '00':
            senal_Tx_Q[i*mpp : (i+1)*mpp] = port_Q*3
            mod_Q[i*mpp : (i+1)*mpp] = 1
        elif element == '01':
            senal_Tx_Q[i*mpp : (i+1)*mpp] = port_Q
            mod_Q[i*mpp : (i+1)*mpp] = 1
            
        elif element == '11':
            senal_Tx_Q[i*mpp : (i+1)*mpp] = port_Q*-1
            mod_Q[i*mpp : (i+1)*mpp] = 0
        else:
            senal_Tx_Q[i*mpp : (i+1)*mpp] = port_Q*-3
            mod_Q[i*mpp : (i+1)*mpp] = 0
    
    senal_Tx = senal_Tx_Q + senal_Tx_I  # Se suman las señales
    
    
    # 5. Calcular la potencia promedio de la señal modulada
    P_I = (1 / (N*Tc)) * np.trapz(pow(senal_Tx_I, 2), t_simulacion)
    P_Q = (1 / (N*Tc)) * np.trapz(pow(senal_Tx_Q, 2), t_simulacion)

    return senal_Tx_I, P_I, port_I, mod_I, senal_Tx_Q, P_Q, port_Q, mod_Q, senal_Tx


# Función para demodulación: 
def demodulador_n(senal_Rx_I, senal_Rx_Q, port_I, port_Q, mpp):
    
    # Cantidad de muestras en senal_Rx_I
    M = len(senal_Rx_I)

    # Cantidad de bits (símbolos) en transmisión
    N = int(M / (2*mpp))
    
    # Vectores para bits obtenidos por la demodulación
    bits_Rx_I = np.zeros(N)
    bits_Rx_Q = np.zeros(N)

    # Vectores para la señal demodulada
    senal_demod_I = np.zeros(M)
    senal_demod_Q = np.zeros(M)

    # Pseudo-energía de un período de la portadora
    EsI = np.sum(port_I**2)
    EsQ = np.sum(port_Q**2)

    # Demodulación
    for i in range(N):
    # Producto interno de dos funciones
        producto_I = senal_Rx_I[i*mpp : (i+1)*mpp] * port_I
        EpI = np.sum(producto_I) 
        senal_demod_I[i*mpp : (i+1)*mpp] = producto_I

    # Criterio de decisión por detección de energía
    if EpI > 0:
        bits_Rx_I[i] = 1
    else:
        bits_Rx_I[i] = 0
        
    for i in range(N):
        # Producto interno de dos funciones
        producto_Q = senal_Rx_Q[i*mpp : (i+1)*mpp] * port_Q
        EpQ = np.sum(producto_Q) 
        senal_demod_Q[i*mpp : (i+1)*mpp] = producto_Q

        # Criterio de decisión por detección de energía
        if EpQ > 0:
            bits_Rx_Q[i] = 1
        else:
            bits_Rx_Q[i] = 0
            
    senal_demodulada = senal_demod_Q + senal_demod_I  # Se suman las señales
            
    bits_lista = []
        
    # Se convierte en un array de números enteros:
    for i in range(len(bits_Rx_I)):
        bits_lista.append(bits_Rx_I[i])
        bits_lista.append(bits_Rx_Q[i])

    bits_lista = [int(a) for a in bits_lista] #int para convertir a enteros
    bits_Rx = np.array(bits_lista)
        
    return bits_Rx.astype(int), senal_demodulada



# In[18]:


# Simulación:

# Parámetros
fc = 5000  # frecuencia de la portadora
mpp = 20   # muestras por periodo de la portadora
SNR = 5   # relación señal-a-ruido del canal

# Iniciar medición del tiempo de simulación
inicio = time.time()

# 1. Importar y convertir la imagen a trasmitir
imagen_Tx = fuente_info('arenal.jpg')
dimensiones = imagen_Tx.shape

# 2. Codificar los pixeles de la imagen
bits_Tx = rgb_a_bit(imagen_Tx)

# 3. Modular la cadena de bits usando 16-QAM
senal_Tx_Q, P_Q, port_Q, mod_Q, senal_Tx_I, P_I, port_I, mod_I, senal_Tx = modulador_n(bits_Tx, fc, mpp)
senal_Tx_QAM = senal_Tx

# 4. Se transmite la señal modulada, por un canal ruidoso
senal_Rx_I = canal_ruidoso(senal_Tx_I, P_I, SNR)
senal_Rx_Q = canal_ruidoso(senal_Tx_Q, P_Q, SNR)
senal_Rx = senal_Rx_Q + senal_Rx_I

# 5. Se desmodula la señal recibida
bits_Rx, senal_demodulada = demodulador_n(senal_Rx_I, senal_Rx_Q, port_I, port_Q, mpp)

# 6. Se visualiza la imagen recibida 
imagen_Rx = bits_a_rgb(bits_Rx, dimensiones)
Fig = plt.figure(figsize=(10,6))

# 7. Calcular número de errores
errores = sum(abs(bits_Tx - bits_Rx))
BER = errores/len(bits_Tx)

#Print resultados:
print('Cantidad original de bits: ', len(bits_Tx))
print('Cantidad luego del proceso: ', len(bits_Rx))
print('Duración de la simulación: ', time.time() - inicio)
print('{} errores, para un BER de {:0.4f}.'.format(errores, BER))

# Mostrar imagen transmitida
ax = Fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(imagen_Tx)
ax.set_title('Transmitido')

# Mostrar imagen recuperada
ax = Fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(imagen_Rx)
ax.set_title('Recuperado')
Fig.tight_layout()

plt.imshow(imagen_Rx)


# In[20]:


import matplotlib.pyplot as plt

# Visualizar el cambio entre las señales
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, sharex=True, figsize=(14, 7))

# La onda cuadrada moduladora (bits de entrada)
ax1.plot(mod_I[0:600], color='r', lw=2) 
ax1.set_ylabel('$b(t)$')

# La señal modulada por 16-QAM
ax2.plot(senal_Tx[0:600], color='g', lw=2) 
ax2.set_ylabel('$s(t)$')

# La señal modulada al dejar el canal
ax3.plot(senal_Rx[0:600], color='b', lw=2) 
ax3.set_ylabel('$s(t) + n(t)$')

# La señal demodulada
ax4.plot(senal_demodulada[0:600], color='m', lw=2) 
ax4.set_ylabel('$b^{\prime}(t)$')
ax4.set_xlabel('$t$ / milisegundos')
fig.tight_layout()
plt.show()


# In[21]:


# 4.3. - Densidad espectral de potencia

from scipy import fft

# Transformada de Fourier
senal_f = fft(senal_Tx)

# Muestras de la señal
Nm = len(senal_Tx)

# Número de símbolos (198 x 89 x 8 x 3)
Ns = Nm // mpp

# Tiempo del símbolo = periodo de la onda portadora
Tc = 1 / fc

# Tiempo entre muestras (período de muestreo)
Tm = Tc / mpp

# Tiempo de la simulación
T = Ns * Tc

# Espacio de frecuencias
f = np.linspace(0.0, 1.0/(2.0*Tm), Nm//2)

# Gráfica
plt.plot(f, 2.0/Nm * np.power(np.abs(senal_f[0:Nm//2]), 2))
plt.xlim(0, 20000)
plt.grid()
plt.show()


# ---
# 
# ### Universidad de Costa Rica
# #### Facultad de Ingeniería
# ##### Escuela de Ingeniería Eléctrica
# 
# ---
