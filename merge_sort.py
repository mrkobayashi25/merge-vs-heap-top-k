from data_loader import StockRecord
from typing import List


def merge_sort_top_k(records: List[StockRecord], metric: str, k: int) -> List[StockRecord]:
    """ Sorts using Merge Sort in descending order and returns the Top-K elements. """
    # Defensive copy to avoid modifying the original filtered data
    data_to_sort = list(records)

    if not data_to_sort:
        return []

    sorted_records = _merge_sort(data_to_sort, metric)

    # Return the first K elements (Top K LARGEST)
    return sorted_records[:k]


def _merge_sort(records: List[StockRecord], metric: str) -> List[StockRecord]:
    """Recursive helper for Merge Sort."""
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left_half = _merge_sort(records[:mid], metric)
    right_half = _merge_sort(records[mid:], metric)

    return _merge(left_half, right_half, metric)


def _merge(left: List[StockRecord], right: List[StockRecord], metric: str) -> List[StockRecord]:
    """Merges two lists in descending order based on the selected metric."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # We want descending order, so we pick the larger value first
        # getattr(record, metric) allows dynamic access (e.g., record.open or record.volume)
        if getattr(left[i], metric) >= getattr(right[j], metric):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result