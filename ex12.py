#Escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, 
#divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "Cada cliente deve pagar:" x valor
conta = int(input("Qual o valor total da conta? "))
clientes = int(input("Quantos clientes existem? "))
pagar = conta / clientes
print("Cada cliente deve pagar: ",pagar)