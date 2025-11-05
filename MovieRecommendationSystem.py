def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_winner(board, player):
    # Check rows & columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row check
            return True
        if all(board[j][i] == player for j in range(3)):  # Column check
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def switch_player(player):
    return "O" if player == "X" else "X"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0,1,2): "))
            col = int(input(f"Player {current_player}, enter col (0,1,2): "))
        except ValueError:
            print("❌ Please enter valid numbers!")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("❌ Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("❌ Cell already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("🤝 It's a draw!")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()
