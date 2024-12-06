import os
import re
import requests
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv("./../.env")
    SESSION_COOKIE = os.getenv("SESSION_COOKIE")
    PUZZLE_YEAR = os.getenv("PUZZLE_YEAR")

    if not SESSION_COOKIE:
        raise ValueError("SESSION_COOKIE is missing. Check your .env file.")
    if not PUZZLE_YEAR:
        raise ValueError("PUZZLE_YEAR is missing. Check your .env file.")

    day=1
    existing_days = False

    INPUT_DIR = f'./../{PUZZLE_YEAR}/input/'

    
    
    headers = {
        "Cookie": f"session={SESSION_COOKIE}"
        }
    
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    if os.path.exists(INPUT_DIR):
        # List all files in the directory
        files = os.listdir(INPUT_DIR)
        for file_name in files:
            # Match files with the pattern "day<number>.txt"
            match = re.match(r'day(\d+)\.txt', file_name)
            if match:
                # Extract the number and add it to the set
                existing_days = int(match.group(1))

    if existing_days:
        day = existing_days + 1
        
    PUZZLE_URL = f'https://adventofcode.com/{PUZZLE_YEAR}/day/{day}/input'
    PUZZLE_NAME = f'{INPUT_DIR}'+f'day{day}.txt'


    response = requests.get(PUZZLE_URL, headers=headers)

    if response.status_code == 200:
        while response.status_code == 200 and day < 26:
            content = response.text
            with open(f'{PUZZLE_NAME}', "w") as file:
                file.write(content)
            print(f'Puzzle saved to {PUZZLE_NAME}')
            day += 1
            PUZZLE_URL = f'https://adventofcode.com/{PUZZLE_YEAR}/day/{day}/input'
            PUZZLE_NAME = f'{INPUT_DIR}'+f'day{day}.txt'
            response = requests.get(PUZZLE_URL, headers=headers)
        print(f'Status Code: {response.status_code} - End of available Inputs!') 
            
    else:
        print(f'Status Code: {response.status_code}') 
