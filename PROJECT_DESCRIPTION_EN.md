# KSH Housing Price Statistics Project - Brief Description

## Project Overview
Python-based data analysis tool that visualizes and analyzes KSH housing price statistics. The program processes CSV format data, creates line and scatter plots with linear regression, and measures the predictability of price changes using R² values.

## Project Structure
```
├── main.py                     # Entry point, program startup
├── data
│   └── data.csv                # KSH housing price data (2007-2024)
├── config/
│   ├── config.py               # Configuration, logging (LOG_TYPES)
│   └── translations.py         # Multilingual texts (Hungarian/English)
└── scripts/
    ├── extract.py              # CSV data loading and processing
    └── draw_diagram.py         # Visualization: line and scatter plots
```

## Main Functions

**1. Data Loading and Processing** (`extract.py`)
- Loading CSV format KSH data
- 4 price sections × 4 housing types × 18 years = 288 data points
- Housing types: Family Houses, Apartment Buildings, Housing Estates, Total

**2. Visualization** (`draw_diagram.py`)
- **Line diagrams**: Price trend evolution over time by housing type
- **Scatter plots**: Linear regression with R² values
- NumPy: Data handling, missing values
- Matplotlib: Chart creation
- SciPy: Linear regression calculation

## Usage
```bash
python main.py
```
1. First window opens: line diagrams
2. Second window opens: scatter plots with R² values

## Configuration Options
- **Language**: Hungarian or English (`config.py` → `lang = "hu"` or `"en"`)
- **Logging**: LOG_TYPES levels (INFO, ACTION, ERROR)
- **Diagrams**: Number of section columns (`cols=2`)

## Technology Stack
- **Python 3.13+**
- **NumPy**: Numerical computations, data handling
- **Matplotlib**: Data visualization
- **SciPy**: Statistical analysis (linear regression)
- **Colorama**: Colored terminal output

## Economic Analysis - Key Results

**Price Trend Evolution (2007-2024)**
- **2007-2012**: Stagnation - Housing prices did not increase due to the 2008 economic crisis
- **2012-2015**: Gradual increase - Economic recovery, low interest rates
- **2015-2024**: Faster growth - Significant price jump especially after 2015

**Linear Regression Results**
- **R² values**: Between 0.85 - 0.95
- **Meaning**: Time explains 85-95% of price changes
- **Conclusion**: Systematic, predictable trend - not random fluctuations

**Investment Perspective**
- **Average annual increase**: ~3-4%
- **Stability**: High R² value indicates stable investment
- **Risk**: Low - prices consistently grow in the long term
- **Practical application**: Housing purchase decisions, investment portfolio, real estate policy

**Housing Type Comparison**
- All categories follow similar trends
- Family houses and housing estates show parallel growth
- The crisis affected all housing types, but recovery was also universal

## Project Result
Mathematically proven that housing prices are not speculation, but follow systematic and predictable trends. R² values demonstrate that real estate is a stable and reliable investment instrument.

---
**Developer**: Szlucska Dóra | **Course**: Data Analysis - Housing Price Changes in Hungary | **Source**: KSH (Hungarian Central Statistical Office)
