from config import LOG_TYPES, MAGENTA, RESET, YELLOW, GREEN, MAGENTA, CYAN, Log

Log("Print table module loaded", level=LOG_TYPES.INFO)

# ======================== Configuration ========================
CELL_WIDTH_LEFT = 30
CELL_WIDTH_RIGHT = 5
COLUMN_SEPARATOR = " │ "


# ======================== Format Helpers ========================
def __format_data_row(row, color=RESET):
    """Format a single data row with colors and proper spacing."""
    first_cell = row[0].ljust(CELL_WIDTH_LEFT)
    rest_cells = [color + cell.rjust(CELL_WIDTH_RIGHT) + RESET for cell in row[1:]]
    return COLUMN_SEPARATOR.join([first_cell] + rest_cells) + " │"
  
  
def __format_title(row, width, color = YELLOW):
    """Format title centered and colored."""
    text = "".join(row)
    return color + text.center(width) + RESET


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

    Log()
    Log(MAGENTA + BORDER, level=LOG_TYPES.DEBUG, show_label=False)
    Log( "Printing formatted table...", level=LOG_TYPES.DEBUG)

    for i, row in enumerate(data):
        # main title
        if i == 0:
            Log("\n" + __format_title(row, TABLE_WIDTH, color=CYAN) + "\n", level=LOG_TYPES.DEBUG, show_label=False)

        # skip dates header for now
        elif i == 1:
            pass

        # subtable titles
        elif len(row) < 3:
            Log("\n" + __format_title(row, TABLE_WIDTH) + "\n", level=LOG_TYPES.DEBUG, show_label=False)
            Log(__format_data_row(DATES_ROW, GREEN), level=LOG_TYPES.DEBUG, show_label=False)
            Log(DIVIDER, level=LOG_TYPES.DEBUG, show_label=False)

        # data rows
        else:
            Log(__format_data_row(row), level=LOG_TYPES.DEBUG, show_label=False)

    Log("\n" + MAGENTA + BORDER + "\n", level=LOG_TYPES.DEBUG, show_label=False)