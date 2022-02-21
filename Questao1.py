"""
Desafio Capgemini
Candidata: Amanda Del Grecco Santana Simões
Data: 19/02/2022
Questão 01
Descrição: Esse algoritmo mostra na tela uma escada de tamanho 'n', utilizando o caraceter '*' e espaços. A base
e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
"""
print("CONSTRUA SUA ESCADA")
qtd_str = input("Digite um número: ")
qtd_int = int(qtd_str)
print(f'Sua escada terá {qtd_int} degraus:')

def escada(qtd_int, sep='   '):
    asteriscos = '*'
    espacos = ''
    for _ in range(qtd_int):
        print('{2}{0:>{n}}'.format(asteriscos, espacos, sep, n=qtd_int))
        asteriscos += '*'
        espacos += ' '

escada(qtd_int)