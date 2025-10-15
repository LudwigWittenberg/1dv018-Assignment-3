from src.utils.graphs.Graph import Graph

class UnpointedGraph(Graph):
  def __init__(self, size):
    super().__init__(size)
    
  def num_edges(self):
    return sum([len(node) for node in self.list]) // 2

  def add_edge(self, node1, node2):
    if super()._valid_node(node1) and super()._valid_node(node2):
      # Check if the edge already exists
      if node2 not in self.list[node1]:
        self.list[node1].append(node2)
        self.list[node2].append(node1)
        
  def remove_edge(self, node1, node2):
    if super()._valid_node(node1) and super()._valid_node(node2):
      if node2 in self.list[node1]:
        self.list[node1].remove(node2)
        self.list[node2].remove(node1)
        
  def degree(self, node):
    if super()._valid_node(node):
      return len(self.list[node])