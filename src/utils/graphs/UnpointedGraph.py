from src.utils.graphs.Graph import Graph
from src.utils.graphs.edges.Edge import Edge

class UnpointedGraph(Graph):
  def __init__(self, size):
    super().__init__(size)
    
  def num_edges(self):
    return sum([len(node) for node in self.list]) // 2

  def add_edge(self, node1, node2):
    self.add_edge_default(node1, node2, 1)
        
  def add_edge_default(self, node1, node2, weight):
    if super()._valid_node(node1) and super()._valid_node(node2):
      # Check if the edge already exists
      if node2 not in self.list[node1]:
        self.list[node1].append(Edge(node1, node2, weight))
        self.list[node2].append(Edge(node2, node1, weight))
        
  def remove_edge(self, node1, node2):
    if super()._valid_node(node1) and super()._valid_node(node2):
      for edge in self.list[node1]:
        if edge.node2 == node2:
          self.list[node1].remove(edge)
          break
      for edge in self.list[node2]:
        if edge.node2 == node1:
          self.list[node2].remove(edge)
          break