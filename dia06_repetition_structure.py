# Receba um número inteiro do usuário e mostre a tabuada desse número
n1 = int(input('Digite o número que deseja saber a tabuada: '))

i = 1
while i <= 10:
    print(f'{n1} X {i} = {n1 * i}')
    i += 1  # vai somar "1" dentro da variável "i"

# Receba notas de um aluno (0 - 10), caso a nota esteja fora, peça para digitar novamente
while True:
    nota_aluno = int(input('Digite a nota do aluno: '))
    if nota_aluno >= 0 and nota_aluno <= 10:
        print('Nota armazenada.')
        break   # vai interromper o laço mesmo que a condição ainda seja verdadeira
                # "continue" retorna a executar diretamente o laço

    print('Nota inválida, digite novamente.')

# Defina um usuário e senha, depois verifique se o login é válido
usuario = "albus"
senha = "Albus_123"

while True:
    usuario_login = input('Digite seu nome de usuário: ')
    senha_login = input('Digite sua senha: ')
    if usuario_login == usuario and senha_login == senha:
        print('Login realizado.')
        break
    else:   # nesse caso não seria necessário o uso do "else", poderia ser direto o "print"
        print('Usuário ou senha inválido, tente novamente.')

# Receba um número e mostre todos os números pares de 0 até o número digitado
n1 = int(input('Digite um número: '))

i = 1
while i <= n1:
    if i % 2 == 0:  # rever o uso do módulo
        print(i)
    i += 1