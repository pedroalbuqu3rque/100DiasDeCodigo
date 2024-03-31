# Adição (+); Subtração (-); Multiplicação (*); Divisão (/); Divisão inteira (//); Módulo (%); Exponenciação (**); [import math]

idade = input("Digite a sua idade: ")
print(f"A sua idade é {idade} anos.") 
# "f" significa que a string vai ser criada a partir de algo dinâmico

# Calculadora de IMC
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

# Escreva um programa onde o usuário digite duas notas e mostre a ele a média das notas
nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))
media = (nota_01 + nota_02) / 2 
print("A media das suas notas é:", media) 