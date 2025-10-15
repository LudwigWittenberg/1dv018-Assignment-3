class DiEdge():
  def __init__(self, node1, node2, weight):
    self.node1 = node1
    self.node2 = node2
    self.weight = weight
    
  def src(self):
    return self.node1
  
  def dst(self):
    return self.node2
  
  def weight(self):
    return self.weight
  
  def __repr__(self):
    return f"DiEdge({self.node1}, {self.node2}, {self.weight})"
  
  def __lt__(self, other):
    return self.weight < other.weight
  
  def __repr__(self):
    return f"DiEdge({self.node1}, {self.node2}, {self.weight})"
  
