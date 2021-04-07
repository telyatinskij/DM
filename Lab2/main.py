from munkres import Munkres, print_matrix

def find_eulerian_tour(graph):
    stack = [];
    tour = []

    stack.append(graph[0][0])

    while len(stack) > 0:
        v = stack[len(stack) - 1]

        degree = get_degree(v, graph)

        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, graph)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
    return tour

def get_degree(v, graph):
    degree = 0
    for (x, y) in graph:
        if v == x or v == y:
            degree += 1

    return degree

def get_edge_and_index(v, graph):
    edge = ();
    index = -1

    for i in range(len(graph)):
        if (v == graph[i][0] or v == graph[i][1]):
            edge, index = graph[i], i
            break

    return index, edge

def Dijkstra(N, S, matrix):
    valid = [True]*N
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
                ps = str(str(S) + ':' + str(i))
                if S == ID_min_weight:
                    di[ps] = str(ID_min_weight) + '->' + str(i)
                    di_nu[ps] = [ID_min_weight,i]
                else:
                    ps2 = str(str(S) + ':' + str(ID_min_weight))
                    di[ps] = str(di[ps2]) + ' ' + str(ID_min_weight) + '->' + str(i)
                    di_nu[ps] = di_nu[ps2] + [i]
        valid[ID_min_weight] = False
    return weight

# Вхідні дані: Таблиця зв'язків. Зчитування з масиву або з файлу на вибір
i = [[0, 22, 98, 0, 0, 0, 0, 81],
[22, 0, 0, 62, 87, 0, 0, 99],
[98, 0, 0, 0, 0, 81, 82, 70],
[0, 62, 0, 0, 99, 0, 97, 70],
[0, 87, 0, 99, 0, 0, 13, 0],
[0, 0, 81, 0, 0, 0, 9, 59],
[0, 0, 82, 97, 13, 9, 0, 80],
[81, 99, 70, 70, 0, 59, 80, 0]]

f = open('l2-3.txt', 'rt')
m = []
i = 0
for line in f: #
    lines = line.split(' ')
    lst = []
    for ln in lines:
        ln = ln.rstrip()
        if ln != '':
            num = int(ln)
            lst = lst + [num]
    m = m + [lst]
print("Вхідні дані = ", m)
f.close()
for i in range(len(m)):
    for j in range(len(m)):
        if i != j and m[i][j] == 0:
            m[i][j] = 1000000

#Кількість зв*язків в кожній вершині
b = [0]*len(m)
for i in range(len(m)):
    for j in range(len(m)):
        if (m[i][j] > 0) & (m[i][j] < 1000000):
            b[i] = b[i] + 1

# Вершини з непарн. к-тю ребер
nech = []
for i in range(len(b)):
    if (b[i] == 0):
        print("Незв'язний граф")
    elif (b[i]%2 == 1):
        nech.append(i)

# Будуємо матрицю найкоротших шляхів і створюємо масив переходів
nech_m = []

n = len(m)
di = {}
di_nu = {}

for x in range(len(m)):
    nech_m.append(Dijkstra(n, x, m))

# Будуємо матрицю для пошуку відповідностей

par = []
for i in range(len(nech_m)):
    vr = []
    for j in range(len(nech_m)):
        if (i in nech) and (j in nech):
            vr.append(nech_m[i][j])
    if vr != []:
        par.append(vr)

for i in range(len(par)):
    for j in range(len(par)):
        if (par[i][j] == 0):
            par[i][j] = 100000

#Найкоротші відповідності

matrix = par
Mu = Munkres()
indexes = Mu.compute(matrix)

total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value

# Вибираємо ребра для дублювання

indexes2 = []
for i,j in indexes:
    if ((nech[i],nech[j]) not in indexes2) and ((nech[j],nech[i]) not in indexes2):
        indexes2.append((nech[i],nech[j]))

b = []
for k,l in indexes2:
    text = str(k) + ":" + str(l)
    for r in range(len(di_nu[text]) - 1):
        b.append((di_nu[text][r],di_nu[text][r+1]))

# Визначаємо початкові ребра

a = []
for i in range(len(m)):
    for j in range(len(m)):
        if (m[i][j] > 0) & (m[i][j] < 1000000) & (i < j):
            d = (i,j)
            a.append(d)

# З'єднуємо і знаходимо Ейлеровий цикл
graph = a + b
print ("ЕЙЛЕРОВИЙ ЦИКЛ:")
print (find_eulerian_tour(graph))

# Сумарна вага
graph = a + b
SUM = 0
for x in range(len(graph)):
    SUM = SUM + m[graph[x][0]][graph[x][1]]

print ("Сумарна вага:", SUM)
