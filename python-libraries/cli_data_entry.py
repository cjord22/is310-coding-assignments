from pathlib import Path
import csv
from rich.console import Console
from rich.table import Table

console = Console()


def show_example_data():
    table = Table(title="Example Restaurant Data")
    table.add_column("Restaurant Name", style="magenta")
    table.add_column("Cuisine Type", style="cyan")
    table.add_column("Location", style="green")
    table.add_column("Rating", style="yellow")

    table.add_row("Bangkok Thai", "Thai", "Urbana", "9/10")
    table.add_row("Sakanaya", "Japanese", "Champaign", "10/10")
    table.add_row("Jerusalem Restaurant", "Middle Eastern", "Urbana", "8/10")

    console.print(table)


def get_restaurant_entry():
    console.print("\nEnter a new restaurant record:", style="bold cyan")

    restaurant_name = input("Restaurant name: ")
    cuisine_type = input("Cuisine type: ")
    location = input("Location: ")
    rating = input("Rating: ")

    restaurant = {
        "Restaurant Name": restaurant_name,
        "Cuisine Type": cuisine_type,
        "Location": location,
        "Rating": rating
    }

    return restaurant


def show_single_entry(restaurant):
    table = Table(title="Your Entered Restaurant")
    table.add_column("Restaurant Name", style="magenta")
    table.add_column("Cuisine Type", style="cyan")
    table.add_column("Location", style="green")
    table.add_column("Rating", style="yellow")

    table.add_row(
        restaurant["Restaurant Name"],
        restaurant["Cuisine Type"],
        restaurant["Location"],
        restaurant["Rating"]
    )

    console.print(table)


def save_to_csv(restaurant_list, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Restaurant Name", "Cuisine Type", "Location", "Rating"]
        )
        writer.writeheader()

        for restaurant in restaurant_list:
            writer.writerow(restaurant)


def main():
    console.print("Welcome to my Restaurant Data Entry App!", style="bold blue")
    console.print("Here is some example restaurant data:\n", style="bold cyan")

    show_example_data()

    confirmed_restaurants = []

    while True:
        restaurant = get_restaurant_entry()

        console.print("\nYou entered:", style="bold green")
        show_single_entry(restaurant)

        confirm = input("Is this correct? (yes/no): ").strip().lower()

        if confirm == "yes":
            confirmed_restaurants.append(restaurant)
            console.print("Restaurant entry saved to the list.\n", style="bold green")
        else:
            console.print("Okay, let's re-enter that restaurant.\n", style="bold red")
            continue

        another = input("Do you want to add another restaurant? (yes/no): ").strip().lower()

        if another != "yes":
            break

    if len(confirmed_restaurants) > 0:
        output_file = Path("restaurant_data.csv")
        save_to_csv(confirmed_restaurants, output_file.resolve())

        console.print("\nYour data has been saved!", style="bold green")
        console.print(f"File location: {output_file.resolve()}", style="bold yellow")
    else:
        console.print("\nNo confirmed data was entered, so nothing was saved.", style="bold red")


main()