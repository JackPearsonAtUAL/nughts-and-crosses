"""
20/11/2025 (UK)
Naughts and Crosses
Jack Pearson
"""

playerTurn = 0
gameIsFinished = False

grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def PrintGrid():
    print(f"{' | '.join(grid[0])}")
    print("--+---+--")
    print(f"{' | '.join(grid[1])}")
    print("--+---+--")
    print(f"{' | '.join(grid[2])}")
    return

def CheckGrid():
    global gameIsFinished # Removes need of a return and will access lobal variable directly
    
    PrintGrid()
  
    # Check the rows
    for row in grid:
        winningSign = ""
        for i, cell in enumerate(row):
            if cell == " ":
                winningSign = ""
                break

            if i == 0:
                winningSign = cell
            elif winningSign != cell:
                winningSign = ""
                break
        
        if winningSign != "":
            print(winningSign, "has won")
            gameIsFinished = True

    # Check the columns
    for column in range(0, 3):
        winningSign = ""
        for row in range(0, 3):
            if grid[row][column] == " ":
                winningSign = ""
                break

            if row == 0:
                winningSign = grid[row][column]
            elif winningSign != grid[row][column]:
                winningSign = ""
                break
        
        if winningSign != "":
            print(winningSign, "has won")
            gameIsFinished = True
    
    if grid[1][1] != " ":
        if grid[0][0] == grid[1][1] and grid[2][2] == grid[1][1]:
            print(f"{grid[1][1]} wins!")
            gameIsFinished = True
        elif grid[0][2] == grid[1][1] and grid[2][0] == grid[1][1]:
            print(f"{grid[1][1]} wins!")
            gameIsFinished = True
    


def DoPlayerTurn():
    inp = "x"
    while gameIsFinished == False:
        if inp == "x":
            row = GetNum("Row")
            col = GetNum("Column")
            grid[row][col] = inp
            CheckGrid()
            inp = "o"
        else:
            row = GetNum("Row")
            col = GetNum("Column")
            grid[row][col] = inp
            CheckGrid()
            inp = "x"      

def GetNum(type):
    e = True
    g = True
    i = input(f"{type}{' Number: '}")
    while e:
        try:
            i = int(i)
            e = False
        except:
            i = input("Invalid number, new number please: ")
    return i

DoPlayerTurn()