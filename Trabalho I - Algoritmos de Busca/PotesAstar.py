def filhos2str(s):
    return ' '.join([str(v) for v in s])


def isGoal(s):
    goal = False
    if s[0] == 4 or s[1] == 4:
        goal = True
    return goal


def geraFilhos(s):

    listaDeFilhos = []

    # esvaziar o pote 1
    state = [0, s[1]]
    listaDeFilhos.append(state)

    # esvaziar o pote 2
    state = [s[0], 0]
    listaDeFilhos.append(state)

    # encher o pote 1
    state = [7, s[1]]
    listaDeFilhos.append(state)

    # encher o pote 2
    state = [s[0], 5]
    listaDeFilhos.append(state)

    # verter pote 1 no pote 2
    if s[0] >= 5-s[1]:
        state = [s[0]-(5-s[1]), 5]
    else:
        state = [0, s[1] + s[0]]
    listaDeFilhos.append(state)

    # verter pote 2 no pote 1
    if s[1] <= 7-s[0]:
        state = [s[0]+s[1], 0]
    else:
        state = [s[0] + (7 - s[0]), s[1] - (7 - s[0])]
    listaDeFilhos.append(state)

    return listaDeFilhos


def estimativaDeCusto(s):
    # Função de custo: Constante = 1
    # Função de Avaliação: Menor diferença entre quantidade atual de liquido e quantidade alvo em um dos recipientes
    # Estimativa de Custo: fa + 1
    if abs(s[0] - 4) <= abs(s[1] - 4):
        return abs(s[0] - 4) + 1
    else:
        return abs(s[1] - 4) + 1


def ordena(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if(estimativaDeCusto(lst[j]) > estimativaDeCusto(lst[j+1])):
                aux = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = aux
    return lst


def buscaAstar(start):
    candidatos = [start]
    pais = dict()
    visitados = [start]

    while len(candidatos) > 0:
        ordena(candidatos)
        pai = candidatos[0]
        print("Lista de candidatos: ", candidatos)
        del candidatos[0]
        print("Visitado: ", pai)
        if isGoal(pai):
            res = []
            node = pai
            while node != start:
                res.append(node)
                node = pais[filhos2str(node)]
            res.append(start)
            res.reverse()
            print("Solucao encontrada: ", res)

        # filhos = geraFilhos(pai)
        # filhosSorted = ordena(filhos)

        for filhos in geraFilhos(pai):
            if filhos not in visitados:
                print("Enfileirado: ", filhos, pai)
                visitados.append(filhos)
                pais[filhos2str(filhos)] = pai
                candidatos.append(filhos)


if __name__ == '__main__':
    buscaAstar([0, 0])


# while len(filhos) > 0:
#     menor = [0, 0]
#     for f in filhos:
#         if estimativaDeCusto(f) <= estimativaDeCusto(menor):
#             menor = f
#             filhosSorted.append(menor)
#             del filhos[0]
