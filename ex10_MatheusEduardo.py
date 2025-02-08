#Escreva um programa que pergunte quantos pedaços o bolo tem, seguida pergunte ao usuário quantos pedaços ele comeu, calcule 
#quantos pedaços ainda tem e exiba o resultado com uma mensagem de livre escolha
pedaços = int(input("Quantos pedaços o bolo tem? "))
comeu = int(input("Quantos pedaços você comeu? "))
sobra = pedaços - comeu
print("Tinham", pedaços, "pedaços\nVocê comeu", comeu, "pedaços\nSobraram", sobra, "pedaços")