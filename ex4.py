#Faça um script para receber um número qualquer e informar na tela se é par ou ímpar.

def par_ou_impar():
    num = float

    num =  float(input("Digite um número: "))

    #   Vai verificar se o numero digitado é par ou impar
    if (num%2) != 0:
        print(f"{num} é ímpar")
    else:
        print(f"{num} é par")



# tenta executar o código se der um erro retona uma msg
try:
    par_ou_impar()

except:
    print("\nPor favor digite um numero!")

