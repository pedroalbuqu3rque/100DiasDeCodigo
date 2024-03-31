# Receba um número e exiba se ele é positivo ou negativo
numero = float(input('Digite um número: '))
if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é 0')

# Receba e exiba o gênero da pessoa
genero = input('Informe seu gênero (F para Feminino, M para Masculino, O para Outro): ')
if genero.upper() == 'F':   # ".upper" converte para maiúsculo
    print('Você é do sexo Femenino.')
elif genero.upper() == 'M':
    print('Você é do sexo Masculino.')
elif genero.upper() == 'O':
    print('Você identificou-se com um gênero diferente do binário.')
else:
    print('Gênero não reconhecido.')

# Receba uma temperatura em farenheit e exiba em graus celsius (c = 5 * f - 32/9)
temp_farenheit = float(input('Digite uma temperatura em farenheit: '))
temp_celsius = 5 * ((temp_farenheit - 32) / 9)
print(f'A temperatura em garus celsius é de {temp_celsius}.')

# Calculadora de IMC
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * 2)
if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif imc < 25:
   classificacao ='Peso normal'
elif imc < 30:
    classificacao = 'Acima do peso'
else:
    classificacao = 'Sobrepeso'

print(f'Seu IMC é: {imc}')
print(f'Classificação: {classificacao}')

# Receba um número e exiba se ele é positivo ou negativo
numero = float(input('Digite um número: '))
if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é 0')

# EXERCISES
    
number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
if number1 > number2:
    print(f'The largest number is: {number1}')
elif number1 < number2:
    print(f'The largest number is: {number2}')