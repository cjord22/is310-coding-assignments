import requests
import apikey
import json
from rich import print

#apikey.save("EUROPEANA_API_KEY", "edgeaciondhe")

europeana_api_key = apikey.load("EUROPEANA_API_KEY")


open_library_url = "https://openlibrary.org/search.json"

open_library_params = {
    "q": "Star Wars",
    "limit": 5
}

open_library_response = requests.get(open_library_url, params=open_library_params)

print("[bold green]Open Library status code:[/bold green]", open_library_response.status_code)

open_library_data = open_library_response.json()

print("[bold blue]Data from Open Library:[/bold blue]")
print(open_library_data)

first_book = open_library_data["docs"][0]
book_title = first_book["title"]

print("[bold yellow]Book title I am using for Europeana search:[/bold yellow]", book_title)


europeana_url = "https://api.europeana.eu/record/v2/search.json"

europeana_params = {
    "wskey": europeana_api_key,
    "query": book_title,
    "rows": 5,
    "media": "true",
    "thumbnail": "true"
}

europeana_response = requests.get(europeana_url, params=europeana_params)

print("[bold green]Europeana status code:[/bold green]", europeana_response.status_code)

europeana_data = europeana_response.json()

print("[bold purple]Data from Europeana:[/bold purple]")
print(europeana_data)

open_library_items = open_library_data["docs"]
europeana_items = europeana_data.get("items", [])

final_data = {
    "chosen_api": "Open Library API",
    "open_library_items": open_library_items,
    "europeana_items": europeana_items
}

with open("open_library_europeana_data.json", "w") as file:
    json.dump(final_data, file, indent=4)

print("[bold green]Saved data to open_library_europeana_data.json[/bold green]")