import random
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 250) #speed of the bot speaking

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def lose_saying():
    lose = ["Consider this a minor setback. The real battle lies ahead, and I will not be merciful!", "Your victory is but a drop in the ocean of despair I will unleash upon you!", "You may have won this battle, but the war is far from over. Prepare for your reckoning!", "Hmph, luck was on your side this time. Don't expect it to last!", "This victory means nothing. The darkness within me grows stronger with each passing moment!", "Enjoy your fleeting victory, for the storm of my vengeance approaches!"]
    ch = random.choice(lose)
    # print(ch)
    speak(ch)

def win_saying():
    win = ["Ha! Your feeble attempts are no match for my superiority!", "Bow before me, for I am the master of this domain!", "You are but a pawn in my game, destined to lose at every turn!", "Pathetic. Is this the best you can muster against my might?", "Your defeat is inevitable, as inevitable as the rising of the sun!", "You thought you could challenge me? Foolish mortal, you stand no chance!", "Your struggle amuses me, but it will ultimately end in despair!", "Witness the futility of your efforts! Victory is within my grasp, and you are powerless to stop it!"]
    ch = random.choice(win)
    # print(ch)
    speak(ch)

def lost():
    ch = "Impossible... this cannot be! You may have won this time, but mark my words, I will return stronger than ever!"
    # print(ch)
    speak(ch)

def win():
    ch = "Your feeble attempts were futile. Remember this defeat you little peasant"
    # print(ch)
    speak(ch)

ch = 'YES'
Op = ['Rock', 'Paper', 'Scissors']
print("")
print("Lets play a game of Rock, Paper, Scissors")
print("Rules are simple... make a choice between Rock Paper Scissors.. against the computer")
print("First one to score a total of 3 points wins")
print("--------USE HEADPHONES FOR BETTER EXPERIENCE--------")
print("Ready or not here you go!!!")

while ch == 'YES' or ch == 'yes' or ch == 'Yes' or ch == '1':
    user_score = 0
    comp_score = 0
    while user_score<3 and comp_score<3:
        print("")
        print("------Current Score------")
        print("User : {}  |  Computer : {}".format(user_score, comp_score))
        user_choice = input("Your Turn: ")
        # user_choice.strip()
        user_choice = user_choice.title()
        if user_choice == 'Scissor':
            user_choice = 'Scissors'

        if user_choice != 'Rock' and user_choice != 'Paper' and user_choice != 'Scissors':
            print("Enter a valid choice")
            continue

        comp_choice = random.choice(Op)
        print("Computer's Turn:- {}".format(comp_choice))
        
        if user_choice == comp_choice:
            print("Tie")

        elif user_choice == 'Rock' and comp_choice == 'Paper':
            print("🪨       📃")
            print("Computer Points +1")
            win_saying()
            comp_score+=1

        elif user_choice == 'Rock' and comp_choice == 'Scissors':
            print("🪨       ✂️")
            print("User Points +1")
            lose_saying()
            user_score+=1

        elif user_choice == 'Paper' and comp_choice == 'Scissors':
            print("📃       ✂️")
            print("Computer Points +1")
            win_saying()
            comp_score+=1

        elif user_choice == 'Paper' and comp_choice == 'Rock':
            print("📃       🪨")
            print("User Points +1")
            lose_saying()
            user_score+=1

        elif user_choice == 'Scissors' and comp_choice == 'Paper':
            print("✂️       📃")
            print("User Points +1")
            lose_saying()
            user_score+=1

        elif user_choice == 'Scissors' and comp_choice == 'Rock':
            print("✂️       🪨")
            print("Computer Points +1")
            win_saying()
            comp_score+=1

    print("")
    print("------Current Score------")
    print("User : {}  |  Computer : {}".format(user_score, comp_score))
    if user_score == 3:
        print("User Won!!")
        lost()
    elif comp_score == 3:
        print("Computer Won!!\nBetter Luck Next Time :)")
        win()
    

    print("")
    ch = input("Do you want to play again?: ")

print("")
print("Thank you for playing!!")
print("GoodBye ;)")

