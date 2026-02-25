# Algorithm Analysis and Implementation

## Overview

This project implements and compares two sorting algorithms: Bubble Sort and QuickSort.  
The objective is to analyse their theoretical time complexity (Big-O notation) and evaluate their practical performance through benchmarking.

## Algorithms

**Bubble Sort** is a comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order.  
- Average/Worst Case: O(n²)  
- Best Case: O(n)

**QuickSort** is a divide-and-conquer algorithm that partitions the array around a pivot and recursively sorts sub-arrays.  
- Average Case: O(n log n)  
- Worst Case: O(n²)

## Benchmarking

Execution time was measured for multiple input sizes using Python’s `time.perf_counter()` function.  
Results were visualised in a performance graph.

## Results and Conclusion

The results confirm that Bubble Sort demonstrates quadratic growth and becomes inefficient as input size increases.  
QuickSort shows significantly better scalability, making it more suitable for large datasets.

This project highlights the importance of combining theoretical complexity analysis with empirical performance evaluation.
