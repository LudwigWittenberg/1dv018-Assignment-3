class Graph:
  def __init__(self, size):
    self.list = [[] for _ in range(size)]
    
  # Returns the number of nodes in the graph
  def num_nodes(self):
    return len(self.list)
  
  def num_edges(self):
    return NotImplementedError("Not implemented")
  
  def add_edge(self, node1, node2):
    return NotImplementedError("Not implemented")
    
  def add_edge_with_weight(self, node1, node2, weight):
    return NotImplementedError("Not implemented")
  
  def remove_edge(self, node1, node2):
    return NotImplementedError("Not implemented")
  
  def degree(self, node):
    return self.get_neighbors(node)
    
  def get_neighbors(self, node):
    if self._valid_node(node):
      return self.list[node]
  
  def _valid_node(self, node):
    return node >= 0 and node < self.num_nodes()
    