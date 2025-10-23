import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from src.utils.sort.DynamicSort import DynamicSort
from src.utils.sort.QuickSort import QuickSort
from src.utils.sort.HeapSort import HeapSort

def generate_test_data(size, num_tests=100):
    """Generate test data for performance testing"""
    test_cases = []
    
    for _ in range(num_tests):
        # Random array
        random_arr = [random.randint(1, 1000) for _ in range(size)]
        test_cases.append(random_arr.copy())
        
        # Sorted array
        sorted_arr = list(range(1, size + 1))
        test_cases.append(sorted_arr.copy())
        
        # Reverse sorted array
        reverse_arr = list(range(size, 0, -1))
        test_cases.append(reverse_arr.copy())
        
        # Array with duplicates
        duplicate_arr = [random.randint(1, 10) for _ in range(size)]
        test_cases.append(duplicate_arr.copy())
    
    return test_cases

def benchmark_dynamicsort(arr, max_depth):
    """Benchmark DynamicSort performance with given max_depth"""
    start_time = time.perf_counter()
    dynamic_sort = DynamicSort(max_depth)
    dynamic_sort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def benchmark_quicksort(arr):
    """Benchmark QuickSort performance"""
    start_time = time.perf_counter()
    quicksort = QuickSort()
    quicksort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def benchmark_heapsort(arr):
    """Benchmark HeapSort performance"""
    start_time = time.perf_counter()
    heapsort = HeapSort(arr.copy())
    heapsort.sort()
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def run_performance_test(sizes, num_tests=100):
    """Run performance tests for different array sizes with sqrt-based depths"""
    results = {
        'sizes': [],
        'dynamicsort_times': [],
        'quicksort_times': [],
        'heapsort_times': [],
        'depths': [],
        'dynamicsort_avg': [],
        'dynamicsort_std': [],
        'quicksort_avg': [],
        'quicksort_std': [],
        'heapsort_avg': [],
        'heapsort_std': []
    }
    
    for size in sizes:
        print(f"Testing array size: {size}")
        
        # Calculate depth based on square root of list length
        depth = int(math.sqrt(size))
        print(f"  Using depth: {depth} (sqrt of {size})")
        
        test_cases = generate_test_data(size, num_tests)
        dynamicsort_times = []
        quicksort_times = []
        heapsort_times = []
        
        for test_case in test_cases:
            # Test DynamicSort with calculated depth
            dynamic_time = benchmark_dynamicsort(test_case, depth)
            dynamicsort_times.append(dynamic_time)

            # Test QuickSort
            quicksort_time = benchmark_quicksort(test_case)
            quicksort_times.append(quicksort_time)

            # Test HeapSort
            heapsort_time = benchmark_heapsort(test_case)
            heapsort_times.append(heapsort_time)
        
        # Calculate statistics
        dynamic_avg = np.mean(dynamicsort_times)
        dynamic_std = np.std(dynamicsort_times)
        quicksort_avg = np.mean(quicksort_times)
        quicksort_std = np.std(quicksort_times)
        heapsort_avg = np.mean(heapsort_times)
        heapsort_std = np.std(heapsort_times)
        
        results['sizes'].append(size)
        results['dynamicsort_times'].append(dynamicsort_times)
        results['quicksort_times'].append(quicksort_times)
        results['heapsort_times'].append(heapsort_times)
        results['depths'].append(depth)
        results['dynamicsort_avg'].append(dynamic_avg)
        results['dynamicsort_std'].append(dynamic_std)
        results['quicksort_avg'].append(quicksort_avg)
        results['quicksort_std'].append(quicksort_std)
        results['heapsort_avg'].append(heapsort_avg)
        results['heapsort_std'].append(heapsort_std)
        
        print(f"  DynamicSort: {dynamic_avg:.3f}ms ± {dynamic_std:.3f}ms")
        print(f"  QuickSort: {quicksort_avg:.3f}ms ± {quicksort_std:.3f}ms")
        print(f"  HeapSort: {heapsort_avg:.3f}ms ± {heapsort_std:.3f}ms")
        print(f"  Depth used: {depth}")
        print()
    
    return results

def create_performance_graphs(results):
    """Create graphs for DynamicSort performance with sqrt depth"""
    
    # Create a figure with 3 subplots
    plt.figure(figsize=(18, 5))
    
    # Graph 1: Performance vs Array Size
    plt.subplot(1, 3, 1)
    plt.plot(results['sizes'], results['dynamicsort_avg'], 
             label='DynamicSort (sqrt depth)', marker='o', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('DynamicSort Performance vs Array Size')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Graph 2: Performance Distribution by Depth (scatter plot)
    plt.subplot(1, 3, 2)
    plt.scatter(results['depths'], results['dynamicsort_avg'], 
               s=100, alpha=0.7, color='green')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('Performance Distribution by Depth')
    plt.grid(True, alpha=0.3)
    
    # Graph 3: Comparison of all three algorithms
    plt.subplot(1, 3, 3)
    plt.plot(results['sizes'], results['dynamicsort_avg'], 
             label='DynamicSort (sqrt depth)', marker='o', linewidth=2, markersize=6)
    plt.plot(results['sizes'], results['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.plot(results['sizes'], results['heapsort_avg'], 
             label='HeapSort', marker='^', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('DynamicSort vs QuickSort vs HeapSort')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/dynamicsort_sqrt_depth.png', dpi=300, bbox_inches='tight')

def analyze_sqrt_depth():
    """Main analysis function"""
    print("=== DynamicSort Performance Analysis ===")
    print("Testing DynamicSort with depth = sqrt(array_size)")
    print()
    
    # Test sizes focusing on small to medium arrays
    test_sizes = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    
    print("Running performance tests...")
    results = run_performance_test(test_sizes, num_tests=50)
    
    print("Creating performance graphs...")
    create_performance_graphs(results)
    
    # Analysis summary
    print("\n=== ANALYSIS SUMMARY ===")
    print("Array Size | Depth | DynamicSort | QuickSort | HeapSort | Winner")
    print("-" * 70)
    
    for i, size in enumerate(results['sizes']):
        depth = results['depths'][i]
        dynamic_avg = results['dynamicsort_avg'][i]
        quick_avg = results['quicksort_avg'][i]
        heap_avg = results['heapsort_avg'][i]
        
        # Find the fastest algorithm
        times = [dynamic_avg, quick_avg, heap_avg]
        algorithms = ['DynamicSort', 'QuickSort', 'HeapSort']
        winner = algorithms[times.index(min(times))]
        
        print(f"{size:10} | {depth:5} | {dynamic_avg:11.3f}ms | {quick_avg:9.3f}ms | {heap_avg:8.3f}ms | {winner}")