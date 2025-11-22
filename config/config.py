from enum import Enum
from colorama import Fore

# ============ diagram format settings ============

NORMAL_FONT_SIZE = 8
TITLE_FONT_SIZE = 10
SHOW_EVERY_NUMBERED_YEAR = 1

# ============ logging configurations for colors ============
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
RESET = Fore.RESET
RED = Fore.RED

# ============ logging helper ============

# lang = "en"
lang = "hu"

LOG_TYPES = Enum('LOG_TYPES', ["INFO", "ERROR", "ACTION", "DEBUG", "DEEP_DEBUG"])

LOG = {
    LOG_TYPES.INFO : True,
    LOG_TYPES.ERROR : True,
    LOG_TYPES.ACTION : True,
    LOG_TYPES.DEBUG : True,
    LOG_TYPES.DEEP_DEBUG : True,
}

# =========== logging function ============

# Color mapping for log levels
LOG_COLORS = {
    LOG_TYPES.DEBUG: Fore.YELLOW,
    LOG_TYPES.DEEP_DEBUG: Fore.LIGHTCYAN_EX,
    LOG_TYPES.INFO: Fore.BLUE,
    LOG_TYPES.ERROR: Fore.RED,
    LOG_TYPES.ACTION: Fore.MAGENTA,
}

# logger
def Log(*args, level=LOG_TYPES.DEBUG, show_label=True, **kwargs):
    """
    Print with color-coded logging levels
        
    Args:
        *args: Arguments to print
        level (LOG_TYPES, optional): Logging level. Defaults to LOG_TYPES.DEBUG
        show_label (bool, optional): Whether to show the log level label. Defaults to True
        **kwargs: Keyword arguments for print function
    """
    if not LOG.get(level, False):
        return
    
    color = LOG_COLORS.get(level, RESET)
    
    if show_label:
        print(f"{color}{level.name}:{RESET}", *args, **kwargs)
    else:
        print(*args, **kwargs)