from colorama import Fore, Style, init

init(autoreset=True)

# ============ Configuration ============
HEADER_COLOR = Fore.YELLOW
DATES_COLOR = Fore.GREEN
BORDER_COLOR = Fore.MAGENTA
MAIN_TITLE_COLOR = Fore.CYAN

CELL_WIDTH_LEFT = 30
CELL_WIDTH_RIGHT = 5
COLUMN_SEPARATOR = " │ "


# ============ Format Helpers ============
def format_data_row(row, color=Fore.RESET):
    """Format a single data row with colors and proper spacing."""
    first_cell = row[0].ljust(CELL_WIDTH_LEFT)
    rest_cells = [color + cell.rjust(CELL_WIDTH_RIGHT) + Style.RESET_ALL for cell in row[1:]]
    return COLUMN_SEPARATOR.join([first_cell] + rest_cells) + " │"
  
  
def format_title(row, width, color = HEADER_COLOR):
    """Format title centered and colored."""
    text = "".join(row)
    return color + text.center(width) + Style.RESET_ALL


def create_border_line(width):
    """Create horizontal line separator."""
    return "─" * ((width) + CELL_WIDTH_LEFT)


def create_column_divider(num_columns):
    """Create row divider with column separators (├─┼─┤)."""
    left_part = " " * CELL_WIDTH_LEFT + " ├"
    middle_part = ("─" * (CELL_WIDTH_RIGHT + 2) + "┼") * (num_columns - 1)
    return left_part + middle_part[:-1] + "┤"


# ============ Table Printing ============
def print_table(data):
    """Print formatted table with titles, headers, and data."""
    if len(data) < 2:
        return
      
    # extract dates header "2007, 2008, ..."
    DATES_ROW = data[1] 
    
    NUM_COLUMNS = len(DATES_ROW)
    TABLE_WIDTH = CELL_WIDTH_LEFT + (NUM_COLUMNS - 1) * (CELL_WIDTH_RIGHT + len(COLUMN_SEPARATOR))

    # init separators
    BORDER = create_border_line(TABLE_WIDTH)
    DIVIDER = create_column_divider(NUM_COLUMNS)

    print()
    print(BORDER_COLOR + BORDER)

    for i, row in enumerate(data):
        # main title
        if i == 0:
            print("\n" + format_title(row, TABLE_WIDTH, color=MAIN_TITLE_COLOR) + "\n")

        # skip dates header for now
        elif i == 1:
            pass

        # subtable titles
        elif len(row) < 3:
            print("\n" + format_title(row, TABLE_WIDTH) + "\n")
            print(format_data_row(DATES_ROW, DATES_COLOR))
            print(DIVIDER)

        # data rows
        else:
            print(format_data_row(row))

    print("\n" + BORDER_COLOR + BORDER + "\n")
