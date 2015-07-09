'''
Interactive Python Trivia game. This game allows for random fun facts.
Created by Golden_Boy

'''


from sys import exit 


class Syntax(object): # Exit class
    def syntax(self):
        S = Start() # Stores the call to Start function as S

        print("Syntax error: possible errors include 'Typing a lowercase letter' ")
        syn = raw_input("Would you like to quit?(Y, N) ")

        if syn == 'Y':
            exit(0)
        else:
            S.begin()
           

class Health_Trivia(object): # Health trivia class/questions
    def Health(self):
        S = Start()
        Sy = Syntax()

        print "A cough releases an explosive charge of air that moves at speeds up to 60 mph."
        raw_input(">>> 'Enter' for next question ")
        print "According to German researchers, the risk of heart attack is higher on Monday than any other day of the week."
        raw_input(">>> 'Enter' for next question ")
        print "Humans shed about 600,000 particles of skin every hour - about 1.5 pounds a year. By 70 years of age, an average person will have lost 105 pounds of skin."
        raw_input(">>> 'Enter' for next question ")
        print "The human body has enough fat to produce 7 bars of soap."
        raw_input(">>> 'Enter' for next question ")
        print "Every square inch of the human body has an average of 32 million bacteria on it."
        raw_input(">>> 'Enter' for next question ")
        print "\n"

        usr_inp = raw_input("Would you like to continue playing?(Y or N) ")
        if usr_inp == 'Y':
            S.begin()
        else:
            Sy.syntax()

class Random_Trivia(object): # Random trivia class/questions
    def Random(self):
        S = Start()
        Sy = Syntax()

        print "Humans and Dolphins are the only species that have sex for pleasure."
        raw_input(">>> 'Enter' for next question ")
        print "The ant can lift 50 times its own weight." 
        raw_input(">>> 'Enter' for next question ") 
        print "Dolphins sleep with one eye open."
        raw_input(">>> 'Enter' for next question ") 
        print "Recycling one glass jar saves enough energy to watch TV for three hours."
        raw_input(">>> 'Enter' for next question ") 
        print "A cockroach can live several weeks with its head cut off."
        raw_input(">>> ")
        print "\n"

        usr_inp = raw_input("Would you like to continue playing?(Y , N) ")
        if usr_inp == 'Y':
            S.begin()
        else:
            Sy.syntax()

class Global_Trivia(object):
    def Global(self):
        S = Start()
        Sy = Syntax()

        print "It takes approximately 600 years for a plastic water bottle to decompose."
        raw_input(">>> 'Enter' for next question ")
        print "The quantity of water used on a daily basis around the world is 400 billion gallons."
        raw_input(">>> 'Enter' for next question ")
        print "The world has only 3% fresh water."
        raw_input(">>> 'Enter' for next question ")
        print "The estimated amount of snow crystals that drop from skies every year all over the world is 1 septillion. That's 24 zeros!"
        raw_input(">>> 'Enter' for next question ")
        print "The Earth moves through space at a speed of 66,700 miles/hour."
        raw_input(">>> ")
        print "\n"

        usr_inp = raw_input("Would you like to continue playing?(Y , N) ")
        if usr_inp == 'Y':
            S.begin()
        else:
            Sy.syntax()

class Animal_Trivia(object):
    def Sports(self):
        S = Start()
        Sy = Syntax()

        print "Only female mosquitos bite. Male mosquitos go for nectar instead "
        raw_input(">>> 'Enter' for next question ")
        print "Elephants are unable to jump because they are just too heavy"
        raw_input(">>> 'Enter' for next question ")
        print "The fastest animal on two legs is an Ostrich"
        raw_input(">>> 'Enter' for next question ")
        print "A pigs' orgasms last for nearly 30 minutes"
        raw_input(">>> 'Enter' for next question ")
        print "Turritopsis nutricula Immortal jellyfish is the only species known to live forever."
        raw_input(">>> ")
        print "\n"

        usr_inp = raw_input("Would you like to continue playing?(Y , N) ")
        if usr_inp == 'Y':
            S.begin()
        elif usr_inp == 'N':
            Sy.syntax()

class Start(Syntax): # Intro text to game
    def begin(self):
        print "Welcome to Python Trivia. The purpose of the game is"
        print "to display random trivia based on the category you've chosen"
        print "To begin the game press 'Enter'"
        I = raw_input(">>> ")
        
        print "Choose a category"
        A = 'A: Animal'
        B = 'B: Random'
        C = 'C: Global'
        D = 'D: Human Body'

        print(A)
        print(B)
        print(C)
        print(D)

        S = Animal_Trivia()
        R = Random_Trivia()
        G = Global_Trivia()
        H = Health_Trivia()
        Sy = Syntax()

        usr_inp = raw_input(">>> ")

        if usr_inp == 'A':
            S.Sports()

        elif usr_inp == 'B':
            R.Random()

        elif usr_inp == 'C':
            G.Global()

        elif usr_inp == 'D':
            H.Health()

        else:
            Sy.syntax()

Welcome = Start() 
Welcome.begin() # Begins program
