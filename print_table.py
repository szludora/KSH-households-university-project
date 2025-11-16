from colorama import Fore, Style, init
from config import HEADER_COLOR, DATES_COLOR, BORDER_COLOR, MAIN_TITLE_COLOR, Log

init(autoreset=True)

# ======================== Configuration ========================
CELL_WIDTH_LEFT = 30
CELL_WIDTH_RIGHT = 5
COLUMN_SEPARATOR = " │ "


# ======================== Format Helpers ========================
def __format_data_row(row, color=Fore.RESET):
    """Format a single data row with colors and proper spacing."""
    first_cell = row[0].ljust(CELL_WIDTH_LEFT)
    rest_cells = [color + cell.rjust(CELL_WIDTH_RIGHT) + Style.RESET_ALL for cell in row[1:]]
    return COLUMN_SEPARATOR.join([first_cell] + rest_cells) + " │"
  
  
def __format_title(row, width, color = HEADER_COLOR):
    """Format title centered and colored."""
    text = "".join(row)
    return color + text.center(width) + Style.RESET_ALL


def __create_border_line(width):
    """Create horizontal line separator."""
    return "─" * ((width) + CELL_WIDTH_LEFT)


def __create_column_divider(num_columns):
    """Create row divider with column separators (├─┼─┤)."""
    left_part = " " * CELL_WIDTH_LEFT + " ├"
    middle_part = ("─" * (CELL_WIDTH_RIGHT + 2) + "┼") * (num_columns - 1)
    return left_part + middle_part[:-1] + "┤"


# ======================== Table Printing ========================
def print_table(data):
    """Print formatted table with titles, headers, and data."""
    if len(data) < 2:
        return
      
    # extract dates header "2007, 2008, ..."
    DATES_ROW = data[1] 
    
    NUM_COLUMNS = len(DATES_ROW)
    TABLE_WIDTH = CELL_WIDTH_LEFT + (NUM_COLUMNS - 1) * (CELL_WIDTH_RIGHT + len(COLUMN_SEPARATOR))

    # init separators
    BORDER = __create_border_line(TABLE_WIDTH)
    DIVIDER = __create_column_divider(NUM_COLUMNS)

    Log(level="INFO")
    Log(BORDER_COLOR + BORDER, level="INFO")

    for i, row in enumerate(data):
        # main title
        if i == 0:
            Log("\n" + __format_title(row, TABLE_WIDTH, color=MAIN_TITLE_COLOR) + "\n", level="INFO")

        # skip dates header for now
        elif i == 1:
            pass

        # subtable titles
        elif len(row) < 3:
            Log("\n" + __format_title(row, TABLE_WIDTH) + "\n", level="INFO")
            Log(__format_data_row(DATES_ROW, DATES_COLOR), level="INFO")
            Log(DIVIDER, level="INFO")

        # data rows
        else:
            Log(__format_data_row(row), level="INFO")

    Log("\n" + BORDER_COLOR + BORDER + "\n", level="INFO")
