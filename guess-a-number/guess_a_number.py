print("==========================")
print("Welcome to Guess a Number!")
print("==========================")





import math
import random


def pick_highest():
    while True:
        print("---------------")
        number=input("Insert a high: ")
        print("---------------")
            
        if int(number)==0 or int(number)==1 or int(number)==2:
            print("Use a different high.")
            
        elif number.isnumeric():
            return number            
                        
        else:
            print ("You need to use a number.")

def tries_pm(number):
    tries=math.log(int(number)-1,2)+1
    return int(tries)
        
def show_ending():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@Thank you for playing!@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def pick_number(number):
    print("I'm thinking of a number from 1 to "+str(number)+".");    

    return random.randint(1, int(number))
        
def get_guess(c_low,number,tries):
    
    while True:
        
        guess=input("Take a guess, "+str(c_low)+" to "+str(number)+": ")
            
        
        if guess.isnumeric():
            guess=int(guess)
            
            if int(c_low)-1<int(guess)<int(number)+1:
                
                return guess

            else:
                print("You need to use a number that is "+str(c_low)+" through "+str(number)+".")
                print("You still have "+str(tries)+" left.")
                
        else:
            print ("You need to use a number.")

            
def check_guess(guess,rand,c_low,number):
    if guess < rand:
        print("You guessed too low.")
        
        return c_low
        
        
    elif guess > rand:
        print("You guessed too high.")
        
        return number
        
    else:
        print("-----------")
        print("You got it!")
        print("-----------")


        
def show_gameover(): 
    print("---------------------")
    print("You ran out of tries!")

def show_gameover2():
    print("---------------------")
    print(">>>>>>>>>-<<<<<<<<<")
    print(">>>>>Game Over<<<<<")
    print(">>>>>>>>>-<<<<<<<<<")
          
def c_tries(tries):
        c_tries=int(tries)-1
        return c_tries

def play():
    
    number=pick_highest()
    guess=-1
    c_low=1
    tries_pm(number)
    tries=tries_pm(number)
    limit=2
    
    rand=pick_number(number)

    

    while guess != rand:
        if tries<limit:
            show_gameover()
            print("The number was "+(str(rand))+".")
            show_gameover2()
            return False
        else:
            c_tries(tries)
            tries=c_tries(tries)
            print("You have "+(str(tries))+" tries left.")

            
            
            guess=get_guess(c_low,number,tries)
            check_guess(guess,rand,c_low,number)
            if guess<rand:
                c_low=guess+1
            elif guess>rand:
                number=guess-1
                
                
            
            
            
            
            

        
       
            
                

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("Please enter 'y' or 'n'.")

            

playing=True
            
while playing:
    play()
    playing=play_again()

show_ending()
