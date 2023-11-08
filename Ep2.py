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





    



