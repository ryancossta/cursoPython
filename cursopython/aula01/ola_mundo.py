print ("olá, mundo!")

#este é um comentário de uma linha 


#VARIÁVEIS

# Define a variável "nota" com o valor 85
nota = 85

# Verifica se a nota é maior ou igual a 90
if nota >= 90:
    print("Excelente")  # Exibe "Excelente" se a condição for verdadeira

# Caso a primeira condição seja falsa, verifica se a nota é maior ou igual a 80
elif nota >= 80:
    print("Muito bom")  # Exibe "Muito bom" se esta condição for verdadeira

# Caso as duas condições anteriores sejam falsas, verifica se a nota é maior ou igual a 70
elif nota >= 70:
    print("Bom")  # Exibe "Bom" se esta condição for verdadeira

# Se nenhuma das condições anteriores for verdadeira
else:
    print("Precisa melhorar")  # Exibe "Precisa melhorar"





 #ESTRUTURA DE DADOS

# Define uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Adiciona a fruta "pera" ao final da lista
frutas.append("pera")
print(frutas)  # Imprime: ["maçã", "banana", "laranja", "pera"]

# Insere a fruta "uva" na posição 1 (segunda posição) da lista
frutas.insert(1, "uva")
print(frutas)  # Imprime: ["maçã", "uva", "banana", "laranja", "pera"]

# Remove a fruta "banana" da lista
frutas.remove("banana")
print(frutas)  # Imprime: ["maçã", "uva", "laranja", "pera"]

# Remove a fruta que está na posição 2 (terceira posição) da lista e armazena o valor removido em uma variável
fruta_removida = frutas.pop(2)
print(frutas)  # Imprime: ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime: "laranja"

# Ordena a lista de frutas em ordem alfabética
frutas.sort()
print(frutas)  # Imprime: ["maçã", "pera", "uva"]

# Inverte a ordem da lista
frutas.reverse()
print(frutas)  # Imprime: ["uva", "pera", "maçã"]


#CONJUNTOS (SET)

frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()