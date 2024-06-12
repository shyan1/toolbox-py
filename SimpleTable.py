from rich.table import Table
from rich import print

table = Table(title="Simple Table")
table.add_column("NAME", style="cyan")
table.add_column("AGE", style="magenta")

table.add_row("ZHANG san", "30")

print(table)


# Simple Table
# ┏━━━━━━━━━━━┳━━━━━┓
# ┃ NAME      ┃ AGE ┃
# ┡━━━━━━━━━━━╇━━━━━┩
# │ ZHANG san │ 30  │
# └───────────┴─────┘
