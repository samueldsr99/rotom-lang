from rich.console import Console
from rich.text import Text


class RichLogger:
    def __init__(self) -> None:
        self.console = Console()

    def log_success(self, msg: str, bold: bool = False):
        text = Text(msg, style=f"{'bold' if bold else ''} green")
        self.console.print(text)

    def log_error(self, msg: str, bold: bool = False):
        text = Text(msg, style=f"{'bold' if bold else ''} red")
        self.console.print(text)

    def log_info(self, msg: str, bold: bool = False):
        text = Text(msg, style=f"{'bold' if bold else ''} white")
        self.console.print(text)
