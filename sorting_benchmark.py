import random
import time
import statistics
import matplotlib.pyplot as plt


# ----------------------------
# Bubble Sort
# ----------------------------
def bubble_sort(data_list):
    copied_list = data_list[:]
    length = len(copied_list)

    for outer_index in range(length):
        for inner_index in range(0, length - outer_index - 1):
            if copied_list[inner_index] > copied_list[inner_index + 1]:
                copied_list[inner_index], copied_list[inner_index + 1] = \
                copied_list[inner_index + 1], copied_list[inner_index]

    return copied_list


# ----------------------------
# Quick Sort
# ----------------------------
def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list

    pivot_value = data_list[len(data_list) // 2]

    smaller_part = [element for element in data_list if element < pivot_value]
    equal_part = [element for element in data_list if element == pivot_value]
    greater_part = [element for element in data_list if element > pivot_value]

    return quick_sort(smaller_part) + equal_part + greater_part


# ----------------------------
# Time Measurement
# ----------------------------
def measure_execution_time(algorithm_function, input_data, repetitions=3):
    execution_times = []

    for run in range(repetitions):
        start_time = time.perf_counter()
        algorithm_function(input_data)
        end_time = time.perf_counter()

        execution_times.append(end_time - start_time)

    return statistics.median(execution_times)


# ----------------------------
# Benchmark
# ----------------------------
def run_benchmark():

    random.seed(20)


    input_sizes = [100, 300, 600, 1000, 1500, 2500, 3500]

    bubble_results = []
    quick_results = []

    for size in input_sizes:
        generated_numbers = [random.randint(0, 1000000) for _ in range(size)]

        bubble_time = measure_execution_time(bubble_sort, generated_numbers)
        quick_time = measure_execution_time(quick_sort, generated_numbers)

        bubble_results.append(bubble_time)
        quick_results.append(quick_time)

    print("Input sizes:", input_sizes)
    print("Bubble Sort times:", bubble_results)
    print("Quick Sort times:", quick_results)

    plt.figure(figsize=(8,5))
    plt.plot(input_sizes, bubble_results, marker="o", label="Bubble Sort O(n^2)")
    plt.plot(input_sizes, quick_results, marker="o", label="Quick Sort O(n log n)")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison of Sorting Algorithms")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("sorting_performance.png", dpi=200)
    plt.show()

    print("Graph saved as sorting_performance.png")


if __name__ == "__main__":
    run_benchmark()