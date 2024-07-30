import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

def calculo_sal(val_hora,horas):
    sal_bruto=val_hora*horas
    sal_liq=sal_bruto-(sal_bruto*0.10)

    return sal_liq

val_hora = float(input("Digite o valor da hoa trabalhada: "))
horas= float(input("Digite a qauntidade de horas trabalhadas: "))

salario = calculo_sal(val_hora,horas)
salario = locale.currency(salario)

print("O seu salario é de {}".format(salario))
