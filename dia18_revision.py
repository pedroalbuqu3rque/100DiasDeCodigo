def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def sum_list(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

def remove_duplicates(lista):
    return list(set(lista))

if __name__ == "__main__":
    prime_gen = prime_generator()
    print("Primeiros 5 números primos:")
    for _ in range(5):
        print(next(prime_gen))
    numeros = [1, 2, 3, 4, 5]
    print("Soma da lista:", sum_list(numeros))
    lista_com_duplicados = [1, 2, 3, 4, 1, 2, 5]
    print("Lista original:", lista_com_duplicados)
    print("Lista sem duplicados:", remove_duplicates(lista_com_duplicados))