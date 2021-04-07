def cheapest_edge(graph, component):
    # список ваг та вузлів
    values_withindexes = []
    for i in component:
        for j in range(len(graph[i])):
            if graph[i][j] != 0 and j not in component:
                # додавання ваги, та два вузли
                values_withindexes.append((graph[i][j], min(i, j), max(i, j)))
    counter = 0
    for i in values_withindexes:
        if counter == 0:
            cheapestEdge = i
        if cheapestEdge[0] > i[0]:
            cheapestEdge = i
        counter += 1

    return cheapestEdge


def merge_common(llist):
    components = []
    for i in llist:
        if len(components) == 0:
            # перший елемент у списку встановлюється як компонент
            components.append(i)
            continue
        if len(components) > 0:
            in_list = False

            for component in range(len(components)):
                if common_value(i, components[component]):
                    # Елемент у списку додається до компонента, коли вони мають спільне значення
                    in_list = True
                    components[component] = components[component] + i
                    continue

            if in_list == False:
                #якщо не знайдено у поточному компоненті
                components.append(i)
    new_components = []
    for i in components:
        new_components.append(list(set(i)))
    return new_components

def common_value(list1, list2):

    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

    return result

def boruvkas(graph):

    components = [[i] for i in range(len(graph))]
    MST = []
    while len(components) > 1:
        cheapest_edges = []
        for i in range(len(components)):
            # створити список для всіх компонентів
            if cheapest_edge(graph, components[i]) not in cheapest_edges:
                cheapest_edges.append(cheapest_edge(graph, components[i]))
        mergers = cheapest_edges
        MST.append(mergers)
        new_components = []
        for i in mergers:
            for j in components:
                # якщо будь-яке значення знаходиться в поточному компоненті, це значення із злиття додається до списку new_components
                if i[1] in j:
                    merge_a = j

                if i[2] in j:
                    merge_b = j

            new_components.append(merge_a + merge_b)
        # ця функція перевіряє новий список компонентів та об'єднує спільні значення
        components = merge_common(new_components)
    return sum(MST, [])

graph2 = [
    [0, 0, 38, 95, 0, 1, 57, 0],
    [0, 0, 0, 0, 79, 0, 36, 19],
    [38, 0, 0, 51, 0, 0, 44, 0],
    [95, 0, 51, 0, 0, 44, 0, 0],
    [0, 79, 0, 0, 0, 93, 41, 48],
    [1, 0, 0, 44, 93, 0, 1, 0],
    [57, 36, 44, 0, 41, 1, 0, 0],
    [0, 19, 0, 0, 48, 0, 0, 0]
]

f = open('l1_3.txt', 'rt')
M2 = []
#Читання даних з файлу та утворення нової матриці
i = 0
for line in f:
    # Конвертувати рядок line в список рядків
    lines = line.split(' ')
    # тимчасовий список
    lst = []
    for ln in lines:
        ln = ln.rstrip()
        if ln != '':
            num = int(ln)
            lst = lst + [num]
    M2 = M2 + [lst] # додати рядок до результуючої матриці
print("Вхідні дані = ", M2)
f.close()

print("------------------------------------------------")
print("Мінімальне покриваюче дерево (Вага, Вершина1, Вершина2)  ", boruvkas(M2))
total = 0
for i in boruvkas(M2):
    total += i[0]

print("Загальна вага: ", total)