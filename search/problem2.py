from typing import Dict, Generator, List, Tuple
from itertools import islice
from queue import PriorityQueue

graph = {
    'S': (set(['A', 'B', 'D'])),
    'A': (set(['C'])),
    'B': (set(['D'])),
    'C': (set(['D', 'G'])),
    'D': (set(['G'])),
    'G': (set())
    }

weights = {
    ('S','A'):2,
    ('S','B'):3,
    ('S','D'):5,
    ('A','C'):4,
    ('B','D'):4,
    ('C','D'):1,
    ('C','G'):2,
    ('D','G'):5,
}

def bfs_paths(graph: Dict[str, set], start: str, goal: str)-> Generator:
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next] #use the + operator to yield the extended list inline
            else:
                queue.append((next, path + [next]))

def dfs_paths(graph: Dict[str, set], start: str, goal: str)-> Generator:
    """
    generator that yields the possible
    paths when searching the graph using depth-first-search
    """
    stack = [(start, [start])] #stack is a list of tuples representing the vertex and the current path
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next] #use the + operator to yield the extended list inline
            else:
                stack.append((next, path + [next]))

def ucs_weight(from_node: str, to_node: str, weights: str):
    return weights.get((from_node, to_node))


def ucs(graph: Dict[str, set], start: str, end: str, weights: Dict[Tuple[str, str], int])->Generator:
    """
    generator that yeilds the possible
    paths when searching the graph using uniform cost search
    """
    frontier = PriorityQueue()
    frontier.put((0, start, []))  # (priority, node, path)
    explored = []
    while True:
        ucs_w, current_node, path = frontier.get()
        explored.append(current_node)
        if current_node == end:
            yield (path + [current_node],ucs_w)
        for node in graph[current_node]:
            if node not in explored:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node,
                    path + [current_node]
                ))


if __name__ == "__main__":
    dfs_result = next(dfs_paths(graph, 'S', 'G'))
    bfs_result = next(bfs_paths(graph, 'S', 'G'))
    ucs_result, ucs_w = next(ucs(graph, 'S', 'G', weights))
    print(f'DFS: {dfs_result}\nBFS: {bfs_result}\nUCS: {ucs_result} with a cost of {ucs_w}')
