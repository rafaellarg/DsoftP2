def filtra(palavras):
    lista_min = []
    for palavra in palavras:
        nova_palavra = ''
        for letra in palavra:
            if letra.isupper():
                nova_palavra += letra.lower()
            else:
                nova_palavra += letra
        lista_min.append(nova_palavra)

    lista_sem_rep = []
    for p in lista_min:
        if p not in lista_sem_rep:
            lista_sem_rep.append(p)

    lista_n = []
    for i in lista_sem_rep:
        if len(i) == 5:
            lista_n.append(i)
    return lista_n


from colorama import Fore, Style

def inidica_posicao(sorteada, especulada):
    lista = []
    if len(sorteada) == len(especulada):
        for i in range(len(sorteada)):
            if sorteada[i] == especulada[i]:
                lista.append(f"{Fore.BLUE}0{Style.RESET_ALL}")
            if especulada[i] not in sorteada:
                lista.append(f"{Fore.LIGHTBLACK_EX}2{Style.RESET_ALL}")
            if especulada[i] in sorteada and especulada[i] != sorteada[i]:
                lista.append(f"{Fore.YELLOW}1{Style.RESET_ALL}")
        return lista
    else:
        return []



