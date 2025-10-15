from src.utils.graphs.Graph import Graph
from src.utils.graphs.edges.DiEdge import DiEdge

class PointedGraph(Graph):
  def __init__(self, size):
    super().__init__(size)
    
  def num_edges(self):
    return sum([len(node) for node in self.list])

  def add_edge(self, node1, node2):
    self.add_edge_with_weight(node1, node2, 1)
        
  def add_edge_with_weight(self, node1, node2, weight):
    if super()._valid_node(node1) and super()._valid_node(node2):
      if node2 not in self.list[node1]:
        self.list[node1].append(DiEdge(node1, node2, weight))

  def remove_edge(self, node1, node2):
    if super()._valid_node(node1) and super()._valid_node(node2):
      for edge in self.list[node1]:
        if edge.dst() == node2:
          self.list[node1].remove(edge)
          break
