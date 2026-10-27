# Apresentação
print("Programa para aparesentar 11 valores, utilizando vetores")
print()

# Declara o setor com 11 posições para armazenar nos números
valores = []
for i in range (11):
    numero = float(input("Informe um número: "))
    valores.append(numero)

print()
print("Números")
for i in range(11):
    print (valores[i])
    print("-----------------------------")