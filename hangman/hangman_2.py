#Hangman
#Made by Shane F.


import time
import random
import os

def splash_screen():
    print("=======================")
    print("~~Welcome to FootRace~~")
    print("=======================")
    print("           .==,_")
    print("         .===,_`\        ,,,,, ")
    print("       .====,_ ` \      .====,\__")
    print(" ---     .==-,`~. \           \ OO__,")
    print("  ---      `~~=-.  \           /__-/")
    print("    ---       `~~=. \         /")
    print("                 `~. \       /")
    print("                   ~. \____./")
    print("                     `.=====)")
    print("                  ___.--~~~--.__")
    print("        ___\.--~~~              ~~~---.._|/")
    print("        ~~~*  ""                           " "/")


def list_rules():
    print("This game is played the same way as Hangman. (try to get all the letters and try not to get six strikes)")
    print("You are the human. To win the race you must guess all the letters in the puzzle.")
    print("Your oppenent is the roadrunner. For it to win the race you must get six strikes.")
    print()
    input("Press 'Enter' when you are ready to start.")


def count_off():
    print("On your mark")
    time.sleep(1)
    print("Get ready")
    time.sleep(1)
    print("Start")
    time.sleep(1)

    
def choose_word_list():
    print("================================")
    print("Choose your category.")
    file_names = os.listdir("data")
    category_position = 0
    for f in enumerate(file_names):
        file = "data/" + file_names[category_position]
        with open(file, 'r') as f:
            lines = f.read().splitlines()
        first_category = lines[0]
        print(str(int(category_position) +1) + ") " + str(first_category))
        category_position += 1               
    choice = input("which one? ")
    choice = int(choice)-1
    file = "data/" + file_names[choice]
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    category = lines[0]
    random_puzzle = random.choice(lines[1:])
    print(category)
    print(random_puzzle)
    return random_puzzle




def get_solved(puzzle, correct_guesses):
    solved = ""
    
    for letter in puzzle:
        if letter in correct_guesses:
            solved += letter
        elif letter.isalpha() == False:
            solved += letter                                
        else:
            solved += "-"
            
    return solved

def get_guess(puzzle, correct_guesses, missed_letters, missed_words):    
    guess = input("Guess a letter:")
    
    if guess.isalpha():
        
        if guess in correct_guesses or guess in missed_letters:
            print("#################################")
            print("You already used this letter.")
            print("#################################")
            guess = ""
            
        while len(guess)>1:
            guessing_word = input("Is "+(guess)+" your answer:")
            
            if guessing_word == 'y':
                
                if guess == puzzle:
                    return guess
                
                else:
                    print("Nope, that is not the word.")
                return guess
            
            if guessing_word == 'n':
                print("#########################")
                print("Only give one letter.")
                print("#########################")
                guess = ""        
        return guess
    
    else:
        print("######################")
        print("Only give letters.")
        print("######################")
        guess = ""
        return guess
        
    
def display_board(puzzle, solved, missed_letters, missed_words, strikes):
    count = 0
    letters_in_solved = 0
    for letter in puzzle:
        if letter.isalpha():
            letters_in_solved += 1
    for s in solved:
        
        if s[:] =='-':
            count += 1
    if solved == puzzle:
        count = 0
        letters_in_solved = 120
        spaces = 0
    
    spaces = 120/(int(letters_in_solved))
    extra_spaces = 120-(120/(int(letters_in_solved)))
    
    print((int(spaces))*(int(letters_in_solved)-int(count))*(" ") +"     @"+ (int(extra_spaces) +((int(count))*(int(spaces))))*(" ") +"   /### ")
    print((int(spaces))*(int(letters_in_solved)-int(count))*(" ") +"   ~/~"+ (int(extra_spaces) +((int(count))*(int(spaces))))*(" ") +"  /### ")
    print((int(spaces))*(int(letters_in_solved)-int(count))*(" ") +"   0  "+ (int(extra_spaces) +((int(count))*(int(spaces))))*(" ") +" / ")
    print(127*(" ") +"!")
    print("=========================================================================================================================finish========")
    print(20*(strikes)*(" ") +"       "+ 20*(6-strikes)*(" ") +"  /### ")
    print(20*(strikes)*(" ") +" `~,_/`"+ 20*(6-strikes)*(" ") +" /### ")
    print(20*(strikes)*(" ") +"   0   "+ 20*(6-strikes)*(" ") +"/ ")
    print("=========================================================================================================================finish========")
    print("Solved: " + solved)
    print("Missed Letters: {" + missed_letters + "}")
    print("Missed Words: {" + missed_words + "}")
    print("Strikes: " + str(strikes))
    print("========================================")   
    

def show_result(solved, puzzle):
    
    if solved==puzzle:
        print("You got the puzzle...")
        print("You Win!")
        
    else:
        print("You ran out of tries...")
        print("You Lose!")
    print("The word was " + (puzzle))

        
#Game Starts

splash_screen()
list_rules()


  
def play():
    puzzle = choose_word_list()
    count_off()
    
    correct_guesses = ""
    missed_words = ""
    missed_letters = ""
    solved = get_solved(puzzle, correct_guesses)
    strikes = 0
    limit = 6
    display_board(puzzle, solved, missed_letters, missed_words, strikes)
    print(solved)
    
    while solved != puzzle and strikes!=6:
        letter = get_guess(puzzle, correct_guesses, missed_letters, missed_words)
        
        if len(letter)>1:
            word = letter
            
        if letter not in puzzle and len(letter)==1:
            missed_letters += letter + " "
            
        elif letter != puzzle and len(letter)>1:
            missed_words += letter + " "
            
        else:
            correct_guesses +=letter        
        solved = get_solved(puzzle, correct_guesses)
        
        if letter == "" or (len(letter)==1 and letter in puzzle) or (len(letter)>1 and letter == puzzle):
            pass
        
        else:
            strikes += 1                
        display_board(puzzle, solved, missed_letters, missed_words, strikes)
    show_result(solved, puzzle)


def play_again():
    
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        
        elif decision == 'n' or decision == 'no':
            return False
        
        else:
            print("Please enter 'y' or 'n'.")

            
def show_credits():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Thank you for playing.")
    print("This game was made by Shane F.!")
    print("12/3/2017")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    
playing=True
            
while playing:
    play()
    playing=play_again()

show_credits()
