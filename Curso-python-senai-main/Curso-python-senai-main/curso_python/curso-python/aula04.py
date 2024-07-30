#Exercicios

#1
idade1= int(input("Digite a sua idade: "))
idade2= int(input("Digite a iade de seu amigo: "))

print("A diferença de suas idades é : ".format((idade1-idade2)*-1))

#2

nome= str(input("Digite seu nome: "))

print("Seu nome em maiusculas é {} e em minusculas é {}".format(nome.upper(),nome.lower()))

#3

sal= float(input("Digite o seu salario em reais: "))
acre = float("Digite o percentual de acrescimo: ")

sal_acre= sal +(sal*(acre/100))

print("O seu salario base é {} e se uacrescimo foi de {}% totalizando {}".format(sal,acre,sal_acre))

#4
print("Bem vindo a imobiliaria Imobilis")
lar= float(input("Digite a largura do terreno: "))
comp= float(input("Digite o comprimento do terreno: "))

print("A aréa do terreno é de {}".formta(lar*comp))

#5

cav= int("Qual a quantidade de cavalos: ")
num_ferra= cav*4

print("A quantidade de ferraduras é de {}".format(num_ferra))

#6
pao= int(input("Digite a qauntidade de paes vendidos: "))
broa= int(input("Digite a quantidade de broas vendidas: "))

val_pao= pao*0.12
val_broa= broa*1.50

val_total=val_pao+val_broa
poup= val_total*0.10
print("O valor arrecadado de paes vendidos é {}, a de broas são {}, totalizando {}, você deve guardar na poupança {} ".format(val_pao,val_broa,val_total,poup))

#7
nome= str(input("Digite seu nome: "))
idade= int("Digite a sua idade: ")

print("{} voce ja viveu {} dias".format(nome,idade*365))

#8

prc_litro= float(input("Digite o valor do litro da gasolina: "))
pag= float(input("Digite o valor pago: "))

print("A quantidade de litros abastecida é : {} ".format(pag/prc_litro))

#9

peso = float(input("Digite o peso do prato de comida do cliente: "))
peso_prato=float(input("Digite o peso do prato:"))

val= (peso-peso_prato)*12

print("O valor a ser cobrado é: {} ".format(val))

#10

def calc_media_pond(notas,pesos):
    if len(notas) != len(pesos):
        return "Erro o numero de notas deve ser o mesmo de pesos"
    
        soma_pond= sum([nota * peso for nota, peso in zip(notas,pesos)])
        soma_pesos = sum(pesos)
    
        if  soma_pesos ==0:
            return "erro: A soma dos pesos não pode ser zero"

            media_pond= soma_pond/ soma_pesos
            return media_pond
        
        notas = []
        pesos = []

        num_notas= int(input("Quantas notas quer inserir?"))

        for i in range(num_notas):
            nota=float(input(f"Informe a nota {i+1}:"))
            notas.append(nota)

            peso=float(input(f"Informe o peso {i+1}:"))
            pesos.append(peso)

            media= calc_media_pond(notas,pesos)

            if isinstance(media,str):
                print("A media é {}".format(media))
            else:
                print(f"A media ponderada é :{media:.2f}")

#11

import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

cam_peq= int(input("Digite a quantidade de camisas pequenas vendidas: "))
cam_med= int(input("Digite a quantidade de camisas medias vendidas: "))
cam_grandes= int(input("Digite a quantidade de camisas grandes vendidas: "))

valor= (cam_peq*10+cam_med*12+cam_grandes*14)
valor = locale.currency(valor)

print("A quantidade camisetas vendidas foi {} e o valor arrecadado foi {}".format(cam_peq+cam_med+cam_grandes,valor))

#12

sal= float(input("Digite seu salário: "))

sal_acre= sal + (sal*0.15)
sal_final= sal_acre-(sal_acre*0.08)

print("O seu salario com acrescimo é {} e com os descontos são {}".format(sal_acre,sal_final))

#13

def calculo_sal(val_hora,horas):
    sal_bruto=val_hora*horas
    sal_liq=sal_bruto-(sal_bruto*0.10)

    return sal_liq

val_hora = float(input("Digite o valor da hoa trabalhada: "))
horas= float(input("Digite a qauntidade de horas trabalhadas: "))

salario = calculo_sal(val_hora,horas)
salario = locale.currency(salario)

print("O seu salario é de {}".format(salario))

#14
