import random
import time
import tkinter as tk


# Define the Tkinter GUI
root = tk.Tk()
root.geometry("400x300")
root.title("Tic Tac Toe Trivia")

# Define three sets of questions with varying difficulty levels
easy_questions = [
    {
        "question": "Which of the following is a high-level programming language?",
        "options": ["Assembly language", "Machine language", "C++", "None of the above"],
        "answer": "C++",
    },
    {
        "question": "Which of the following is a dynamically typed programming language?",
        "options": ["Java", "Python", "C#", "C"],
        "answer": "Python",
    },
]

medium_questions = [
    {
        "question": "What is the output of the following code in Python? a = 5, b = 3, print(a // b)",
        "options": ["1", "1.67", "2", "2.5"],
        "answer": "2",
    },
    {
        "question": "What is the purpose of the 'finally' block in a try-except block in Python?",
        "options": [
            "To execute the code if the try block raises an exception",
            "To execute the code if the except block does not catch an exception",
            "To execute the code regardless of whether an exception is raised or not",
            "None of the above",
        ],
        "answer": "To execute the code regardless of whether an exception is raised or not",
    },
]

hard_questions = [
    {
        "question": "What is the output of the following code in JavaScript? for (var i = 0; i < 5; i++) { (function(j) { setTimeout(function(){console.log(j); }, j * 1000 );})(i)",
        "options": ["0 1 2 3 4", "1 2 3 4 5", "5 5 5 5 5", "None of the above"],
        "answer": "0 1 2 3 4",
    },
    {
        "question": "What is the difference between \"const\" and \"let\" in JavaScript?",
        "options": [
            "\"const\" variables can not be reassigned while \"let\" variables can be reassigned",
            "\"const\" variables can only be declared once while \"let\" variables can be declared multiple times",
            "\"const\" variables can only be declared inside functions while \"let\" variables can be declared both inside and outside functions",
            "None of the above",
        ],
        "answer": "\"const\" variables can only be reassigned once while \"let\" variables can be reassigned multiple times",
    },
]

board = [" " for _ in range(9)]
difficulty = None

# Define the Tkinter widgets
board_frame = tk.Frame(root)
question_frame = tk.Frame(root)
option_buttons = []


def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("___|___|___")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("___|___|___")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")


def get_computer_move(board, mark):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)


def generate_question(difficulty):

   
    if difficulty == 0:
        question = random.choice(easy_questions)
        easy_questions.remove(question);
    elif difficulty == 1:
        question = random.choice(medium_questions)
        medium_questions.remove(question);
    else:
        question = random.choice(hard_questions)
        hard_questions.remove(question);
    # Return the question along with its options, answer, and difficulty
    return {
        "question": question["question"],
        "options": question["options"],
        "answer": question["answer"],
        "difficulty": difficulty
    }
def get_answer(question):
    # prompt the player to select an option and return their answer
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i+1) + ". " + option)
    
    while True:
        try:
            answer = int(input("Enter your answer (1-" + str(len(question["options"])) + "): "))
            if answer < 1 or answer > len(question["options"]):
                print("Invalid option. Please enter a number between 1 and " + str(len(question["options"])))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return question["options"][answer-1]


def answer_question(question, answer):
    # check if the player's answer is correct and return True or False
    if answer == question["answer"]:
        return True
    else:
        return False

def player_wins(board, player, computer_mark):
    # check if the player has won horizontally
    if board[0] == board[1] == board[2] == player:
        print("You can win by placing your mark at position 3")
        return True
    elif board[3] == board[4] == board[5] == player:
        print("You can win by placing your mark at position 6")
        return True
    elif board[6] == board[7] == board[8] == player:
        print("You can win by placing your mark at position 9")
        return True
    # check if the player has won vertically
    elif board[0] == board[3] == board[6] == player:
        print("You can win by placing your mark at position 1")
        return True
    elif board[1] == board[4] == board[7] == player:
        print("You can win by placing your mark at position 2")
        return True
    elif board[2] == board[5] == board[8] == player:
        print("You can win by placing your mark at position 3")
        return True
    # check if the player has won diagonally
    elif board[0] == board[4] == board[8] == player:
        print("You can win by placing your mark at position 1")
        return True
    elif board[2] == board[4] == board[6] == player:
        print("You can win by placing your mark at position 3")
        return True
    # check if the computer has won horizontally
    elif board[0] == board[1] == board[2] == computer_mark:
        print("The computer wins!")
        return True
    elif board[3] == board[4] == board[5] == computer_mark:
        print("The computer wins!")
        return True
    elif board[6] == board[7] == board[8] == computer_mark:
        print("The computer wins!")
        return True
    # check if the computer has won vertically
    elif board[0] == board[3] == board[6] == computer_mark:
        print("The computer wins!")
        return True
    elif board[1] == board[4] == board[7] == computer_mark:
        print("The computer wins!")
        return True
    elif board[2] == board[5] == board[8] == computer_mark:
        print("The computer wins!")
        return True
    # check if the computer has won diagonally
    elif board[0] == board[4] == board[8] == computer_mark:
        print("The computer wins!")
        return True
    elif board[2] == board[4] == board[6] == computer_mark:
        print("The computer wins!")
        return True
    else:
        return False

        

