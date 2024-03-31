nomes = ['José', 'João', 'Pedro', 'Marcos']   # index se refere à posição de um elemento dentro da lista
nomes[2] = 'Albus'   # os valores podem ser modificados
nomes.append('Maria')   # adiciona um elemento na lista
print(nomes[4]) 

add_nomes = []
while True:
    nome = input('Cadastre os nomes e digite "OK" quando concluir:  ')
    if nome.upper() == 'OK':
        break 
    add_nomes.append(nome)
print(add_nomes)

nomes = ['Pedro', 'Paulo', 'Joaquim', 'Marcos', 'Antônio']
nomes.insert(0 , 'Jonas')   # adiciona elemento, posição e valor
print(nomes)

nomes = ['Carla', 'Maria', 'Ana', 'Vitória']
nomes.pop(2)   # remove elemento, posição
print(nomes)

nomes = ['Luis', 'Sofia', 'Alex', 'Júlia', 'Lucas']
print(nomes.index('Lucas'))   # mostra a posição

numeros = [57, 14.5, 134, 11, 29.45, 489, 6.4]
numeros.sort()   # ordena a lista / "reverse = True" inverte
print(numeros)

numeros = [23, 4, 78, 22, 61]
numeros_ord = sorted(numeros)   # não altera a lista original
print(numeros_ord)

idades = [3, 5, 27, 'Albus', 2, 45, 60,]   # uso de duas variáveis
for i, j in enumerate(idades):  # acessa index e valor
    print(f'i = {i} j = {j}')

idades = [32, 45, 68, 3, 21, 14, 19, 10, 7, 93]
idades_pares = []
for i in idades: 
    if i % 2 == 0:
        idades_pares.append(i)   # se for par, adiciona à lista
print(idades_pares)

numeros_id = [[1, 2, 3, 4, 5],
              [6, 7, 8 , 9, 10],
              [11, 12, 13, 14, 15]
]
for i in range(0, len(numeros_id)):
    for j in range(0, len(numeros_id[i])):
        print(numeros_id[i][j])

# Receba 10 valores e exiba a soma de todos eles
x = [int(input()) for i in range(0, 10)]  # "sum()" soma todos os valores da lista
soma = 0
for i in x:
    soma += i
print(soma)