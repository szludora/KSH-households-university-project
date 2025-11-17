import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from config.config import LOG_TYPES, Log, lang
from config.translations import diagram_texts


Log("Draw diagram module loaded", level=LOG_TYPES.INFO)

# =================================== Diagram Drawing Helpers ===================================

langIxd = "1" if lang == "hu" else "0"

def to_numeric(values):
    """Convert string values to floats, handle missing data (..)"""
    result = []
    for v in values:
        try:
            if v.strip() == "..":
                result.append(np.nan)
            else:
                result.append(float(v.replace(",", ".").replace(" ", "")))
        except (ValueError, AttributeError):
            result.append(np.nan)
    return result


# =================================== Main Diagram Drawing Function ===================================

def draw_diagrams(data, cols=2):  # Draw line diagrams and scatter plots with regression for all sections
    if not data:
        Log("No data", level=LOG_TYPES.ERROR)
        return
    
    sections = list(data.items())
    num_sections = len(sections)
    num_cols = max(1, min(cols, 3))
    num_rows = math.ceil(num_sections / num_cols)
    
    years = list(range(2007, 2025))
    
    fig_lines, axes_lines = plt.subplots(num_rows, num_cols, figsize=(8 * num_cols, 5 * num_rows))
    if isinstance(axes_lines, np.ndarray):
        axes_lines = axes_lines.flatten()
    else:
        axes_lines = [axes_lines]
    
    title_lines =  diagram_texts["line_title"][int(langIxd)]
    xlabel = diagram_texts["year"][int(langIxd)]
    ylabel = diagram_texts["price"][int(langIxd)]
    
    for idx, (section_name, section_data) in enumerate(sections):
        ax = axes_lines[idx]
        
        for house_type, values in section_data.items():
            nums = to_numeric(values)
            if len(nums) < len(years):
                nums.extend([np.nan] * (len(years) - len(nums)))
            
            ax.plot(years, nums, marker='o', linewidth=2, label=house_type)
        
        ax.set_title(section_name, fontsize=12, fontweight='bold')
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.legend(loc='best', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(years[::2])
        ax.tick_params(axis='x', rotation=45, labelsize=8)
    
    for i in range(num_sections, len(axes_lines)):
        axes_lines[i].axis('off')
    
    fig_lines.suptitle(title_lines, fontsize=14, fontweight='bold')
    plt.tight_layout()
    Log("OPENED: Line diagrams", level=LOG_TYPES.ACTION)
    plt.show()
    Log("CLOSED: Line diagrams", level=LOG_TYPES.ACTION)
    
    fig_scatter, axes_scatter = plt.subplots(num_rows, num_cols, figsize=(8 * num_cols, 5 * num_rows))
    if isinstance(axes_scatter, np.ndarray):
        axes_scatter = axes_scatter.flatten()
    else:
        axes_scatter = [axes_scatter]
    
    title_scatter = diagram_texts["scatter_title"][int(langIxd)]
    data_label = diagram_texts["data"][int(langIxd)]
    ylabel = diagram_texts["price"][int(langIxd)]
    trend_label = diagram_texts["trend"][int(langIxd)]
    
    for idx, (section_name, section_data) in enumerate(sections):
        ax = axes_scatter[idx]
        
        for house_type, values in section_data.items():
            nums = to_numeric(values)
            valid = [(y, v) for y, v in zip(years, nums) if not np.isnan(v)]
            
            if not valid:
                continue
            
            valid_years, valid_nums = zip(*valid)
            ax.scatter(valid_years, valid_nums, s=60, alpha=0.7, label=f"{house_type} {data_label}")
            
            if len(valid_nums) >= 2:
                slope, intercept, r, _, _ = stats.linregress(valid_years, valid_nums)
                trend_line = [slope * y + intercept for y in valid_years]
                r_squared = r ** 2
                ax.plot(valid_years, trend_line, '--', linewidth=1.5,
                        label=f"{house_type} {trend_label} (R={r_squared:.2f})")
        
        ax.set_title(section_name, fontsize=12, fontweight='bold')
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.legend(loc='best', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xticks(years[::2])
        ax.tick_params(axis='x', rotation=45, labelsize=8)
    
    for i in range(num_sections, len(axes_scatter)):
        axes_scatter[i].axis('off')
    
    fig_scatter.suptitle(title_scatter, fontsize=14, fontweight='bold')
    plt.tight_layout()
    Log("OPENED: Scatter plots", level=LOG_TYPES.ACTION)
    plt.show()
    Log("CLOSED: Scatter plots", level=LOG_TYPES.ACTION)