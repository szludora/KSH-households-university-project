# from print_table import print_table


def load_csv(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip().split(';') for line in file]
        return [[cell for cell in row if cell] for row in rows]


def print_data_raw(data):
    print("\n\n")
    for row in data: print(row)


def main():
    data = load_csv("data.csv")

    # print_table(data)
    print_data_raw(data)




if __name__ == "__main__":
    main()