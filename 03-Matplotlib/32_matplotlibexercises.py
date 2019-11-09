# -*- coding: utf-8 -*-
"""32-MatplotlibExercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gOSConzQcin1nRAx_545QcKQS6K81Ugs

# Exercícios

Siga as instruções para recriar os gráficos usando estes dados:

## Dados
"""

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

"""**Importe matplotlib.pyplot como plt e defina% matplotlib inline se você estiver usando o bloco de anotações jupyter. Que comando você usa se não estiver usando o notebook jupyter**"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

"""## Exercício 1

**Siga estas etapas:**
* **Crie um objeto de figura chamado fig usando plt.figure ()**
* **Use add_axes para adicionar um eixo à tela da figura em [0,0,1,1]. Chame esse novo eixo de eixo.**
* **Plote (x, y) nesses eixos e defina os rótulos e títulos para coincidir com o gráfico abaixo:**
"""

fig = plt.figure()

eixo = fig.add_axes([0,0,1,1])
eixo.set_title('title')
eixo.set_xlabel('x')
eixo.set_ylabel('y')

eixo.plot(x,y)

"""## Exercício 2
**Crie um objeto de figura e coloque dois eixos nele, ax1 e ax2. Localizado em [0,0,1,1] e [0,2,0,5, .2, .2], respectivamente.**
"""

figura = plt.figure()

ax1 = figura.add_axes([0,0,1,1])
ax2 = figura.add_axes([0.2,0.5,.2,.2])

"""**Agora plote (x, y) nos dois eixos. E chame seu objeto de figura para mostrá-lo.**"""

figura = plt.figure()

ax1 = figura.add_axes([0,0,1,1])
ax2 = figura.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,y)
ax2.plot(x,y)

"""## Exercício 3

**Crie o gráfico abaixo adicionando dois eixos a um objeto de figura em [0,0,1,1] e [0,2,0,5, .4, .4]**
"""

figura = plt.figure()
ax0 = figura.add_axes([0,0,1,1])
ax1 = figura.add_axes([0.2,0.5,.4,.4])

ax0.set_xlabel('X')
ax0.set_ylabel('Z')

ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_ylim(30,50)
ax1.set_xlim(20,22)

ax0.plot(x,z)
ax1.plot(x,y)

"""**Agora use as matrizes x, ye z para recriar o gráfico abaixo. Observe os limites xlimits e y no gráfico inserido:**"""

figura = plt.figure()

ax3 = figura.add_axes([0,0,1,1])
ax4 = figura.add_axes([0.2,0.5,.4,.4])

"""## Exercício 4

**Use plt.subplots (nrows = 1, ncols = 2) para criar o gráfico abaixo.**
"""

fig,axes = plt.subplots(nrows=1,ncols=2)

"""**Agora plote (x, y) e (x, z) nos eixos. Brinque com a largura de linha e o estilo**"""

fig,axes = plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y,color='blue',lw="5",ls="--")
axes[1].plot(x,z,color='red',lw="3")

"""**Veja se você pode redimensionar o gráfico adicionando o argumento figsize () em plt.subplots () está copiando e colando o código anterior.**"""

fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,3))

axes[0].plot(x,y,color='blue',lw="5",ls="--")
axes[1].plot(x,z,color='red',lw="3")