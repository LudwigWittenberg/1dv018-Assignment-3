class Graph:
  def __init__(self, size):
    self.list = [[] for _ in range(size)]
    
  # Returns the number of nodes in the graph
  def num_nodes(self):
    return len(self.list)
  
  def num_edges(self):
    assert False, "Not implemented"
  
  def add_edge(self, node1, node2):
    assert False, "Not implemented"
    
  def add_edge_with_weight(self, node1, node2, weight):
    assert False, "Not implemented"
  
  def remove_edge(self, node1, node2):
    assert False, "Not implemented"
  
  def degree(self, node):
    assert False, "Not implemented"
  
  def _valid_node(self, node):
    return node >= 0 and node < self.num_nodes()
  