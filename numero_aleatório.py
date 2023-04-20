# primeiro importamos uma função do Python para gerar um número de forma aleatória
# essa função (dá forma que foi escrita) só cria um número randomico dde 0.0 até 1.0

import random

# round arredonda o número caso ele seja uma dízima periódica
# em seguida atribuimos o valor aleatório feito pela função 'random' para uma variaável

numero_secreto = round(random.randrange(1,101) * 100) 

# usando a função 'randrange(1,101)' geramos um número aleatório de 1 até 100 (pois o ultimo valor não retorna)