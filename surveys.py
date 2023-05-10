# %%

import numpy as np
from pkg_resources import invalid_marker
import scipy
import matplotlib.pyplot as plt

# %%

# Essa é a demanda "assumida", que avisamos para todos os consumidores
# Demanda se mantém constante
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



# %%


