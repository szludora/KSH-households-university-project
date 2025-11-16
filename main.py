import matplotlib.pyplot as plt         # pip install matplotlib
import numpy as np                      # pip install numpy

from extract import extract_data
from print_table import print_table



def load_csv(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip().split(';') for line in file]
        return [[cell for cell in row if cell] for row in rows]


def main():
    raw = load_csv("data.csv")
    print_table(raw)  # print formatted table
    data = extract_data(raw)  # extract raw data into structured format


if __name__ == "__main__":
    main()