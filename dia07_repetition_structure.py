for i in range(0, 100, 2):   # o último número adicionado é o "step"
    print(i)

for i in range(100, 0, -1):    # exemplo de ordem decrescente
    print(i)
print(list( range(0, 5)))

k = 0
for i in range(0, 1000):
    for j in range(0, 1000):    # dois loops aninhados
        print(f'i = {i} j = {j}')
        k += 1
print(k)

# Receba um número e mostre a tabuada completa dele usando o laço "for"
n1 = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{n1} x {i} =+ {n1 * i}')

# Mostre a tabuada completa de todos os números de 1 a 10
for i in range(1, 11):
    print(f'----------[TABUADA {i}]----------')
    for j in range(1, 11):
        print(f'{i} x {j} =+ {i * j}')

# Exiba todos os números pares entre 1 e 1000 usando o "for"
for i in range(1, 1001):    # pode usar o "step" (1, 1001, 2)
    if i % 2 == 0:
        print(i)