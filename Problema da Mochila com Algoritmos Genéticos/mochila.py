import random


class objetos:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor


peso_max = 0

lista_objetos = []
lista_objetos.append(objetos(4, 2))
lista_objetos.append(objetos(3, 7))
lista_objetos.append(objetos(2, 5))
lista_objetos.append(objetos(1, 1))
lista_objetos.append(objetos(3, 9))
lista_objetos.append(objetos(1, 2))
lista_objetos.append(objetos(5, 3))
lista_objetos.append(objetos(4, 4))
lista_objetos.append(objetos(4, 4))
lista_objetos.append(objetos(3, 7))

#lista_objetos.append(objetos(4, 2))
#lista_objetos.append(objetos(5, 2))
#lista_objetos.append(objetos(7, 3))
#lista_objetos.append(objetos(9, 4))
#lista_objetos.append(objetos(6, 4))


# inicialização
# produz sempre 8 individuos válidos
população_inicial = []


class individuo:
    def __init__(self, cromossomo, peso, valor):
        self.cromossomo = cromossomo
        self.peso = peso
        self.valor = valor


def inicializar(tamanho_população, tamanho_mochila, peso_maximo):
    c = 0
    peso_max = peso_maximo
    while(c < tamanho_população):
        cromossomo = []
        for p in range(0, tamanho_mochila):
            cromossomo.append(random.randint(0, 1))
        print(cromossomo)
        if(validar(cromossomo)):
            c += 1
            população_inicial.append(
                individuo(cromossomo, getPeso(cromossomo), getValor(cromossomo)))
    print("\nPopulação:")
    for i in população_inicial:
        print(i.cromossomo)


def getValor(cromossomo):
    valor = 0
    for i in range(0, len(cromossomo)):
        if(cromossomo[i] != 0):
            valor += lista_objetos[i].valor
    return valor


def getPeso(cromossomo):
    peso = 0
    for i in range(0, len(cromossomo)):
        if(cromossomo[i] != 0):
            peso += lista_objetos[i].peso
    return peso


def validar(cromossomo):
    if getPeso(cromossomo) <= peso_max and getPeso(cromossomo) != 0:
        return True
    else:
        print("\nCromossomo Inválido")
        return False

# função Fitness, determina a adequação do individuo para o ambiente


def fitness(população):
    fitness_população = []
    for individuo in população:
        fitness = individuo.valor
        fitness_população.append(fitness)
    print("\nFitness da população:")
    print(fitness_população)
    print("\nFitness total")
    print(fitness_total(fitness_população))
    return fitness_população


def fitness_total(fitness):
    soma = 0
    for i in fitness:
        soma += i
    return soma

# seleção randomica, seleciona os individuos pelo metodo da roleta


def seleção(population, fitness):
    # calcula o fitness total
    ftotal = 0
    for f in fitness:
        ftotal += f

    # define a chance de seleção de cad aindividuo
    chance_seleção = []
    chão = 0
    for ind in population:
        chance_ind = (360 * ind.valor) / ftotal
        chance_seleção.append((chão, chão + chance_ind))
        chão += chance_ind

    # sorteia um intervalo aleatório
    sorteado = random.randint(0, 359)

    # retorna o individuo selecionado
    for i in range(0, len(population)):
        if(sorteado >= chance_seleção[i][0] and sorteado < chance_seleção[i][1]):
            return population[i]


def reproduce(x, y):
    xc = x.cromossomo
    yc = y.cromossomo
    n = len(xc)
    novo_cromossomo = []
    corte = random.randrange(1, n)
    novo_cromossomo = xc[0:corte] + yc[corte:n]
    if(validar(novo_cromossomo) == False):
        rand = random.randrange(0, 1)
        if(rand == 0):
            pai_aleatorio = xc
        else:
            pai_aleatorio = yc
        novo_cromossomo = pai_aleatorio
    return individuo(novo_cromossomo, getPeso(
        novo_cromossomo), getValor(novo_cromossomo))


def mutate(child):
    cc = child.cromossomo
    valido = False
    while(valido == False):
        pos = random.randrange(0, len(cc))
        if(cc[pos] == 0):
            cc[pos] = 1
        else:
            cc[pos] = 0
        if(validar(cc) == True):
            valido = True
    mutated = individuo(cc, getPeso(cc), getValor(cc))
    return mutated


def getBest(population):
    fit = fitness(population)
    maior_fit = 0
    best = population[0]
    for i in range(0, len(population)):
        if(fit[i] > maior_fit):
            maior_fit = fit[i]
            best = population[i]
    print("\nMELHOR INDIVIDUO: " + str(best.cromossomo) +
          "\nPeso: " + str(best.peso) + "\nValor: " + str(best.valor))
    return fit[0]


def genetic_algorithm(population):
    for i in range(0, 250):
        fit = fitness(population)
        new_population = []
        for i in range(0, len(population)):
            x = seleção(population, fit)
            y = seleção(population, fit)
            child = reproduce(x, y)
            mutation_chance = random.random()
            if(mutation_chance < 0.3):
                child = mutate(child)
            new_population.append(child)
        print('\nNOVA POPULAÇÃO: \n')
        population = new_population

        for i in population:
            print(str(i.cromossomo))

    return getBest(population)


if __name__ == '__main__':
    inicializar(10, 10, 15)
    genetic_algorithm(população_inicial)
