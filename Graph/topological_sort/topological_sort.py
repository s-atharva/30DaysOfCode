class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs(self, i, visited, my_stack):
        visited[i] = 1
        for neighbour in self.adj_list[i]:
            if visited[neighbour] == 0:
                self.dfs(neighbour, visited, my_stack)
        my_stack.append(i)

    def topological_sort(self, vertices):
        my_stack = []
        visited = [0 for _ in range(vertices)]
        for i in range(vertices):
            if visited[i] == 0:
                self.dfs(i, visited, my_stack)
        return my_stack[::-1]


V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]

graph = Graph(V)
for x, y in edges:
    graph.add_edge(x, y)

print(graph.topological_sort(vertices=V))
