import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from src.utils.sort.DynamicSort import DynamicSort
from src.utils.sort.QuickSort import QuickSort
from src.utils.sort.HeapSort import HeapSort

def generate_test_data(size, num_tests=50):
    """Generate test data for performance testing"""
    test_cases = []
    
    for _ in range(num_tests):
        random_arr = [random.randint(1, 10000) for _ in range(size)]
        test_cases.append(random_arr.copy())
        
        sorted_arr = list(range(1, size + 1))
        test_cases.append(sorted_arr.copy())
        
        reverse_arr = list(range(size, 0, -1))
        test_cases.append(reverse_arr.copy())
        
        duplicate_arr = [random.randint(1, 100) for _ in range(size)]
        test_cases.append(duplicate_arr.copy())
    
    return test_cases

def benchmark_dynamicsort(arr, max_depth):
    """Benchmark DynamicSort performance with given max_depth"""
    start_time = time.perf_counter()
    dynamic_sort = DynamicSort(max_depth)
    dynamic_sort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

def benchmark_quicksort(arr):
    """Benchmark QuickSort performance"""
    start_time = time.perf_counter()
    quicksort = QuickSort()
    quicksort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

def benchmark_heapsort(arr):
    """Benchmark HeapSort performance"""
    start_time = time.perf_counter()
    heapsort = HeapSort(arr.copy())
    heapsort.sort()
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

def run_performance_test(sizes, depth_strategy, num_tests=25):
    """Run performance tests for different array sizes"""
    results = {
        'sizes': [],
        'dynamicsort_avg': [],
        'quicksort_avg': [],
        'heapsort_avg': [],
        'depths': []
    }
    
    for size in sizes:
        print(f"Testing array size: {size}")
        
        if depth_strategy == 'sqrt':
            depth = int(math.sqrt(size))
        elif depth_strategy == 'log2':
            depth = int(math.log2(size))
        elif depth_strategy == '2log2':
            depth = 2 * int(math.log2(size))
        
        print(f"  Using depth: {depth} ({depth_strategy} of {size})")
        
        test_cases = generate_test_data(size, num_tests)
        dynamicsort_times = []
        quicksort_times = []
        heapsort_times = []
        
        for test_case in test_cases:
            dynamic_time = benchmark_dynamicsort(test_case, depth)
            dynamicsort_times.append(dynamic_time)
            
            quicksort_time = benchmark_quicksort(test_case)
            quicksort_times.append(quicksort_time)
            
            heapsort_time = benchmark_heapsort(test_case)
            heapsort_times.append(heapsort_time)
        
        dynamic_avg = np.mean(dynamicsort_times)
        quicksort_avg = np.mean(quicksort_times)
        heapsort_avg = np.mean(heapsort_times)
        
        results['sizes'].append(size)
        results['dynamicsort_avg'].append(dynamic_avg)
        results['quicksort_avg'].append(quicksort_avg)
        results['heapsort_avg'].append(heapsort_avg)
        results['depths'].append(depth)
        
        print(f"  DynamicSort: {dynamic_avg:.3f}ms")
        print(f"  QuickSort: {quicksort_avg:.3f}ms")
        print(f"  HeapSort: {heapsort_avg:.3f}ms")
        print()
    
    return results

