#include <iostream>
#include "data_loader.h"

int main() {
    auto data = loadDataset("../data/All_data.csv");
    std::cout<< "Records loaded: " << data.size() << std::endl;
    if (!data.empty()) {
        std::cout << "First record: "
                  << data[0].ticker << " "
                  << data[0].date << " "
                  << data[0].close << std::endl;
    }

    return 0;
}