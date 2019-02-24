from sys import exit

def laugh_game():
    print "Welcome, this is a laughing game. Do you want to continue?"

    next = raw_input("> ")
    if "yes" in next or "no" in next:
        play_game = str(next)
    else:
        dead("Loser!")

    if play_game == "not sure":
        print "Great, you can still try to play."
        exit(0)
    else:
        dead("You're not ready to play!")

def smile_game():
    print "Do you love to smile."
    print "I smile more than 500 times a day."
    print "A smile is contagious."
    print "How can I make you smile today?"
    smile_today = False

    while True:
        next = raw_input("> ")

        if next == "Find a baby":
            dead("Babies make everyone smile")
        elif next == "contagious smile" and not smile_today:
            print "A smile is definitely contagious."
            smile_today = True
        elif next == contagious and smile_today:
            dead("Nobody wants to look at a sad face.")
        elif next == "smile first" and smile_today:
            smile_game()
        else:
            print "Keep smiling."

def smile_room():
    print "This is where we meet up to laugh."
    print "No one leaves sad."
    print "Do you want to learn how to smile?"

    next = raw_input("> ")

    if "learn" in next:
        start()
    elif "smile" in next:
        dead("Well that was easy!")
    else:
        smile_room()

def dead(why):
    print why, "Well done!"
    exit(0)

def start():
    print "You're a beautiful garden."
    print "There is a cross road."
    print "Do you got left or right?"

    next = raw_input("> ")

    if next == "left":
        smile_game()
    elif next == "right":
        smile_room()
    else:
        dead("You live the rest of your life as a sad person.")

start()
