graph = {"A": {"neighbours": ["B", "D", "E"]},
         "B": {"neighbours": ["A", "C", "D"]},
         "C": {"neighbours": ["B", "G"]},
         "D": {"neighbours": ["A", "B", "E", "F"]},
         "E": {"neighbours": ["A", "D"]},
         "F": {"neighbours": ["D"]},
         "G": {"neighbours": ["C"]}}
visited = []


def depth_first_search(currentNode):
    global visited, graph
    visited.append(currentNode)
    for neighbour in graph[currentNode]["neighbours"]:
        if neighbour not in visited:
            depth_first_search(neighbour)
    return visited


print(depth_first_search("A"))
