from src.utils.graphs.Graph import Graph
from src.utils.graphs.search.First_Search import FS

class DFS(FS):
  def __init__(self, graph: Graph, start_node):
    super().__init__(graph, start_node)
    
  def _search(self, node):
    self.visited[node] = True
    for neighbor in self.graph.get_neighbors(node):
      if not self.visited[neighbor.node2]:
        self._search(neighbor.node2)
        self.edge_to[neighbor.node2] = node
