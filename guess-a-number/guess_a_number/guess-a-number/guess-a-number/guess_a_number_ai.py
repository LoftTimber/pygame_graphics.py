#Guess a number AI
#This game was made by Shane F.
#10/22/2017

import math
import random

print("=============================")
print("Welcome to Guess a Number AI!")
print("=============================")



def give_high():
    
    while True:
        c_high=input("Insert a high limit.")
        
        if c_high.isnumeric():
            
            if int(c_high)<3:
                print("May you uses a different number, please.")
                    
            else:
                return c_high
                
        else:
            print("Please enter a number.")


    
def give_low(c_high):
    
    while True:
        c_low=input("Insert a low limit.")
        
        if c_low.isnumeric():
            
            if int(c_low)<1:
                print("May you use a different number, please.")
                
            elif int(c_low)>int(c_high)-2:
                print("May you use a different number, please.")
                
            else:
                return c_low
            
        else:
            print("Please enter a number.")



def tries_pm(c_low,c_high):
    tries=math.log(int(c_high)-1,2)+2
    return int(tries)


        
def show_ending():
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@Thank you for playing!@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")
    print("This program was made by Shane.")
    print("10/22/2017")
          


def check_answer(c_low,c_high,answer,tries,limit):
    
    while True:                        
        your_answer=input("Tell me higher, lower, or yes.")
        
        if your_answer=='h' or your_answer=='higher':            
            return 'h'
        
        elif your_answer=='l' or your_answer=='lower':           
            return 'l'
        
        elif your_answer == 'y' or your_answer == 'yes':
            print("Alright, I got it!")
            return False
        
        else:
            print("...")


            
def def_tries(tries,limit,c_low,c_high,answer):
    
    if tries<limit:
        show_gameover()       
        show_gameover2()
        
    elif tries==1:
        answer=c_high
        print("Is your number "+str(answer)+".")
        
    elif tries>limit-1:
        print("Is your number "+str(answer)+".")



def play():
    
    c_high=give_high()
    c_low=give_low(c_high)
    print("---")
    print("Think of a number from "+str(c_low)+" to "+str(c_high)+" and I will try to guess it.")
    input("Press enter when you are ready.")      
    c_low=int(c_low)
    c_high=int(c_high)  
    tries=tries_pm(c_low,c_high)    
    limit=1
    game_play=True
    
    while game_play:
        answer=(c_high+c_low)//2        
        print("I have "+(str(tries))+" tries left.")
        
        if c_high-c_low>0:
            def_tries(tries,limit,c_low,c_high,answer)
        
        if c_high-c_low<1:
            cur=c_high
            print("Well, the number has to be "+str(cur)+".")
            print("Right?")
            your_answer=input("Tell me yes or no:")
            
            if your_answer=='y' or your_answer=='yes':
                print("Alright, I got it!")
                game_play=False
                return False
            
            elif your_answer=='n' or your_answer=='no':
                your=input("Are you sure "+str(cur)+" is not your number?")
                
                if your=='y' or your=='yes':
                    print("Hmm, there must have been a mistake somewhere...")
                    return False
                
                elif your=='n' or your=='no':
                    print("Okay, so your number was "+str(cur)+".")
                    print("Right, looks like I got the number then.")
                    return False
                
            else:
                print("May you enter yes or no, please.")
                
        elif tries>=limit:
            pos=check_answer(c_low,c_high,answer,tries,limit)            
            print("=====================")
            
            if pos=='h':                
                c_low=answer+1
                
            elif pos=='l':
                
                if answer==c_low:
                    real=True
                    
                    while real:
                        print("Wait, that can not be right!")
                        thing=input("Are you sure that is right?")
                    
                        if thing=='y' or thing=='yes':
                            print("Oh...")
                            print("There must have been a mistake somewhere.")
                            game_play=False
                            return False
                        
                        elif thing=='n' or thing=='no':
                            qu=input("Okay, so tell me yes if your number is "+str(answer)+", or tell me if it is higher?")
                            
                            if qu=='y' or qu=='yes':
                                print("Alright, I got it!")
                                game_play=False
                                return False
                            
                            elif qu=='h' or qu=='high':
                                c_low=answer+1
                                real=False                              
                                
                            else:
                                print("Please tell me yes or no.")
                            
                        else:
                            print("Please tell me yes or no.")
                            
                else:
                    c_high=answer-1
                
            elif pos==False:
                game_play=False           
            tries-=1
            
        else:
            game_play=False


                                                                                                                                 
def play_again():
    
    while True:
        decision = input("Would you like to play again? (y/n) ")
        print("------------------------------------")

        if decision == 'y' or decision == 'yes':
            return True
        
        elif decision == 'n' or decision == 'no':
            return False
        
        else:
            print("Please enter 'y' or 'n'.")

           


#game starts
playing=True

while playing:
    play()
    playing=play_again()

show_ending()

