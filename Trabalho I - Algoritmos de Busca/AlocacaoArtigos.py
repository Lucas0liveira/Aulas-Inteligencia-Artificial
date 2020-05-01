import random as rng
import numpy as np

matrizDeAfinidade = []


class AlocacaoArtigos:

    def __init__(self, dataFilePath):

        self.dataFilePath = dataFilePath
        self.loadDataFromFile()

    def loadDataFromFile(self):
        dataSetLoded = np.loadtxt(self.dataFilePath, delimiter=',')
        self.nArtigos = len(dataSetLoded[0]) - 1
        self.individuos = []
        # TODO refatorar para codigo mais bonito
        for i in dataSetLoded:
            artigos = []
            capacidade = 0
            for j in range(len(i)):
                if j < self.nArtigos:
                    artigos.append(i[j])
                else:
                    capacidade = i[j]
            self.individuos.append([artigos, capacidade])
        # matrizDeAfinidade.append(self.individuos)
        matrizDeAfinidade.append(self.individuos)

    def run(self):
        print('running')
        print(matrizDeAfinidade)  # matriz para referencia de afinidade
        print(matrizDeAfinidade[0][2])  # recuperando um individuo na matriz

    def initialize(matrizDeAfinidade):  # gera a população inicial aleatoriamente
        return

    # valida um individuo de acordo com seus limites e distribuição de artigos
    def validate(individuo):
        return

    def mutate(individuo):  # causa mutação em um individuo, descartando resultados inválidos
        return

    # mescla parte de um individuo com parte de outro, descartando resultados invalidos
    def reproduce(individuo1, individuo2):
        return

    def selection(individuo):  # seleciona os individuos mais adaptados para a próxima geração
        return

    def fitness(individuo):  # Função fitness do individuo, baseada na média de afinidade entre os revisores e artigos
        return

    # função principal, aloca revisores e artigos usando mutação, reprodução e seleção.
    def alocate(population):
        return


if __name__ == '__main__':
    geneticAlg = AlocacaoArtigos("./database.txt")
    geneticAlg.run()
