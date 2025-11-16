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
LOG = True

LOG = {
    "EXTRACT": False,
    "PRINT_TABLE": True,
}

def Log(*args, **kwargs):
    """Print only if logging is enabled"""
    if LOG:
        print(*args, **kwargs)