# ------------------------------------------
# NOTE:
# This code was created with the help of AI:
# https://gemini.google.com
# ------------------------------------------
# It's purpose is...
# 1. Download the code to use on your local computer;
# and, then, run it using: Python3 filename.py
# 2. It will, then, fetch an external file data,
# which is stored inside of GitHub:
# phonebook.csv
# ...and, allows the user to query that data. 
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
