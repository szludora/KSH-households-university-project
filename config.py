from enum import Enum
from colorama import Fore
from matplotlib.pylab import Enum

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
    LOG_TYPES.DEBUG : False,
    LOG_TYPES.DEEP_DEBUG : False,
}

def Log(*args, level=LOG_TYPES.DEBUG, show_label=True, **kwargs):
    """Print only if logging is enabled"""
    if LOG[level]:
      if level == LOG_TYPES.DEBUG:
          print(Fore.YELLOW + LOG_TYPES.DEBUG.name + ":" + RESET, *args, **kwargs) if show_label else print(*args, **kwargs)
      elif level == LOG_TYPES.DEEP_DEBUG:
          print(Fore.LIGHTCYAN_EX + LOG_TYPES.DEEP_DEBUG.name + ":" + RESET, *args, **kwargs) if show_label else print(*args, **kwargs)
      elif level == LOG_TYPES.INFO:
        print(Fore.BLUE + LOG_TYPES.INFO.name + ":" + RESET, *args, **kwargs) if show_label else print(*args, **kwargs)
      elif level == LOG_TYPES.ERROR:
          print(Fore.RED + LOG_TYPES.ERROR.name + ":" + RESET, *args, **kwargs) if show_label else print(*args, **kwargs)
      elif level == LOG_TYPES.ACTION:
          print(Fore.MAGENTA + LOG_TYPES.ACTION.name + ":" + RESET, *args, **kwargs) if show_label else print(*args, **kwargs)
      else:
        print(*args, **kwargs)