from datetime import datetime
from itertools import permutations

INPUT_PATH = f'./input/day2.txt'

def partTwoAnswer(input):

    safeDampenerReports = getDampenerCount(input)
    print(f'Day Two, Part Two\nThere are {safeDampenerReports} Safe Dampener Reports!')

    return

def partTwoConditions(input):

    intput = convertToInt(input)

    for row in intput:
        for n in range(0, len(row)):
            reducedRow = row.pop(n)
            permsList = permutations(reducedRow)
            for perms in permsList:
                diffList = []
                for k in range(0,len(perms)):
                    diffList.append(perms[k+1] - perms[k])
            
    

def getDampenerCount(input):
    
    return checkConditions(removeOneDirection(input))

def removeOneDirection(input):

    intputTable = getDirection(input)
    betterInput = []

    for row in list(intputTable.keys()):

        indexRemove = False
        for n in range(0,len(row)-1):
            print(row)
            if intputTable[row] == 'increasing':
                if row[n+1] < row[n] or row[n+1] == row[n]:
                    indexRemove = n+1
            else:
                if row[n+1] > row[n] or row[n+1] == row[n]:
                    indexRemove = n+1
        if indexRemove:
            betterInput.append(list(row).remove(row[indexRemove]))
        else:
            betterInput.append(list(row))

        return betterInput

def getDirection(input):

    intput = convertToInt(input)
    intputTable = {}

    for row in intput:

        increasing = 0
        decreasing = 0
        flat = 0

        for n in range(0,len(row)-1):

            if row[n+1] > row[n]:
                increasing += 1
            if row[n+1] < row[n]:
                decreasing += 1
            else:
                flat += 1
        if flat < 2:
            
            if (increasing > decreasing) and (decreasing < 2):
                intputTable[tuple(row)] = 'increasing'
            if (decreasing > increasing) and (increasing < 2):
                intputTable[tuple(row)] = 'decreasing'
    return intputTable
                       

def partOneAnswer(input):

    safeReports = checkConditions(input)
    print(f'Day Two, Part One\nThere are {safeReports} Safe Reports!')
    
def checkConditions(input):

    intput = convertToInt(input)
    validCounter = 0
    stepSet = {-3, -2, -1, 1, 2, 3}
    for row in intput:
        
        increasing = True
        decreasing = True
        inStepSet = True
        endOfRow = True
        while (increasing or decreasing) and inStepSet and endOfRow:

            for n in range(0,len(row)-1):
                if not (row[n+1] - row[n] in stepSet):
                    inStepSet = False
                if (row[n] > row[n+1]):
                    decreasing = False
                if (row[n] < row[n+1]):
                    increasing = False
            if (increasing or decreasing) and inStepSet:
                validCounter += 1
            endOfRow = False

    return validCounter

def convertToInt(input):

    intput = [list(map(int,row)) for row in input ]
    
    return intput

def getInput():
    
    with open(INPUT_PATH, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split(" ") for line in lines]

    return lines

if __name__ == "__main__":
    start = datetime.now()
    input = getInput()
    partOneAnswer(input)
    print(f'Part One ran in {((datetime.now() - start).total_seconds()*1000):.2} miliseconds\n')
    startTwo = datetime.now()
    partTwoAnswer(input)
    print(f'Part Two ran in {((datetime.now() - startTwo).total_seconds()*1000):.2f} miliseconds\n')
    print(f'Day Two ran in {((datetime.now() - start).total_seconds()*1000):.2f} miliseconds')
