import pygame
import random
from tkinter import *
from tkinter import messagebox
import time 
import sys


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


# Define three sets of questions with varying difficulty levels
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
        }
    ]  
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

pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((600,750))
screen.fill((108, 207, 246))

font=pygame.font.SysFont('arial',40) 

board=[None]*9
empty=[i for i in range(9)]
clock=pygame.time.Clock()
box=pygame.Surface((200,200))


option_box=pygame.Surface((600,150))
difficulty="easy"
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
    # pygame.draw.line(screen,(0,0,0),(200,150),(200,750),5)
    # pygame.draw.line(screen,(0,0,0),(400,150),(400,750),5)
    # pygame.draw.line(screen,(0,0,0),(0,150),(600,150),5)
    # pygame.draw.line(screen,(0,0,0),(0,350),(600,350),5)
    # pygame.draw.line(screen,(0,0,0),(0,550),(600,550),5)
    # pygame.draw.line(screen,(0,0,0),(0,150),(600,150),5)
    res=player_wins(board)
    if res=="player":
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("You Win!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(3)
        exit()
    elif res=="comp":
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("Computer Wins!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(3)
        exit()
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
        txt=font.render("Your turn!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        mouse_buttons=pygame.mouse.get_pressed()
        #print(mouse_buttons)
        if wait[1] and wait[0]:
            screen.fill((108, 207, 246))
            for i,j in enumerate(box_rects):
                box.fill((52, 84, 209))
                drawing(i,j)
            txt=font.render("Computers turn!!",True,(0,0,0))
            txt_rect=txt.get_rect(center=(300,75))
            screen.blit(txt,txt_rect)
            pygame.display.update()
            time.sleep(1)
            wait=False,False
            phase="comp"
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
        phase="player"
        print(choice)
        screen.fill((108, 207, 246))
        for i,j in enumerate(box_rects):
            box.fill((52, 84, 209))
            drawing(i,j)
        txt=font.render("Computers turn!!",True,(0,0,0))
        txt_rect=txt.get_rect(center=(300,75))
        screen.blit(txt,txt_rect)
        pygame.display.update()
        time.sleep(1)
    elif phase=="Question":
        screen.fill((108, 207, 246))
        for i,j in enumerate(option_box_rects):
            option_box.fill((50*i,50*i,50*i))
            screen.blit(option_box,j)
        pygame.display.update()
        time.sleep(2)
        phase="player"
    pygame.display.update()
    clock.tick(60)


Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Continue','OK')