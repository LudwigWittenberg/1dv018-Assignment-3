from src.utils.graphs.UnpointedGraph import UnpointedGraph
from src.utils.graphs.PointedGraph import PointedGraph
from src.utils.graphs.distance.Dijkstras_algorithm import DJKAlgorithm

def task4():
  print("Unpointed Graph")
  
  el = [(0,1,5), (0,3,8), (0,6,9), (1,2,15), (1,3,4), (1,4,12),
    (2,7,9), (3,4,7), (3,5,6), (4,2,3), (4,7,11), (5,4,1),
    (5,7,13), (6,3,5), (6,5,4), (6,7,20)
  ]
  
  graph = UnpointedGraph(8)
  for edge in el:
    graph.add_edge_with_weight(edge[0], edge[1], edge[2])
  
  print("List: ", graph.list)
  print("Number of nodes: ", graph.num_nodes())
  print("Number of edges: ", graph.num_edges())
  print("Degree of node 0: ", graph.degree(0))
  
  djk = DJKAlgorithm(graph, 0)
  print("Dijkstra's algorithm: ", djk.dist_to)
  
  print("")
  print("Pointed Graph")
  
  pGraph = PointedGraph(8)
  for edge in el:
    pGraph.add_edge_with_weight(edge[0], edge[1], edge[2])
  
  print("List: ", pGraph.list)
  print("Number of nodes: ", pGraph.num_nodes())
  print("Number of edges: ", pGraph.num_edges())
  print("Degree of node 0: ", pGraph.degree(0))
  
  djk = DJKAlgorithm(pGraph, 0)
  print("Dijkstra's algorithm: ", djk.dist_to)