from src.utils.graphs.UnpointedGraph import UnpointedGraph
from src.utils.graphs.PointedGraph import PointedGraph

def task2():
  print("Unpointed Graph")
  
  graph = UnpointedGraph(10)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge_with_weight(0, 3, 2)
  graph.remove_edge(0, 1)
  print("List: ", graph.list)
  print("Number of nodes: ", graph.num_nodes())
  print("Number of edges: ", graph.num_edges())
  print("Degree of node 0: ", graph.degree(0))
  
  print("")
  print("Pointed Graph")
  
  pGraph = PointedGraph(10)
  print("List: ", pGraph.list)
  print("Number of nodes: ", pGraph.num_nodes())
  print("Number of edges: ", pGraph.num_edges())
  print("Degree of node 0: ", pGraph.degree(0))
  print("")
  pGraph.add_edge(0, 1)
  pGraph.add_edge(0, 2)
  pGraph.add_edge(0, 3)
  pGraph.add_edge(7, 4)
  pGraph.add_edge_with_weight(7, 5, 8)
  pGraph.remove_edge(0, 1)
  print("List: ", pGraph.list)
  print("Number of nodes: ", pGraph.num_nodes())
  print("Number of edges: ", pGraph.num_edges())
  print("Degree of node 0: ", pGraph.degree(0))