def get_hint(board, player,computer_mark):
    # check if there is a position where the player can win in the next move
    for i in range(9):
        if board[i] == " ":
            temp_board = board.copy()
            temp_board[i] = player
            if player_wins(temp_board, player,computer_mark):
                return "Hint: Place your next move at position " + str(i+1)
    return "No hint available."
    # check if the player can win horizontally
    for i in range(0, 9, 3):
        if board[i:i+3].count(player) == 2 and board[i:i+3].count(" ") == 1:
            return i + board[i:i+3].index(" ")
    # check if the player can win vertically
    for i in range(3):
        if board[i::3].count(player) == 2 and board[i::3].count(" ") == 1:
            return i + 3*board[i::3].index(" ")
    # check if the player can win diagonally
    if board[0::4].count(player) == 2 and board[0::4].count(" ") == 1:
        return board[0::4].index(" ") * 4
    if board[2:7:2].count(player) == 2 and board[2:7:2].count(" ") == 1:
        return board[2:7:2].index(" ") * 2 + 2
    return None
def provide_hint(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                # Check if placing X in this position would lead to a win
                board[row][col] = 'X'
                if player_wins(board, 'X'):
                    print(f"A winning move for X is to place their piece at row {row+1}, column {col+1}")
                board[row][col] = '-'
def get_player_choice(board, player,computer_mark):
    if player == "X":
        choice = input("Enter your move (1-9): ")
    elif player == computer_mark :
        computer_mark="O"
        # Computer generates its own move
        available_moves = [i+1 for i in range(9) if board[i] == " "]
        choice = random.choice(available_moves)
        print("Computer chooses:", choice)
        time.sleep(1)  # Add a delay to simulate "thinking" time for the computer
    return int(choice)

def play_game():
    def submit_answer():
        nonlocal answer_submitted
        nonlocal player_answer
        player_answer = var.get()
        answer_submitted = True
        answer_window.destroy()

    # Create a window to display the question and options
    answer_submitted = False
    player_answer = ""
    answer_window = tk.Tk()
    answer_window.title("Trivia Question")
    answer_window.geometry("400x300")
    question = generate_question(difficulty)
    tk.Label(answer_window, text=question["question"]).pack(pady=10)
    var = tk.StringVar()
    for i, option in enumerate(question["options"]):
        tk.Radiobutton(answer_window, text=option, variable=var, value=i).pack()
    tk.Button(answer_window, text="Submit", command=submit_answer).pack(pady=10)


    # Play the game as before
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    computer_mark="O"
    moves = []  # initialize list to keep track of moves
    game_over = False
    start_time = time.time()
    incorrect_answers = 0
    question_difficulties = []
    diff_level = 0;
    while not game_over:
        print_board(board)
        if player == "X":
            question = generate_question(diff_level)
            question_difficulties.append(question['difficulty'])
            answer = get_answer(question)
            if not answer_question(question, answer):
                print("Incorrect answer! You cannot make a move.")
                player = "X"
                incorrect_answers += 1
                print("Computer chooses:")
                move = [i+1 for i in range(9) if board[i] == " "]
                choice = random.choice(move)
                print(choice)
                board[choice-1] = computer_mark
                time.sleep(1)
                moves.append(choice)  # add computer's move to the list
                continue
            else:
                print("Congratulations! You answered the question correctly.")
                hint = get_hint(board, player,computer_mark)
                if hint:
                    print(hint)
                diff_level += 1
            print("It's " + player + "'s turn.")
            move = int(input("Enter a position from 1 to 9: ")) - 1
##            while True:
##                      try:
##                          for move in board;
##                        if move < 0 or move > 8:
##                            print("Invalid input. Please enter a number from 1 to 9.")
##                            continue
##                        if board[move] != " ":
##                            print("That position is already occupied. Please try again.")
##                            continue
##                        break
##                      except ValueError:
##                            print("Invalid input. Please enter a number from 1 to 9.")//
              
            while True:
                        try:
                            user_input = int(input("Enter a position from 1 to 9: ")) - 1
                            if user_input < 0 or user_input > 8:
                                print("Invalid input. Please enter a number from 1 to 9.")
                                continue
                            if board[user_input] != " ":
                                print("That position is already occupied. Please try again.")
                                continue
                            move = user_input
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number from 1 to 9.")


            if board[move] == " ":
                board[move] = player
                moves.append(move+1)  # add player's move to the list
                if player_wins(board, player,computer_mark):
                    print_board(board)
                    print(player + " wins!")
                    game_over = True
                elif board.count(" ") == 0:
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    computer_mark = "O" if player == "X" else "X"
            else:
                print("That position is already occupied. Please try again.")
        else:
            print("Computer chooses:")
            move = [i+1 for i in range(9) if board[i] == " "]
            choice = random.choice(move)
            print(choice)
            time.sleep(1)
            moves.append(choice)  # add computer's move to the list
            board[choice-1] = computer_mark
            if player_wins(board, player,computer_mark):
                print_board(board)
                print(computer_mark + " wins!")
                game_over = True
            elif board.count(" ") == 0:
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                player = "X" if player == "O" else "O"
    end_time = time.time()
    time_taken = end_time - start_time
    if player == "X":
        print("Computer O wins!")
    else:
        print("Player X wins!")
    print("Time taken: " + str(time_taken))
    print("Number of incorrect answers: " + str(incorrect_answers))
    print("Question difficulties: " + str(question_difficulties))

    # Wait for the player to submit an answer
    answer_window.mainloop()

    # Get the player's answer and check if it is correct
    player_answer = question["options"][int(player_answer)]
    correct_answer = answer_question(question, player_answer)
    if correct_answer:
        print("Congratulations! You answered the question correctly.")
    else:
        print("Sorry, your answer was incorrect.")
    
    

# Start the Tkinter event loop
root.mainloop()

