from art import text2art # Importei uma biblioteca para fazer textos em ASCII
import random
import time

# Cria um texto em arte ASCII
arte = text2art("Gerador de Senha")
print(arte)

print('                                 Developed by: Miguel Vasco                          ')
while True:
    try: # Aqui eu criei uma exceção para não quebrar o código caso o usuário digite uma letra
        numero_de_senhas = int(input("\nDígite o número de senha(s) que você deseja que seja gerada:") or 1)
        tamanho_da_senha = 0
        break
    except ValueError: # Se o usuário digitou uma letra provavelmente esse código e o que está embaixo vai ser executado
        print("Você provavelmente digitou um número inválido. Tente Novamente!")

# tamanho mínimo da senha deve ser 8 dígitos
while True:
    try:
        tamanho_da_senha = int(input("Digite um total de caracteres que você deseja colocar na(s) sua(s) senha(s):"))
        if tamanho_da_senha < 8:
            print("A senha deve conter pelomenos 8 dígitos")
        else:
            break
    except ValueError:
        print("Digite um valor válido. Por favor tente novamente!")
        

print(131*"=")

# Os nossos queridos caracteres!
caracteres_especiais = ['.', '+', '-', '@', '#', '*', '!', '?', '~']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Criei uma função para gerar as nosssas senhas
def gerar_senha(numero_de_senhas, t_senha): # Criei uma função chamada gerar_senha com dois atributos que são: "num_senha e t_senha"
    senhas = [] # Eu criei uma lista vázia para colocar a senha que vai ser gerada
    i = 1 # Criei uma variável chamada "i" que vai receber o valor de 1

  
    while i <= numero_de_senhas: # Enquanto 1 for menor que o número de senha vai criar uma lista chamada senha vazia
        senha = [] 


        while len(senha) < t_senha: # Enquanto o tamanho da lista senha for menor que o valor da variavel t_senha vai o que está embaixo
            senha.append(random.choice(caracteres_especiais)) # Vai acessar a variavel caracteres_especiais e depois vai escolher um caractere especial aleatóriamente e depois vai sair do loop while
            if len(senha) == t_senha: # Se o tamanho da lista senha e da variavel t_senha coincidirem vair ocasionar em um break
                break
            senha.append(random.choice(numeros))
            if len(senha) == t_senha:
                break
            senha.append(random.choice(letras_minusculas))
            if len(senha) == t_senha:
                break
            senha.append(random.choice(letras_maiusculas))
            if len(senha) == t_senha:
                break
        
        senhas.append(senha)
        i = i + 1
        
    return senhas # Vai retornar a senha criada com os devidos caracteres
senhas_geradas_pelo_nosso_gerador = gerar_senha(numero_de_senhas, tamanho_da_senha) # Vai chamar a nossa função e vai colocar os devidos atributos
a = tamanho_da_senha
print(f"A senha gerada têm um total de {a} caracteres")
# Imprimindo e iterando as nossas 
over = numero_de_senhas
print("Números de senhas geradas: ", over)
print(131*'=')


i = 0
for senha in senhas_geradas_pelo_nosso_gerador:
    print(f'Senha {i} {senha}')
    i +=1

print(131*"=")

