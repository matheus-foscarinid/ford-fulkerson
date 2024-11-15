from FordFulkerson import DirectedGraph

def test_simple_graph():
  V = 4
  graph = DirectedGraph(V)
  graph.add_edge(0, 1, 10)
  graph.add_edge(0, 2, 5)
  graph.add_edge(1, 2, 15)
  graph.add_edge(1, 3, 10)
  graph.add_edge(2, 3, 10)
  
  source, sink = 0, 3
  max_flow = graph.ford_fulkerson(source, sink)
  print(f'Test Simple Graph - Max Flow: {max_flow}')
  print()
  assert max_flow == 15

def test_graph_with_bottleneck():
  V = 4
  graph = DirectedGraph(V)
  graph.add_edge(0, 1, 10)
  graph.add_edge(0, 2, 10)
  graph.add_edge(1, 2, 1)
  graph.add_edge(1, 3, 10)
  graph.add_edge(2, 3, 10)
  
  source, sink = 0, 3
  max_flow = graph.ford_fulkerson(source, sink)
  print(f'Test Graph with Bottleneck - Max Flow: {max_flow}')
  print()
  assert max_flow == 20

def test_larger_graph():
  V = 6
  graph = DirectedGraph(V)
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
  print(f'Test Larger Graph - Max Flow: {max_flow}')
  print()
  assert max_flow == 23

def test_disconnected_graph():
  V = 4
  graph = DirectedGraph(V)
  graph.add_edge(0, 1, 10)
  graph.add_edge(2, 3, 10)
  
  source, sink = 0, 3
  max_flow = graph.ford_fulkerson(source, sink)
  print(f'Test Disconnected Graph - Max Flow: {max_flow}')
  print()
  assert max_flow == 0

def test_graph_with_multiple_paths():
  V = 6
  graph = DirectedGraph(V)
  graph.add_edge(0, 1, 10)
  graph.add_edge(0, 2, 10)
  graph.add_edge(1, 2, 2)
  graph.add_edge(1, 3, 4)
  graph.add_edge(1, 4, 8)
  graph.add_edge(2, 4, 9)
  graph.add_edge(3, 5, 10)
  graph.add_edge(4, 3, 6)
  graph.add_edge(4, 5, 10)
  
  source, sink = 0, 5
  max_flow = graph.ford_fulkerson(source, sink)
  print(f'Test Graph with Multiple Paths - Max Flow: {max_flow}')
  print()
  assert max_flow == 19

if __name__ == '__main__':
  test_simple_graph()
  test_graph_with_bottleneck()
  test_larger_graph()
  test_disconnected_graph()
  test_graph_with_multiple_paths()
  print('All tests passed!')