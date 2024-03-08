#file : CS112_A1_T2_20231090.py 
# purpose: 100 game . Two players start from 0 , who reachs 100 wins ! 
# Author: Anoud Mohamed Ahmed Abdelkhalek
# ID : 20231090

def main():
#Initialize the coins status
    n_coins= 0
    player= 1
#Display a welcome message
    print("Welcome to 100 Game")
    print(" Number of coins =100")
#loop until the game is over while n_coins <100
    while n_coins <100 :
        move = int(input("player 1 : please take 1-10 coins "))
        while move<1 or move >10 :
            move = int(input("player 1 : please take 1-10 coins "))
#check the  input validation ( between 1and 10)          
            if move <1 or move>10:
                print("please select a valid number")
                continue
        n_coins+= move
        print (f" Now we have {n_coins}")
#Check if player 1 has reached number of coins = 100 or more
        if n_coins >= 100 :
            print (" player 1 is the winner")
            break 
        move = int(input("player 2 : please take 1-10 coins " ))
        while move<1 or move>10 :
            move=int(input("player 2 : please take 1-10 coins "))
#check the  input validation ( between 1and 10)
            if move <1 or move>10:
                print("please select a valid number")
                continue
        n_coins += move
        print (f" Now we have {n_coins}")  
#Check if player 2 has reached number of coins = 100 or more
        if n_coins>= 100 :
            print ("player 2 is the winner")
            break 
main()         
        
