#Ler 10 números inteiros e imprimir quantos são pares e quantos são ímpares.

def count_even_or_odd(): 

    num = 0 #numeros digitados

    counter_allNubers = 1    #Vai contar o total de numeros digitados

    num_list = []   #Vai armazenar os numeros digitados

    counter_even = 0 #Vai contar os numeros pares

    counter_odd = 0 #Vai contar os numeros impares


    # Mostra  pro usuario a opções de cancelar a operação
    print("Digite 0 se quiser finalizar.\n")


    # Conforme os numeros vão sendo digitados eles serão adicionados em uma lista
    while counter_allNubers <= 10:
        num = float(input(f"Digite o {counter_allNubers}º número: "))
        
        if num == 0:
            break

        num_list.append(num)
        counter_allNubers += 1




    # Vai verificar se os numeros da lista são impares ou pares e conta a quantidade de cada um
    for numero in num_list:
        if (numero%2) != 0:
            counter_odd += 1
        else:
            counter_even += 1



    print(f"\n{counter_even} desses números são pares")
    print(f"{counter_odd} desses números são impares") 

    # tenta executar o código se der um erro retona uma msg
try:
    count_even_or_odd()

except:
    print("\nPor favor digite um numero!")