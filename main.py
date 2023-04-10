import pygame
import random
# from tkinter import *
# from tkinter import messagebox
import time 
import sys

start_time = time.time()
incorrect=0
score=[0,0,0]
def new_line(s):
    if len(s)<75:
        return s," "
    ind=s.find(" ",75)
    return s[:ind],s[ind:]

def drawing(i,j):
    if not board[i]:
        screen.blit(box,j)
    elif board[i]=="X":
        pygame.draw.line(box, (0,0,0), (50,50),(150,150), width=5)
        pygame.draw.line(box, (0,0,0), (50,150),(150,50), width=5)
        screen.blit(box,j)
    else:
        pygame.draw.circle(box,(0,0,0),(100,100),50,width=5)
        screen.blit(box,j)

def player_wins(board):
    player="X"
    computer_mark="O"
    # check if the player has won horizontally
    if board[0] == board[1] == board[2] == player:
        return "player"
    elif board[3] == board[4] == board[5] == player:
        return "player"
    elif board[6] == board[7] == board[8] == player:
        return "player"
    # check if the player has won vertically
    elif board[0] == board[3] == board[6] == player:
        return "player"
    elif board[1] == board[4] == board[7] == player:
        return "player"
    elif board[2] == board[5] == board[8] == player:
        return "player"
    # check if the player has won diagonally
    elif board[0] == board[4] == board[8] == player:
        return "player"
    elif board[2] == board[4] == board[6] == player:
        return "player"
    # check if the computer has won horizontally
    elif board[0] == board[1] == board[2] == computer_mark:
        return "comp"
    elif board[3] == board[4] == board[5] == computer_mark:
        return "comp"
    elif board[6] == board[7] == board[8] == computer_mark:
        return "comp"
    # check if the computer has won vertically
    elif board[0] == board[3] == board[6] == computer_mark:
        return "comp"
    elif board[1] == board[4] == board[7] == computer_mark:
        return "comp"
    elif board[2] == board[5] == board[8] == computer_mark:
        return "comp"
    # check if the computer has won diagonally
    elif board[0] == board[4] == board[8] == computer_mark:
        return "comp"
    elif board[2] == board[4] == board[6] == computer_mark:
        return "comp"
    else:
        return False

def predict():
    copy=board[:]
    for i in range(len(copy)):
        copy=board[:]
        if copy[i]==None:
            copy[i]='X'
            if player_wins(copy):
                return i+1


