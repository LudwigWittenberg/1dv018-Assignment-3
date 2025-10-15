import numpy as np
from src.utils.graphs.Graph import Graph

class FS:
  def __init__(self, graph: Graph, start_node):
    self.graph = graph
    self.start_node = start_node
    self.visited = np.zeros(graph.num_nodes(), dtype=bool)
    self.edge_to = np.zeros(graph.num_nodes(), dtype=int)
    self._search(start_node)

  def _search(self, node):
    raise NotImplementedError("Not implemented")
        
  def has_path_to(self, node):
    return self.visited[node]
  
  def path_to(self, node):
    if not self.has_path_to(node):
      return None
    
    current_node = node
    path = []
    
    while current_node != self.start_node:
      path.insert(0, current_node)
      current_node = self.edge_to[current_node]
    
    path.insert(0, self.start_node)
    
    return path