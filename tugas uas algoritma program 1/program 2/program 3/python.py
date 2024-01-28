"""
Program python sederhana - Gunting batu kertas
"""
 
 
from random import randint
 
#create a list of play options
t = ["Batu", "Kertas", "Gunting"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
#set player to False
player = False
 
while player == False:
#set player to True
    player = input("Batu, Gunting, Kertas?")
    if player == computer:
        print("Seri!")
    elif player == "Batu":
        if computer == "Kertas":
            print("Anda Kalah!", computer, "menutup", player)
        else:
            print("Anda Menang!", player, "memukul", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print("Anda Kalah!", computer, "memotong", player)
        else:
            print("Anda Menang!", player, "menutup", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Anda Kalah...", computer, "memukul", player)
        else:
            print("Anda Menang!", player, "memotong", computer)
    else:
        print("Input tidak valid. Perhatikan penulisan Anda!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]