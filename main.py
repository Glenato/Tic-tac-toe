from random import randint

def selected_computer():
    print ("Select computer to play against : ")
    print ("- Basic (chooses the first empty square he sees)")
    print ("- Random (chooses a random square each time)")
    global choosen 
    choosen = input("Choose : ")
    while choosen.lower() not in ("basic", "random"):
        print ("Invalid input, choose basic or random")
        choosen = input("Choose : ")
    choosen = choosen.lower()


def user_input_to_row_and_col(user_input):
    row = int(user_input / 3)
    col = (user_input - (row*3))
    return row, col


def check_if_move_is_valid(row, col):
    if board[row][col] == " ":
        add_users_move_to_board(row, col)
        #print(f"User has played on row {row} and colonne {col}")
        return True
    else:
        print (f"This square is already used.")
        return False

def computer_move():
    if choosen == "basic":
        basic_computer()
    elif choosen == "random":
        random_computer()
            
def basic_computer():
    for i in range(3):
        for x in range (3):
            if board[i][x] == " ":
                board [i][x] = "O"
                return 

def get_num_of_available():
    count = 0
    for i in range (3):
        for x in range (3):
            if board[i][x] == " ":
                count +=1
    return count

def random_computer():
    
    random_num = randint(1, get_num_of_available())
    count = 1
    for i in range (3):
        for x in range (3):
            if board [i][x] == " ":
                if count == random_num:
                    board [i][x] = "O"
                    return 
                else:
                    count+=1

def check_if_won(symbol, user):
    for i in range (3):
        for x in range (3):
            if board[i][x] == symbol:
                if x == 2: 
                    print (f"{user} won")
                    return True
            else:
                break
        for x in range (3):
            if board[x][i] == symbol:
                if x == 2: 
                    print (f"{user} won")
                    return True
            else:
                break
    for i in range (3):
        if board [i][i] == symbol:
            if i == 2:
                return True
        else:
            break
    for i in range (3):
        if board [i][2-i] == symbol:
            if i == 2:
                return True
        else:
            break
    return False

def check_if_board_is_full():
    for i in range (3):
        for x in range (3):
            if board [i][x] == " ":
                return False
    else:
        return True


def add_users_move_to_board(row, col):
    board[row][col] = "X"
    print_board()

def square_of_board(row, col):
    if board[row][col] != " ":
        return board[row][col]
    else:
        return " "  
    
def print_board():
    print()
    for i in range(3):
        print (" ", end = "")
        for x in range (3):
            print (f"{square_of_board(i, x)}", end = " ")
            if x != 2:
                print ("| ", end = "")
        print ()
        if i != 2:
                print ("-"*11)
    print ("")

def reset ():
    print ("\nThe board has been reset")
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]


board = [[" " for _ in range(3)] for _ in range(3)]
selected_computer()
print_board()

while True:
    user_input = input("Give a number : ")
    #and check_if_move_is_valid(user_input)
    try:
        if int(user_input) in range(1,10):
            user_input = int (user_input) -1
            row, col = user_input_to_row_and_col(user_input)
            if check_if_move_is_valid(row, col) == True:
                if check_if_won("X", "User"):
                    print ("Congrats, you have won !")
                    reset()
                    print_board()
                    continue 
                if check_if_board_is_full():
                    print ("It is a Draw")
                    reset()
                    print_board()
                    continue 
                
                print("Computers move :")
                computer_move()
                print_board()

                if check_if_won("O", "Computer"):
                    print ("You have lost...")
                    reset()

            #add_users_move_to_board(user_input)
    except ValueError:
        print ("You have to input a number from 1 to 9 corresponding")