# Define three sets of questions with varying difficulty levels
def questions():
    global easy_questions,medium_questions,hard_questions
    easy_questions = [
            {
                "question": "Which of the following is a high-level programming language?",
                "options": ["Assembly language", "Machine language", "C++", "None of the above"],
                "answer": "C++"
            },
            {
                "question": "Which of the following is a dynamically typed programming language?",
                "options": ["Java", "Python", "C#", "C"],
                "answer": "Python"
            },
            {
                "question": "Which of the following is a built-in function in Python to get the length of a string?",
                "options": ["length()", "size()", "len()", "count()"],
                "answer": "len()"
            },
            {
                "question": "What does HTML stand for?",
                "options": ["Hypertext Markup Language", "Hyperlinks and Text Markup Language", "High-level Markup Language", "None of the above"],
                "answer": "Hypertext Markup Language"
            },
            {
                "question": "What does HTML stand for?",
                "options": ["Hypertext Markup Language", "Hyperlinks and Text Markup Language", "High-level Markup Language", "None of the above"],
                "answer": "Hypertext Markup Language"
            },
            {
                "question": "Which of the following is a built-in function in Python to get the length of a string?",
                "options": ["length()", "size()", "len()", "count()"],
                "answer": "len()"
            }]  
    medium_questions = [
            {
                "question": "What is the output of the following code in Python? a = 5, b = 3, print(a // b)",
                "options": ["1", "1.67", "2", "2.5"],
                "answer": "2"
            },
            {
                "question": "What is the purpose of the 'finally' block in a try-except block in Python?",
                "options": ["To execute the code if the try block raises an exception", "To execute the code if the except block does not catch an exception", "To execute the code regardless of whether an exception is raised or not", "None of the above"],
                "answer": "To execute the code regardless of whether an exception is raised or not"
            },
            {
                "question": "Which of the following is a disadvantage of using a relational database?",
                "options": ["Low security", "Low scalability", "Low performance", "None of the above"],
                "answer": "Low scalability"
            },
            {
                "question": "What is the difference between an abstract class and an interface in Java?",
                "options": ["An abstract class can have constructor while interface cannot", "An interface can have concrete methods while abstract class cannot", "An abstract class can implement interfaces while interface cannot", "None of the above"],
                "answer": "An abstract class can have constructor while interface cannot"
            },
            {
                "question": "What is the difference between an abstract class and an interface in Java?",
                "options": ["An abstract class can have constructor while interface cannot", "An interface can have concrete methods while abstract class cannot", "An abstract class can implement interfaces while interface cannot", "None of the above"],
                "answer": "An abstract class can have constructor while interface cannot"
            }
        ]
    hard_questions = [
        {
        "question": "What is the output of the following code in JavaScript? for (var i = 0; i < 5; i++) { (function(j) { setTimeout(function(){console.log(j); }, j * 1000 );})(i)",
            "options": ["0 1 2 3 4", "1 2 3 4 5", "5 5 5 5 5", "None of the above"],
            "answer": "0 1 2 3 4"
        },
        {
            "question": "What is the difference between \"const\" and \"let\" in JavaScript?",
            "options": ["\"const\" variables can not be reassigned while \"let\" variables can be reassigned","\"const\" variables can only be declared once while \"let\" variables can be declared multiple times","\"const\" variables can only be declared inside functions while \"let\" variables can be declared both inside and outside functions","None of the above"],
            "answer": "\"const\" variables can only be reassigned once while \"let\" variables can be reassigned multiple times"
        },
        {
            "question": "Which of the following is a benefit of using a functional programming approach?",
            "options": ["It promotes side-effects and mutable state","It is only suitable for small-scale projects","It makes it easier to reason about the code and avoid bugs","None of the above"],
            "answer": "It makes it easier to reason about the code and avoid bugs"
        },
        {
            "question": "What is the purpose of the \"yield\" keyword in Python?",
            "options": ["To create a generator function","To define a variable as a generator","To terminate a generator function","None of the above"],
            "answer": "To create a generator function"
        }
    ]

questions()
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((600,850))
screen.fill((108, 207, 246))

font=pygame.font.SysFont('arial',40) 
small_font=pygame.font.SysFont('arial',20)

board=[None]*9
empty=[i for i in range(9)]
clock=pygame.time.Clock()
box=pygame.Surface((200,200))

get_question=True
option_box=pygame.Surface((600,150))
difficulty=1
phase="player"
wait=False,False
#creating rectangles for the game
box_rects=[]
for i in range(0,600,200):
    box_rects.append(box.get_rect(topleft=(i,150)))
for i in range(0,600,200):
    box_rects.append(box.get_rect(topleft=(i,350)))
for i in range(0,600,200):
    box_rects.append(box.get_rect(topleft=(i,550)))

option_box_rects=[]
for i in range(4):
    option_box_rects.append(option_box.get_rect(topleft=(0,150+i*150)))
