from rich.progress import Progress
from time import sleep

with Progress() as progress:
    task = progress.add_task("[green]Processing...", total=100)
    for i in range(100):
        sleep(0.1)
        progress.update(task, advance=1)
