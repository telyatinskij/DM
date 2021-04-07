from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

f = open('l3-3.txt', 'rt')
data2 = []
i = 0
for line in f:
    lines = line.split(' ')
    lst = []
    for ln in lines:
        ln = ln.rstrip()
        if ln != '':
            num = int(ln)
            lst = lst + [num]
    data2 = data2 + [lst]
print("Вхідні дані = ", data2)
f.close()

def create_data_model():
    data = {}
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def print_solution(manager, routing, solution):
    print('Довжина маршруту: {} '.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Шлях проходить з 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Відстань: {}\\n'.format(route_distance)


def main():
    # дані
    data = create_data_model()

    # індекси маршрутизації
    manager = pywrapcp.RoutingIndexManager(len(data2),
                                           data['num_vehicles'], data['depot'])

    # Створення модель маршрутизації.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        # відстань між двома вузлами.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data2[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # вартість кожної дуги
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(manager, routing, solution)

if __name__ == '__main__':
    main()