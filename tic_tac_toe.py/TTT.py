## Manas Mishra
import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row number (0-2): "))
            col = int(input("Enter column number (0-2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = random.randint(0, 1)  

    while True:
        print_board(board)
        player = players[turn % 2]

        if player == 'X':
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            if player == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn += 1


if __name__ == "__main__":
    tic_tac_toe()

