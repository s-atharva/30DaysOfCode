class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edges(self, x, y):
        self.adj_list[x].append(y)
        self.adj_list[y].append(x)

    def display_graph(self):
        print(self.adj_list)


g = Graph(5)
g.add_edges(0, 1)
g.add_edges(0, 2)
g.add_edges(1, 3)
g.add_edges(2, 4)
g.add_edges(3, 4)
g.display_graph()
