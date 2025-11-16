from colorama import Fore

# ============ logging configurations for colors ============
HEADER_COLOR = Fore.YELLOW
DATES_COLOR = Fore.GREEN
BORDER_COLOR = Fore.MAGENTA
MAIN_TITLE_COLOR = Fore.CYAN

ACTION_COLOR = Fore.MAGENTA
RESET_COLOR = Fore.RESET


# ============ logging helper ============

# lang = "en"
lang = "hu"

LOG = {
    "DEBUG": True,
    "INFO": True,
    "DEEP_DEBUG": False,
}

def Log(*args, level="DEBUG", **kwargs):
    """Print only if logging is enabled"""
    if LOG[level]:
        print(*args, **kwargs)