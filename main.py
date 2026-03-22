from data_loader import loadDataset, StockRecord
from benchmark import benchmark_trials, print_benchmark_summary
from merge_sort import merge_sort_top_k
from heap_sort import heapsort_top_k

VALID_METRICS = ["open", "high", "low", "close", "adjClose", "volume"]


def filterByTicker(records, ticker):
    return [record for record in records if record.ticker.upper() == ticker.upper()]


def formatTopKRecord(record, metric):
    return (
        f"Ticker: {record.ticker} | "
        f"Date: {record.date} | "
        f"Category: {metric} | "
        f"Value: {getattr(record, metric)}"
    )


def runProgram(data):
    ticker = input("Enter ticker: ").strip()
    metric = input("Enter metric (open, high, low, close, adjClose, volume): ").strip()
    k = input("Enter K: ").strip()

    if metric not in VALID_METRICS:
        print("Invalid metric.")
        return

    try:
        k = int(k)
        if k <= 0:
            print("K must be greater than 0.")
            return
    except ValueError:
        print("Invalid K.")
        return

    filteredData = filterByTicker(data, ticker)
    print("Records found for", ticker + ":", len(filteredData))

    if len(filteredData) == 0:
        print("No records found for that ticker.")
        return

    print("Selected ticker:", ticker)
    print("Selected metric:", metric)
    print("Selected K:", k)

    # remember, top k LARGEST values
    # use full StockRecord objects
    # compare records using the selected metric
    # final output format should display ticker, date, category, and value

    # data flow for algorithms:
    # first, loadDataset() loads full dataset
    # second, filterByTicker() creates filtered list of StockRecord objects
    # third, both algorithms receive the same filteredData
    # lastly, algorithm interface: function(records, metric, k)
    # records = filteredData
    # metric = selected metric string
    # k = positive integer

    # merge sort
    ms_results, ms_runtimes, ms_avg = benchmark_trials(merge_sort_top_k, filteredData, metric, k)
    print_benchmark_summary("Merge Sort", ms_runtimes, ms_avg)

    print(f"\nTop {len(ms_results)} Results (Merge Sort):")
    for record in ms_results:
        print(formatTopKRecord(record, metric))

    # heap sort
    heap_results, heap_runtimes, heap_avg = benchmark_trials(heapsort_top_k, filteredData, metric, k)
    print_benchmark_summary("Heap Sort", heap_runtimes, heap_avg)

    print(f"\nTop {len(heap_results)} Results (Heap Sort):")
    for record in heap_results:
        print(formatTopKRecord(record, metric))

    # both approaches should receive the same filteredData
    # both approaches should use the same ticker
    # both approaches should use the same metric
    # both approaches should use the same K value
    # both approaches should give output in the same format

    # check if correct results were pulled
    if len(ms_results) == len(heap_results):
        same_results = True
        for i in range(len(ms_results)):
            if ms_results[i].ticker != heap_results[i].ticker or ms_results[i].date != heap_results[i].date or getattr(ms_results[i], metric) != getattr(heap_results[i], metric):
                same_results = False
                break

        if same_results:
            print("\nCorrectness check: Merge Sort and Heap Sort produced matching Top-K results.")
        else:
            print("\nCorrectness check: Warning - Merge Sort and Heap Sort results do not fully match.")
    else:
        print("\nCorrectness check: Warning - Merge Sort and Heap Sort returned different numbers of results.")

    # compare runtimes together
    print("\nRuntime Comparison Summary:")
    print(f"Merge Sort Average Runtime: {ms_avg:.8f} seconds")
    print(f"Heap Sort Average Runtime: {heap_avg:.8f} seconds")

    if heap_avg < ms_avg:
        print("Heap Sort was faster on this trial set.")
    elif ms_avg < heap_avg:
        print("Merge Sort was faster on this trial set.")
    else:
        print("Both approaches had the same average runtime.")


# menu
def main():
    data = loadDataset("data/All_data.csv")
    print("Records loaded:", len(data))

    if len(data) == 0:
        print("No data loaded.")
        return

    while True:
        runProgram(data)

        choice = input("\nEnter 'r' to run again or 'e' to exit: ").strip().lower()

        if choice == "e":
            print("Program ended.")
            break

        elif choice != "r":
            print("Invalid choice. Program ended.")
            break


if __name__ == "__main__":
    main()