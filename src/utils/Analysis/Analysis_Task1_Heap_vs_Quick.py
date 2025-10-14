import time
import random
import matplotlib.pyplot as plt
import numpy as np
from src.utils.HeapSort import HeapSort
from src.utils.QuickSort import QuickSort

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

def benchmark_heapsort(arr):
    """Benchmark HeapSort performance"""
    start_time = time.perf_counter()
    heap_sort = HeapSort(arr.copy())
    heap_sort.sort()
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def benchmark_quicksort(arr):
    """Benchmark QuickSort performance"""
    start_time = time.perf_counter()
    quick_sort = QuickSort()
    quick_sort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def run_performance_test(sizes, num_tests=100):
    """Run performance tests for different array sizes"""
    results = {
        'sizes': [],
        'heapsort_times': [],
        'quicksort_times': [],
        'heapsort_avg': [],
        'quicksort_avg': [],
        'heapsort_std': [],
        'quicksort_std': []
    }
    
    for size in sizes:
        print(f"Testing array size: {size}")
        
        test_cases = generate_test_data(size, num_tests)
        heapsort_times = []
        quicksort_times = []
        
        for test_case in test_cases:
            # Test HeapSort
            heap_time = benchmark_heapsort(test_case)
            heapsort_times.append(heap_time)
            
            # Test QuickSort
            quick_time = benchmark_quicksort(test_case)
            quicksort_times.append(quick_time)
        
        # Calculate statistics
        heap_avg = np.mean(heapsort_times)
        quick_avg = np.mean(quicksort_times)
        heap_std = np.std(heapsort_times)
        quick_std = np.std(quicksort_times)
        
        results['sizes'].append(size)
        results['heapsort_times'].append(heapsort_times)
        results['quicksort_times'].append(quicksort_times)
        results['heapsort_avg'].append(heap_avg)
        results['quicksort_avg'].append(quick_avg)
        results['heapsort_std'].append(heap_std)
        results['quicksort_std'].append(quick_std)
        
        print(f"  HeapSort: {heap_avg:.3f}ms ± {heap_std:.3f}ms")
        print(f"  QuickSort: {quick_avg:.3f}ms ± {quick_std:.3f}ms")
        print(f"  Winner: {'HeapSort' if heap_avg < quick_avg else 'QuickSort'}")
        print()
    
    return results

def create_performance_graphs(results):
    """Create line graph for performance comparison"""
    
    # Create a single figure with only the performance comparison graph
    plt.figure(figsize=(10, 6))
    
    # Performance comparison line graph
    plt.plot(results['sizes'], results['heapsort_avg'], 
             label='HeapSort', marker='o', linewidth=2, markersize=6)
    plt.plot(results['sizes'], results['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('HeapSort vs QuickSort - Performance Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/heapsort_vs_quicksort_small_arrays.png', dpi=300, bbox_inches='tight')

def analyze_Heap_vs_Quick():
    """Main analysis function"""
    print("=== HeapSort vs QuickSort Performance Analysis ===")
    print("Testing your theory: HeapSort will be faster on smaller arrays")
    print()
    
    # Test sizes focusing on small arrays (max size 100)
    test_sizes = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
    
    print("Running performance tests...")
    results = run_performance_test(test_sizes, num_tests=50)
    
    print("Creating performance graphs...")
    create_performance_graphs(results)
    
    # Analysis summary
    print("\n=== ANALYSIS SUMMARY ===")
    print("Array Size | HeapSort Avg | QuickSort Avg | Winner | Ratio")
    print("-" * 60)
    
    for i, size in enumerate(results['sizes']):
        heap_avg = results['heapsort_avg'][i]
        quick_avg = results['quicksort_avg'][i]
        winner = "HeapSort" if heap_avg < quick_avg else "QuickSort"
        ratio = heap_avg / quick_avg
        
        print(f"{size:10} | {heap_avg:11.3f}ms | {quick_avg:12.3f}ms | {winner:6} | {ratio:.3f}")
    
    # Theory validation
    small_sizes = [5, 10, 20, 50, 100]
    heap_wins = 0
    quick_wins = 0
    
    for size in small_sizes:
        if size in results['sizes']:
            idx = results['sizes'].index(size)
            if results['heapsort_avg'][idx] < results['quicksort_avg'][idx]:
                heap_wins += 1
            else:
                quick_wins += 1