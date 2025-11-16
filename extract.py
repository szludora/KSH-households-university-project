from config import HEADER_COLOR, Log, LOG, RESET_COLOR, ACTION_COLOR, lang
from translations import section_titles, row_types

def extract_data(data):
    Log(ACTION_COLOR + "\n\n\nCleaning data..." + RESET_COLOR, level="INFO")
    
    
    raw_data = __remove_first_two_headers(data)
    extracted = __get_subtables(raw_data)
    
    __print_data_raw(raw_data)  # only when DEEP_DEBUG is enabled in config.py
    
    Log(ACTION_COLOR + "Extracting data into dict..." + RESET_COLOR, level="INFO")
    
    Log("", level="DEEP_DEBUG")
    Log(extracted, level="DEEP_DEBUG")
    Log("\n\n", level="DEEP_DEBUG")
    
    Log(ACTION_COLOR + "Extraction complete.\n\n\n" + RESET_COLOR, level="INFO")

    return extracted
# ======================== helpers for cleaning data and formatting print output ========================


def __remove_first_two_headers(data, from_cell=2):    # Skip first two header rows
    return data[from_cell:]     

is_new_table_start = lambda row: len(row) == 1      # print raw data for debugging


def __print_data_raw(data):
    for i in range(len(data)):
        row = data[i]
        if is_new_table_start(row):
            Log('\n' + HEADER_COLOR + str(*row) + RESET_COLOR + '\n', level="DEEP_DEBUG")
        else:
            title = data[i][0]
            rest = '\t'.join(row[1:])
            Log(f"{title:<20}\t{rest}", level="DEEP_DEBUG")                    
    Log("\n\n", level="DEEP_DEBUG")



def __get_subtables(data):
    # Select index: 0 for English, 1 for Hungarian
    lang_idx = 1 if lang and lang == "hu" else 0
    
    tables = {}
    current_section = None
    
    for row in data:
        # create new section in dictionary
        if is_new_table_start(row):
            section = row[0]
            current_section = section_titles[section][lang_idx]
            tables[current_section] = {}
        # add row data to current section
        else:
            row_type_hu = row[0]
            row_type_key = row_types[row_type_hu][lang_idx]
            tables[current_section][row_type_key] = row[1:] # skip first cell
    
    return tables
