# GETting Culture Across APIs

For this assignment, I used the Open Library API and the Europeana API.

I chose the Open Library API because it provides cultural data about books and does not require an API key. This made it easier to work with while still connecting to the assignment topic of getting cultural data from APIs.

In my script, I searched Open Library for Star Wars books. Then I used one of the book titles from that response to search for related items in Europeana. Finally, I saved the item data from both APIs into a JSON file called `open_library_europeana_data.json`.

The files in this folder are:

- `getting_culture.py`: the Python script that gets data from Open Library and Europeana
- `open_library_europeana_data.json`: the saved API data