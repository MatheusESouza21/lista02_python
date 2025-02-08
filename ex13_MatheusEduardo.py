#Escreva um programa que solicite um determinado número de dias, em seguida exiba o quanto esses dias equivalem em horas, minutos e segundos
dias = int(input("Escreva uma quantidade de dias: "))
horas =  dias * 24
minutos = horas * 60
segundos = minutos * 60
print(dias, "equivalem",horas,"horas, ",minutos, "minutos e",segundos, "segundos.")
