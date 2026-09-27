class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edges(self, source, destination):
        self.adj_list[source].append(destination)

    def dfs(self, i, visited, my_stack):
        visited[i] = 1

        for adj_node in self.adj_list[i]:
            if visited[adj_node] == 0:
                self.dfs(adj_node, visited, my_stack)

        my_stack.append(i)

    def topo_sort(self):
        visited = [0] * self.vertices
        my_stack = []

        for i in range(self.vertices):
            if visited[i] == 0:
                self.dfs(i, visited, my_stack)

        return my_stack[::-1]


vertices = 6

edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

graph = Graph(vertices)

for source, destination in edges:
    graph.add_edges(source, destination)

result = graph.topo_sort()

print(result)
