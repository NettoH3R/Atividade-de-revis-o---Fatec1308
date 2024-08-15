# O IMC Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. 
# A fórmula é IMC = peso/(altura)2
# Elabore um script que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.

# IMC em adultos Condição
# Abaixo de 18,5                         Abaixo do peso
# Entre 18,5 e 25 (18,5 <= imc <= 25)    Peso normal
# Entre 25 e 30 (25 < imc < 30)          Acima do peso
# Acima de 30                            Obeso

#função pricipal
def calculadora_imc():

    #variaveis
    altura = float
    peso = float
    imc = float

    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em Kg: ")) 

    # verificar se os numeros não são menores que 0 para continuar o codigo
    if altura  < 0 or peso < 0:
        return("Altura ou Peso inválidos!")

    #calculando imc
    imc = round(peso/(altura**2),2)


    #informa o resultado
    if imc < 18.5:
        print("\nAbaixo do peso! ╯︿╰")
    
    elif 18.5 <= imc  <= 25:
        print("\nPeso normal (❁´◡`❁)")
    
    elif 25 < imc <30:
        print("\nAcima do peso! OwO")
    
    else:
        print("\nObeso! ヽ（≧□≦）ノ")


# tenta executar o código se der um erro retona uma msg
try:
    calculadora_imc()

except:
    print("\nPor favor digite um numero!")