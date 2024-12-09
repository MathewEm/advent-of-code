from datetime import datetime

INPUT_PATH = f'./input/day2.txt'

def partTwoAnswer(input):

    safeDampenerReports = countConditions(input)
    print(f'Day Two, Part Two\nThere are {safeDampenerReports} Safe Dampener Reports!')

    return

def countConditions(input):

    intput = convertToInt(input)
    validCounter = 0

    for row in intput:
        if partTwoConditions(row):
            validCounter += 1

    return validCounter
    
def partTwoConditions(input):

    stepSet = {-3, -2, -1, 1, 2, 3}
    for n in range(0,len(input)):
        removeOne = input.copy()
        removeOne.pop(n)
        diffList = []
        isIncreasing = []
        passCondition = True
        for k in range(0,len(removeOne)-1):
            diffList.append(removeOne[k+1] - removeOne[k])
        for j in diffList:
            if j not in stepSet:
                passCondition = False
        for l in diffList:
            isIncreasing.append(l > 0)
        if len(set(isIncreasing)) > 1:
            passCondition = False
        if passCondition:
            return True
        
    return passCondition
                       
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
