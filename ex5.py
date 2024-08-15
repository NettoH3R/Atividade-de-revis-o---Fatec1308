#Faça um script em Python para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.
def calcular_ferraduras():

    #variaveis
    cavalos = int
    ferraduras = int

    cavalos = int(input("informe quantos cavalos foram comprados: "))

    #calculo
    ferraduras = cavalos * 4

    print(f"Serão necesssarias {ferraduras}.")


# tenta executar o código se der um erro retona uma msg
try:
    calcular_ferraduras()

except:
    print("\nPor favor digite um numero!")