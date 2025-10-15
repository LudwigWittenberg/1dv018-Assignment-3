from src.utils.graphs.UnpointedGraph import UnpointedGraph
from src.utils.graphs.PointedGraph import PointedGraph

def task2():
  graph = UnpointedGraph(10)
  graph.add_edge(0, 1)
  # graph.add_edge(0, 2)
  # graph.add_edge_default(0, 3, 2)
  graph.remove_edge(0, 1)
  print(graph.list)
  print(graph.num_nodes())
  print(graph.num_edges())
  print(graph.degree(0))
  
  # print("Pointed Graph")
  
  # pGraph = PointedGraph(10)
  # pGraph.add_edge(0, 1)
  # pGraph.add_edge(0, 2)
  # print(pGraph.list)
  # print(pGraph.num_nodes())
  # print(pGraph.num_edges())
  # print(pGraph.degree(0))