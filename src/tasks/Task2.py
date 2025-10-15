from src.utils.graphs.UnpointedGraph import UnpointedGraph

def task2():
  graph = UnpointedGraph(10)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  # graph.remove_edge(0, 1)
  print(graph.list)
  print(graph.num_nodes())
  print(graph.num_edges())
  print(graph.degree(0))