from dataclasses import dataclass
from typing import List


# rows from dataset
# records should filter by ticker
# analyze by whatever metric user picks for top-k
# use full StockRecord objects for output
# compare records using the selected metric
@dataclass
class StockRecord:
    date: str
    open: float
    high: float
    low: float
    close: float
    adjClose: float
    volume: int
    ticker: str
    company: str


# function will read CSV and convert rows into StockRecord objects
def loadDataset(filename: str) -> List[StockRecord]:
    records: List[StockRecord] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            # read/discard header row
            file.readline()

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                columns = line.split(",")

                # expected columns: 0. date, 1. open, 2. high, 3. low, 4. close,
                # 5. adjClose, 6. volume, 7. ticker, 8. company
                if len(columns) != 9:
                    continue

                try:
                    # assign values to fields in StockRecord
                    record = StockRecord(
                        date=columns[0],
                        open=float(columns[1]),
                        high=float(columns[2]),
                        low=float(columns[3]),
                        close=float(columns[4]),
                        adjClose=float(columns[5]),
                        volume=int(columns[6]),
                        ticker=columns[7],
                        company=columns[8]
                    )

                    records.append(record)

                except ValueError:
                    continue

    except FileNotFoundError:
        print("Error: cannot open dataset", filename)

    return records