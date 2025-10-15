class Edge:
  def __init__(self, node1, node2, weight):
    self.node1 = node1
    self.node2 = node2
    self.weight = weight
    
  def either(self):
    return self.node1
  
  def other(self, node):
    if node == self.node1:
      return self.node2
    else:
      return self.node1
    
  def __lt__(self, other):
    return self.weight < other.weight
  
  def __repr__(self):
    return f"Edge({self.node1}, {self.node2}, {self.weight})"