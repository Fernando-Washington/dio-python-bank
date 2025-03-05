from resources_v1 import msg
from resources_v1 import menu

saldo = 100
count = 0

def add_saldo() -> None:
    """
    Função para adicionar valor ao saldo.
    """
    global saldo
    try:
        n = int(input('Digite o quanto gostaria de adicionar: \n'))
        if n <= 0:
            print('O valor de depósito deve ser positivo')
        else:
            saldo += n # atribuição com incremento mesmo que saldo = saldo + n
            print(f'Você adicionou R${n:.2f}.') 
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def rm_saldo() -> None:
    """
    Função para realizar saque do saldo.
    """
    global saldo, count
    try:
        print(f'Você tem {count + 1}/3 saques disponíveis')
        n = int(input('Digite o quanto gostaria de sacar: \n'))
        if n <= 0:
            print('O valor do saque deve ser positivo')           
        elif n > saldo:
            print('Saldo insuficiênte:')
        else:
            if n > 500:
                print('Erro, o saque máximo é limitado a R$500')
            else: 
                count += 1
                saldo -= n 
                print(f'Você sacou R${n:.2f}.') 
            
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def extrato():
    """
    Função de extrato para mostrar o saldo atual do usuário.
    """
    msg(f"Seu saldo atual é: R$ {saldo:.2f}")

option = {
    1: add_saldo,
    2: rm_saldo,
    3: extrato,
}

x = True

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