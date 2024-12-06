# Advent of Code

## Tools

### Requirements

- Python3 
- Pip

### How to Use

#### Setup .env

1. Copy the .env.example file
```bash
cp ./.env.example ./.env
```
2. Edit the .env with your text editor of choice and set your [Advent of Code Session
Cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1), Year of puzzle inputs, and Private Leaderboard URL
  - Year is required for the Puzzle Downloader tool only
  - Private Leaderboard URL is required for the Leaderboard Map generator only
  - Session Cookie is required for both
```bash
SESSION_COOKIE="532c13....ff3" // Quoatations required around the cookie
PUZZLE_YEAR=2024
LEADERBOARD_URL=https://adventofcode.com/2024/leaderboard/private/view/4499709
```
### Activate Virtual Python Environment

1. Navigate to the ./Tools/ directory and create the enviroment with the Makefile
```bash
make setup
```
2. Activate the environment
```bash
source ./venv/bin/activate
```

### Puzzle Downloader

The puzzle downloader will download all available puzzle inputs for the given year. Puzzle inputs are saved in
`../advent_of_code/{PUZZLE_YEAR}/inputs/` as text files. If the directories do not exist they will be created
automatically.

```bash
python3 GetPuzzle.py
```

### Leaderboard Map

The Leaderboard Map generator will generate a png image showing the progress of each person in your private
leaderboard. This script can be run every day of Advent of Code to show daily process. Images are saved in
`../advent_of_code/Leaderboard-Map/`. If the directory does not exist it will be created automatically.

```bash
python3 LeaderboardMap.py
```