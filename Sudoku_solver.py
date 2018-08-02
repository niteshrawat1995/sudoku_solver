'''
Approch:
1. Read and convert the sudoku format into a list of lists.
2. Check the row and column for particular square and eliminate the existing numbers.
3. Create subboard and eliminate numbers existing in the subboard.
4. Loop through the board until now new change can be made.
5. Utility funcs for printing the board elegantly, checking if the board is completely field or not.
6. Recursively solve the board and assign new board till solution is found.
'''
import copy
board = ['53..7....',
         '6..195...',
         '.98....6.',
         '8...6...3',
         '4..8.3..1',
         '7...2...6',
         '.6....28.',
         '...419..5',
         '....8..79',
         ]

def main():
    global board
    for idx,row in enumerate(board):
        board[idx] = list(row)
    #print(getPossiblities(4,4))
    #printBoard()
    solve()
    printBoard()

    
def solve():
    global board
    fillAllObvious()
    if isComplete():
        return True

    i,j=0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == '.':
                i,j = rowIdx,colIdx
    possiblities = getPossiblities(i,j)
    for value in possiblities:
        snapshot = copy.deepcopy(board)
        board[i][j]=value
        #recursively solve the board with this value.
        result = solve()
        if result ==True:
            return True
        #if board doesnt get solved with this value , we'll roll back to orginal board with new intial value from possibilites.
        else:
            board = copy.deepcopy(board)
                


def fillAllObvious():
    global board
    while True:
        
        somethingChanged = False
        for i in range(9):
            for j in range(9):
                    possibilties = getPossiblities(i,j)
                    if possibilties == False:
                        continue
                    if len(possibilties) ==1:
                        board[i][j]= possibilties[0]
                        somethingChanged = True
        if somethingChanged == False:
            return
                    
            
def getPossiblities(i,j):
    possiblities = {str(n) for n in range(1,10)}
    if board[i][j] != '.':
        return False

    for row in board[i]:
        possiblities -= set(row)
    for col in range(9):
        possiblities -= set(board[i][col])

    iStart = (i//3)*3
    jStart = (j//3)*3

    subboard = board[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx]= row[jStart:jStart+3]
    for row in subboard:
        for col in row:
            possiblities -= set(col)
        
    return list(possiblities)
    
def printBoard():
    global board
    for row in board:
        for col in row:
            print(col,end='')
        print()
        
def isComplete():
    global board
    for row in board:
        for col in row:
            if col =='.':
                return False
    return True
main()
