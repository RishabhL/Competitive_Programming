graph = {"A": {"B": 7, "D": 3},
         "B": {"A": 7, "D": 2, "C": 3},
         "C": {"B": 3, "D": 4, "E": 1},
         "D": {"A": 3, "B": 2, "C": 4, "E": 7},
         "E": {"C": 1, "D": 7}}

INF = 999999
distances = {"A": 0}
for k in range(1, len(graph.keys())):
    distances[list(graph.keys())[k]] = INF

queue = []


def update_queue():
    global queue, distances
    queue = []
    for n in distances.keys():
        queue.append((distances[n], n))
    queue = sorted(queue)


update_queue()


while len(queue) != 0:
    currentnode = queue.pop(0)[1]
    for neighbour in graph[currentnode]:
        new_distance = graph[currentnode][neighbour] + distances[currentnode]
        if new_distance < distances[neighbour]:
            distances[neighbour] = new_distance
            update_queue()

print(distances)