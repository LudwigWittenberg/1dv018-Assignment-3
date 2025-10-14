import time
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from src.utils.DynamicSort import DynamicSort

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

def run_performance_test(sizes, num_tests=100):
    """Run performance tests for different array sizes with sqrt-based depths"""
    results = {
        'sizes': [],
        'dynamicsort_times': [],
        'depths': [],
        'dynamicsort_avg': [],
        'dynamicsort_std': []
    }
    
    for size in sizes:
        print(f"Testing array size: {size}")
        
        # Calculate depth based on square root of list length
        depth = int(math.sqrt(size))
        print(f"  Using depth: {depth} (sqrt of {size})")
        
        test_cases = generate_test_data(size, num_tests)
        dynamicsort_times = []
        
        for test_case in test_cases:
            # Test DynamicSort with calculated depth
            dynamic_time = benchmark_dynamicsort(test_case, depth)
            dynamicsort_times.append(dynamic_time)
        
        # Calculate statistics
        dynamic_avg = np.mean(dynamicsort_times)
        dynamic_std = np.std(dynamicsort_times)
        
        results['sizes'].append(size)
        results['dynamicsort_times'].append(dynamicsort_times)
        results['depths'].append(depth)
        results['dynamicsort_avg'].append(dynamic_avg)
        results['dynamicsort_std'].append(dynamic_std)
        
        print(f"  DynamicSort: {dynamic_avg:.3f}ms ± {dynamic_std:.3f}ms")
        print(f"  Depth used: {depth}")
        print()
    
    return results

def create_performance_graphs(results):
    """Create line graph for DynamicSort performance"""
    
    # Create a single figure with only the performance comparison graph
    plt.figure(figsize=(10, 6))
    
    # Performance comparison line graph
    plt.plot(results['sizes'], results['dynamicsort_avg'], 
             label='DynamicSort (sqrt depth)', marker='o', linewidth=2, markersize=6)
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (milliseconds)')
    plt.title('DynamicSort Performance - Depth = sqrt(Array Size)')
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
    print("Array Size | Depth | DynamicSort Avg | Std Dev")
    print("-" * 50)
    
    for i, size in enumerate(results['sizes']):
        depth = results['depths'][i]
        dynamic_avg = results['dynamicsort_avg'][i]
        dynamic_std = results['dynamicsort_std'][i]
        
        print(f"{size:10} | {depth:5} | {dynamic_avg:13.3f}ms | {dynamic_std:6.3f}ms")
    
    # Depth analysis
    print(f"\n=== DEPTH ANALYSIS ===")
    print("Depth progression based on sqrt(array_size):")
    for i, size in enumerate(results['sizes']):
        depth = results['depths'][i]
        print(f"Array size {size:3}: depth = {depth} (sqrt({size}) = {math.sqrt(size):.2f})")