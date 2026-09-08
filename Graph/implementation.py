class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]
        # [[], [], [], [], []]

    def add_edge(self, i, j):
        self.adj[i].append(j)
        self.adj[j].append(i)

    def print_graph(self):
        print(self.adj)
        for i in range(self.vertices):
            print(f'{i} -> {self.adj[i]}')


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.print_graph()
