from tools import clear_view, jarak
clear_view()
jarak(4)


from rich.console import Console
from rich.markdown import Markdown

console = Console()

markdown_text = """
# Belajar Rich Python
Rich adalah library Python untuk tulisan *rich* dan format visual di terminal.

## Fitur Unggulan:
* **Tables**
* **Progress Bars**
* **Syntax Highlighting**

> "Terminal tidak harus membosankan!"
"""

md = Markdown(markdown_text)

console.print(md)

jarak(4)
