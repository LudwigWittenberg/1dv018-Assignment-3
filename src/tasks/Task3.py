from src.utils.graphs.UnpointedGraph import UnpointedGraph
from src.utils.graphs.PointedGraph import PointedGraph
from src.utils.graphs.search.Depth_first_search import DFS
from src.utils.graphs.search.Breadth_first_search import BFS

def task3():
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
  dfs = DFS(graph, 0)
  print("DFS: ", dfs.path_to(3))
  print("Has path to 3: ", dfs.has_path_to(3))
  print("Has path to 8: ", dfs.has_path_to(8))
  
  print("")
  bfs = BFS(graph, 0)
  print("BFS: ", bfs.path_to(3))
  print("Has path to 3: ", bfs.has_path_to(3))
  print("Has path to 8: ", bfs.has_path_to(8))
  
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
  
  print("")
  dfs = DFS(pGraph, 0)
  print("DFS: ", dfs.path_to(3))
  print("Has path to 3: ", dfs.has_path_to(3))
  print("Has path to 8: ", dfs.has_path_to(8))
  
  print("")
  bfs = BFS(pGraph, 0)
  print("BFS: ", bfs.path_to(3))
  print("Has path to 3: ", bfs.has_path_to(3))
  print("Has path to 8: ", bfs.has_path_to(8))
  
  