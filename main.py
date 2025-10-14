from src.utils.QuickSort import QuickSort
from src.utils.HeapSort import HeapSort
from src.utils.DynamicSort import DynamicSort
import random, math

def main():
  print("-------------Task 1-------------")
  print("---------QuickSort---------")
  arr = []
  
  for _ in range(20):
    arr.append(random.randint(0, 20))
  
  print(f"Unsorted array: {arr}")
  
  quick_sort = QuickSort()
  quick_sort.sort(arr)
  
  print(f"Sorted array: {arr}")
  
  print(f"Count: {quick_sort.get_stats()}")
  
  print("---------HeapSort---------")
  
  rl = [1, 4, 8, 2, 5, 9, 3, 7, 6]
  
  heap_sort = HeapSort(rl)
  print(f"Un Sorted array: {heap_sort.height[1:]}")
  heap_sort.sort()
  
  print(f"Sorted array: {heap_sort.height[1:]}")

  print("---------DynamicSort---------")
  
  d_arr = []
  
  for _ in range(100):
    d_arr.append(random.randint(0, 100))
    
  max_depth = 2 * math.log2(len(d_arr))
  
  print(f"Max depth: {max_depth}")
  
  print(f"Unsorted array: {d_arr}")
  
  dynamic_sort = DynamicSort(max_depth)
  dynamic_sort.sort(d_arr)
  
  print(f"Sorted array: {d_arr}")
  
main()