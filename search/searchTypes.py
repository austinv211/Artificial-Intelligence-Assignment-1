from typing import List, Dict

class Edge():
    def __init__(self, start_vertex, end_vertex, value):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.value = value

    def __repr__(self):
        return f'({self.start_vertex},{self.end_vertex},{self.value})'


class Vertex():
    def __init__(self, identity, edges: List[Edge]):
        self.identity = identity
        self.edges = edges

    def neighbors(self):
        return [edge for edge in self.edges]

    def shortest_path_to_neighbor(self):
        if len(self.neighbors()) != 0:
            return min([(edge.end_vertex, edge.value) for edge in self.edges], key=lambda x: x[1])[0]
        else:
            return None
    
    def longest_path_to_neighbor(self):
        if len(self.neighbors()) != 0:
            return max([(edge.end_vertex, edge.value) for edge in self.edges], key=lambda x: x[1])[0]
        else:
            return None

    def __repr__(self):
        return f'{self.identity} -> {[edge for edge in self.edges]}'
    
    def __str__(self):
        return f'{self.identity}'


def parse_dict_into_graph(graph_dict: dict):
    graph = {}
    for key, connections in graph_dict.items():
        vertex = Vertex(key, [Edge(key, connection[0], connection[1]) for connection in connections])
        graph[key] = vertex
    return graph

graph = parse_dict_into_graph({
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)],
    'G': []
})

def simplify_path(path_dict, start, goal):
    simplified_path = [goal]
    previous = path_dict[goal].start_vertex
    while previous != start:
        simplified_path.append(previous)
        previous = path_dict[previous].start_vertex
    simplified_path.append(start)
    simplified_path.reverse()
    print(simplified_path)
        

def bfs(graph: Dict[str, Vertex], start_vertex: str, goal: str):
    queue, visited, path = [graph[start_vertex]], set(start_vertex), {}
    while queue:
        s = queue.pop(0) 
        for i in s.neighbors(): 
            if i.end_vertex not in visited:
                path[i.end_vertex] = i
                queue.append(graph[i.end_vertex])
                visited.add(i.end_vertex)
                if i.end_vertex == goal:
                    break
    return simplify_path(path, start_vertex, goal)

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

    



if __name__ == "__main__":
    bfs(graph, 'S', 'G')
    print(list(dfs_paths(graph1, 'C', 'F')))