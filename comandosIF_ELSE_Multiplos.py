num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))

print("Escolha uma operação:")
print("Digite 1 para soma;")
print("Digite 2 para subtração;")
print("Digite 3 para multiplicação;")
print("Digite 4 para divisão.")
op = int(input())

if op == 1:
    resultado = num1 + num2
    print("A soma é:", resultado)
elif op == 2:
    resultado = num1 - num2
    print("A subtração é:", resultado)
elif op == 3:
    resultado = num1 * num2
    print("A multiplicação é:", resultado)
else:
    resultado = num1 / num2
    print("A divisão é:", resultado) 