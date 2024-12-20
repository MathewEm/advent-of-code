from datetime import datetime

INPUT_PATH = f'./input/.txt'

def PartTwoAnswer(input):

    return f'Incomplete'

def PartOneAnswer(input):

    return f'Incomplete'

def getInput():
    
    with open(INPUT_PATH, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    return lines

if __name__ == "__main__":
    
    start = datetime.now()
    input = getInput()
    PartOneAnswer(input)
    print(f'Part One ran in {((datetime.now() - start).total_seconds()*1000):.2} miliseconds\n')
    startTwo = datetime.now()
    PartTwoAnswer(input)
    print(f'Part Two ran in {((datetime.now() - startTwo).total_seconds()*1000):.2f} miliseconds\n')
    print(f'Day Two ran in {((datetime.now() - start).total_seconds()*1000):.2f} miliseconds')
