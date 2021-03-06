print("=============================")
print("Welcome to Guess a Number AI!")
print("=============================")





    




import math
import random



def tries_pm(number):
    tries=math.log(int(number)-1,2)+1
    return int(tries)
        
def show_ending():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@Thank you for playing!@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


        
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

def check_answer(your_answer,answer):
    while True:
        
        
        
        if your_answer == 'y' or your_answer == 'yes':
            return False
        elif your_answer=='h' or your_answer=='higher':
            c_low=answer
            return c_low
        elif your_answer=='l' or your_answer=='lower':
            c_high=answer
            return c_high
        else:
            print("Please enter yes, higher, or lower.")
            
def guess_answer(c_low,c_high,tries,limit):
    print("Ok")
    if tries==limit+1:
        print("gooooo")
        
        rand=random.randint(c_low+1,c_high)
        answer=str(rand)
    else:
        answer=(c_high+c_low)//2
    
    return answer



def play():
    print("Think of a number from 1 to 100 and I will try to guess it.")
    input("Press enter when you are ready.")
    c_low=1
    c_high=100
    
    game_play=True
    number=100
    tries_pm(number)
    tries=tries_pm(number)
    tries=7
    limit=0
    
    
    while limit+1>tries:
        show_gameover()
    

    while game_play and limit<tries:
        if tries<limit:
            show_gameover()
            print("The number was "+(str(rand))+".")
            show_gameover2()
            return False
        else:
            print("I have "+(str(tries))+" tries left.")
            answer=guess_answer(c_low,c_high,tries,limit)
            print("Is your number "+str(answer)+".")
            print("Or is it higher or lower.")
            your_answer=input("Tell me yes, higher, or lower:")
            tries-=1
            if your_answer=='h':
                
                    
                c_low=check_answer(your_answer,answer)
            elif your_answer=='l':
                c_high=check_answer(your_answer,answer)
                
            elif your_answer=='y':
                print("Alright, I got it.")
                return False
            else:
                print("Please tell me yes, higher, or lower.")
            
            print("Okay")

    
            
            
            
                
                
            
            
            
            
            

        
       
            
                

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

