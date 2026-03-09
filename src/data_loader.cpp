#include "data_loader.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

// function will read CSV and convert rows into StockRecord objects
std::vector<StockRecord> loadDataset(const std::string& filename) {
    std::vector<StockRecord> records;
    std::ifstream file(filename);
    std::string line;

    if (!file.is_open()) {
        std::cerr << "Error: cannot open dataset: " << filename << std::endl;
        return records;
    }

    // read/discard header row
    std::getline(file, line);

    while (std::getline(file, line)) {
        if (line.empty()) {
            continue;
        }

        std::stringstream lineStream(line);
        std::string columnValue;
        std::vector<std::string> columns;

        while (std::getline(lineStream, columnValue, ',')) {
            columns.push_back(columnValue);
        }

        if (columns.size() != 9) {
            continue;
        }

        try {
            StockRecord record;

            // assign values to fields in StockRecord
            record.date = columns[0];
            record.open = std::stod(columns[1]);
            record.high = std::stod(columns[2]);
            record.low = std::stod(columns[3]);
            record.close = std::stod(columns[4]);
            record.adjClose = std::stod(columns[5]);
            record.volume = std::stoll(columns[6]);
            record.ticker = columns[7];
            record.company = columns[8];

            records.push_back(record);
        }
        catch (...) {
            continue;
        }
    }

    return records;
}