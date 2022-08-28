from src.application.config import LINHAPERSONALIZADA, mensagem_1
def personalizacao():
    print('='* LINHAPERSONALIZADA )

def boa_pratica():  
    
    print(mensagem_1)

def identificacao()->None:
    nome = input("Digite seu nome : ").upper()
    idade =int(input("Digite a sua idade : "))
    return nome, idade

