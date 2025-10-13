from src.utils.QuickSort import QuickSort
from src.utils.HeapSort import HeapSort
import random

def main():
  arr = []
  
  for _ in range(1000):
    arr.append(random.randint(0, 1000))
  
  print(f"Unsorted array: {arr}")
  
  # quick_sort = QuickSort()
  # quick_sort.sort(arr)
  
  # print(f"Sorted array: {arr}")
  
  # print(f"Count: {quick_sort.get_stats()}")
  
  rl = [1, 4, 8, 2, 5, 9, 3, 7, 6]
  
  heap_sort = HeapSort(rl)
  print(f"Un Sorted array: {heap_sort.height[1:]}")
  heap_sort.sort()
  
  print(f"Sorted array: {heap_sort.height[1:]}")

  
main()