from config import LOG_TYPES, Log
from draw_diagram import draw_diagrams
from extract import extract_data
from print_table import print_table


def load_csv(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip().split(';') for line in file]
        return [[cell for cell in row if cell] for row in rows]


def main():
    Log("Main module loaded", level=LOG_TYPES.INFO)
    raw = load_csv("data.csv")
    print_table(raw)    
    draw_diagrams(extract_data(raw), cols=2)

if __name__ == "__main__":
    main()