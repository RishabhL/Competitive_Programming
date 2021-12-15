graph = {"A": {"visited": False, "neighbours": ["B", "D", "E"]},
         "B": {"visited": False, "neighbours": ["A", "C", "D"]},
         "C": {"visited": False, "neighbours": ["B", "G"]},
         "D": {"visited": False, "neighbours": ["A", "B", "E", "F"]},
         "E": {"visited": False, "neighbours": ["A", "D"]},
         "F": {"visited": False, "neighbours": ["D"]},
         "G": {"visited": False, "neighbours": ["C"]}}


def breath_first_search():
    queue = []
    visited = []
    currentNode = None

    queue.append("A")

    while len(queue) != 0:
        currentNode = queue.pop(0)
        visited.append(currentNode)
        graph[currentNode]["visited"] = True
        for neighbour in graph[currentNode]["neighbours"]:
            if graph[neighbour]["visited"] is False and neighbour not in queue:
                queue.append(neighbour)

    return visited


print(breath_first_search())


