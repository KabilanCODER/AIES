# Create the board
board = [' ' for _ in range(9)]
# Print the board
def print_board():
    print()
    for i in range(3):
        print(board[3*i] + ' | ' + board[3*i+1] + ' | ' + board[3*i+2])
        if i < 2:
            print('--+---+--')
    print()
# Check for a win
def check_winner(player):
    win_combinations = [
    [0,1,2], [3,4,5], [6,7,8], # rows
    [0,3,6], [1,4,7], [2,5,8], # columns
    [0,4,8], [2,4,6] # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
# Main game loop
def play_game():
    current_player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1 
        if board[move] == ' ':
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That spot is taken! Try again.")
            turn -= 1 # repeat the turn
    print_board()
    print("It's a draw!")
    # Run the game
play_game()
