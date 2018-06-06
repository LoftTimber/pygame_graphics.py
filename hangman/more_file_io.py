import os
import random

def choose_word_list():
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

    #print(lines)

    category = lines[0]
    puzzle = random.choice(lines[1:])

    print(category)
    print(puzzle)
choose_word_list()