while True:
    
    screen.fill((108, 207, 246))
    for i in pygame.event.get():
        if i.type==256:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE and phase=="end_game":
                score=[0,0,0]
                difficulty=1
                board=[None]*9
                phase="player"
                wait=False,False
                get_question=True
                incorrect=0
                empty=[i for i in range(9)]
                questions()
    # pygame.draw.line(screen,(0,0,0),(200,150),(200,750),5)
    # pygame.draw.line(screen,(0,0,0),(400,150),(400,750),5)
    # pygame.draw.line(screen,(0,0,0),(0,150),(600,150),5)
    # pygame.draw.line(screen,(0,0,0),(0,350),(600,350),5)
    # pygame.draw.line(screen,(0,0,0),(0,550),(600,550),5)
    # pygame.draw.line(screen,(0,0,0),(0,150),(600,150),5)
    res=player_wins(board)
    #print(phase,res)
    mouse_buttons=pygame.mouse.get_pressed()
    if res=="player":
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("You Win!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(2)
        res2=res
        res=''
        board=[None]*9
        phase="end_game"
        continue
    elif res=="comp":
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("Computer Wins!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(2)
        res2=res
        res=''
        board=[None]*9
        phase="end_game"
        continue
    if not empty:
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("Tie!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(3)
        exit()
    if phase=="player":
        move=predict()
        if move:
            txt=font.render(f"hint: You can win by marking position {move} ",True,(0,0,0))
        else:
            txt=font.render(f"hint: No hint available at the moment",True,(0,0,0))
        txt_rect=txt.get_rect(topleft=(30,780))
        screen.blit(txt,txt_rect)
        txt=font.render("Your turn!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        
        #print(mouse_buttons)
        if wait[1] and wait[0]:
            screen.fill((108, 207, 246))
            for i,j in enumerate(box_rects):
                box.fill((52, 84, 209))
                drawing(i,j)
            txt=font.render("Question Time!!",True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,75))
            screen.blit(txt,txt_rect)
            pygame.display.update()
            time.sleep(1)
            wait=False,False
            phase="question"
            continue
        elif not wait[1] and wait[0]:
            screen.fill((108, 207, 246))
            for i,j in enumerate(box_rects):
                box.fill((52, 84, 209))
                drawing(i,j)
            txt=font.render("Invalid!!",True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,75))
            screen.blit(txt,txt_rect)
            pygame.display.update()
            time.sleep(1)
            wait=False,False

        mouse=pygame.mouse.get_pos()
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
            if j.collidepoint(mouse):
                #print(i+1)
                box.fill((52, 84, 230))
                drawing(i,j)
                if mouse_buttons[0]:
                    if not board[i]:
                        board[i]='X'
                        empty.remove(i)
                        wait=True,True
                    else:
                        wait=True,False

    elif phase=="comp":
        if empty:
            choice=random.choice(empty)
            board[choice]="O"
            empty.remove(choice)
        phase="question"
        #print(choice)
        screen.fill((108, 207, 246))
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("Computers turn!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(1)
    elif phase=="question":
        #print(len(easy_questions))
        if difficulty==1 and get_question:
            question=easy_questions.pop()
            get_question=False
        elif difficulty==2 and get_question:
            question=medium_questions.pop()
            get_question=False
        elif difficulty==3 and get_question:
            question=hard_questions.pop()
            get_question=False
        #print(question)
        #print("in")
        screen.fill((108, 207, 246))
        #print(len(option_box_rects))
        mouse=pygame.mouse.get_pos()
        
        for i,j in enumerate(option_box_rects):
            if j.collidepoint(mouse):
                option_box.fill((52, 84, 230))
            else:
                option_box.fill((52, 84, 209))
            txt=small_font.render(question["options"][i],True,(0,0,0))
            #print(question["options"][i])
            txt_rect=txt.get_rect(midtop=(300,50))
            option_box.blit(txt,txt_rect)
            screen.blit(option_box,j)
            #print(new_line(question["question"]))
            txt=small_font.render(new_line(question["question"])[0],True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,50))
            screen.blit(txt,txt_rect)
            txt=small_font.render(new_line(question["question"])[1],True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,80))
            screen.blit(txt,txt_rect)
            #pygame.display.update()
            
    
        pygame.display.update()
        #time.sleep(2)
        #print(mouse)
        ans=-1
        if mouse_buttons[0]==True:
            for i,j in enumerate(option_box_rects):
                if j.collidepoint(mouse):
                    ans=i
            if ans!=-1:
                phase="result"
                get_question=True
                time.sleep(1)
    elif phase=="result":
        screen.fill((108, 207, 246))
        if question['options'][ans]==question['answer']:
            txt=small_font.render('Correct Answer!!',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,300))
            screen.blit(txt,txt_rect)
            if difficulty<3:difficulty+=1
            score[difficulty-1]+=1
            phase="player"
            
        else:
            txt=small_font.render('Wrong Answer!!',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,300))
            screen.blit(txt,txt_rect)
            phase="comp"
            incorrect+=1
        pygame.display.update()
        time.sleep(2)
    elif phase=="end_game":
        screen.fill((108, 207, 246)) 
        if res2=='player':
            txt=small_font.render(f'number of questions answered correctly: {sum(score)}',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,300))
            screen.blit(txt,txt_rect)
            txt=small_font.render(f'number of questions answered incorrectly: {incorrect}',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,350))
            screen.blit(txt,txt_rect)
            txt=font.render('Press space to try again!!',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,400))
            screen.blit(txt,txt_rect)
        elif res2=="comp":
            screen.blit(txt,txt_rect)
            txt=font.render('Computer wins!!',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,340))
            screen.blit(txt,txt_rect)
            txt=font.render('Press space to try again!!',True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,400))
            screen.blit(txt,txt_rect)
        pygame.display.update() 
    pygame.display.update()
    clock.tick(60)


