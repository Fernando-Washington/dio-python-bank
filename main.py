from resources import menu

saldo = 100

def add_saldo() -> None:
    global saldo
    try:
        n = int(input('Digite o quanto gostaria de adicionar: \n'))
        saldo += n # atribuição com incremento mesmo que saldo = saldo + n
        print(f'Você adicionou R${n}.') 
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def rm_saldo() -> None:
    global saldo
    try:
        n = int(input('Digite o quanto gostaria de sacar: \n'))
        if n > saldo:
            print('Saldo insuficiênte:')
        else:
            print(f'Você sacou R${n}.') 
            saldo -= n 
    except ValueError: 
        print('Não foi possível realizar a operação.')
    
def extrato():
    print(f"Seu saldo atual é: {saldo}")

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
            elif option_chosen == 4:
                print('saindo...')
                x = False
                break
            else:
                print('Opção Inválida! Tente novamente.')
        except ValueError:
            print('Opção Inválida! Tente novamente.')
        
main()
