# %%

import numpy as np
import scipy
import matplotlib.pyplot as plt

# %%

# Como funciona a simulação via questionario:
# 1. Temos uma população de consumidores
# 2. Temos uma demanda inicial ficticia
# 3. Para cada consumidor, perguntamos quanto ele compraria do produto por aquele preço
# 4. D_i = a - bP, onde a e b são parametros individuais que são tirados de uma distribuição X e P são os diferentes preços

D_T = 400

preco = np.arange(100, 1, -10)
demanda = np.arange(1,11)
plt.plot(demanda, preco)
plt.show()

# Preço 1
b1 = np.random.normal(0, 1, 1)

# Preço 1
b2 = np.random.normal(0, 1, 1)

# Preço 1
b3 = np.random.normal(0, 1, 1)

P = [10, 100, 1000]
b = np.absolute([b1, b2, b3])

demandas = []

# FIX: Precisamos de um loop por preço e por demanda individual
for i in range(len(b)):
    D_i = np.array([])
    for p in P:
        d_i = 100 - b[i] * p
        np.append(D_i, d_i)
    D_i[D_i > D_T] = 400
    D_i[D_i <= 0] = 0
    demandas.append(D_i)

demandas

# %%

# Plotar as demandas individuais baseadas no preço
plt.plot(demandas[0], P)

b


# %%

# Essa é a demanda "assumida", que avisamos para todos os consumidores
# Demanda se mantém constante entre cada rodada
D_T = 400

# Total de consumidores que vão responder o survey
numero_consumidores = 1000

# Preços do produto, pulando de 2 em 2
precos = np.arange(10, 100, 60)

# Fator pessoal da populacao
fp = np.random.normal(0, 1, numero_consumidores)
fp = (fp - np.min(fp)) / (np.max(fp) - np.min(fp))


# A ideia é que para cada preço, a demanda seja fixa
# E nossos consumidores falem quanto que eles comprariam de fato

# Ao final do questionário N, somamos a demanda individual de cada consumidor
# Para o questionário N+1, usamos como demanda do mercado, o valor de N

# TODO: Verificar texto abaixo 
# A demanda do questionário N+1 sempre >= ao questionário N

# A demanda individual é em função de demanda total do mercado
# D_i = (1 - (P / D_T) * fp)

# Um consumidor nunca vai comprar mais do que o total de itens em demanda
# Logo, nosso limite é D_T (demanda total)
# Mas ele também pode não querer comprar nada caso o preço fique muito alto


# %%

# Começamos a simulação

# Sempre vamos guardar o resultado do último survey
D_i_ultimo = 0

# Para cada preço p, vamos rodar N surveys
for P in precos:

    # Rodamos N surveys
    for survey in range(100):

        # Perguntamos para cada individuo, quanto ele compraria (rodar formula)
        D_is = np.sum(D_T * (1 - (P / D_T) * fp))
        
        print(f'Survey {survey} com D_is={D_is:.0f}')
        
        if D_is == D_i_ultimo:
            print(f'Alcançamos equilíbrio no survey {survey} com demanda {D_is}')
            break

        if D_is > D_i_ultimo:
            D_i_ultimo = D_is
        
        
        if D_is < D_i_ultimo:
            print('Temos um grande problema')

    print('###' * 10)



# %%


plt.hist(fp)


# %%

# Veblen
# d = a - bP + c(Pc-P),onde c é o quanto a pessoa se importa com o consumo conspicuo (0 ~ 1). Pc é o preço conspicuo



# %%


