def configureBoard(board, state):
    for i in range(4):
        board[state[i]][i] = 1

def printBoard(board):
    for row in board:
        print(*row)
    print()

def calculateObjective(state):
    attacking = 0
    for i in range(4):
        row = state[i]
        for col in range(i):
            if state[col] == row:
                attacking += 1
            if abs(state[col] - row) == abs(col - i):
                attacking += 1
    return attacking

def generateBoard(board, state):
    for i in range(4):
        for j in range(4):
            board[i][j] = 0
    for i in range(4):
        board[state[i]][i] = 1

def getNeighbour(state):
    best_state = state[:]
    best_objective = calculateObjective(state)
    for i in range(4):
        original_row = state[i]
        for j in range(4):
            if j != original_row:
                state[i] = j
                objective = calculateObjective(state)
                print(f"Current state: {state}, Cost: {objective}")
                if objective < best_objective:
                    best_objective = objective
                    best_state = state[:]
        state[i] = original_row
    return best_state, best_objective

def hillClimbing(board, state):
    while True:
        generateBoard(board, state)
        current_objective = calculateObjective(state)
        print(f"Current state: {state}, Cost: {current_objective}")
        if current_objective == 0:
            print("Goal configuration reached!")
            printBoard(board)
            break
        next_state, next_objective = getNeighbour(state)
        if next_objective >= current_objective:
            print("No better neighbor found, stopping.")
            printBoard(board)
            break
        state[:] = next_state

N = 4
state = [0] * N
board = [[0 for _ in range(N)] for _ in range(N)]

print("Enter the starting positions of the queens (0 to 3) for each column (0-based index):")
for i in range(N):
    while True:
        try:
            pos = int(input(f"Column {i}: "))
            if pos < 0 or pos >= N:
                print(f"Please enter a number between 0 and {N-1}.")
            else:
                state[i] = pos
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

configureBoard(board, state)
hillClimbing(board, state)
