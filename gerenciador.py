import random
from os.path import exists
from cryptography.fernet import Fernet


def escreva_chave():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
            

chave_existe = exists('key.key')
if chave_existe == False:
    escreva_chave()
else:
    pass

def carregar_chave():
    arquivo = open('key.key', 'rb')
    chave = arquivo.read()
    arquivo.close()
    return chave


chave = carregar_chave()
fer = Fernet(chave)

def gerador_de_senha():
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z', '1', '2', '3', '4', '5','6' ,'7', '8', '9', '0', '!', '@', '#','$','%','&','*', '(',')','-','_','=','+','/', '<', '>', '.', ';', ':', '?',  '[',  ']', '{',  '}', ',']
    random.shuffle(caracteres)
    senha_aleatoria = []
    for c in range(13):
        senha_aleatoria.append(random.choice(caracteres))
    random.shuffle(senha_aleatoria)
    senha_pronta = "".join(senha_aleatoria)
    print('Sua senha de 13 digitos aleatoria é: ')
    print('')
    print(senha_pronta)   
    print('')
    nome = input('Nome do Serviço: ')
    with open('senhas.txt', 'a') as senhas:
        senhas.write(nome + '|' + fer.encrypt(senha_pronta.encode()).decode() + "\n" )
    print('')
    print('Sua senha foi salva com sucesso')
    print('')


def ver():
    try:
        print('')
        with open('senhas.txt' , 'r') as senhas:
            for line in senhas.readlines():
                data = line.rstrip()
                serv, senha = data.split("|")
                print('Serviço:', serv, "| Senha:", fer.decrypt(senha.encode()).decode())
        print('')
    except FileNotFoundError:
        print('')
        print('Você ainda não tem nenhuma senha salva para visualizar')
        print('')


def adcionar():
    nome = input('Nome do Serviço: ')
    pwd = input('Senha: ')
    with open('senhas.txt', 'a') as senhas:
        senhas.write(nome + '|' + fer.encrypt(pwd.encode()).decode() + "\n")
    print('')
    print('Sua senha foi salva com sucesso')
    print('')


while True:
    print('Gerenciador de Senhas')
    print('[1] - Adicionar senha')
    print('[2] - Ver senhas')
    print('[3] - Criar e salva senha')
    print('[4] - Sair')
    opção = int(input('Você deseja adcionar um senha, ver suas senhas, criar uma senha ou sair?: '))
    if opção == 4:
        print('Tenha um bom dia/boa noite')
        break
    if opção == 1:
        adcionar()
    if opção == 2:
        ver()
    if opção == 3:
        gerador_de_senha()
 