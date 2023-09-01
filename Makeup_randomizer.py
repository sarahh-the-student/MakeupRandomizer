#Using OOP to create a program that will randomize my makeup looks

#Things needed for input: weather, season, eye look (y/n), lip gloss colour, type
# eye-liner, time of day, time we have to do makeup, foundation (y/n)
# if eye_look: colours needed,
# optional: event (class/party/coffee), colour of outfit
#optional: blush (y/n), glowy or matte

print("Heyyyy, welcome to your makeup randomizer! \n We are currently in the testing phases of thingsss so lets see if this works.")
options = int(input("Please type 1 to try inputting the Makeup Looks. Type 2 to try get a response. Type 3 to try something else (dont do this!)"))



class MakeupLooks:



    #constructor for the makeup feautures I believe are most mandatory: eye look, type, weather, season, lip gloss colour and aesthetic

    def __init__(self, type = str, eye_look = str, weather = str, season = int or str, lipGlossColour = str, aesthetic = str):

        #convert user input into what we want printed in the summary, this will also help us when we implement the pictures

        #makeup type, Glowy or Matte
        if type == 'G':
            self.type = "Glowy"
        elif type == 'M':
            self.type = "Matte"
        else:

        #TODO : figure out if we having the program just take the answer if they type foolishness or loop around until they do something sensible
        #consider throwing errors. How does that work?? Does it avoid the runtime of loops??
        #TODO: find out how throwing errors works lmao
            print("That is not an acceptable makeup type babes.")
            self.type = type
        
        #boolean logic, so simple and sexy. Too bad we have to consider too many letters and stuff can confuse user. hmm do we want a web dev or some kind of UX
        #for this. UX may be needed very much to avoid confusion

        #eye look, yes or no
        if eye_look == 'N':
            self.eye_look = "No eye look"
        elif eye_look == 'Y':
            self.eye_look = "to have an eye look."
        else:
            #again consider either throwing error or looping through non-sense
            self.eye_look = eye_look

        #yess int logic, also so simple but not as sexy as i would like. In an ideal world we would have pics but that sounds yucky

        #season, 1- Summer, 2- Winter, 3-Spring, 4- Fall
        if season == 1:
            self.season = "Summer"
        elif season == 2:
            self.season = "Winter"
        elif season == 3:
            self.season = "Spring"
        elif season == 4:
            self.season = "Fall"
        else:
            #They cant pick again as yet but error is needed
            print("Please pick again. 1 for Summer, 2 for Winter, 3 for Spring or 4 for Fall.")
            self.season = season

        #weather, S- Sunny, O - Overcast, R - rainy, B - Breezy
        if weather == 'S':
            self.weather = 'Sunny'
        elif weather == 'O':
            self.weather = 'Overcast'
        elif weather == 'R':
            self.weather = 'Rainy'
        elif weather == 'B':
            self.weather = 'Breezy'
        else:
            self.weather = weather

        #lip gloss colour, C- Clear, P -Pink, R - Red, B- Brown
        if lipGlossColour == 'C':
            self.lipGlossColour = 'Clear'
        elif lipGlossColour == 'P':
            self.lipGlossColour = 'Pink'
        elif lipGlossColour == 'R':
            self.lipGlossColour = 'Red'    
        elif lipGlossColour == 'B':
            self.lipGlossColour = 'Brown'
        else:
            self.lipGlossColour = lipGlossColour

        #aesthetic, S - Soft Girl, N - No Makeup, I- Intimidating
        if aesthetic == 'S':
            self.aesthetic = 'Soft Girl'
        elif aesthetic == 'N':
            self.aesthetic = 'No-Makeup'
        elif aesthetic == 'I':
            self.aesthetic = 'Intimidating'
        else:
            self.aesthetic = aesthetic

    #printing the summary of your makeup look:

    def makeup_summary(self):
        self.my_name = "Sarah"
        print(f"Hello {self.my_name}! Your makeup look today is {self.type} and {self.aesthetic} aesthetic. You chose {self.eye_look}, with {self.lipGlossColour} lip gloss.")
        print(f"Your influences were the {self.weather} weather and the {self.season} season.")

#inputting everything in the makeup looks class 
type = input("What type of makeup are we wearing today Bestie? Glowy (G) or Matte (M)" )
eye_look = input("Are we going eye look or not? (Y/N)")
weather = input("Is it Sunny (S), Over-cast (O), Rainy (R) or Breezy? (B) ")
season = int(input("What season are we in girlie? Summer, Winter, Spring or Fall. Enter 1 for Summer, 2 for Winter, 3 for Spring or 4 for Fall."))
lipGlossColour = input("What colour gloss are we going for? Clear (C), Pink (P), Red (R) or Brown (B)")
aesthetic = input("What's our aesthetic sis? Soft girl (S), No-Makeup (N) or Intimidating? (I)")

my_makeup = MakeupLooks(type, eye_look, weather, season, lipGlossColour, aesthetic)
my_makeup.makeup_summary()
    


class Response:  

    def __init__(self, wear_foundation, type):
        self.wear_foundation = wear_foundation
        self.type = type

    def is_wearing_foundation(self):
        if self.wear_foundation == False:
            print("Today you are not wearing foundation")
        print( "Today you are wearing foundation")
    
    
    def get_type(self):
        return self.type

    
class OptionalMakeup:

    def __init__(self):
        self.blush = True
    
    def event(self):
        print("What is the event for this look? Average day of class, Party, Ice-cream??")
    

'''
makeup_type = MakeupLooks("Glowy", "natural")
no_foundation = Response(False, "glowy")
print(no_foundation.is_wearing_foundation())
no_foundation.makeup_summary()
'''