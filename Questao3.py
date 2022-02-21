"""
Desafio Capgemini
Candidata: Amanda Del Grecco Santana Simões
Data: 20/02/2022
Questão 03
Descrição: Esse algoritmo encontra e imprime o número de pares de substrings que são anagramas.
"""
print("ANAGRAMA")
def Anagrama(letra1: object, letra2: object) -> object:
    n1 = len(letra1)
    n2 = len(letra2)

    if n1 != n2:
        return 0

    letra1 = sorted(letra1)
    letra2 = sorted(letra2)

    for i in range(0, n1):
        if letra1[i] != letra2[i]:
            return 0
    return 1

letra1 = input("Digite a primeira palavra: ")
letra2 = input("Digite a segunda palavra: ")

ListaAnagrama = [letra1, letra2]
Resultado = [ListaAnagrama]

print("")
print("RESULTADO")
if Anagrama(letra1, letra2):
    print("As duas palavras são anagramas uma da outra!")
    print(f"A lista de todos os anagramas pares são: {Resultado}")
    print()

else:
    print("As duas palavras não são anagramas uma da outra!")
