# Housing Prices Statistics - University project

## Description

This project analyzes and visualizes Hungarian housing price data from the Central Statistical Office (KSH).

The application:
- Reads CSV data with semicolon delimiters
- Parses and cleans the data (removes empty cells)
- Formats the data into a readable table with:
  - Aligned columns
  - Color-coded headers and data
  - Proper spacing and borders
  - Dates as column headers
  - Subsection titles for different categories

## Features

- **CSV Parsing**: Automatically loads and processes CSV files
- **Formatted Output**: Clean, human-readable table display
- **Color Support**: Uses colored text for better readability (headers in yellow, dates in green, borders in magenta)
- **Data Organization**: Groups data by subsections (Used apartments, New apartments, etc.)

## Data Source

The project works with housing price data from the Hungarian Central Statistical Office (KSH):
[KSH - Housing Price Statistics](https://www.ksh.hu/stadat_files/lak/hu/lak0014.html)

**Note**: This program was tested specifically with [data.csv](./data.csv) from the KSH. Other CSV formats may not work properly.

## Installation and usage

### Requirements
- Python 3.9 or higher


### Dependencies
- numpy - Numerical computations
- matplotlib - Data visualization
- pandas - Data manipulation
- colorama - Terminal color support


### Setup

Clone or download this project
```

```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage
Run the main script:

```bash
python main.py
```

Or use the formatter directly:

```bash
python extract_and_format_clean.py
```

## Project Structure
```
.
├── main.py                      # Main entry point
├── extract_and_format_clean.py  # CSV parsing and formatting
├── data.csv                     # Housing price data
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## License
MIT License

## Author
Szlucska Dóra