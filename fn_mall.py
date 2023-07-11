import datetime
import pickle

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

print("-----------------------------------------")
print("WELCOME TO MIND-BLOWING MALL")
print("-----------------------------------------")

# Assigning global variables
game_zone = 0
outfit = 0
gadget = 0
grocery = 0
b = {
    "First_Floor": [],
    "Second_Floor": [],
    "Third_Floor": [],
    "Fourth_Floor": []
}

# Function for 4th floor
def game_zone1(game_zone):
    print("Welcome to the Game Zone.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        try:
            game = input('''1. 8 BALL POOL           [Rs100/-]
2. BALLING               [Rs101/-]
3. FIFA 18               [Rs99/-]
4. CoD WW2               [Rs79/-]
5. ARM WRESTLING         [Rs20/-]
[Don't want to play? Type 'exit', 'q', or 'quit'.]
Which game do you want to play? ''')
            if game == "1":
                game_zone += 100
                b["Fourth_Floor"].append("8 BALL POOL                 [Rs100/-]")
            elif game == "2":
                game_zone += 101
                b["Fourth_Floor"].append("BALLING                          [Rs101/-]")
            elif game == "3":
                game_zone += 99
                b["Fourth_Floor"].append("FIFA 18                             [Rs99/-]")
            elif game == "4":
                game_zone += 79
                b["Fourth_Floor"].append("CoD WW2                      [Rs79/-]")
            elif game == "5":
                game_zone += 20
                b["Fourth_Floor"].append("ARM WRESTLING         [Rs20/-]")
            elif game.lower() in ("exit", "q", "quit"):
                break
            else:
                print("There are no more games available other than those above.")
            ans = input("Would you like to play other games? (y/n) ")
        except Exception as e:
            print(e)
    return game_zone

# Function for 2nd floor
def outfit1(outfit):
    print("Welcome to the Outfit Zone.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        try:
            game = input('''1. SHIRT                [Rs800/-]
2. PANT                 [Rs1200/-]
3. SHOCKS               [Rs100/-]
4. HAND GLOVES          [Rs180/-]
5. SWEATER              [Rs1999/-]
[Don't want to buy? Type 'exit', 'q', or 'quit'.]
Which item do you want to buy? ''')
            if game == "1":
                outfit += 800
                b["Second_Floor"].append("1. SHIRT                             [Rs800/-]")
            elif game == "2":
                outfit += 1200
                b["Second_Floor"].append("2. PANT                              [Rs1200/-]")
            elif game == "3":
                outfit += 100
                b["Second_Floor"].append("3. SHOCKS                            [Rs100/-]")
            elif game == "4":
                outfit += 180
                b["Second_Floor"].append("4. HAND GLOVES                       [Rs180/-]")
            elif game == "5":
                outfit += 1999
                b["Second_Floor"].append("5. SWEATER                           [Rs1999/-]")
            elif game.lower() in ("exit", "q", "quit"):
                break
            else:
                print("There are no more items available other than those above.")
            ans = input("Would you like to purchase more from this Outfit Zone? (y/n) ")
        except Exception as e:
            print(e)
    return outfit

# Function for 3rd floor
def gadget1(gadget):
    print("Welcome to the Electronic Shop.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        try:
            game = input('''1. PHONE              [Rs10000/-]
2. LAPTOP             [Rs56000/-]
3. TELEVISION         [Rs7500/-]
4. WATCH              [Rs2000/-]
5. KEYBOARD           [Rs200/-]
[Don't want to buy? Type 'exit', 'q', or 'quit'.]
Which item do you want to buy? ''')
            if game == "1":
                gadget += 10000
                b["Third_Floor"].append("1. PHONE                  [Rs10000/-]")
            elif game == "2":
                gadget += 56000
                b["Third_Floor"].append("2. LAPTOP                 [Rs56000/-]")
            elif game == "3":
                gadget += 7500
                b["Third_Floor"].append("3. TELEVISION             [Rs7500/-]")
            elif game == "4":
                gadget += 2000
                b["Third_Floor"].append("4. WATCH                  [Rs2000/-]")
            elif game == "5":
                gadget += 200
                b["Third_Floor"].append("5. KEYBOARD               [Rs200/-]")
            elif game.lower() in ("exit", "q", "quit"):
                break
            else:
                print("There are no more items available other than those above.")
            ans = input("Would you like to purchase more from this Electronic Shop? (y/n) ")
        except Exception as e:
            print(e)
    return gadget

# Function for 1st floor
def grocery1(grocery):
    print("Welcome to the Grocery Shop.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        try:
            game = input('''1. SUGAR                [Rs44/- per kg]
2. RICE                 [Rs20/- per kg]
3. OIL                  [Rs165/- per liter]
4. WHEAT FLOUR          [Rs25/- per kg]
5. SALT                 [Rs28/- per kg]
[Don't want to buy? Type 'exit', 'q', or 'quit'.]
Which item do you want to buy? ''')
            if game == "1":
                grocery += 44
                b["First_Floor"].append("1. SUGAR                            [Rs44/- per kg]")
            elif game == "2":
                grocery += 20
                b["First_Floor"].append("2. RICE                             [Rs20/- per kg]")
            elif game == "3":
                grocery += 165
                b["First_Floor"].append("3. OIL                              [Rs165/- per liter]")
            elif game == "4":
                grocery += 25
                b["First_Floor"].append("4. WHEAT FLOUR                      [Rs25/- per kg]")
            elif game == "5":
                grocery += 28
                b["First_Floor"].append("5. SALT                             [Rs28/- per kg]")
            elif game.lower() in ("exit", "q", "quit"):
                break
            else:
                print("There are no more items available other than those above.")
            ans = input("Would you like to purchase more from this grocery shop? (y/n) ")
        except Exception as e:
            print(e)
    return grocery

# Function for bill amount
def billamt(grocery, outfit, gadget, game_zone):
    Totalamt = grocery + outfit + gadget + game_zone
    bill = '''-----------------------------------------
                 BILL
-----------------------------------------
1. Your purchase amount from 1st floor = {}
2. Your purchase amount from 2nd floor = {}
3. Your purchase amount from 3rd floor = {}
4. Your purchase amount from 4th floor = {}
5. Grand Total Amount = Rs{}
Date and Time: {}'''.format(b["First_Floor"], b["Second_Floor"], b["Third_Floor"], b["Fourth_Floor"], Totalamt, formatted_datetime)

    with open(f"bill_records_{formatted_datetime}.pickle", "wb") as file:
        pickle.dump(bill, file)

# Function for returning items
def returning(grocery, outfit, gadget):
    ans = "y"
    while ans == "y" or ans == "Y":
        try:
            floor = int(input('''This is the return section.
1. Grocery Shop
2. Cloth Shop
3. Electronic Shop
Enter the floor number you want to return items from: '''))
            if floor == 1:
                print("{}\n".format(b["First_Floor"]))
                r = int(input("Enter the item number to return: "))
                if r in range(1, len(b["First_Floor"]) + 1):
                    item = b["First_Floor"][r - 1]
                    if item.startswith("1. SUGAR"):
                        grocery -= 44
                        b["First_Floor"].remove(item)
                    elif item.startswith("2. RICE"):
                        grocery -= 20
                        b["First_Floor"].remove(item)
                    elif item.startswith("3. OIL"):
                        grocery -= 165
                        b["First_Floor"].remove(item)
                    elif item.startswith("4. WHEAT FLOUR"):
                        grocery -= 25
                        b["First_Floor"].remove(item)
                    elif item.startswith("5. SALT"):
                        grocery -= 28
                        b["First_Floor"].remove(item)
                    else:
                        print("Error! Item not found.")
                else:
                    print("Error! Invalid item number.")
            elif floor == 2:
                print("{}\n".format(b["Second_Floor"]))
                r = int(input("Enter the item number to return: "))
                if r in range(1, len(b["Second_Floor"]) + 1):
                    item = b["Second_Floor"][r - 1]
                    if item.startswith("1. SHIRT"):
                        outfit -= 800
                        b["Second_Floor"].remove(item)
                    elif item.startswith("2. PANT"):
                        outfit -= 1200
                        b["Second_Floor"].remove(item)
                    elif item.startswith("3. SHOCKS"):
                        outfit -= 100
                        b["Second_Floor"].remove(item)
                    elif item.startswith("4. HAND GLOVES"):
                        outfit -= 180
                        b["Second_Floor"].remove(item)
                    elif item.startswith("5. SWEATER"):
                        outfit -= 1999
                        b["Second_Floor"].remove(item)
                    else:
                        print("Error! Item not found.")
                else:
                    print("Error! Invalid item number.")
            elif floor == 3:
                print("{}\n".format(b["Third_Floor"]))
                r = int(input("Enter the item number to return: "))
                if r in range(1, len(b["Third_Floor"]) + 1):
                    item = b["Third_Floor"][r - 1]
                    if item.startswith("1. PHONE"):
                        gadget -= 10000
                        b["Third_Floor"].remove(item)
                    elif item.startswith("2. LAPTOP"):
                        gadget -= 56000
                        b["Third_Floor"].remove(item)
                    elif item.startswith("3. TELEVISION"):
                        gadget -= 7500
                        b["Third_Floor"].remove(item)
                    elif item.startswith("4. WATCH"):
                        gadget -= 2000
                        b["Third_Floor"].remove(item)
                    elif item.startswith("5. KEYBOARD"):
                        gadget -= 200
                        b["Third_Floor"].remove(item)
                    else:
                        print("Error! Item not found.")
                else:
                    print("Error! Invalid item number.")
            else:
                print("You can only return items from floors 1 to 3. Please enter a valid floor number.")
            ans = input("Do you want to visit other floors to return your purchased items? (y/n) ")
        except Exception as e:
            print(e)
    billamt(grocery, outfit, gadget, game_zone)

# Entry of the mall
ans = "y"
while ans == "y" or ans == "Y":
    try:
        floor = int(input('''1. Grocery Shop
2. Cloth Shop
3. Electronic Shop
4. Game Zone
Enter the floor number you want to go: '''))
        if floor == 1:
            grocery = grocery1(grocery)
        elif floor == 2:
            outfit = outfit1(outfit)
        elif floor == 3:
            gadget = gadget1(gadget)
        elif floor == 4:
            game_zone = game_zone1(game_zone)
        else:
            print("There is no floor above the 4th floor. Please enter a number from 1 to 4.")
        ans = input("Do you want to visit other floors? (y/n) ")
    except Exception as e:
        print(e)

# Calling function to return purchased items
try:
    a = input("Do you want to return your purchased items? (y/n) ").lower()
    if a == "y":
        returning(grocery, outfit, gadget)
    elif a == "n":
        # Calling function to show the bill
        billamt(grocery, outfit, gadget, game_zone)
    else:
        print("Error! Please restart the program and type either 'y' or 'n'.")
except Exception as e:
    print(e)
