"""
Desafio Capgemini
Candidata: Amanda Del Grecco Santana Simões
Data: 20/02/2022
Questão 02
Descrição: Esse algoritmo recebe dados para cadastro em uma rede social e tem como parâmetros, a definição de uma
senha forte. São eles: (a) Possuir no mínimo 6 caracteres, (b) Conter no mínimo 1 dígito, (c) Conter no mínimo 1
letra em minúsculo, (d) Conter no mínimo 1 letra em maiúsculo, (e) Conter no mínimo 1 caractere especial e
(f) Os caracteres especiais são: !@#$%^&*()-+.
"""
import re
from itertools import count

print("SEJA BEM-VINDO(A)! \n"
      "Por gentileza: (1) Insira o seu nome completo; (2) Crie uma senha forte! Para tanto, a sua senha deverá atender"
      "aos seguintes requisitos: \n (a) Possuir no mínimo 6 caracteres, (b) Conter no mínimo 1 dígito, (c) Conter no mínimo "
      "1 letra em minúsculo, (d) Conter no mínimo 1 letra em maiúsculo, \n (e) Conter no mínimo 1 caractere especial e (f) "
      "Os caracteres especiais são: !@#$%^&*()-+ \n")

nome = input("Digite o seu nome: ")
senha = input("Digite uma senha: ")

i = 0
while i < len(senha):
    i = i + 1

print("")
print("DADOS RECEBIDOS:")
print(f'Seu nome é: {nome}')
print(f'Sua senha é: {senha}')

print("")
print("FEEDBACK PARA A SENHA: ")

status = 0
while True:
    if len(senha) < 6:
        status = -1
        break
    elif not re.search("[a-z]", senha):
        status = -1
        break
    elif not re.search("[A-Z]", senha):
        status = -1
        break
    elif not re.search("[!@#$%^&*()-+]", senha):
        status = -1
        break
    else:
        status = 0
        print("Senha forte! Seu cadastro foi realizado com sucesso!")
        break

if status == -1:
    print(f'Senha inválida! A sua senha possui {i} caracteres! \n'
          f'Por favor, insira uma nova senha, com no mínimo 6 caracteres, atentando-se para a sugestão de senha forte!')
