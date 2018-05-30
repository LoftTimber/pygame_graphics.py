class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " says 'Mmmmmm, so good and tasty!'")
        else:
            print(self.name + " is too ded to eat.")
            
    def sleep(self):
        if self.is_alive:
            print("I'm schleeep")
        else:
            print(self.name + " is too ded to schleeep.")

    def play(self):
        if self.is_alive and self.happiness > 1:
            print("Yeet!")

        elif self.is_alive and self.happiness == 0:
            print(self.name + " is too grump to play.")
        else:
            print(self.name + " is too ded to yeet.")

        
        

    def rotate_right(self):
        if self.is_alive:
            self.direction += 1

            if self.direction == 4:
                self.direction = 0

        else:
            print(self.name + " is too ded to rotate right.")

    def rotate_left(self):
        if self.is_alive:
            self.direction -= 1

            if self.direction == -1:
                self.direction = 3

        else:
            print(self.name + " is too ded to rotate left.")

    def move(self):
        if self.is_alive:
            if self.direction == 0:
                self.y += 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y -= 1
            elif self.direction == 3:
                self.x -= 1
        else:
            print(self.name + " is too ded to move.")

    def kill(self, other):
        if self.is_alive and other.is_alive:
            print(self.name + " attacks " + other.name +"!")
            print(other.name + " goes 'oof' and dies.")
            other.is_alive = False
            other.happiness = 0
        elif self.is_alive and not other.is_alive:
            print(other.name + " is too ded to git ded.")
        else:
            print(self.name + " is too ded to kill.")

    def hug(self, other):
        if self.is_alive and other.is_alive:
            print(self.name + " hugs " + other.name +"!")
            other.happiness += 1

            if other.happiness < 10:
                print(other.name + " says, 'I'm like " + str(other.happiness) + " happy now.")
            else:
                print(other.name + " says, 'Um, this is awkward.'")
        elif self.is_alive and not other.is_alive:
            print(self.name + " hugs " + other.name + ".")
            print(other.name + " is too ded to notice.")
        else:
            print(self.name + " is too ded to hug.")

    def revive(self, other):
        if self.is_alive:
            if other.is_alive:
                print(other.name + " is still not ded.")

            else:
             print(self.name + " brings " + other.name +" back to not ded!")
             other.is_alive = True
        else:
            print(self.name + " is too ded to revive.")
         
            
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Emma")
pet2 = Pet("Shane")
pet3 = Pet("Enrique")
