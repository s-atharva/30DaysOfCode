from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, x, y):
        self.adj_list[x].append(y)
        self.adj_list[y].append(x)
        # [
        #     [1, 2],
        #     [0, 3],
        #     [0, 4],
        #     [1, 4],
        #     [2, 3]
        # ]

    def display(self):
        print(self.adj_list)

    def bfs(self, start):
        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)

        # as long as there is something in queue. Keep Searching
        while queue:
            node = queue.popleft()
            print(node)
            for neighbours in self.adj_list[node]:
                if neighbours not in visited:
                    visited.add(neighbours)
                    queue.append(neighbours)


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.bfs(0)
