t = []

def isGoal(s):
    goal = False
    if s[0] == 4 or s[1] == 4:
        goal = True
    return goal


def generateSons(s):

    # esvaziar o pote 1
    state = [0, s[1]]
    if s[0] == 7 and s[1]>0:
        t.append(state)
        print("filho: ",state)

    # esvaziar o pote 2
    state = [s[0], 0]
    if s[1] == 5 and s[0]>0:   #só ezvazia se esviter cheio
        t.append(state)
        print("filho: ",state)

    # encher o pote 1
    state = [7, s[1]]
    if s[0] == 0 and s[1]!=5:   #só enche se estiver vazio e não deixa os dois cheios
        t.append(state)
        print("filho: ",state)

    # encher o pote 2
    state = [s[0], 5]
    if s[1] == 0 and s[0]!=7:
        t.append(state)
        print("filho: ",state)

    # verter pote 1 no pote 2
    if s[0] > 0 and s[1]<5:     #só passa se tiver o que passar e pote 2 já não estiver cheio
        if s[0] >= 5-s[1]:
            state = [s[0]-(5-s[1]), 5]
        else:
            state = [0, s[1] + s[0]]
        t.append(state)
        print("filho: ",state)

     # verter pote 2 no pote 1
    if s[1] > 0 and s[0]<7:
        if s[1] <= 7-s[0]:
            state = [s[0]+s[1], 0]
        else:
            state = [s[0] + (7 - s[0]), s[1] - (7 - s[0])]
        t.append(state)
        print("filho: ",state)



def dfs(start):
    s = start
    i = 0
    x = 0
    g = []
    generateSons(s)
    print(s)
    for i in range(100):
        print("Nó visitado: ",t[i])
        if isGoal(t[i]):
            g = t[i]
            x = i
            break
        generateSons(t[i])

def main():
    dfs([0,0])
    end = input("fim da execução")

