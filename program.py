import random

print('----------------------------------------')
print('         A QUEST FOR AN INT             ')
print('----------------------------------------'+ "\n")

print("The Quest: you must find an Int, a close relative of the Ent, in the Dark Forest." + "\n")

that_number = random.randint(0, 10)
user_guess = -1

you_shall_not_pass = ["Sauron", "Saruman", "Gollum"] #names that are not permitted to play
user_name = input("Every hero must have a name! What is yours? ")

if user_name not in you_shall_not_pass:
    user_quest_response = input ("Will you accept this quest, " + user_name + "? ")
    if user_quest_response == "Yes":
        print("May the winds be in your favor, " + user_name +".")
    elif user_quest_response == "No":
        print("I will wait for another brave soul. Leave me in peace, " + user_name + ".")
    else:
        print("I don't understand these words you speak - give me a simple yes or no.")
    while user_guess != that_number:
        guess_text = input('Find the int between trees 0 and 10: ')
        user_guess = int(guess_text)
        if that_number < user_guess:
            print("I am a helpful forest sprite - your guess of {} was too high, {}!".format(user_guess, user_name))
        elif that_number > user_guess:
            print("I am a helpful forest sprite - your guess of {} was too low, {}!".format(user_guess, user_name))
        else:
            print("You have found the Int!" + "\n" + "Your journey is over." "\n" + "I am eternally grateful.")
else:
    print(user_name + " is not allowed in the Dark Forest. And now, I banish you forever!")


