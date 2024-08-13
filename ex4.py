#Faça um script para receber um número qualquer e informar na tela se é par ou ímpar.

num = float

num =  float(input("Digite um número: "))

#   Vai verificar se o numero digitado é par ou impar
if (num%2) != 0:
    print(f"{num} é ímpar")
else:
    print(f"{num} é par")

