import random
import getpass
import socket
import time
import sys

# function to print a message with a typing effect
def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# # print message with typing effect
# print_with_typing_effect("How are you?")

# # prompt for input with typing effect
# print_with_typing_effect("What is your name?")
# a = input()

username=getpass.getuser()
Computer=socket.gethostname()
inp=["1", "2", "3"]

pts_player=0
pts_comp=0

print_with_typing_effect(Computer+": Nice to meet you, "+username+"! Ready for a game of rock-paper-scissors?")
print_with_typing_effect(Computer+": Let me read the rules of the game for you.")
print_with_typing_effect(Computer+": A rock(1) beats scissors(3), scissors(3) beat paper(2) by cutting it, and paper(2) beats rock(1) by covering it.\n ")

while True:
    try:
        print_with_typing_effect(Computer+": How many rounds you want to play?: ")
        rounds=int(input())
        if rounds >= 15:
            print_with_typing_effect(Computer+" Exceeded Maximum Limits")
        else:
            break
    except:
        print_with_typing_effect(Computer+": Please enter an integer")
        break
for rounds in range(rounds):
    playerinput=input(username+": ")
    computerinput=inp[random.randint(0, len(inp)-1)]
    print_with_typing_effect(Computer+": "+computerinput)
    if playerinput==computerinput:
        pts_comp
        pts_player
    elif (playerinput=="1" and computerinput=="2"):
        print_with_typing_effect(Computer+": I win!")
        pts_comp+=1
    elif (playerinput=="2" and computerinput=="1"):
        print_with_typing_effect(Computer+": You win!")
        pts_player+=1
    elif (playerinput=="1" and computerinput=="3"):
        print_with_typing_effect(Computer+": You win!")
        pts_player+=1
    elif (playerinput=="3" and computerinput=="1"):
        print_with_typing_effect(Computer+": I win!")
        pts_comp+=1
    elif (playerinput=="2" and computerinput=="3"):
        print_with_typing_effect(Computer+": I win!")
        pts_comp+=1
    elif (playerinput=="3" and computerinput=="2"):
        print_with_typing_effect(Computer+": You win!")
        pts_player+=1
    print_with_typing_effect(Computer+": Current Score is: ")
    print_with_typing_effect(Computer+": Your score= "+str(pts_player))
    print_with_typing_effect(Computer+": My score= "+str(pts_comp))
    
diff1=pts_player-pts_comp
diff2=pts_comp-pts_player

if pts_player>pts_comp:
    print_with_typing_effect(Computer+": Congrats "+username+"! You win by "+ str(diff1)+"pts")
else:
    print_with_typing_effect(Computer+": You lost by "+str(diff2)+"pts")