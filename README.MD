# Housing Prices Statistics - University Project

## Description

This project analyzes and visualizes Hungarian housing price data from the Central Statistical Office (KSH).

The application:
- Reads CSV data with semicolon delimiters
- Extracts and structures data by housing type and time period
- Generates statistical analysis (mean, standard deviation, min, max, trend)
- Creates line diagrams to show price trends over time
- Creates scatter plots with linear regression analysis
- Displays all visualizations with proper formatting and legends

## Features

- **CSV Parsing**: Automatically loads and processes CSV files from KSH
- **Data Extraction**: Organizes data by subsections and housing types
- **Statistical Analysis**: Calculates mean, std dev, min, max, and trend values
- **Line Diagrams**: Visualizes price trends for each housing type over 2007-2024
- **Scatter Plots**: Shows data distribution with linear regression overlay
- **Linear Regression**: Calculates R² values to measure correlation quality
- **Multilingual Support**: Supports both Hungarian and English interfaces
- **Color Support**: Uses colored output for better readability

## Data Source

The project works with housing price data from the Hungarian Central Statistical Office (KSH):
[KSH - Housing Price Statistics](https://www.ksh.hu/stadat_files/lak/hu/lak0014.html)

**Note**: This program was tested specifically with [data.csv](./data/data.csv) from the KSH. Other CSV formats may not work properly.

## Installation and Usage

### Requirements
- Python 3.9 or higher

### Dependencies
- **numpy** - Numerical computations
- **matplotlib** - Data visualization
- **scipy** - Statistical analysis and linear regression
- **colorama** - Terminal color support

### Setup

1. Clone or download this project
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage
Run the main script:

```bash
python main.py
```

## Project Structure
```md
.
├── [main.py](main.py)                                  # Main entry point
│
├── config/
│   ├── [config.py](config/config.py)                   # Configuration and logging setup
│   └── [translations.py](config/translations.py)       # Multilingual text support
│
├── scripts/
│   ├── [draw_diagram.py](scripts/draw_diagram.py)      # Line and scatter plot generation
│   ├── [extract.py](scripts/extract.py)                # CSV parsing and data extraction
│   └── [print_table.py](scripts/print_table.py)        # Formatted table display
│
├── data/
│   └── [data.csv](data/data.csv)                       # Housing price data
│
├── [pyproject.toml](pyproject.toml)                    # Project configuration
├── [requirements.txt](requirements.txt)                # Python dependencies
└── [README.md](README.md)                              # This file

```

## Features in Detail

### Data Visualization

- **Line Diagrams**: Show price trends for Family Houses, Apartment Buildings, Housing Estates, and Total
- **Scatter Plots**: Display individual data points with regression line overlay
- **Regression Analysis**: Calculates slope, intercept, and R² value for each housing type

### Statistical Metrics

- Mean price
- Standard deviation
- Minimum value
- Maximum value
- Trend (change from 2007 to 2024)

### Supported Languages

- Hungarian (hu)
- English (en)

Configure language in [`config/config.py`](config/config.py):

```python
lang = "hu"  # or "en"
```

## License
MIT License

## Author
Szlucska Dóra