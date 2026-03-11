from data_loader import loadDataset


def main():
    data = loadDataset("../data/All_data.csv")
    print("Records loaded:", len(data))

    if len(data) > 0:
        print("First record:", data[0].ticker, data[0].date, data[0].close)


if __name__ == "__main__":
    main()