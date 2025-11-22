from config.config import LOG_TYPES, Log
from scripts.draw_diagram import draw_diagrams
from scripts.extract import extract_data
from scripts.print_table import print_table

FILE_PATH = "./data/data.csv"

# helper function to load CSV data
def load_csv(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip().split(';') for line in file]
        return [[cell for cell in row if cell] for row in rows]


def main():
    Log("Main module loaded", level=LOG_TYPES.INFO)
    raw = load_csv(FILE_PATH) # load CSV data from file
    print_table(raw)  # for debugging purposes
    draw_diagrams(extract_data(raw), cols=2)  # draw line and plot diagrams with regressions

if __name__ == "__main__":
    main()