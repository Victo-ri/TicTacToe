def init_board():
    return [" " for _ in range(9)] 

def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i * 3:(i + 1) * 3])
        print(f" {row} ")
        if i < 2:
            print("---|---|---")
    print("\n")

def check_winner(board, sign):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        if all(board[pos] == sign for pos in combo):
            return True
    return False

def is_draw(board):
    return all(cell != (" ") for cell in board)

def two_player_game():
    board = init_board()
    current_player = "X" 
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        try:
            move = int(input("Choose a cell number (0-8): "))
            if move < 0 or move > 8 or board[move] in ("X", "O"):
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 0 and 8.")
            continue

        board[move] = current_player

        if check_winner(board, current_player): 
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):  
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    two_player_game()
