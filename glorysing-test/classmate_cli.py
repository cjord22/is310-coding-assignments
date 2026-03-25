import json
import os
from rich.console import Console
from rich.table import Table

console = Console()

def get_game_entry():
    while True:
        console.print("\nPlease enter a new game entry.", style="bold blue")

        title = input("Enter the game title: ")
        release_year = input("Enter the release year: ")
        genre = input("Enter the genre: ")
        platform = input("Enter the platform: ")

        console.print("\nYou entered the following data:", style="bold green")
        console.print(f"Title: {title}")
        console.print(f"Release Year: {release_year}")
        console.print(f"Genre: {genre}")
        console.print(f"Platform: {platform}")

        confirm = input("Is this information correct? (y/n): ").strip().lower()

        if confirm == "y":
            return {
                "title": title,
                "release_year": release_year,
                "genre": genre,
                "platform": platform
            }
        else:
            console.print("Let's re-enter the data.", style="bold red")

console.print("Hello! Welcome to the CLI Data Entry App.", style="bold cyan")
console.print("Here is some example game data:\n", style="bold green")

table = Table(title="Video Game Collection")
table.add_column("Title", style="magenta")
table.add_column("Release Year", style="cyan")
table.add_column("Genre", style="green")
table.add_column("Platform", style="yellow")

table.add_row("The Legend of Zelda: Breath of the Wild", "2017", "Action-adventure", "Nintendo Switch")
table.add_row("Minecraft", "2011", "Sandbox", "Multi-platform")
table.add_row("League of Legends", "2009", "MOBA", "PC")

console.print(table)

entries = []

while True:
    entry = get_game_entry()
    entries.append(entry)

    another = input("Do you want to add another entry? (y/n): ").strip().lower()
    if another != "y":
        break

console.print("\nAll confirmed entries:", style="bold green")
for item in entries:
    console.print(item)

file_name = "game_data.json"

with open(file_name, "w", encoding="utf-8") as file:
    json.dump(entries, file, indent=4)

full_path = os.path.abspath(file_name)

console.print("\nData has been saved successfully!", style="bold cyan")
console.print(f"File location: {full_path}", style="bold yellow")