import csv
import os
import cloudscraper
from bs4 import BeautifulSoup

url = "https://animaljam.fandom.com/wiki/Category:Animals"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

animal_links = soup.find_all("a", class_="category-page__member-link")

animals = []

for link in animal_links:
    name = link.get_text().strip()
    href = link.get("href")

    if href and href.startswith("/wiki/"):
        full_link = "https://animaljam.fandom.com" + href
        animals.append([name, full_link])

script_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_folder, "animal_jam_animals.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["animal_name", "animal_link"])

    for animal in animals:
        writer.writerow(animal)

print("Finished! Saved", len(animals), "animals.")
print("File saved at:", csv_path)