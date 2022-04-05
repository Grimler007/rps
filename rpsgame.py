import random
import time
# start screen
print("--------------------------------------------------------------------")
print("|  Welcome to Rock, Paper, Scissors                                |")
print("|          The rules are quiete simple                             |")
print("|  Paper beats rock.                                               |")
print("|              Rock beats Scissors                                 | ")
print("|                         Scissors beats paper                     |")
print("|                                                                  |")
print("|                                                                  |")
print("|  Press 1: Rock                                                   |")
print("|  Press 2: Paper                                                  |")
print("|  Press 3: Scissors                                               |")
print("|                                                                  |")
print("--------------------------------------------------------------------")
# player input options
while True:
    choice = input("What is your Move? \n Press: 1 for Rock \n Press: 2 for Paper \n Press: 3 for Scissors \n You selected: ")
    if choice == "1":
        choice_name = "Rock"
        choice_value = 1
        print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                         @
@                                                         @
@                                          88             @
@        8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8       @
@        88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"        @
@        88         8b       d8 8b         8888[          @
@        88         "8a,   ,a8" "8a,   ,aa 88`"Yba,       @ 
@        88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a      @
@                                                         @
@        You chose rock. You seem bolder than most.       @
@                                                         @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
        time.sleep(2)


    elif choice == "2":
        choice_name = "Paper"
        choice_value = 2
        print('''
#######################################################################
#                                                                     #
#        8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,     #
#       88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8      #
#       88       d8 ,adPPPPP88 88       d8 8PP""""""" 88              #
#       8b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88               #
#       88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88              #
#       88                     88                                     #
#       88                     88                                     #
#                                                                     #
#            You chose Paper! Don't worry it's card-stock             #
#                                                                     #
# #####################################################################  
                                                                        ''')

        time.sleep(2)


    elif choice == "3":
        choice_name = "Scissors"
        choice_value = 3
        print('''
 -----------------------------------------------------------
|                        _    _                            |
|                       (_)  / )                           |
|                         | (_/                            |
|                         _+/                              |
|                        //|\                              |
|                       // | )                             |
|                      (/  |/                              |
|                                                          |
|   You Chose Scissors! Try not to run with them.          |
------------------------------------------------------------  ''')
        time.sleep(2)

# FIX THIS TOMORROW 
    else:
        print('''
        
################################################################
## #############################################################
####                                                        ####
####                           ________                     #### 
####                        _jgN########Ngg_                ####
####                    _N##N@@""  ""9NN##Np_               ####
####                    d###P            N####p             ####
####                    "^^"              T####             #### 
####                                      d###P             ####
####                                   _g###@F              ####
####                                   _gN##@P              ####
####                                  gN###F"               ####
####                                d###F                   ####
####                                0###F                   ####
####                              0###F                     ####
####                             0###F                      ####
####                            "NN@'                       ####
####                                                        ####
####                             ___                        ####
####                           q###r                        ####
####                            ""                          ####
####                                                        ####
####                                                        ####
####             That wasn't even an option                 #### 
################################################################   
# ##############################################################''')
    time.sleep(2)
    

# computer chooses random int between 1 and 3 

    print(''' 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                                               @
@    ,----------------------------------------------------,     @
@    | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |     @
@    |                                                    |     @
@    |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |     @
@    |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |     @
@    | [][_][][][][][][][][][][][][]||     []    [][][][] |     @
@    | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |     @
@    |   [__][________________][__]              [__][]|| |     @
@    `----------------------------------------------------'     @
@                                                               @
@                The Computer will now Choose                   @
@                                                               @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ''')
    time.sleep(2)
    comp_choice = random.randint(1, 3)
     
    
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
 
    # computer choice is given value
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

# define match up         
    print(f'''
############################################
                                          
  Computer selected: {comp_choice_name}  
       You selected: {choice_name}        
                                          
############################################''')
    time.sleep(1.5)
   

# rock logic
    if choice_value == 1 and comp_choice == 2:
        print('''
#####################################
#                                   #
#   Paper covers rock. You loose    #
#                                   #
#####################################''')
        

    elif choice_value == 1 and comp_choice == 1:
        print(''' 
######################################
#                                    #
#   Rock smashes into Rock. You Tie  # 
#                                    #
###################################### ''')
       

    elif choice_value == 1 and comp_choice ==3:
        print('''
#######################################
#                                     #
#    Rock breaks Scissors You Win!    #
#                                     #  
#######################################''')


# paper logic
    elif choice_value ==2 and comp_choice == 1:
        print('''
######################################
#                                    #
#   Paper Covers Rock: You Win!      # 
#                                    #
######################################''')


    elif choice_value == 2 and comp_choice == 2:
        print('''
 
######################################
#                                    #
#   Paper Covers Paper: You Tie!     # 
#                                    #
###################################### ''')


    elif choice_value == 2 and comp_choice == 3:
        print('''
######################################
#                                    #
#   Scissors Cuts Paper: You Lose    # 
#                                    #
######################################''')


# scissors logic
    elif choice_value == 3 and comp_choice == 1:
        print('''
######################################
#                                    #
#   Rock Smashes Paper: You lose!    # 
#                                    #
######################################''')
        

    elif choice_value == 3 and comp_choice == 2:
        print('''
######################################
#                                    #
#   Scissors Cuts Paper: You Win!    # 
#                                    #
######################################''')
       

    elif choice_value == 3 and comp_choice == 3:
        print('''
######################################
#                                    #
#   Scissors do nothing to Scissors: #
#           You Tie                  # 
#                                    #
######################################''')
       

    # exit or restart
    print('''
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&                                 &
&  Would you like to play again?  &
&             Yes or No           &
&                                 &
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&''')
    ans = input()
    if ans == "No" or ans == "NO" or ans == "no" or ans =="nO" :
        print('''
        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                 _                         @ 
@                /(|                        @
@               (  :                        @
@              __\  \  _____                @
@             (____)  `|                    @
@            (____)|   |                    @
@             (____).__|                    @
@              (___)__.|_____               @
@                                           @
@             Thanks for Playing!           @
@                                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')
        time.sleep(5)
        break
     
    