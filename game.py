import sys
import time


##### Player setup #####


class player:

    def __init__(self):
        player.name = ''
        player.job = ''
        player.location = 'b2'
        player.game_over = False


myPlayer = player()

##### Title screen ######


def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    print('********************************')
    print(' Welcome to my exploration Game ')
    print('********************************')
    print('            -PLAY-         ')
    print('            -HELP-         ')
    print('            -QUIT-         ')
    title_screen_selection()


def help_menu():
    print('**********************')
    print('Welcome to my exploration Game')
    print('**********************')
    print('-Use UP,DOWN,LEFT,RIGHT TO MOVE-')
    print('-TYPE YOUR COMMANDS TO DO THEM-')
    print('-USE "look or examine" TO INSPECT SOMETHING-')
    title_screen_selection()

##### Game Functionality #####


def start_game():
    return
##### MAP #####

""" 
This is the east part of the city Guria.
------------------------------------------
       a1                      a2    
-----------------------------------------------------------------------------------
|   Town Market    |    East Entrance     |    Town Square     |      Church      | a4
-----------------------------------------------------------------------------------
|      Stables     |         Home         |       Tavern       |     Cemetery     | b4
-----------------------------------------------------------------------------------
Have fun in my exploration game
"""


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'Foreign and topical products are sold here. Many people are gathered in here to buy food,flowers and many more.',
        EXAMINATION: 'A gentle smell is spread in the air. A merchant is selling some perfumes and some ladies are around his stock.',
        'UP': '',
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2',
    },
    'a2': {
        ZONENAME: 'East Entrance',
        DESCRIPTION: 'This is one of the 4 entrances of this city.',
        EXAMINATION: '4 soldiers are checking who is entering and who is going out of the city.',
        'UP': '',
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3',
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'This is the central square of this part of the city. Many families are having a walk in the park',
        EXAMINATION: 'You see a couple sitting near the fountain',
        'UP': '',
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4',
    },
    'a4': {
        ZONENAME: 'Church',
        DESCRIPTION: 'The place where everyone come closer to the God',
        EXAMINATION: 'You sit on a bench and hear ',
        'UP': '',
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': '',
    },
    'b1': {
        ZONENAME: 'Stables',
        DESCRIPTION: 'This is the home of the horses in this city',
        EXAMINATION: 'You can count 15 horses in here and at least 10 are out of the building',
        'UP': 'a1',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'b2',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Maybe in the future your can think of a renovation or moving to a new house in the Northern part of the City',
        'UP': 'a2',
        'DOWN': '',
        'LEFT': 'b1',
        'RIGHT': 'b3',
    },
    'b3': {
        ZONENAME: 'Tavern',
        DESCRIPTION: 'The place where all the citizens and foreign merchants are gathered. The home of good music and Ale',
        EXAMINATION: 'You cannot find an empty table at the moment',
        'UP': 'a3',
        'DOWN': '',
        'LEFT': 'b2',
        'RIGHT': 'b4',
    },
    'b4': {
        ZONENAME: 'Cemetery',
        DESCRIPTION: 'The dead of the city rest in this place',
        EXAMINATION: 'You read the writings upon the Tombstones to check out whose grave are you watching to',
        'UP': 'a4',
        'DOWN': '',
        'LEFT': 'b3',
        'RIGHT': '',
    },
}


##### GAME INTERACTIVITY #####
def print_location():
    print('#' + myPlayer.location + '#')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')

def prompt():
    print("\n" + "---------------------")
    print("What do want to do?")
    action = input(">")
    acceptable_actions = ['move', 'go', 'examine',
                          'walk', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action,try again.\n")
        action = input(">")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'walk', 'go']:
        player_move()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        destination = myPlayer.location
        player_examine(destination)


def player_move():
    ask = "Where would you like to go?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location]['UP']
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location]['LEFT']
        movement_handler(destination)
    elif dest in ['east', 'right']:
        destination = zonemap[myPlayer.location]['RIGHT']
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location]['DOWN']
        movement_handler(destination)


def movement_handler(destination):
    print("\n" "You have moved to the " + zonemap[destination][ZONENAME] + ".")
    myPlayer.location = destination
    print_location()


def player_examine(destination):
    print("\n""While you explore......" + zonemap[destination][EXAMINATION] + "." )
    
    
    

##### GAME FUNCTIONALITY #####

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def setup_game():    

##### NAME COLLECTION #####
    question1 = "Hello, please tell me your name \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(">")
    myPlayer.name = player_name

##### JOB-CLASS HANDLING #####
    question2 = "Please tell me your role\n"
    question2added = "(You can be a Merchant, a Priest or a Citizen)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input(">")
    valid_jobs = ['merchant', 'priest', 'citizen']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input(">")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

##### INTRO #####
    question3 = "Welcome, " + player_name + ",the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(">")
    myPlayer.name = player_name

    speech1 = "Welcome to Guria,"
    speech2 = "I hope you like the east part of the city,"
    speech3 = "Just make sure you don't get lost..."
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

    print("Let's start now !")
    main_game_loop()


title_screen()
