from resources_v2 import msg
from resources_v2 import menu
from random import randint

x = randint(1000, 9999)
print(x)

balance_bank = 100
count = 0
x = True 
user = {} # maybe I move for the function, for occupy less space in the memory

# adicionar endreço: str formato: logradouro, nmr - bairro - cidade/cigla estado
# Deve ser rmazenado somente os números do cpf (sem pontos e traços)
#não podemos cadastrar usuários com o mesmo cpf

'''
Criar conta corrente:

O programa deve armazenar contas em uma lista, uma conta é composta: por agência, número da conta e usuário. O número da conta é sequencial < iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

Dica:

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista
'''

is_user_registered = False # if is_user_registered = can execute te main

def new_user():
    global is_user_registered, x
    
    msg('Cadastro')
    print('Por favor cadastre antes de continuar')
    
    go_out = input("Aperte qualquer tecla para continuar ou digite 'sair' para sair do sistema: \n").lower()
    
    if go_out == "sair" or go_out == "s":
        x = False
    else:
        try:
            user["name"] = input('Digite o seu nome: \n')
            user["cpf"] = int(input('Digite seu cpf (pode colocar algo aleatório como 1234): \n'))
            user["password"] = input('Digite sua senha: \n')
            is_user_registered = True
            
        except ValueError:
            print('Tente novamente.')
new_user()

def login():
    ... # let in account, if name, cpf and pass be equal some a user, you can enter 

def add_funds() -> None:
    """
    Função para adicionar valor ao saldo.
    """
    global balance_bank
    try:
        n = int(input('Digite o quanto gostaria de adicionar: \n'))
        if n <= 0:
            print('O valor de depósito deve ser positivo')
        else:
            balance_bank += n # atribuição com incremento mesmo que balance_bank = balance_bank + n
            print(f'Você adicionou R${n:.2f}.') 
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def withdraw_funds() -> None:
    """
    Função para realizar saque do saldo.
    """
    DAILY_LIMIT = 500
    global balance_bank, count
    try:
        print(f'Você tem {count + 1}/3 saques disponíveis')
        n = int(input('Digite o quanto gostaria de sacar: \n'))
        if n <= balance_bank:
            print('O valor de depósito deve ser positivo')           
        elif n > balance_bank:
            print('Saldo insuficiênte:')
        else:
            if n > DAILY_LIMIT:
                print('Erro, o saque máximo é limitado a R$500')
            else: 
                count += 1
                balance_bank -= n 
                print(f'Você sacou R${n:.2f}.') 
            
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def bank_statement():
    """
    Função de extrato para mostrar o saldo atual do usuário.
    """
    msg(f"Seu saldo atual é: R$ {balance_bank:.2f}")

option = {
    1: add_funds,
    2: withdraw_funds,
    3: bank_statement,
}

if is_user_registered:
    def main():
        global x
        while x == True:
            menu()
            try:
                option_chosen = int(input('Escolha uma opção: \n'))
                if option_chosen in option:
                    option[option_chosen]()
                    if count == 3: 
                        print('Limite diário atingido!')
                        x = False
                elif option_chosen == 4:
                    print('saindo...')
                    x = False
                else:
                    print('Opção Inválida! Tente novamente.')
            except ValueError:
                print('Opção Inválida! Tente novamente.')
    main()
else:
    print('Cadastre antes de continuar!')