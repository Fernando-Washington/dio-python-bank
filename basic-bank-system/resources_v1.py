def msg(text):
    """Função que exibe texto formatado

    Args:
        text (str): Texto a ser exibido no console.
    """
    print("-" * 18)
    print(text.center(18))
    print("-" * 18)

def menu():
    """
    Função para exibir o menu principal.
    """
    msg('Menu')
    print("-" * 18)
    print('- 1 - Depósito   -')
    print('- 2 - Saque      -')
    print('- 3 - Extrato    -')
    print('- 4 - Sair       -')
    print("-" * 18)


