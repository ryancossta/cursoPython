#ENTRADA DE USUÁRIO 

#nome = input("Insira seu nome:")
#idade = input("Insira sua idade:")

#print("Olá," + nome + "!")
#print("Você tem " + idade + " anos")

#A função input() sempre retorna uma cadeia de texto. Se você 
# deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes,
#  deve realizar uma conversão explícita utilizando funções como int() ou float().

#SAÍDA DE DADOS 
nome1 = "Ryan"
idade1 = 18
print(f"Olá, meu nome é {nome1} e tenho {idade1} anos.")

#DATA E HORA ATUAL
import datetime
data_atual = datetime.datetime.now()
print(data_atual)

x = 5
y = "3"
z = x + int(y)
print(z)