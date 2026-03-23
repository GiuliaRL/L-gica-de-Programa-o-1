# Faça um algorítmo que leia dois números inteiros e retorne
# a soma desses dois números
# a divisão inteira entre os dois números
# a multiplicação entre os dois números
# o quociente inteiro da divisão entre os dois números
# o resto da divisão inteira entre os dois números

#ENTRADAS
num1 = int (input("informe o primeiro número: "))
num2 = int (input("informe o segundo número: "))
#soma
soma = int(num1 + num2)
print (f"Soma:{soma}")
#Subtração
subtracao = int(num1 - num2)
print(f"Subtração:{subtracao}")
#Multiplicação
multiplicacao = int(num1 * num2)
print(f"Multiplicação:{multiplicacao}")
#Divisão inteira
divInteira = int(num1 // num2)
print(f"Quociente inteiro da divisão:{divInteira}")
#Resto da divisão
resto = int(num1 % num2)
print(f"Resto da divisão inteira:{resto}")


