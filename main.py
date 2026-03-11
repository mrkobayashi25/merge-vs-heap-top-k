from data_loader import loadDataset

VALID_METRICS = ["open", "high", "low", "close", "adjClose", "volume"]


def filterByTicker(records, ticker):
    return [record for record in records if record.ticker.upper() == ticker.upper()]


def extractMetricValues(records, metric):
    return [getattr(record, metric) for record in records]


def main():
    data = loadDataset("../data/All_data.csv")
    print("Records loaded:", len(data))

    if len(data) == 0:
        print("No data loaded.")
        return

    print("First record:", data[0].ticker, data[0].date, data[0].close)

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

    metricValues = extractMetricValues(filteredData, metric)

    print("Selected ticker:", ticker)
    print("Selected metric:", metric)
    print("Selected K:", k)
    print("First few metric values:", metricValues[:5])

# later: call merge sort top-k and heap top-k


if __name__ == "__main__":
    main()