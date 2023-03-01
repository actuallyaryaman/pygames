import random
import time

name=input("Computer: Hi! What's your name? ")
inp=["r", "p", "s"]

print("Nice to meet you, "+name+"! Ready for a game of rock-paper-scissors?")
ready=input()
if ready=="yes":
    print("Let me read the rules of the game for you: ")
    print("A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.\nIn this simulation, the computer has two different strategies that it can follow. ")
    playerinput=input("your turn: ")
    computerinput=inp[random.randint(0, len(inp)-1)]
    print(computerinput)
    if playerinput==computerinput:
        print("Draw")
    elif (playerinput=="r" and computerinput=="p"):
        print("Computer wins!")
    elif (playerinput=="p" and computerinput=="r"):
        print((name+" wins!"))
    elif (playerinput=="r" and computerinput=="s"):
        print((name+" wins!"))
    elif (playerinput=="s" and computerinput=="r"):
        print("Computer wins!")