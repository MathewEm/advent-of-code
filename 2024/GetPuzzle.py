import os
import requests
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    session_cookie = os.getenv("SESSION_COOKIE")
    if not session_cookie:
        raise ValueError("SESSION_COOKIE is missing. Check your .env file.")
    
    headers = {
        "Cookie": f"session={session_cookie}"
        }
    
    puzzleUrl = input("Please paste url for puzzle:\n")
    puzzleName = "./input/"+''.join(puzzleUrl.split("/")[-3:-1])+".txt"

    if os.path.isfile(f'{puzzleName}'):
        raise ValueError(f'{puzzleName} already exists!')

    response = requests.get(puzzleUrl, headers=headers)
    
    if response.status_code == 200:
        content = response.text
        with open(f'{puzzleName}', "w") as file:
            file.write(content)
        print(f'Puzzle saved to {puzzleName}')
    else:
        print(f'Status Code: {response.status_code}')
        
