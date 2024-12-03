INPUT_PATH = f'./input/day1.txt'

###
# Part 2
###

def getAnswerPartTwo(input):

    similarity_score = 0
    multiplier_table = getMultiplierTable(input)

    for row in input:
        similarity_score += int(row[0]) * multiplier_table[row[0]]

    print(f'Day 1, Part 2 Answer\nSimilarity Score is: {similarity_score}')

    return

def getMultiplierTable(input):

    right = []
    left_set = getLeftSet(input)
    multiplier = {}

    for row in input:
        right.append(row[1])
        
    for val in left_set:
        multiplier[val] = right.count(val)

    return multiplier

def getLeftSet(input):

    left = []
    for row in input:
        left.append(row[0])
        
    return set(left)
    
###
# Part One
###

def getAnswerPartOne(input):

    difference = getDifference(sortArray(input))
    
    dist = 0
    for row in difference:
        dist += row[-1]
    print(f'Day 1, Part 1 Answer\n Total Distance between left and right is: {dist}')

    return
    

def getDifference(input):

    for row in input:
        row.append(abs(row[1] - row[0]))

    return input

def sortArray(input):
    index_0 = []
    index_1 = []
    sorted_input = []
    
    for row in input:
        index_0.append(int(row[0]))
        index_1.append(int(row[1]))
    
    index_0.sort()
    index_1.sort()

    for row in range(0,len(input)):
        sorted_input.append([index_0[row], index_1[row]])

    return sorted_input
    

def getInput():

    with open(INPUT_PATH, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split("   ") for line in lines]

    return lines

if __name__ == '__main__':

    input = getInput()
    getAnswerPartOne(input)
    getAnswerPartTwo(input)
