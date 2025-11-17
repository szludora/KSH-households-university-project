from config.config import LOG_TYPES, YELLOW, Log, LOG, RESET, MAGENTA, lang
from config.translations import section_titles, row_types


Log("Main module loaded", level=LOG_TYPES.INFO)


def extract_data(data):
    Log("Cleaning data..." + RESET, level=LOG_TYPES.DEBUG)
    
    
    raw_data = __remove_first_two_headers(data)
    extracted = __get_subtables(raw_data)
    
    __print_data_raw(raw_data)  # only when DEEP_DEBUG is enabled in config.py
    
    Log("Extracting data..." + RESET, level=LOG_TYPES.INFO)
    
    Log("", level=LOG_TYPES.DEEP_DEBUG)
    Log(extracted, level=LOG_TYPES.DEEP_DEBUG)
    Log("\n\n", level=LOG_TYPES.DEEP_DEBUG)
    
    Log("Extraction complete." + RESET, level=LOG_TYPES.DEBUG)

    return extracted
# ======================== helpers for cleaning data and formatting print output ========================


def __remove_first_two_headers(data, from_cell=2):    # Skip first two header rows
    return data[from_cell:]     

is_new_table_start = lambda row: len(row) == 1      # print raw data for debugging


def __print_data_raw(data):
    for i in range(len(data)):
        row = data[i]
        if is_new_table_start(row):
            Log('\n' + YELLOW + str(*row) + RESET + '\n', level=LOG_TYPES.DEEP_DEBUG, show_label=False)
        else:
            title = data[i][0]
            rest = '\t'.join(row[1:])
            Log(f"{title:<20}\t{rest}", level=LOG_TYPES.DEEP_DEBUG, show_label=False)                    
    Log("\n\n", level=LOG_TYPES.DEEP_DEBUG)



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
