from datetime import datetime
import re

INPUT_PATH = f'./input/day3.txt'

def partTwoAnswer(input):

    PartTwo = partTwoController(input)
    
    return print(f'Day Three, Part Two\nTotal valid multiplication summation: {PartTwo}')

def partTwoController(input):

    PartTwo = 0
    
    for row in input:
        validString = getValidString(row)
        mulNumbers = getMulMatches(validString)
        print(f'{mulNumbers}\n')
        if len(mulNumbers) > 0:
            for pair in mulNumbers:
                PartTwo += int(pair[0]) * int(pair[1])

    return PartTwo

def getValidString(input):

    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"


    doMatches = re.search(doPattern, input)
    dontMatches = re.search(dontPattern, input)

    if dontMatches:
        dontCount = len(re.findall(dontPattern, input))
        dontSplit = re.split(dontPattern, input)
        return dontSplit[0] + testString(dontSplit[1:][0])
    elif doMatches:
        doSplit = re.split(doPattern, input)
        return testString(doSplit[1:][0])
    else:
        return input

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

def testString(testStr = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"):

    
    mulPattern = r"mul\(\d+,\d+\)"
    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"


    doMatches = re.search(doPattern, testStr)
    dontMatches = re.search(dontPattern, testStr)

    if dontMatches:
        dontCount = len(re.findall(dontPattern, testStr))
        dontSplit = re.split(dontPattern, testStr)
        return dontSplit[0] + testString(dontSplit[1:][0])
    elif doMatches:
        doSplit = re.split(doPattern, testStr)
        return testString(doSplit[1:][0])
    else:
        return testStr
        
    

if __name__ == "__main__":
    #print(f'Test String: {testString()}')
    
    start = datetime.now()
    input = getInput()
    partOneAnswer(input)
    print(f'Part One ran in {((datetime.now() - start).total_seconds()*1000):.2} miliseconds\n')
    startTwo = datetime.now()
    partTwoAnswer(input)
    print(f'Part Two ran in {((datetime.now() - startTwo).total_seconds()*1000):.2f} miliseconds\n')
    print(f'Day Two ran in {((datetime.now() - start).total_seconds()*1000):.2f} miliseconds')
