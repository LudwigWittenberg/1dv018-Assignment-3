from src.utils.QuickSort import QuickSort
import random

def main():
  arr = []
  
  for _ in range(1000):
    arr.append(random.randint(0, 1000))
  
  print(f"Unsorted array: {arr}")
  
  quick_sort = QuickSort()
  quick_sort.sort(arr)
  
  print(f"Sorted array: {arr}")
  
  
main()