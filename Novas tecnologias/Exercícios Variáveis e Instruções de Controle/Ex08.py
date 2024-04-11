"""Escreva um programa que converta uma temperatura digitada em "C” em
“F”. A fórmula para essa conversão é:  F=9/5*C+32"""

tc = float(input("Digite a temperatura em Celsius: "))

tf = (9/5 * tc) + 32

print(f"{tc:.2f} graus Celsius equivalem a {tf:.2f} graus Fahrenheit.")