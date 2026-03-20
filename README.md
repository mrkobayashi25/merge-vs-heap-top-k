Top-K Extraction from Historical Stock Data Using Sorting and Heap Data Structures

Our project compares merge sort and heap sort approaches for Top-K extraction on a dataset containing
over 100k rows of historical stock market data for select companies. Our goal is to compare efficiency
of both methods where only the highest metrics are the desired output. 

Required files:
  - main.py
  - data_loader.py
  - benchmark.py
  - merge_sort.py
  - heap_sort.py (to be added...)
  - data/All_data.csv

How to run:
  - open a terminal in the project folder and run: python main.py

When prompted: 
  Records loaded: 108696
  Enter ticker: (here, users should enter one of the valid stock market tickers; AA, B, C, D, E, F, G, 
  H, IAC, J, K, L)
  Enter metric (open, high, low, close, adjClose, volume): (input one of the given metrics in the 
  prompt)
  Enter K: (this should be a positie integer)
