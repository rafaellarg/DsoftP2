import random
from arq_palavras import palavras
from funcoes import filtra, inicializa, inidica_posicao, exibir_quadriculado

cor_azul = "\033[34m"
cor_amarela = "\033[33m"
cor_cinza = "\033[90m"
reset_cor = "\033[0m"

print(" ===========================\n"
      "|                           |\n"
      "| Bem-vindo ao Insper Termo |\n"
      "|                           |\n"
      " ==== Design de Software ===\n"
      "Comandos: desisto\n"
      " Regras:\n"
      "  - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.\n"
      "  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n"
      f"    . {cor_azul}Azul  {reset_cor}: a letra está na posição correta;\n"
      f"    . {cor_amarela}Amarelo{reset_cor}: a palavra tem a letra, mas está na posição errada;\n"
      f"    . {cor_cinza}Cinza{reset_cor}: a palavra não tem a letra.\n"
      f"  - Os acentos são ignorados;\n"
      f"  - As palavras podem possuir letras repetidas.")

while True:
    lista = filtra(palavras, 5)
    dic = inicializa(lista)
    sorteada = dic['sorteada']
    tentativas = dic['tentativas']
    print(" ")
    print("Sorteando uma palavra...")
    break

print("Já tenho uma palavra, tente adivinhar!")

quadriculado = [[' ' for _ in range(5)] for _ in range(6)]

for i in range(tentativas + 1)[::-1]:
    if i != 0:
        print("Você tem", i, "tentativas")
    if i == 0:
        print("Você perdeu, a palavra era:", sorteada)
        break

    especulada = input('Digite seu palpite: ')
    if especulada in lista:
        if len(especulada) != 5:
            print("Você tem", i, "tentativas")
            especulada = input('Digite seu palpite: ')
        if especulada == sorteada:
            print("Parabéns! Você acertou!")
            break

        lista_posicao = inidica_posicao(sorteada, especulada)
        for j in range(len(lista_posicao)):
            if lista_posicao[j] == 0:
                quadriculado[tentativas - i][j] = f'{cor_azul}{especulada[j]}{reset_cor}'
            elif lista_posicao[j] == 1:
                quadriculado[tentativas - i][j] = f'{cor_amarela}{especulada[j]}{reset_cor}'
            elif lista_posicao[j] == 2:
                quadriculado[tentativas - i][j] = f'{cor_cinza}{especulada[j]}{reset_cor}'

        exibir_quadriculado(quadriculado)

    else:
        print(" ")
        print("Palavra desconhecida")
        print("Você tem", i, "tentativas")
        especulada = input('Digite seu palpite: ')

        lista_posicao = inidica_posicao(sorteada, especulada)
        for j in range(len(lista_posicao)):
            if lista_posicao[j] == 0:
                quadriculado[tentativas - i][j] = f'{cor_azul}{especulada[j]}{reset_cor}'
            elif lista_posicao[j] == 1:
                quadriculado[tentativas - i][j] = f'{cor_amarela}{especulada[j]}{reset_cor}'
            elif lista_posicao[j] == 2:
                quadriculado[tentativas - i][j] = f'{cor_cinza}{especulada[j]}{reset_cor}'

        exibir_quadriculado(quadriculado)