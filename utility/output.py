class CliTextColor:
    """
    Provides text colors for command line.
    """
    BEIGE = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLACK = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Subject:
    """
    Provides subjects for output in command line.
    """
    TEST = f'{CliTextColor.BEIGE}[TEST]{CliTextColor.ENDC}'
    INFO = f'{CliTextColor.BLUE}[INFO]{CliTextColor.ENDC}'
    OK = f'{CliTextColor.GREEN}[OK]{CliTextColor.ENDC}'
    WARNING = f'{CliTextColor.YELLOW}[WARNING]{CliTextColor.ENDC}'
    ERROR = f'{CliTextColor.RED}[ERROR]{CliTextColor.ENDC}'
    DEBUG = f'{CliTextColor.PURPLE}[DEBUG]{CliTextColor.ENDC}'
