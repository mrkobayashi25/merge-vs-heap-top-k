import time

# rules for benchmark testing:
# both receive exact same dataset
# both use same ticker
# both use same metric
# both use same K value
# both give output in same format
# measure algorithm time not user input time

# algorithm interface: function(records, metric, k) -> list of full StockRecord

# records should be filtered before testing
# both algorithms should return LARGEST values
# results should be ordered the same way consistently for neatness in display

DEFAULT_TRIALS = 5

# run a single timed benchmark
def benchmark_once(algorithm_function, records, metric, k):
    start_time = time.perf_counter()
    result = algorithm_function(records, metric, k)
    end_time = time.perf_counter()

    runtime = end_time - start_time
    return result, runtime

# run multiple trials to get mean of runtime
def benchmark_trials(algorithm_function, records, metric, k, trials=DEFAULT_TRIALS):
    runtimes = []
    last_result = None

    for _ in range(trials):
        result, runtime = benchmark_once(algorithm_function, records, metric, k)
        last_result = result
        runtimes.append(runtime)

    average_runtime = sum(runtimes) / len(runtimes)
    return last_result, runtimes, average_runtime

# print times and mean
def print_benchmark_summary(name, runtimes, average_runtime):
    print(f"\n{name} Benchmark Results")
    for i, runtime in enumerate(runtimes, start=1):
        print(f"Trial {i}: {runtime:.8f} seconds")
    print(f"Average Runtime: {average_runtime:.8f} seconds")

# do outputs have same number of results?
def compare_result_lengths(results_a, results_b):
    return len(results_a) == len(results_b)

# is result a list
def is_valid_result_structure(results):
    return isinstance(results, list)