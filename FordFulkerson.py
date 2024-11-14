from abc import ABC
from typing import List

class Graph(ABC):
  def __init__(self, V: int) -> None:
    if V < 0:
      raise ValueError('Number of vertices must be non-negative')
    self._V = V
    self._E = 0
    self._adj: List[List[int]] = []
    self.clear()

  def __len__(self) -> int:
    return self._V

  def __str__(self) -> str:
    to_string: str = '\n'
    for i in range(self._V):
      to_string += f'[{i}] => {self._adj[i]}\n'
    return to_string

  def is_empty(self) -> bool:
    return self._V == 0

  def clear(self) -> None:
    self._E = 0
    self._adj: List[List[int]] = []
    for _ in range(self._V):
      self._adj.append([])

  def add_edge(self, v: int, w: int) -> None:
    self._validate_vertex(v)
    self._validate_vertex(w)
    self._E += 1

  def adj(self, v: int) -> List[int]:
    self._validate_vertex(v)
    return self._adj[v]

  def _validate_vertex(self, v: int) -> None:
    if not (0 <= v < self._V):
      raise ValueError(f'Vertex {v} is not between 0 and {self._V - 1}')

  def dfs(self, s: int, t: int):
        visited = [False] * self._V
        path = []

        def dfs(v, t):
          # first mark the vertex as visited and add it to the path
          visited[v] = True
          path.append(v)
          
          # if we reached the target vertex, return the path
          if v == t:
            return path

          # else, visit all adjacent vertices
          for w in self.adj(v):
            # if the vertex is not visited, recursively visit it 
            if not visited[w]:
              result_path = dfs(w, t)
              # if the path is found, return it
              if result_path:
                return result_path

          # if the path is not found, remove the vertex from the path
          path.pop()
          # and return None so that the parent vertex knows that the path is not found
          return None

        return dfs(s, t)

class DirectedGraph(Graph):
  def add_edge(self, v: int, w: int) -> None:
    super().add_edge(v, w)
    self._adj[v].append(w)
    
def ford_fulkerson(graph: DirectedGraph, source: int, sink: int) -> int:
  max_flow = 0
  
  path = graph.dfs(source, sink)
  while path:
    bottleneck = float('inf')
    for i in range(len(path) - 1):
      v,w = path[i], path[i + 1]
      for edge in graph.adj(v):
        if edge == w:
          bottleneck = min(bottleneck, edge.weight)
          break
      for edge in graph.adj(w):
        if edge == v:
          edge.weight += bottleneck
          break
    max_flow += bottleneck
    path = graph.dfs(source, sink)

if __name__ == '__main__':
  V = 5
  graph = DirectedGraph(V)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(1, 3)
  graph.add_edge(3, 4)
  print(graph.dfs(0, 4))