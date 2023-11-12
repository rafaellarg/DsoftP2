import random
from arq_palavras import palavras



def filtra(palavras, n):
    lista_min = []
    for palavra in palavras:
        if len(palavra) == 5:
            lista_min.append(palavra.lower())
    return lista_min











def inicializa(palavras):
    dic = {}
    for palavra in palavras:
        dic['n'] = len(palavra)
        dic['tentativas'] = len(palavra) + 1

    dic['sorteada'] = random.choice(palavras)
    dic ['especuladas'] = []

    return dic











def inidica_posicao(sorteada, especulada):
    lista = []
    if len(sorteada) == len(especulada):
        for i in range(len(sorteada)):
            if sorteada[i] == especulada[i]:
                lista.append(0)
            if especulada[i] not in sorteada:
                lista.append(2)
            if especulada[i] in sorteada and especulada[i] != sorteada[i]:
                lista.append(1)
        return lista
    else:
        return []




def exibir_quadriculado(quadriculado):
    linha_formatada = " ---" * len(quadriculado[0])
    for linha in quadriculado:
        print(linha_formatada)
        print("| " + " | ".join(linha) + " |")
    print(linha_formatada)







