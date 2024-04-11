"""Escreva um programa que leia a quantidade em segundos e imprima o resultado em dias, horas, minutos e segundos."""

segundos = int(input("Digite a quantidade de segundos: "))

dias = segundos // 86400
horas_restantes = segundos % 86400
horas = horas_restantes // 3600
minutos_restantes = horas_restantes % 3600
minutos = minutos_restantes // 60
segundos_restantes = minutos_restantes % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos")