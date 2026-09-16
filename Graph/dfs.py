class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, x, y):
        self.adj_list[x].append(y)
        self.adj_list[y].append(x)

    def display_graph(self):
        print(self.adj_list)

    def dfs(self, start):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            print(node)
            for neighbour in self.adj_list[node]:
                if neighbour not in visited:
                    dfs_helper(neighbour)

        dfs_helper(start)


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.dfs(0)
