from FordFulkerson import DirectedGraph

def water_pipes_example():
  V = 6
  graph = DirectedGraph(V)
  graph.set_vertex_name(0, "Novo Hamburgo")
  graph.set_vertex_name(1, "São Leopoldo")
  graph.set_vertex_name(2, "Canoas")
  graph.set_vertex_name(3, "Porto Alegre")
  graph.set_vertex_name(4, "Gravataí")
  graph.set_vertex_name(5, "Cachoeirinha")
  
  graph.add_edge(0, 1, 16)
  graph.add_edge(0, 2, 13)
  graph.add_edge(1, 2, 10)
  graph.add_edge(1, 3, 12)
  graph.add_edge(2, 1, 4)
  graph.add_edge(2, 4, 14)
  graph.add_edge(3, 2, 9)
  graph.add_edge(3, 5, 20)
  graph.add_edge(4, 3, 7)
  graph.add_edge(4, 5, 4)
  
  source, sink = 0, 5
  max_flow = graph.ford_fulkerson(source, sink)
  print(f'Fluxo máximo da tubulação: {max_flow}')
  
if __name__ == '__main__':
  water_pipes_example()