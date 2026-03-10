#ifndef DATA_LOADER_H
#define DATA_LOADER_H

#include <string>
#include <vector>

// rows from dataset
struct StockRecord {
    std::string date;
    double open;
    double high;
    double low;
    double close;
    double adjClose;
    long long volume;
    std::string ticker;
    std::string company;
};

// read csv and return vector
std::vector<StockRecord> loadDataset(const std::string& filename);

#endif