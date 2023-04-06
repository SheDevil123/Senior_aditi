import random
import time
import tkinter as tk


# Define the Tkinter GUI
root = tk.Tk()
root.geometry("400x300")
root.title("Tic Tac Toe Trivia")

# create a canvas object
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

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

def print_board(board):
    canvas.delete("all") # clear the canvas
    for i, mark in enumerate(board):
        if mark == 'X':
            x = (i % 3) * 67 + 20
            y = (i // 3) * 67 + 20
            canvas.create_line(x, y, x+27, y+27)
            canvas.create_line(x, y+27, x+27, y)
        elif mark == 'O':
            x = (i % 3) * 67 + 33
            y = (i // 3) * 67 + 33
            canvas.create_oval(x, y, x+27, y+27)
    root.update()

def get_computer_move(board, mark):
    available_moves = [i for i in range(9) if board[i] == " "]
    computer_move = random.choice(available_moves)
    board[computer_move] = mark
    print_board(board)
    return computer_move

def generate_question(difficulty):
    # Select a random difficulty level
    #difficulty = random.choice(["easy", "medium", "hard"])
    
    # Select a random question from the chosen difficulty level
    if difficulty == 0:
        question = random.choice(easy_questions)
        easy_questions.remove(question);
    elif difficulty == 1:
        question = random.choice(medium_questions)
        medium_questions.remove(question);
    else:
        question = random.choice(hard_questions)
        hard_questions.remove(question);
    
    # Ask the question and return the answer along with the question, options, and difficulty
    answer = ask_question(question)
    return {
        "question": question["question"],
        "options": question["options"],
        "answer": question["options"][answer-1],
        "difficulty": difficulty
    }

def ask_question(question):
    # create a new window for the question
    question_window = tk.Toplevel(root)
    question_window.title("Question")
    
    # create a label to display the question
    question_label = tk.Label(question_window, text=question["question"])
    question_label.pack()
    
    # create a variable to store the selected option
    selected_option = tk.StringVar()
    
    # create radio buttons for the options
    for i, option in enumerate(question["options"]):
        option_button = tk.Radiobutton(question_window, text=option, variable=selected_option, value=str(i+1))
        option_button.pack()
    
    # create a button to submit the answer
    submit_button = tk.Button(question_window, text="Submit", command=lambda: get_answer(question))
    submit_button.pack()
    
    # wait for the question window to be closed
    question_window.wait_window()
    
    # return the selected answer
    return int(selected_option.get())

def get_answer(question):
    # create a new window for the answer
    answer_window = tk.Toplevel(root)
    answer_window.title("Answer")
    
    # create a label to display the answer
    answer_label = tk.Label(answer_window, text=question["answer"])
    answer_label.pack()
    
    # create a button to close the answer window
    close_button = tk.Button(answer_window, text="Close", command=lambda: answer_window.destroy())
    close_button.pack()
    
    # wait for the answer window to be closed
    answer_window.wait_window()

def answer_question(question):
    # create a new window for the question
    question_window = tk.Toplevel(root)
    question_window.title("Question")
    
    # create a label to display the question
    question_label = tk.Label(question_window, text=question["question"])
    question_label.pack()
    
    # create a variable to store the selected option
    selected_option = tk.StringVar()
    
    # create radio buttons for the options
    for i, option in enumerate(question["options"]):
        option_button = tk.Radiobutton(question_window, text=option, variable=selected_option, value=str(i+1))
        option_button.pack()
    
    # create a button to submit the answer
    submit_button = tk.Button(question_window, text="Submit", command=lambda: get_answer(question))
    submit_button.pack()
    
    # define the function to get the answer and close the window
    def get_answer(question):
        # get the selected option
        answer_index = int(selected_option.get()) - 1
        
        # check if the answer is correct
        if question["options"][answer_index] == question["answer"]:
            result = "Correct!"
        else:
            result = "Incorrect"
        
        # create a label to display the result
        result_label = tk.Label(question_window, text=result)
        result_label.pack()
        
        # wait for 1 second and close the window
        question_window.after(1000, question_window.destroy)
    
    # wait for the user to submit the answer
    question_window.wait_window(question_window)

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

        

def get_hint(board, player, computer_mark):
    # Check if the current player is the computer player
    if player == computer_mark:
        return
    
    # Find the first available move that can result in a win
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            for j in range(0,9,3):
                if board[j] == board[j+1] == board[j+2] != " ":
                    hint = "Play in position {}".format(i+1)
                    show_hint_window(player, hint)
                    board[i] = " "
                    return
            for j in range(3):
                if board[j] == board[j+3] == board[j+6] != " ":
                    hint = "Play in position {}".format(i+1)
                    show_hint_window(player, hint)
                    board[i] = " "
                    return
            if board[0] == board[4] == board[8] != " ":
                hint = "Play in position {}".format(i+1)
                show_hint_window(player, hint)
                board[i] = " "
                return
            if board[2] == board[4] == board[6] != " ":
                hint = "Play in position {}".format(i+1)
                show_hint_window(player, hint)
                board[i] = " "
                return
            board[i] = " "
            
    # If no winning move is available, show a random hint
    hint = "Try playing in position {}".format(random.choice([1,3,5,7,9]))
    show_hint_window(player, hint)
    
def show_hint_window(player, hint):
    # create a new window for the hint
    hint_window = tk.Toplevel(root)
    hint_window.title("Hint")
    
    # create a label to display the hint
    hint_label = tk.Label(hint_window, text="Player {}: {}".format(player, hint))
    hint_label.pack()
    
    # create a button to close the hint window
    close_button = tk.Button(hint_window, text="Close", command=lambda: hint_window.destroy())
    close_button.pack()

def get_player_choice(board, player, computer):
    # create a new window for the player to make their move
    player_window = tk.Toplevel(root)
    player_window.title("Make Your Move")
    
    # create a label to display the current player
    player_label = tk.Label(player_window, text=f"It's {player}'s turn")
    player_label.pack()
    
    # create a canvas to display the board
    board_canvas = tk.Canvas(player_window, width=200, height=200)
    board_canvas.pack()
    
    # draw the board
    for i, mark in enumerate(board):
        x = (i % 3) * 67 + 20
        y = (i // 3) * 67 + 20
        board_canvas.create_rectangle(x, y, x+27, y+27)
    
    # create a function to handle clicks on the board
    def board_click(event):
        x, y = event.x, event.y
        # determine which cell was clicked
        col = (x - 20) // 67
        row = (y - 20) // 67
        cell = row * 3 + col
        # check if the cell is empty
        if board[cell] == " ":
            # update the board
            board[cell] = player
            print_board(board)
            # close the player window
            player_window.destroy()
        else:
            # display an error message
            error_label.config(text="That cell is already taken!")
    
    # bind the board_canvas to the board_click function
    board_canvas.bind("<Button-1>", board_click)
    
    # create a label to display error messages
    error_label = tk.Label(player_window, fg="red")
    error_label.pack()
    
    # wait for the player window to be closed
    player_window.wait_window()
    
    # return the updated board
    return board

def play_game():
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

   
# Start the Tkinter event loop
root.mainloop()

