import sys
inpt = sys.argv[1]
def bomb(i):
    global score
    liste = []
    for x in range(len(matris)):
        if matris[x][i[1]] == "X":
            score += scores[matris[x][i[1]]]
            matris[x][i[1]] = " "
            bomb([x,i[1]])
        if [x,i[1]] not in liste:
            liste.append([x,i[1]])
        score += scores[matris[x][i[1]]]
        matris[x][i[1]] = " "
    for y in range(len(matris[0])):
        if matris[i[0]][y] == "X":
            score += scores[matris[i[0]][y]]
            matris[x][i[1]] = " "
            bomb([i[0],y])
        if [i[0],y] not in liste:
            liste.append([i[0],y])
        score += scores[matris[i[0]][y]]
        matris[i[0]][y] = " "
    return liste
def score_keep(key, tuple):
    global score
    score += scores[key] * len(tuple)
def search(i, indexes):
    try:
        if matris[i[0]][i[1]] == matris[i[0]+1][i[1]]:
            i[0] += 1
            if not [i[0], i[1]] in indexes:
                indexes.append([i[0], i[1]])
                search(i, indexes)
            i[0] -= 1
    except:pass
    try:
        if matris[i[0]][i[1]] == matris[i[0]-1][i[1]]:
            if not i[0] - 1 == -1:
                i[0] -= 1
                if not [i[0], i[1]] in indexes:
                    indexes.append([i[0], i[1]])
                    search(i, indexes)
                i[0] += 1
    except:pass
    try:
        if matris[i[0]][i[1]] == matris[i[0]][i[1]+1]:
            i[1] += 1
            if not [i[0], i[1]] in indexes:
                indexes.append([i[0], i[1]])
                search(i, indexes)
            i[1] -= 1
    except:pass
    try:
        if matris[i[0]][i[1]] == matris[i[0]][i[1]-1]:
            if not i[1] - 1 == -1:
                i[1] -= 1
                if not [i[0], i[1]] in indexes:
                    indexes.append([i[0], i[1]])
                    search(i, indexes)
                i[1] += 1
    except:pass
    if len(indexes) == 1: indexes = []
    return indexes
def edit(tuple):
    for indexes in tuple: matris[indexes[0]][indexes[1]] = " "
def reshape(matris, liste):
    liste.sort()
    for z in liste:
        for i in range(z[0]):
            matris[z[0]-i][z[1]] = matris[z[0]-i-1][z[1]]
            matris[z[0]-i-1][z[1]] = " "
    for sublist in matris:
        if sublist.count(" ") == len(matris[0]): matris.remove(sublist)
    temp = 0
    delete = []
    for l in range(len(matris[0])):
        for t in range(len(matris)):
            if matris[t][l] == " ":
                temp += 1
        if temp == len(matris): delete.append(l)
        temp = 0
    delete.sort(reverse=True)
    for n in delete:
        for c in range(len(matris)):matris[c].pop(n)
def check():
    ind = [[x, y] for x in range(len(matris)) for y in range(len(matris[0]))]
    for i in ind:
        if matris[i[0]][i[1]] == " ": continue
        elif matris[i[0]][i[1]] == "X": return True
        try:
            if matris[i[0]][i[1]] == matris[i[0]+1][i[1]]: return True
        except:pass
        try:
            if matris[i[0]][i[1]] == matris[i[0]-1][i[1]]:
                if not i[0] - 1 == -1: return True
        except:pass
        try:
            if matris[i[0]][i[1]] == matris[i[0]][i[1]+1]: return True
        except:pass
        try:
            if matris[i[0]][i[1]] == matris[i[0]][i[1]-1]:
                if not i[1] - 1 == -1: return True
        except:pass
    return False
def show_matris(matris):
    for line in matris: print("  ".join(line))
if __name__ == '__main__':
    matris = []
    score = 0
    scores = {"B": 9, "G": 8, "W":  7, "Y": 6, "R": 5, "P": 4, "O": 3, "D": 2, "F": 1, "X": 0, " ": 0}
    file = open(inpt, "r+")
    for line in file.readlines(): matris.append(line.rstrip("\n").split())
    while check():
        stats = True
        show_matris(matris)
        print("\nYour score is: {}\n".format(score))
        while stats:
            try:
                i = list(map(int, input("Please enter a row and column number: ").split()))
                if i[0] >= len(matris) and i[1] >= len(matris[0]) or matris[i[0]][i[1]] == " ":
                    print("Please enter a valid size!")
                else: stats = False
            except: print("You entered wrong input")
        key = matris[i[0]][i[1]]
        indexes = [[i[0], i[1]]]
        if matris[i[0]][i[1]] == "X":
            reshape(matris,bomb(i))

        else:
            liste = search(i, indexes)
            edit(liste)
            in1 = len(matris)
            in2 = len(matris[0])
            reshape(matris, liste)
            score_keep(key, liste)
    show_matris(matris)
    print("\nYour score is: {}\n".format(score))
    print("Game over!")
