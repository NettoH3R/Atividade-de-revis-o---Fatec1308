# Criar um script que entre com cinco números e imprimir o quadrado de cada número.

def show_sq():
    #VARIAVEIS
    num = float  # vai receber o numero que o usuario digitar

    counter_numTyped = 0 #conta a quantidade de numeros digitados


    #LISTAS
    num_list = []   # vai armazenar os numeros digitados



    # vai pedir um numero pro usuario e coloca-lo na lista
    while 5 > counter_numTyped: 
        num = float(input("Digite o número: "))
        
        num_list.append(num)

        counter_numTyped += 1

    # percore a lista e mostra pro usuario o numero e seu quadrado
    for number in num_list:
            print(f"A raiz quadrada de {number} é {(number**2)}")


# tenta executar o código se der um erro retona uma msg
try:
    show_sq()

except:
    print("\nPor favor digite um numero!")