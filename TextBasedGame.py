import sys
import time
# Dictionary of areas

rooms = {
    'Main Street': {'North': 'Run Down Burger Shack', 'South': 'Strange Hut', 'East': 'Eerie House',
                    'West': 'Abandoned Motel'},
    'Strange Hut': {'North': 'Main Street', 'East': 'Back Room', 'Item': 'Great Staff'},
    'Back Room': {'West': 'Strange Hut', 'Item': 'Shield'},
    'Abandoned Motel': {'East': 'Main Street', 'Item': 'Roll of Duct Tape'},
    'Run Down Burger Shack': {'South': 'Main Street', 'East': 'Burned Down Car', 'Item': 'Mysterious Burger'},
    'Burned Down Car': {'West': 'Run Down Burger Shack', 'Item': 'Sharp Metal Piece'},
    'Eerie House': {'West': 'Main Street', 'North': 'Red Room', 'Item': 'Flashlight'},
    'Red Room': {'South': 'Eerie House', 'Villain': 'Serial Killer'}
}

full_inventory = ('Great Staff', 'Shield', 'Roll of Duct Tape', 'Mysterious Burger', 'Sharp Metal Piece',
                  'Flashlight')
inventory = set()
# Starting location of the player
location = 'Main Street'
# No direction, will prompt for it
playerMove = ''


#  Function for player winning game
def victory():
    print('You see a deranged man standing in the corner of the room')
    time.sleep(2)
    print('\nHe sees you and begins to approach you\nOut of fear you quickly assemble your items into a weapon')
    time.sleep(2.5)
    print('The serial killer lunges towards you, but you react just in time striking and killing the deranged man')
    time.sleep(3)
    print('\nCongratulations! You successfully gathered all the items and defeated the villain!')
    sys.exit()


#  Function for player losing game
def loser():
    print('You see a deranged man standing in the corner of the room')
    time.sleep(2)
    print('\nHe sees you and begins to approach you\nOut of fear you quickly assemble your items into a weapon')
    time.sleep(2.5)
    print('You realize you did not grab all of the required items and you are frozen with fear')
    time.sleep(2.5)
    print('The Serial Killer lunges and strikes you over the head making you his next victim')
    time.sleep(1.5)
    print('YOU LOSE!\nBetter luck next time!')
    sys.exit()


#  Function to determine if user has required items to continue
def villain(villaininfo):
    boss_fight = input('Face the villain? Y/N').strip().capitalize()
    if boss_fight == 'Y':
        if villaininfo == 'Serial Killer' and len(inventory) == len(full_inventory):
            victory()
        elif villaininfo == 'Serial Killer' and len(inventory) != len(full_inventory):
            loser()
    elif boss_fight == 'N':
        print('You chose not to face the villain')
    else:
        print(f'\033[1;37;40mInvalid input. Choose a possible action\033[1;32;40m')


#  Function to retrieve items and store in inventory
def get_item(locationInfo):
    search = input(f'Search the area? Y/N ').strip().capitalize()
    if search == 'Y':
        print(f"You find a \033[1;31;40m{locationInfo['Item']}\033[1;32;40m  and take it")
        inventory.add(locationInfo.pop('Item'))
    elif search == 'N':
        print('You do not search the area\n')
    else:
        print(f'\033[1;37;40mInvalid input. Choose a possible action\033[1;32;40m')


#  Function to show players location and current inventory
def playerinfo(location, inventory):
    #  Display current inventory and location
    print('Inventory:', inventory)
    print(f"You are at the : \033[1;31;40m{location}\033[1;32;40m")


#  Introduction to the game
while True:
    # Change the color of the text
    print('\n\033[1;32;40mWelcome to the abandoned city of Winchester\n'
          'to win the game you must collect the 6 items and face the \033[1;31;40mSerial Killer\033[1;32;40m')
    play = input('Would you like to explore? y/n: ').strip().capitalize()
    #  Branches to continue with game
    if play == 'Y':
        print('At any point in the game if you would like\n'
              'to quit just type "exit" to exit the game')
        print('Good luck and stay safe!\n')
        time.sleep(2.5)
        break
    elif play == 'N':
        print("Good! You wouldn't survive anyway!")
        sys.exit()
    else:
        print(f'\033[1;37;40mInvalid input\033[1;32;40m')


#  Game Loop
def main():
    while True:
        global location
        playerinfo(location, inventory)
        #  Shows the user possible inputs
        choices = rooms[location].keys()
        print("Possible actions:" + '\033[1;31;40m', {*choices}, '\033[1;32;40m\n')

        #  Ask for user input, strip away whitespace and capitalize input
        playermove = input("What would you like to do? ").strip().capitalize()
        #  Display users move, Change color of text
        print(f'You chose: \033[1;31;40m{playermove}\033[1;32;40m\n')

        #  Call function to pick up the item in th room
        if playermove == 'Item':
            if 'Item' in rooms[location]:
                get_item(rooms[location])
            elif 'Item' not in rooms[location]:
                print(f'\033[1;37;40mThere is no item to retrieve here\033[1;32;40m')
        #  Call function to face the final boss
        elif playermove == 'Villain':
            if 'Villain' in (rooms[location]):
                villain(rooms[location][playermove])
            else:
                print(f'\033[1;37;40mInvalid input. Choose a possible action\033[1;32;40m')
            #  Call function to move between rooms
        elif playermove in rooms[location]:
            location = rooms[location][playermove]
        #  System exit if user inputs 'Exit'
        elif playermove == 'Exit':
            print('You exited the game')
            sys.exit()

        #  input validation
        elif 'Item' or 'Exit' or 'Villain' or choices != playermove:
            print(f'\033[1;37;40mInvalid input. Choose a possible action\033[1;32;40m')


main()