def create_performance_graphs(results_sqrt, results_log2, results_2log2):
    """Create comparison graphs for three depth strategies"""
    
    plt.figure(figsize=(20, 6))
    
    # Graph 1: sqrt depth strategy
    plt.subplot(1, 3, 1)
    plt.plot(results_sqrt['sizes'], results_sqrt['dynamicsort_avg'], 
             label='DynamicSort (sqrt)', marker='o', linewidth=2, markersize=6)
    plt.plot(results_sqrt['sizes'], results_sqrt['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.plot(results_sqrt['sizes'], results_sqrt['heapsort_avg'], 
             label='HeapSort', marker='^', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('Depth = sqrt(n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Graph 2: log2 depth strategy
    plt.subplot(1, 3, 2)
    plt.plot(results_log2['sizes'], results_log2['dynamicsort_avg'], 
             label='DynamicSort (log2)', marker='o', linewidth=2, markersize=6)
    plt.plot(results_log2['sizes'], results_log2['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.plot(results_log2['sizes'], results_log2['heapsort_avg'], 
             label='HeapSort', marker='^', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('Depth = log2(n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Graph 3: 2*log2 depth strategy
    plt.subplot(1, 3, 3)
    plt.plot(results_2log2['sizes'], results_2log2['dynamicsort_avg'], 
             label='DynamicSort (2*log2)', marker='o', linewidth=2, markersize=6)
    plt.plot(results_2log2['sizes'], results_2log2['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.plot(results_2log2['sizes'], results_2log2['heapsort_avg'], 
             label='HeapSort', marker='^', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('Depth = 2*log2(n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/dynamicsort_depth_strategies_large.png', dpi=300, bbox_inches='tight')

def analyze_depth_strategies_large():
    """Main analysis function comparing depth strategies on large arrays"""
    print("=== DynamicSort Depth Strategies Comparison (Large Arrays) ===")
    print()
    
    test_sizes = [100, 200, 300, 400, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000]
    
    print("Testing sqrt depth strategy...")
    results_sqrt = run_performance_test(test_sizes, 'sqrt', num_tests=20)
    
    print("Testing log2 depth strategy...")
    results_log2 = run_performance_test(test_sizes, 'log2', num_tests=20)
    
    print("Testing 2*log2 depth strategy...")
    results_2log2 = run_performance_test(test_sizes, '2log2', num_tests=20)
    
    print("Creating performance graphs...")
    create_performance_graphs(results_sqrt, results_log2, results_2log2)
    
    # Analysis summary for sqrt
    print("\n=== SQRT DEPTH ANALYSIS ===")
    print("Array Size | Depth | DynamicSort | QuickSort | HeapSort | Winner")
    print("-" * 70)
    for i, size in enumerate(results_sqrt['sizes']):
        depth = results_sqrt['depths'][i]
        dynamic_avg = results_sqrt['dynamicsort_avg'][i]
        quick_avg = results_sqrt['quicksort_avg'][i]
        heap_avg = results_sqrt['heapsort_avg'][i]
        winner = ['DynamicSort', 'QuickSort', 'HeapSort'][[dynamic_avg, quick_avg, heap_avg].index(min(dynamic_avg, quick_avg, heap_avg))]
        print(f"{size:10} | {depth:5} | {dynamic_avg:11.3f}ms | {quick_avg:9.3f}ms | {heap_avg:8.3f}ms | {winner}")
    
    # Analysis summary for log2
    print("\n=== LOG2 DEPTH ANALYSIS ===")
    print("Array Size | Depth | DynamicSort | QuickSort | HeapSort | Winner")
    print("-" * 70)
    for i, size in enumerate(results_log2['sizes']):
        depth = results_log2['depths'][i]
        dynamic_avg = results_log2['dynamicsort_avg'][i]
        quick_avg = results_log2['quicksort_avg'][i]
        heap_avg = results_log2['heapsort_avg'][i]
        winner = ['DynamicSort', 'QuickSort', 'HeapSort'][[dynamic_avg, quick_avg, heap_avg].index(min(dynamic_avg, quick_avg, heap_avg))]
        print(f"{size:10} | {depth:5} | {dynamic_avg:11.3f}ms | {quick_avg:9.3f}ms | {heap_avg:8.3f}ms | {winner}")
    
    # Analysis summary for 2*log2
    print("\n=== 2*LOG2 DEPTH ANALYSIS ===")
    print("Array Size | Depth | DynamicSort | QuickSort | HeapSort | Winner")
    print("-" * 70)
    for i, size in enumerate(results_2log2['sizes']):
        depth = results_2log2['depths'][i]
        dynamic_avg = results_2log2['dynamicsort_avg'][i]
        quick_avg = results_2log2['quicksort_avg'][i]
        heap_avg = results_2log2['heapsort_avg'][i]
        winner = ['DynamicSort', 'QuickSort', 'HeapSort'][[dynamic_avg, quick_avg, heap_avg].index(min(dynamic_avg, quick_avg, heap_avg))]
        print(f"{size:10} | {depth:5} | {dynamic_avg:11.3f}ms | {quick_avg:9.3f}ms | {heap_avg:8.3f}ms | {winner}")
