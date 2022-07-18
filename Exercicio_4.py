valores = [["SP", 67836.43], ["RJ", 36678.66], ["MG", 29229.88], ["ES", 27165.48], ["Outros", 9849.53]]

#calculando o faturamento mensal total
soma = 0; i = 0
while i < len(valores):
    soma = soma + valores[i][1]
    i += 1

#calculando a porcentagem de cada estado sob o faturamento total
j = 0
while j < len(valores):
    porcentagem = (valores[j][1]*100)/soma
    final = round(porcentagem, 2)
    print(valores[j][0], " = ", final, "%")
    j += 1



