def filhosToString(s):
    return ' '.join([str(v) for v in s])


def objetivo(s):
    goal = False
    if (s[0] == 0) and (s[1] == 0) and (s[2] == 0):
        goal = True
    return goal


def validar(s):
    # mais canibais que missionarios em qualquer lado do rio
    if(s[0] > 0 and s[0] < s[1]) or (s[0] < 3 and s[0] > s[1]):
        return False

    return True


def geraFilhos(s):
    listaDeFilhos = []

    if(s[2] == 0):  # partindo do lado direito do rio

        if(s[0] < 3) and (s[1] < 3):  # atravessar um de cada
            estado = [s[0]+1, s[1]+1, 1]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[1] < 2):  # atravessar dois canibais
            estado = [s[0], s[1]+2, 1]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[0] < 2):  # atravessar dois missionários
            estado = [s[0]+2, s[1], 1]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[1] < 3):  # atravessar um canibal
            estado = [s[0], s[1]+1, 1]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[0] < 3):  # atravessar um missionário
            estado = [s[0]+1, s[1], 1]
            if validar(estado):
                listaDeFilhos.append(estado)

    else:  # partindo do lado esquerdo do rio

        if(s[0] >= 1) and (s[1] >= 1):  # atravessar um de cada
            estado = [s[0]-1, s[1]-1, 0]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[1] >= 2):  # atravessar dois canibais
            estado = [s[0], s[1]-2, 0]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[0] >= 2):  # atravessar dois missionários
            estado = [s[0]-2, s[1], 0]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[1] >= 1):  # atravessar um canibal
            estado = [s[0], s[1]-1, 0]
            if validar(estado):
                listaDeFilhos.append(estado)

        if (s[0] >= 1):  # atravessar um missionário
            estado = [s[0]-1, s[1], 0]
            if validar(estado):
                listaDeFilhos.append(estado)

    return listaDeFilhos


def estimativaDeCusto(s):
    # Função de Avaliação: numero de pessoas na margem destino
    # Função de Custo: constante (1)
    # Estimativa de Custo total = fa + 1
    return (s[0]) + (s[1]) + 1


def ordena(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if(estimativaDeCusto(lst[j]) > estimativaDeCusto(lst[j+1])):
                aux = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = aux
    return lst


def buscaAstar(inicio):
    candidatos = [inicio]
    pais = dict()
    visitados = [inicio]

    while len(candidatos) > 0:
        ordena(candidatos)
        pai = candidatos[0]
        print("Lista de candidatos: ", candidatos)
        del candidatos[0]
        print("Visitado: ", pai)
        if objetivo(pai):
            res = []
            node = pai
            while node != inicio:
                res.append(node)
                node = pais[filhosToString(node)]
            res.reverse()
            print("Solucao encontrada: ", res)

        for son in geraFilhos(pai):
            if son not in visitados:
                print("Enfileirado: ", son, pai)
                visitados.append(son)
                pais[filhosToString(son)] = pai
                candidatos.append(son)


if __name__ == '__main__':
    buscaAstar([3, 3, 1])
