valor = 0
while valor != -1:

    print("\n")
    valor = int(input("Digite o número: "))
    if valor == -1:
        break
     
    #variáveis para iniciar a sequencia de fib
    a = 0
    b = 1
    c = 1

    #caso o valor seja 0 ou 1 já retornamos a resposta aqui
    if (valor == 0 or valor == 1):
        print("O número", valor, " pertence a sequencia de Fibonacci.")

    #calculamos a sequencia de fib enquanto f3 seja menor que valor
    else: 
        while a < valor:
            a = b + c
            c = b
            b = a
        if a == valor:
            print("O número", valor, " pertence a sequencia de Fibonacci.")
        else:
            print("O número", valor, " NAO pertence a sequencia de Fibonacci.")
