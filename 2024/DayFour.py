from datetime import datetime

INPUT_PATH = f'./input/day4.txt'
TEST_PATH = f'./input/test.txt'

def PartTwoAnswer(input):

    Answer = P2_Splitter(input)
    return f'Day 4, Part 2\n There were {Answer} X-Mas\' found!'

def P2_Splitter(input):

    mas_counter = 0

    for n in range(0, len(input)-2):
        selected_rows = input[n:n+3]
        for k in range(0,len(selected_rows[0])-2):
            sub_array = []
            sub_array.append(selected_rows[0][k:k+3])
            sub_array.append(selected_rows[1][k:k+3])
            sub_array.append(selected_rows[2][k:k+3])
            mas_counter += Check_Mas(sub_array)

    return mas_counter

def Check_Mas(input):

    mas_set = {'MAS','SAM'}
    mas_counter = 0
    left_to_right = ""
    right_to_left = ""
    # Check diagonals
    for x in range(0,3):
        left_to_right += input[x][x]
        right_to_left += input[x][2-x]
    if (left_to_right in mas_set) and (right_to_left in mas_set):
        mas_counter += 1

    return mas_counter

def PartOneAnswer(input):

    Answer = ArraySplitter(input)
    
    return f'Day 4, Part 1\nThere were {Answer} Xmas\' found!'

def ArraySplitter(input):
    XmasCounter = 0

    #Check Rows
    for row in input:
        for o in range(0,len(row)-3):
            subArray = []
            subArray.append(row[o:o+4])
            
            XmasCounter += Check_Row(subArray)

    for n in range(0,len(input)-3):
        SelectedRows = input[n:n+4]

        for k in range(0,len(SelectedRows[0])-3):
            subArray = []
            subArray.append(SelectedRows[0][k:k+4])
            subArray.append(SelectedRows[1][k:k+4])
            subArray.append(SelectedRows[2][k:k+4])
            subArray.append(SelectedRows[3][k:k+4])


            XmasCounter += Check_Diagonal(subArray)

            
        for j in range(0,len(SelectedRows[0])-3,4):
            subArray = []
            subArray.append(SelectedRows[0][j:j+4])
            subArray.append(SelectedRows[1][j:j+4])
            subArray.append(SelectedRows[2][j:j+4])
            subArray.append(SelectedRows[3][j:j+4])


            
            XmasCounter += Check_Column(subArray)
            
        if (len(input))%4 != 0:
            subArray = []
            subArray.append(SelectedRows[0][-(len(input)%4):])
            subArray.append(SelectedRows[1][-(len(input)%4):])
            subArray.append(SelectedRows[2][-(len(input)%4):])
            subArray.append(SelectedRows[3][-(len(input)%4):])

            XmasCounter += Check_Column(subArray)
            
    return XmasCounter

def Check_Row(input):
    
    XmasCounter = 0
    XmasSet = {'XMAS','SAMX'}

    for row in input:
        if row in XmasSet:
            XmasCounter += 1
            
    return XmasCounter

def Check_Column(input):

    XmasCounter = 0
    XmasSet = {'XMAS','SAMX'}
        
    for x in range(0,len(input[0])):
        Column = ""
        for y in range(0,4):
            Column += input[y][x]
        if Column in XmasSet:
            XmasCounter += 1
                
    return XmasCounter

def Check_Diagonal(input):

    XmasSet = {'XMAS','SAMX'}
    XmasCounter = 0
    DiagonalDown = ""
    DiagonalUp = ""
    # Check diagonals
    for x in range(0,4):
        DiagonalDown += input[x][x]
        DiagonalUp += input[x][3-x]
    if DiagonalDown in XmasSet:
        XmasCounter += 1
    if DiagonalUp in XmasSet:
        XmasCounter += 1
        
    return XmasCounter
    
def getInput(path):
    
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    return lines

if __name__ == "__main__":
    
    start = datetime.now()
    input = getInput(INPUT_PATH)
    print(PartOneAnswer(input))
    print(f'Part One ran in {((datetime.now() - start).total_seconds()*1000):.2} miliseconds\n')
    startTwo = datetime.now()
    print(PartTwoAnswer(input))
    print(f'Part Two ran in {((datetime.now() - startTwo).total_seconds()*1000):.2f} miliseconds\n')
    print(f'Day Two ran in {((datetime.now() - start).total_seconds()*1000):.2f} miliseconds')
