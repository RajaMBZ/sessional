def readGraph():
    graph = {}

    N = 13

    for i in range(N):

            if(i==1): line = "Arad Zerind 75 Timisoara 118 Sibiu 140"
            if(i==2): line = "Zerind Oradea 71 Arad 75"
            if(i==3): line = "Timisoara Arad 118 Lugoj 111"
            if(i==4): line = "Sibiu Arad 140 Oradea 151 Fagaras 99 RimnicuVilcea 80"
            if(i==5): line = "Oradea Zerind 71 Sibiu 151"
            if(i==6): line = "Lugoj Timisoara 111 Mehadia 70"
            if(i==7): line = "RimnicuVilcea Sibiu 80 Pitesti 97 Craiova 146"
            if(i==8): line = "Mehadia Lugoj 70 Dobreta 75"
            if(i==9): line = "Craiova Dobreta 120 RimnicuVilcea 146 Pitesti 138"
            if(i==10): line = "Pitesti RimnicuVilcea 97 Craiova 138 Bucharest 101"
            if(i==11): line = "Fagaras Sibiu 99 Bucharest 211"
            if(i==12): line = "Dobreta Mehadia 75 Craiova 120"
            if(i==13): line = "Bucharest Fagaras 211 Pitesti 101"

        tokens = line.split()

        node = tokens[0]
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            graph[node][tokens[i]] = int(tokens[i + 1])

    return graph

def __findPathDFS(graph, current, goal, visited):
    if current == goal:
        return [current]

    if current in graph:
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add( neighbor )
                path = __findPathDFS(graph, neighbor, goal, visited)

                if path is not None:
                    path.insert(0, current)
                    return path
    return None

def findPathDFS(graph, start, goal):
    if start not in graph or goal not in graph:
        return False

    visited = set()
    visited.add( start )

    return __findPathDFS(graph, start, goal, visited)

graph = readGraph()

print( findPathDFS(graph, 'Arad', 'Bucharest') )
