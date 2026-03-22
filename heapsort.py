from data_loader import StockRecord
from typing import List


def heapsort_top_k(records: List[StockRecord], metric: str, k: int) -> List[StockRecord]:
    # Manual implementation of Heap Sort to return top-k elements
    # Time complexity of O(nlogn)
    data = list(records)
    n = len(data)

    if n == 0 or k == 0:
        return []

    for i in range(n // 2 - 1, -1, -1):
        _heapify(data, n, i, metric)

    result = []

    for i in range(n - 1, n - 1 - min(k, n), -1):

        result.append(data[0])

        data[0] = data[i]
        _heapify(data, i, 0, metric)

    return result


def _heapify(arr: List[StockRecord], n: int, i: int, metric: str):
    # Helper function for heapsort

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and getattr(arr[left], metric) > getattr(arr[largest], metric):
        largest = left

    if right < n and getattr(arr[right], metric) > getattr(arr[largest], metric):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest, metric)