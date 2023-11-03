def filtra(palavras, n):
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
        if len(i) == n:
            lista_n.append(i)
    return lista_n
