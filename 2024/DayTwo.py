INPUT_PATH = f'./input/day2.txt'

def getInput():
    
    with open(INPUT_PATH, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split(" ") for line in lines]

    return lines

if __name__ == "__main__":
    input = getInput()
    print(f'{input[0]}')
