from abc import ABC
from typing import List, Optional

class Graph(ABC):
  def __init__(self, V: int) -> None:
    if V < 0:
      raise ValueError('Number of vertices must be non-negative')
    self._V = V
    self._E = 0
    self._adj: List[List[int]] = []
    self._vertex_names: List[Optional[str]] = []
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
    for index in range(self._V):
      self._adj.append([0] * self._V)
      self._vertex_names.append(str(index))

  def add_edge(self, v: int, w: int) -> None:
    self._validate_vertex(v)
    self._validate_vertex(w)
    self._E += 1

  def adj(self, v: int) -> List[int]:
    self._validate_vertex(v)
    return self._adj[v]
  
  def set_vertex_name(self, v: int, name: str) -> None:
    self._validate_vertex(v)
    self._vertex_names[v] = name
    
  def get_vertex_name(self, v: int) -> Optional[str]:
    self._validate_vertex(v)
    return self._vertex_names[v]

  def _validate_vertex(self, v: int) -> None:
    if not (0 <= v < self._V):
      raise ValueError(f'Vertex {v} is not between 0 and {self._V - 1}')

  def dfs(self, source: int, target: int):
    visited = [False] * self._V
    path = []

    def dfs(vertex, target):
      # first mark the vertex as visited and add it to the path
      visited[vertex] = True
      path.append(vertex)
      
      # if we reached the target vertex, return the path
      if vertex == target:
        return path

      # else, visit all adjacent vertices
      for index, val in enumerate(self._adj[vertex]):
        # if the vertex is not visited, and has a weight then visit it
        if not visited[index] and val > 0:
          result_path = dfs(index, target)
          # if the path is found, return itt5
          if result_path:
            return result_path

      # if the path is not found, remove the vertex from the path
      path.pop()
      # and return None so that the parent vertex knows that the path is not found
      return None

    return dfs(source, target)

class DirectedGraph(Graph):
  def add_edge(self, v: int, w: int, weight: int) -> None:
    super().add_edge(v, w)
    self._adj[v][w] = weight
    
  def ford_fulkerson(self, source: int, sink: int) -> int:
    max_flow = 0
    
    path = self.dfs(source, sink)
    while path:
      bottleneck = float('inf')

      for i in range(len(path) - 1):
        v,w = path[i], path[i + 1]
        bottleneck = min(bottleneck, self._adj[v][w])
      
      for i in range(len(path) - 1):
        v,w = path[i], path[i + 1]
        self._adj[v][w] -= bottleneck
        self._adj[w][v] += bottleneck
        
      max_flow += bottleneck
      path_names = [self.get_vertex_name(v) for v in path]
      print("Path:", " -> ".join(path_names), ", Flow adicional:", bottleneck)
      
      path = self.dfs(source, sink)
      
    return max_flow