import json


def load_companies_from_file():
    try:
        with open("./app/data/companies.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_companies_to_file(companies):
    with open("./app/data/companies.json", "w", encoding="utf-8") as file:
        json.dump(companies, file)
