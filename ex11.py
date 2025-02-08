#Escreva um programa que pergunte o nome do aniversariante, em seguida pergunte a sua idade, acrescente mais 1 e exiba: o nome do aniversariante seguida
#da mensagem "no próximo aniversario você terá "idade + anos"
nome = input("Qual o nome do aniversariante? ")
idade = int(input("Qual a sua idade? "))
novaidade = idade + 1
print("O nome do aniversariante é", nome,"\nNo próximo aniversário você terá", novaidade,"anos")