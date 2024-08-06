numero = int(input("Digite um número para calcular a tabuada (somente numero pares): "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    if resultado % 2 == 0 :
        print(f"{numero} x {i} = {resultado}")
