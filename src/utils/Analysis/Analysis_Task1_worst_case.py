import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from src.utils.DynamicSort import DynamicSort
from src.utils.QuickSort import QuickSort

def generate_worst_case_data(size, num_tests=50):
    """Generate worst case test data for performance testing"""
    test_cases = []
    
    for _ in range(num_tests):
        # Worst case for QuickSort: Already sorted array (ascending)
        sorted_asc = list(range(1, size + 1))
        test_cases.append(sorted_asc.copy())
        
        # Worst case for QuickSort: Already sorted array (descending)
        sorted_desc = list(range(size, 0, -1))
        test_cases.append(sorted_desc.copy())
        
        # Partially sorted arrays (90% sorted)
        partially_sorted = list(range(1, size + 1))
        # Randomly swap 10% of elements
        for _ in range(size // 10):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            partially_sorted[i], partially_sorted[j] = partially_sorted[j], partially_sorted[i]
        test_cases.append(partially_sorted.copy())
        
        # Nearly sorted arrays (95% sorted)
        nearly_sorted = list(range(1, size + 1))
        # Randomly swap 5% of elements
        for _ in range(size // 20):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
        test_cases.append(nearly_sorted.copy())
        
        # Worst case for QuickSort: Array with many duplicates
        duplicate_arr = [1] * (size // 2) + [2] * (size - size // 2)
        test_cases.append(duplicate_arr.copy())
        
        # Worst case for QuickSort: Array with pivot always being the smallest/largest
        pivot_worst = [size] + list(range(1, size))
        test_cases.append(pivot_worst.copy())
    
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
    quick_sort = QuickSort()
    quick_sort.sort(arr.copy())
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def run_performance_test(sizes, num_tests=50):
    """Run performance tests for different array sizes in worst case scenarios"""
    results = {
        'sizes': [],
        'dynamicsort_times': [],
        'quicksort_times': [],
        'depths': [],
        'dynamicsort_avg': [],
        'quicksort_avg': [],
        'dynamicsort_std': [],
        'quicksort_std': []
    }
    
    for size in sizes:
        print(f"Testing array size: {size} (Worst Case Scenarios)")
        
        # Calculate depth based on log2 of list length
        depth = int(math.log2(size))
        print(f"  Using depth: {depth} (log2 of {size})")
        
        test_cases = generate_worst_case_data(size, num_tests)
        dynamicsort_times = []
        quicksort_times = []
        
        for test_case in test_cases:
            # Test DynamicSort with calculated depth
            dynamic_time = benchmark_dynamicsort(test_case, depth)
            dynamicsort_times.append(dynamic_time)
            
            # Test QuickSort
            quick_time = benchmark_quicksort(test_case)
            quicksort_times.append(quick_time)
        
        # Calculate statistics
        dynamic_avg = np.mean(dynamicsort_times)
        quick_avg = np.mean(quicksort_times)
        dynamic_std = np.std(dynamicsort_times)
        quick_std = np.std(quicksort_times)
        
        results['sizes'].append(size)
        results['dynamicsort_times'].append(dynamicsort_times)
        results['quicksort_times'].append(quicksort_times)
        results['depths'].append(depth)
        results['dynamicsort_avg'].append(dynamic_avg)
        results['quicksort_avg'].append(quick_avg)
        results['dynamicsort_std'].append(dynamic_std)
        results['quicksort_std'].append(quick_std)
        
        print(f"  DynamicSort: {dynamic_avg:.3f}ms ± {dynamic_std:.3f}ms")
        print(f"  QuickSort: {quick_avg:.3f}ms ± {quick_std:.3f}ms")
        print(f"  Winner: {'DynamicSort' if dynamic_avg < quick_avg else 'QuickSort'}")
        print(f"  Speedup: {max(dynamic_avg, quick_avg) / min(dynamic_avg, quick_avg):.2f}x")
        print()
    
    return results

def create_performance_graphs(results):
    """Create graphs for worst case performance comparison"""
    
    # Create a figure with 3 subplots
    plt.figure(figsize=(18, 5))
    
    # Graph 1: Performance vs Array Size (Worst Case)
    plt.subplot(1, 3, 1)
    plt.plot(results['sizes'], results['dynamicsort_avg'], 
             label='DynamicSort (log2 depth)', marker='o', linewidth=2, markersize=6)
    plt.plot(results['sizes'], results['quicksort_avg'], 
             label='QuickSort', marker='s', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('Worst Case Performance: DynamicSort vs QuickSort')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Graph 2: Performance Ratio (QuickSort/DynamicSort)
    plt.subplot(1, 3, 2)
    ratios = [q/d for q, d in zip(results['quicksort_avg'], results['dynamicsort_avg'])]
    plt.plot(results['sizes'], ratios, marker='o', color='red', linewidth=2, markersize=6)
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Equal Performance')
    plt.xlabel('Array Size')
    plt.ylabel('Performance Ratio (QuickSort/DynamicSort)')
    plt.title('Performance Ratio: >1 = QuickSort Slower, <1 = DynamicSort Slower')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Graph 3: Speedup Analysis
    plt.subplot(1, 3, 3)
    speedups = [max(q, d) / min(q, d) for q, d in zip(results['quicksort_avg'], results['dynamicsort_avg'])]
    colors = ['green' if q > d else 'red' for q, d in zip(results['quicksort_avg'], results['dynamicsort_avg'])]
    plt.bar(results['sizes'], speedups, alpha=0.7, color=colors)
    plt.xlabel('Array Size')
    plt.ylabel('Speedup Factor')
    plt.title('Speedup: Green = DynamicSort Faster, Red = QuickSort Faster')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/worst_case_dynamicsort_vs_quicksort.png', dpi=300, bbox_inches='tight')

def analyze_worst_case():
    """Main analysis function"""
    print("=== Worst Case Performance Analysis ===")
    print("Testing DynamicSort vs QuickSort in worst case scenarios")
    print("Worst cases: Sorted arrays, reverse sorted, partially sorted, nearly sorted, duplicates, bad pivots")
    print("Testing on larger arrays: 100-3000 elements")
    print()
    
    # Test sizes focusing on larger arrays and partially sorted scenarios
    test_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000]
    
    print("Running worst case performance tests...")
    results = run_performance_test(test_sizes, num_tests=25)  # Reduced tests for larger arrays
    
    print("Creating performance graphs...")
    create_performance_graphs(results)
    
    # Analysis summary
    print("\n=== WORST CASE ANALYSIS SUMMARY ===")
    print("Array Size | Depth | DynamicSort | QuickSort | Winner | Speedup")
    print("-" * 70)
    
    for i, size in enumerate(results['sizes']):
        depth = results['depths'][i]
        dynamic_avg = results['dynamicsort_avg'][i]
        quick_avg = results['quicksort_avg'][i]
        
        winner = "DynamicSort" if dynamic_avg < quick_avg else "QuickSort"
        speedup = max(dynamic_avg, quick_avg) / min(dynamic_avg, quick_avg)
        
        print(f"{size:10} | {depth:5} | {dynamic_avg:11.3f}ms | {quick_avg:9.3f}ms | {winner:6} | {speedup:.2f}x")
