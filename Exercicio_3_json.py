#escolhi utilizar o arquivo json para o exercício

import json

f = open('dados.json')

data = json.load(f)

valores = [] #lista para adicionar os valores de cada dia
i = 0

#iterando sobre o json e adicionando o valor de cada dia a lista 'valores' caso o valor seja != 0
while i < len(data):
    if data[i]['valor'] == 0:
        i += 1
    else:
        valores.append(data[i]['valor'])
        i += 1

print("O MENOR valor de faturamento ocorrido em um dia do mês foi: ", min(valores))
print("O MAIOR valor de faturamento ocorrido em um dia do mês foi: ", max(valores), "\n")


media_mensal = sum(valores)/len(valores)

j = 0
count = 0

#iterando sob a lista 'valores' para achar onde um dia teve faturamento maior do que a média mensal
while j < len(valores):
    if valores[j] > media_mensal:
        count += 1
        j += 1
    else:
        j += 1

print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", count, "dias.")

f.close()
