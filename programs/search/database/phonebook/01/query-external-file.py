# ------------------------------------------
# NOTE:
# This code was created with the help of AI:
# https://gemini.google.com
# ------------------------------------------
# It's purpose is to fetch 'raw' 
# phonebook data (name,number) from github:
# phonebook.csv
# ------------------------------------------

import csv
import io
from urllib.request import urlopen

# Your raw GitHub URL
URL = "https://raw.githubusercontent.com/pramnora/python/main/phonebook.csv"


def query_phonebook(search_term):
    try:
        # Fetch data over HTTP
        with urlopen(URL) as response:
            lines = [line.decode("utf-8") for line in response.readlines()]

        # Parse CSV lines
        reader = csv.DictReader(lines)

        print(f"--- Search Results for '{search_term}' ---")
        found = False
        for row in reader:
            if search_term.lower() in row["Name"].lower():
                print(f"Name: {row['Name']} | Number: {row['Number']}")
                found = True

        if not found:
            print("No matching contacts found.")

    except Exception as e:
        print(f"Failed to retrieve data: {e}")


# Example usage:
query_phonebook("Bank")
