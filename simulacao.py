# %%

import numpy as np
import matplotlib.pyplot as plt



# %%

# TODO: Tentar distribuição normal
# TODO: Tentar outros parametros
# TODO: Criar média das demandas individuais e desenhar curva de demanda

# %%

"""
Di = a - bP
b = em função do preço
a >> b

Demanda Individual é igual a a - bP

a e b são parametros individuais que são tirados de uma distribuição uniforme
"""

numero_agentes = 1000
parametro_a = (400, 10)
parametro_b = (1, 1.0)
parametro_preco = (10, 400, 2)

# Variável a começa em 0 e pode ir até 10 (o que nosso consumidor está disposto a pagar naturalmente)
# a_s = np.random.uniform(low=parametro_a[0], high=parametro_a[1], size=numero_agentes)
a_s = np.random.normal(loc=parametro_a[0], scale=parametro_a[1], size=numero_agentes)

# Variável b começa em 100, isso mostra inclinação para comprar um produto
# b_s = np.random.uniform(low=parametro_b[0], high=parametro_b[1], size=numero_agentes)
b_s = np.random.normal(loc=parametro_b[0], scale=parametro_b[1], size=numero_agentes)

# Preços alterando de 10 a 1000 steps de 5 (200 steps)
P_s = np.arange(parametro_preco[0], parametro_preco[1], parametro_preco[2])

# Guardamos as demandas individuais em uma lista de listas
demandas = np.zeros(shape=(numero_agentes, len(P_s)))

# Para cada agente, calculamos as demandas individuais para cada preço
for consumidor in range(numero_agentes):
    # print(f'Iniciando consumidor {consumidor}')
    for i, p in enumerate(P_s):
        # print(f'D_i_{consumidor} = {a_s[consumidor] - b_s[consumidor] * p}')
        D_i = a_s[consumidor] - b_s[consumidor] * p
        if D_i >= 0:
            demandas[consumidor, i] = D_i
    

medias_demanda = np.mean(demandas, axis=0)

plota_consumidores = False

fig, ax = plt.subplots(figsize=(10,10))
if plota_consumidores:
    for consumidor in range(numero_agentes):
        plt.plot(P_s, demandas[consumidor], alpha=0.3)
plt.xlabel('Preço')
plt.ylabel('Demanda')
plt.title(f'Preço por Demanda Individual Dist Normal\na={parametro_a}|b={parametro_b}|P={parametro_preco}')
plt.plot(P_s, medias_demanda, marker='*', color='red', linewidth=5, alpha=1, figure=fig)
plt.savefig('demanda9.jpg')

# %%

# plt.hist(np.random.normal(loc=500, scale=100, size=1000))
