from turtle import position

from IPython.display import clear_output

game_list=[0,1,2]

def display_game(game_list):
    print("Here is the current list")
    print(game_list)
display_game(game_list)

def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=input('Please enter a position to replace: ')
        if choice not in ['0','1','2']:
            print("Please enter a valid choice (0,1,2)")
    return int(choice)

def replacement_choice(game_list,position):
    user_placement=input('Type a string to place at the position: ')
    game_list[position]=user_placement
    return game_list

def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input('Keep Playing Y or N?: ')
    if choice=='Y':
        return True
    else:
        return False

game_on=True

while game_on:
    
    position=position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    clear_output()
    
    display_game(game_list)
    
    game_on = gameon_choice()





