# Faça um script que leia N números.
# Finalizar quando digitar 0.
# No final mostrar o total de números digitados, o total de números ímpares e o total de números pares.




num = 0 #numeros digitados

counter_allNubers = 0    #Vai contar o total de numeros digitados

num_list = []   #Vai armazenar os numeros digitados

counter_even = 0 #Vai contar os numeros pares

counter_odd = 0 #Vai contar os numeros impares


# Mostra  pro usuario a opções de cancelar a operação
print("Digite 0 se quiser finalizar.\n")


# Conforme os numeros vão sendo digitados eles serão adicionados em uma lista
while True:
    num = float(input('Digite um número: '))
    
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



print(f"O total de numeros digitado é de: {counter_allNubers} números")
print(f"{counter_even} desses números são pares")
print(f"{counter_odd} desses números são impares") 