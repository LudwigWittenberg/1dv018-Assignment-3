class HeapSort:
  def __init__(self, length):
    self.height = [None] + length
    self.size = len(self.height) - 1
    
  def _sink(self, value):
    while 2 * value <= self.size:
      j = 2 * value
      
      if j < self.size and self.height[j] < self.height[j + 1]:
        j += 1
        
      if not self.height[value] < self.height[j]:
        break
      
      self.height[value], self.height[j] = self.height[j], self.height[value]
      
      value = j
      
  def sort(self):
    size = self.size // 2
    
    while size >= 1:
      self._sink(size)
      size -= 1
      
    while self.size > 1:
      self.height[1], self.height[self.size] = self.height[self.size], self.height[1]
      self.size -= 1
      self._sink(1)
      
    return self.height