# Operadores Relacionais: Igual (==); Diferença (!=); Menor que (<); Maior que (>); Maior ou Menor que (<=, >=)
operador_relacional = 2 > 1
print(operador_relacional)

x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False

# Operadores Lógicos: and; or; not
operador_logico = False or True    # se pelo menos um dos lados for falso, vai retornar False
print(operador_logico)             # "not" inverte a operação: not False == True

operador = not ( (5 == 7 or 3 > 2) and (2 == 2 or 5 < 5) )  # False
print(operador)

# Estrutura de Decisão: if; else; elif
idade = 20

if idade < 18:   # se a condição for verdadeira, é executado
    print("Menor de idade")
elif idade >= 18 and idade < 65: # se a segunda condição for verdadeira o código deve ser executado 
    print("Adulto")
else:     # se nenhuma das condições anteriores forem verdadeiras, é executado
    print("Idoso")



