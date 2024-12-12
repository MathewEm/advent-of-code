from datetime import datetime
import re

INPUT_PATH = f'./input/day3.txt'

def partTwoAnswer(input):

    return print(f'Incomplete')

def partOneAnswer(input):

    PartOne = 0

    for row in input:
        mulNums = getMulMatches(row)
        if len(mulNums) > 0:
            for pair in mulNums:
                PartOne += int(pair[0]) * int(pair[1])
            
    return print(f'Day Three, Part One\nTotal multiplication summation: {PartOne}')

def getMulMatches(input):

    pattern = r"mul\(\d+,\d+\)"

    mulMatches = re.findall(pattern, input)

    mulNumbers = []
    for match in mulMatches:
         mulNumbers.append(re.split(r"[(,)]+", match)[1:3])

    return mulNumbers

def getInput():
    
    with open(INPUT_PATH, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    return lines

def testString():

    testStr = "-~who()?!-{ where()mul(764,406)?^why()%[how(420,460)mu"
    pattern = r"mul\(\d+,\d+\)"

    matches = re.findall(pattern, testStr)
    print(f'Matches: {matches}')

    mulNums = []
    for match in matches:
         mulNum = re.split(r"[(,)]+", match)[1:3]
    print(f'mulNum: {mulNum}')
    

if __name__ == "__main__":
    
    start = datetime.now()
    input = getInput()
    partOneAnswer(input)
    print(f'Part One ran in {((datetime.now() - start).total_seconds()*1000):.2} miliseconds\n')
    startTwo = datetime.now()
    partTwoAnswer(input)
    print(f'Part Two ran in {((datetime.now() - startTwo).total_seconds()*1000):.2f} miliseconds\n')
    print(f'Day Two ran in {((datetime.now() - start).total_seconds()*1000):.2f} miliseconds')
