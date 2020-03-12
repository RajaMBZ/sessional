def readGraph():
    graph = {}
    N = 13
    for i in range(N):
        line = input()
        tokens = line.split()

        node = tokens[0]
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph

def second(graph, current, goal, visited):
    if current == goal:
        return [current]
    if current in graph:
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add( neighbor )
                path = second(graph, neighbor, goal, visited)
                if path is not None:
                    path.insert(0, current)
                    return path
    return None

def findPathDFS(graph, start, goal):
    if start not in graph or goal not in graph:
        return False

    visited = set()
    visited.add( start )

    return second(graph, start, goal, visited)

graph = readGraph()

print( findPathDFS(graph, 'Arad', 'Bucharest') )
