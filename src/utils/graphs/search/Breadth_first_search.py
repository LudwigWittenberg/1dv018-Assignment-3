from src.utils.graphs.search.First_Search import FS
from src.utils.graphs.Graph import Graph

class BFS(FS):
  def __init__(self, graph: Graph, start_node):
    super().__init__(graph, start_node)
    
  def _search(self, node):
    queue = []
    queue.insert(0, node)
    
    self.visited[node] = True
    
    while queue:
      node_value = queue.pop()
      
      for neighbor in self.graph.get_neighbors(node_value):
        if not self.visited[neighbor.node2]:
          queue.insert(0, neighbor.node2)
          self.visited[neighbor.node2] = True
          self.edge_to[neighbor.node2] = node_value