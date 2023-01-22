class Vertex:
    def __init__(self, name):
        self.name = name
        self._neighbours = set()
        self._marked: bool = False

    def add_neighbour(self, new_neighbour: 'Vertex'):
        self._neighbours.add(new_neighbour)

    def get_name(self):
        return self.name

    def is_marked(self):
        return self._marked

    def mark(self):
        self._marked = True

    def __iter__(self):
        return iter(self._neighbours)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Graph:
    def __init__(self, edges: dict):
        self._vertices = {name: Vertex(name) for name in edges.keys()}
        for name, neighbours in edges.items():
            current_vertex = self._vertices[name]
            for neighbour in neighbours:
                current_vertex.add_neighbour(self._vertices[neighbour])

    def find_shortest_way(self, start: str, finish: str, path=None):
        if path is None:
            path = []
        start_vertex = self._vertices[start]
        path = path + [start_vertex]
        if start == finish:
            return path
        if start not in self._vertices:
            return None
        shortest_path = None
        for neighbour in self._vertices[start]:
            if neighbour not in path:
                sp = self.find_shortest_way(neighbour.get_name(), finish, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


my_edges = {
         '1': ['2', '3', '4'],
         '2': ['1', '5', '6'],
         '3': ['1'],
         '4': ['1', '7', '8'],
         '5': ['2', '9', '10'],
         '6': ['2', '11', '12'],
         '7': ['4', '13', '14'],
         '8': ['4', '15', '16'],
         '9': ['5'],
         '10': ['5'],
         '11': ['6'],
         '12': ['6'],
         '13': ['7'],
         '14': ['7'],
         '15': ['8'],
         '16': ['8'],
         }

graph = Graph(my_edges)
print(graph.find_shortest_way('11', '16'))
