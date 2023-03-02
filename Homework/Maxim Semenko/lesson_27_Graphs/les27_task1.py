from collections import defaultdict


class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)

    def add_edge(self, start, finish):
        self.graph[start].append(finish)

    def depth_first_search(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.depth_first_search(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(d)

    def transpose(self):
        graph = Graph(self.vertex)

        for i in self.graph:
            for j in self.graph[i]:
                graph.add_edge(j, i)
        return graph

    def print_strongly_connected_components(self):
        stack = []
        visited_vertex = [False] * self.vertex
        for i in range(self.vertex):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        gr = self.transpose()
        visited_vertex = [False] * self.vertex
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.depth_first_search(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_strongly_connected_components()
