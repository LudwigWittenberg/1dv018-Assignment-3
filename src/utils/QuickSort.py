class QuickSort:
  def __init__(self,):
    pass
    
  def _partition(self, arr, low, high):
    i, j = low, high + 1
    
    medium = (low + high) // 2
    
    arr[low], arr[medium] = arr[medium], arr[low]
    pivot = arr[low]
    
    while True:
      i += 1
      
      while arr[i] < pivot:
        if i == high:
          break
        
        i += 1
        
      j -= 1
      
      while pivot < arr[j]:
        if j == low:
          break
        
        j -= 1
        
      if i >= j:
        break
      
      arr[i], arr[j] = arr[j], arr[i]
      
    arr[low], arr[j] = arr[j], arr[low]
    
    return j
  
  def sort(self, arr):
    self.count = 0
    
    if len(arr) <= 1:
      return arr
    
    low, high = 0, len(arr) - 1
    
    self._sort(arr, low, high)
    
  def _sort(self, arr, low, high):
    if high <= low:
      return
    
    self.count += 1
    
    j = self._partition(arr, low, high)
    
    self._sort(arr, low, j - 1)
    self._sort(arr, j + 1, high)
    
  def get_stats(self):
    return self.count