# Housing Prices Statistics - University Project

## Description

This project analyzes and visualizes Hungarian housing price data from the Central Statistical Office (KSH). Created for the Basics of the Software Development course, the program demonstrates data visualization, and linear regression techniques.

The application:

- Reads CSV data with semicolon delimiters
- Extracts and structures data by housing type and time period (2007-2024)
- Generates line diagrams to show price trends over time
- Creates scatter plots with linear regression analysis
- Calculates R² values to measure trend reliability
- Displays all visualizations with proper formatting and legends
- Supports both Hungarian and English languages

## Features

- **CSV Parsing**: Automatically loads and processes CSV files from KSH
- **Data Extraction**: Organizes data by 4 price sections and 4 housing types
- **Line Diagrams**: Visualizes price trends for each housing type (2007-2024)
- **Scatter Plots**: Shows data distribution with linear regression overlay
- **Linear Regression**: Calculates R² values (0.85-0.95) showing strong correlation
- **Multilingual Support**: Supports both Hungarian and English interfaces
- **Configurable Logging**: Color-coded terminal output with adjustable log levels
- **Modular Design**: Clean, well-organized code structure

## Data Source

The project works with housing price data from the Hungarian Central Statistical Office (KSH):
[KSH - Housing Price Statistics](https://www.ksh.hu/stadat_files/lak/hu/lak0014.html)

**Data Coverage**:

- **Time Period**: 2007-2024 (18 years)
- **Housing Types**: Family Houses, Apartment Buildings, Housing Estates, Total
- **Data Points**: ~288 (4 sections × 4 types × 18 years)

**Note**: This program was tested specifically with [data.csv](./data.csv) from the KSH. Other CSV formats may not work properly.

## Installation and Usage

### Requirements

- Python 3.13 or higher (tested with Python 3.13.3)

### Dependencies

- **numpy** - Numerical computations and data handling
- **matplotlib** - Data visualization and chart generation
- **scipy** - Statistical analysis and linear regression
- **colorama** - Terminal color support for logging

### Setup

1. Clone or download this project
2. Install dependencies:

```bash
pip install numpy matplotlib scipy colorama
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

### Usage

Run the main script:

```bash
python main.py
```

**Output**:

1. Line diagrams window opens (close to continue)
2. Scatter plots with regression lines window opens

## Project Structure

```
├── main.py                      # Main entry point
├── data.csv                     # KSH housing price data
├── config/
│   ├── config.py               # Configuration, logging (LOG_TYPES, lang)
│   └── translations.py         # Multilingual text support (hu/en)
├── scripts/
│   ├── extract.py              # CSV data extraction and processing
│   └── draw_diagram.py         # Visualization (line & scatter plots)
├── _out/                        # Output files (transcripts, descriptions)
├── pyproject.toml              # Project metadata
└── requirements.txt            # Python dependencies
```

### Key Files

- **[main.py](main.py)** – Entry point: loads CSV, prints table, draws diagrams
- **[config/config.py](config/config.py)** – Logging configuration (LOG_TYPES), language setting
- **[config/translations.py](config/translations.py)** – Bilingual text mappings for diagrams
- **[scripts/extract.py](scripts/extract.py)** – CSV parsing and data extraction by sections
- **[scripts/draw_diagram.py](scripts/draw_diagram.py)** – Line and scatter plot generation with regression
- **[data.csv](data/data.csv)** – KSH housing price data (2007-2024)

## Features in Detail

### Data Visualization

#### Line Diagrams

- Display price trends for 4 housing types: Family Houses, Apartment Buildings, Housing Estates, and Total
- Shows historical data from 2007-2024
- Color-coded lines for easy comparison
- Interactive legend (click to toggle lines)

#### Scatter Plots with Linear Regression

- Individual data points for each year
- Regression lines showing systematic trends
- R² values displayed on each plot (typically 0.85-0.95)
- Demonstrates strong correlation between time and housing prices

### Economic Analysis Results

**Key Findings**:

- **R² Values**: 0.85-0.95 → Time explains 85-95% of price changes
- **Average Annual Growth**: ~3-4% per year
- **Trend**: Systematic, predictable increase (not random fluctuations)
- **Investment Insight**: Housing proves to be stable, reliable investment

**Price Trend Phases**:

- **2007-2012**: Stagnation (economic crisis period)
- **2012-2015**: Gradual recovery
- **2015-2024**: Accelerated growth

### Configuration Options

#### Language Support

Configure language in [`config/config.py`](config/config.py):

```python
lang = "hu"  # Hungarian
lang = "en"  # English
```

#### Logging Configuration

Adjust log levels in [`config/config.py`](config/config.py):

```python
LOG_TYPES.INFO    # General information
LOG_TYPES.ACTION  # User actions (file open/close)
LOG_TYPES.ERROR   # Error messages
```

#### Diagram Customization

Modify diagram columns in [`main.py`](main.py):

```python
draw_diagrams(extract_data(raw), cols=2)  # 2 columns layout
```

## Technical Implementation

### Libraries and Their Roles

- **NumPy**: Data handling, missing value management (`np.nan`)
- **Matplotlib**: Chart generation and visualization
- **SciPy**: Linear regression calculation (`stats.linregress`)
- **Colorama**: Colored terminal output

### Linear Regression Details

The program uses SciPy's `stats.linregress()` to calculate:

- **Slope**: Rate of price increase per year
- **Intercept**: Starting value
- **R value**: Correlation coefficient
- **R² value**: Coefficient of determination (quality of fit)

High R² values (0.85-0.95) indicate that the regression line accurately models the data, proving systematic price trends.

## Use Cases

- **Real Estate Investment Analysis**: Understand long-term price trends
- **Housing Purchase Decisions**: Data-driven decision making
- **Economic Policy Research**: Statistical evidence for housing market behavior
- **Educational Purpose**: Demonstration of data analysis and visualization techniques

## Future Enhancements

Potential improvements:

- Additional statistics
- Predictive modeling for future price estimates
- Interactive web-based dashboard
- Support for multiple regions/cities
- Export functionality (PDF reports, data tables)

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
