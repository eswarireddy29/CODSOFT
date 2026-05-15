import random
import os

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Score tracker
score = {"You": 0, "AI": 0, "Draw": 0}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Color.CYAN + Color.BOLD)
    print("╔══════════════════════════════════════╗")
    print("║       🎮 TIC-TAC-TOE AI GAME 🎮      ║")
    print("║        Built by Eswari Reddy          ║")
    print("║        CodSoft Internship             ║")
    print("╚══════════════════════════════════════╝")
    print(Color.RESET)

def print_score():
    print(Color.YELLOW + f"\n🏆 SCORE => You: {score['You']}  |  AI: {score['AI']}  |  Draw: {score['Draw']}" + Color.RESET)

def print_board(board):
    print(Color.BOLD + "\n    1   2   3" + Color.RESET)
    print("  ╔═══╦═══╦═══╗")
    for i in range(3):
        row = "  ║"
        for j in range(3):
            cell = board[i][j]
            if cell == "X":
                row += Color.GREEN + f" {cell} " + Color.RESET + "║"
            elif cell == "O":
                row += Color.RED + f" {cell} " + Color.RESET + "║"
            else:
                row += Color.BLUE + f" {cell} " + Color.RESET + "║"
        print(f"{i+1} {row}")
        if i < 2:
            print("  ╠═══╬═══╬═══╣")
    print("  ╚═══╩═══╩═══╝")

def initialize_board():
    return [["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]]

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] in ["X", "O"] for i in range(3) for j in range(3))

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                empty.append((i, j))
    return empty

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -1000
        for (i, j) in get_empty_cells(board):
            board[i][j] = "O"
            best = max(best, minimax(board, depth+1, False))
            board[i][j] = str(i*3 + j + 1)
        return best
    else:
        best = 1000
        for (i, j) in get_empty_cells(board):
            board[i][j] = "X"
            best = min(best, minimax(board, depth+1, True))
            board[i][j] = str(i*3 + j + 1)
        return best

def ai_move_hard(board):
    best_score = -1000
    best_move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = "O"
        move_score = minimax(board, 0, False)
        board[i][j] = str(i*3 + j + 1)
        if move_score > best_score:
            best_score = move_score
            best_move = (i, j)
    return best_move

def ai_move_easy(board):
    empty = get_empty_cells(board)
    return random.choice(empty)

def player_move(board):
    while True:
        try:
            move = int(input(Color.GREEN + "\n👉 Your turn! Enter position (1-9): " + Color.RESET))
            if move < 1 or move > 9:
                print(Color.RED + "❌ Invalid! Enter a number between 1 and 9!" + Color.RESET)
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ["X", "O"]:
                print(Color.RED + "❌ That position is already taken! Try again!" + Color.RESET)
                continue
            return row, col
        except ValueError:
            print(Color.RED + "❌ Please enter a valid number!" + Color.RESET)

def play_game(difficulty):
    board = initialize_board()
    clear_screen()
    print_banner()
    print_score()
    print(Color.YELLOW + f"\n🎯 Difficulty: {'HARD 🔥' if difficulty == 'hard' else 'EASY 😊'}" + Color.RESET)
    print(Color.CYAN + "You are X  |  AI is O" + Color.RESET)
    print_board(board)

    while True:
        # Player move
        row, col = player_move(board)
        board[row][col] = "X"
        clear_screen()
        print_banner()
        print_score()
        print_board(board)

        if check_winner(board, "X"):
            print(Color.GREEN + Color.BOLD + "\n🎉 CONGRATULATIONS! YOU WIN! 🎉\n" + Color.RESET)
            score["You"] += 1
            return

        if is_board_full(board):
            print(Color.YELLOW + Color.BOLD + "\n🤝 IT'S A DRAW! WELL PLAYED!\n" + Color.RESET)
            score["Draw"] += 1
            return

        # AI move
        print(Color.RED + "\n🤖 AI is thinking..." + Color.RESET)
        if difficulty == "hard":
            row, col = ai_move_hard(board)
        else:
            row, col = ai_move_easy(board)

        board[row][col] = "O"
        clear_screen()
        print_banner()
        print_score()
        print_board(board)

        if check_winner(board, "O"):
            print(Color.RED + Color.BOLD + "\n😔 AI WINS THIS ROUND! TRY AGAIN!\n" + Color.RESET)
            score["AI"] += 1
            return

        if is_board_full(board):
            print(Color.YELLOW + Color.BOLD + "\n🤝 IT'S A DRAW! WELL PLAYED!\n" + Color.RESET)
            score["Draw"] += 1
            return

def main():
    clear_screen()
    print_banner()

    while True:
        print(Color.CYAN + "\n🎮 MAIN MENU" + Color.RESET)
        print("1. Play vs AI (Easy 😊)")
        print("2. Play vs AI (Hard 🔥)")
        print("3. View Scores 🏆")
        print("4. Quit 👋")

        choice = input(Color.YELLOW + "\nEnter your choice (1-4): " + Color.RESET)

        if choice == "1":
            play_game("easy")
        elif choice == "2":
            play_game("hard")
        elif choice == "3":
            print_score()
        elif choice == "4":
            print(Color.CYAN + Color.BOLD + "\nThanks for playing! Goodbye! 👋\n" + Color.RESET)
            break
        else:
            print(Color.RED + "❌ Invalid choice! Please enter 1-4!" + Color.RESET)

main()