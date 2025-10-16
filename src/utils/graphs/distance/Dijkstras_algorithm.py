from heapq import heappop, heappush, heapify
from src.utils.graphs.Graph import Graph
import numpy as np

class DJKAlgorithm:
  def __init__(self, graph: Graph, start_node):
    self.edge_to = [None] * graph.num_nodes()
    self.dist_to = np.full(graph.num_nodes(), np.inf, dtype=np.double)
    self.dist_to[start_node] = 0.0
    self.pq = []
    
    heappush(self.pq, (0.0, start_node))
    
    while self.pq:
      _, node = heappop(self.pq)
      
      for edge in graph.get_neighbors(node):
        self._relax(edge)
        
  def _relax(self, edge):
    if self.dist_to[edge.dst()] > self.dist_to[edge.src()] + edge.get_weight():
      self.dist_to[edge.dst()] = self.dist_to[edge.src()] + edge.get_weight()
      self.edge_to[edge.dst()] = edge
      
      for index, value in enumerate(self.pq):
        if value[1] == edge.dst():
          self.pq[index] = (self.dist_to[edge.dst()], edge.dst())
          heapify(self.pq)
          break
      else:
        heappush(self.pq, (self.dist_to[edge.dst()], edge.dst()))