import random
from arq_palavras import palavras
from funcoes import filtra, inicializa, inidica_posicao


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

print("Já tenho uma palavra, tente adivinha-la")

print(" ")





for i in range(tentativas + 1)[::-1]:
      print("Você tem", i , "tentativas")
      if i == 0:
            break
      
      especulada = input('Digite seu palpite: ')
      if especulada in lista:
            if len(especulada) != 5:
                  print("Você tem", i , "tentativas")
                  especulada = input('Digite seu palpite: ')
            if especulada == sorteada:
                  print("parabens! Voce acertou!")

            lista_posicao = inidica_posicao(sorteada, especulada)
            s = ''
            for i in range(len(lista_posicao)):
                  if lista_posicao[i] == 0:
                        s = f'{s}{cor_azul}{especulada[i]}{reset_cor}'
                  if lista_posicao[i] == 1:
                        s = f'{s}{cor_amarela}{especulada[i]}{reset_cor}'
                  if lista_posicao[i] == 2:
                        s = f'{s}{cor_cinza}{especulada[i]}{reset_cor}'

            print(s)

      else:
            print(" ")
            print("palavra desconhecida")
            print("Você tem", i , "tentativas")
            especulada = input('Digite seu palpite: ')

            lista_posicao = inidica_posicao(sorteada, especulada)
            s = ''
            for i in range(len(lista_posicao)):
                  if lista_posicao[i] == 0:
                        s = f'{s}{cor_azul}{especulada[i]}{reset_cor}'
                  if lista_posicao[i] == 1:
                        s = f'{s}{cor_amarela}{especulada[i]}{reset_cor}'
                  if lista_posicao[i] == 2:
                        s = f'{s}{cor_cinza}{especulada[i]}{reset_cor}'

            print(s)

      
      

      



    



