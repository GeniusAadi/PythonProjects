#Mind Blowing Mall Bill System
print("-----------------------------------------")
print("WELL COME TO MIND BLOWING MALL")
print("-----------------------------------------")
#assigning global variables
game_zone=0
outfit=0
gadget=0
grocery=0
b={"First_Floor" : [],"Second_Floor" : [],"Third_Floor" : [],"Fourth_Floor" : []}
#function for 4th floor
def game_zone1(game_zone):
    print("Well Come To Game Zone.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        game = input('''1.for 8 BALL POOL           [Rs100/-]
2.for BALLING               [Rs101/-]
3.for FIFA 18               [Rs99/-]
4. for CoD WW2              [Rs79/-]
5.for ARM WRESTLING         [Rs20/-]
[Don't want to play then type (exit,q or quit).]
You want to play=''')
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
        elif game in ("exit","Exit","EXIT","q","Quit","QUIT","quit"):
            break
        else:
            print("There's no more games rather than those above.")
        ans = input("Would you like to play other games?(y/n)")
    return game_zone
#function for 2nd floor
def outfit1(outfit):
    print("Well Come To Outfit Zone.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        game = input('''1.for SHIRT                [Rs800/-]
2.for PANT                 [Rs1200/-]
3.for SHOCKS               [Rs100/-]
4. for HAND GLOVES         [Rs180/-]
5.for SWEATER              [Rs1999/-]
[Don't want to buy then type (exit,q or quit).]
You want to buy=''')
        if game == "1":
            outfit += 800
            b["Second_Floor"].append("1.SHIRT                             [Rs800/-]")
        elif game == "2":
            outfit += 1200
            b["Second_Floor"].append("2.PANT                              [Rs1200/-]")
        elif game == "3":
            outfit += 100
            b["Second_Floor"].append("3.SHOCKS                        [Rs100/-]")
        elif game == "4":
            outfit += 180
            b["Second_Floor"].append("4.HAND GLOVES         [Rs180/-]")
        elif game == "5":
            outfit += 1999
            b["Second_Floor"].append("5.SWEATER                      [Rs1999/-]")
        elif game in ("exit","Exit","EXIT","q","Quit","QUIT","quit"):
            break
        else:
            print("There's no more items rather than those above.")
        ans = input("Would you like to purchase more from this Outfit Zone?(y/n)")
#Returning process of outfit zone
    pr = input("Do you want to return your purchased item from this Outfit Zone?(y/n)")
    if pr == "y":
        r = int(input("{}\nEnter the item no. to return= ".format(b["Second_Floor"])))
        if r == 1:
            outfit -= 800
            b["Second_Floor"].remove("1.SHIRT                             [Rs800/-]")
        elif r == 2:
            outfit -= 1200
            b["Second_Floor"].remove("2.PANT                              [Rs1200/-]")
        elif r == 3:
            outfit -= 100
            b["Second_Floor"].remove("3.SHOCKS                        [Rs100/-]")
        elif r == 4:
            outfit -= 180
            b["Second_Floor"].remove("4.HAND GLOVES         [Rs180/-]")
        elif r == 5:
            outfit -= 1999
            b["Second_Floor"].remove("5.SWEATER                      [Rs1999/-]")
        else:
            r = int(input("Error! Item out of the list.Please enter correct item no. = "))
    elif pr == "n":
        ans = input("Would you like to purchase more from this Outfit Zone?(y/n)")
    else:
        pr = input("Please type either y or n. ")
    return outfit
#function for 3rd floor
def gadget1(gadget):
    print("Well Come To Electronic Shop.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        game = input('''1.for PHONE              [Rs10000/-]
2.for LAPTOP             [Rs56000/-]
3.for TELEVISION         [Rs7500/-]
4. for WATCH             [Rs2000/-]
5.for KEYBOARD           [Rs200/-]
[Don't want to buy then type (exit,q or quit).]
You want to buy=''')
        if game == "1":
            gadget += 10000
            b["Third_Floor"].append("1.PHONE                  [Rs10000/-]")
        elif game == "2":
            gadget += 56000
            b["Third_Floor"].append("2.LAPTOP                 [Rs56000/-]")
        elif game == "3":
            gadget += 7500
            b["Third_Floor"].append("3.TELEVISION         [Rs7500/-]")
        elif game == "4":
            gadget += 2000
            b["Third_Floor"].append("4.WATCH                [Rs2000/-]")
        elif game == "5":
            gadget += 200
            b["Third_Floor"].append("5.KEYBOARD          [Rs200/-]")
        elif game in ("exit","Exit","EXIT","q","Quit","QUIT","quit"):
            break
        else:
            print("There's no more items rather than those above.")
        ans = input("Would you like to purchase more from this Electronic Shop?(y/n)")
#Returning process of gadget zone
    pr = input("Do you want to return your purchased item from this Electronic Shop?(y/n)")
    if pr == "y":
        r = int(input("{}\nEnter the item no. to return= ".format(b["Third_Floor"])))
        if r == 1:
            gadget -= 10000
            b["Third_Floor"].remove("1.PHONE                  [Rs10000/-]")
        elif r == 2:
            gadget -= 56000
            b["Third_Floor"].remove("2.LAPTOP                 [Rs56000/-]")
        elif r == 3:
            gadget -= 7500
            b["Third_Floor"].remove("3.TELEVISION         [Rs7500/-]")
        elif r == 4:
            gadget -= 2000
            b["Third_Floor"].remove("4.WATCH                [Rs2000/-]")
        elif r == 5:
            gadget -= 200
            b["Third_Floor"].remove("5.KEYBOARD          [Rs200/-]")
        else:
            r = int(input("Error! Item out of the list.Please enter correct item no. = "))
    elif pr == "n":
        ans = input("Would you like to purchase more from this Electronic Shop?(y/n)")
    else:
        pr = input("Please type either y or n. ")
    return gadget
#function for 1st floor
def grocery1(grocery):
    print("Well Come To Grocery Shop.")
    ans = "Y"
    while ans == "y" or ans == "Y":
        game = input('''1.for SUGAR                [Rs44/- per kg]
2.for RICE                 [Rs20/- per kg]
3.for OIL                  [Rs165/- per Litre]
4. for WHEAT FLOUR         [Rs25/- per kg]
5.for SALT                 [Rs28/- per kg]
[Don't want to buy then type (exit,q or quit).]
You want to buy= ''')
        if game == "1":
            grocery += 44
            b["First_Floor"].append("1.SUGAR                           [Rs44/- per kg]")
        elif game == "2":
            grocery += 20
            b["First_Floor"].append("2.RICE                                [Rs20/- per kg]")
        elif game == "3":
            grocery += 165
            b["First_Floor"].append("3.OIL                               [Rs165/- per Litre]")
        elif game == "4":
            grocery += 25
            b["First_Floor"].append("4.WHEAT FLOUR         [Rs25/- per kg]")
        elif game == "5":
            grocery += 28
            b["First_Floor"].append("5.SALT                               [Rs28/- per kg]")
        elif game in ("exit","Exit","EXIT","q","Quit","QUIT","quit"):
            break
        else:
            print("There's no more items rather than those above.")
        ans = input("Would you like to purchase more from this grocery shop?(y/n)")
#Returning process of grocery shop
    pr = input("Do you want to return your purchased item from this grocery shop?(y/n)")
    if pr == "y":
        r = int(input("{}\nEnter the item no. to return= ".format(b["First_Floor"])))
        if r == 1:
            grocery -= 44
            b["First_Floor"].remove("1.SUGAR                           [Rs44/- per kg]")
        elif r == 2:
            grocery -= 20
            b["First_Floor"].remove("2.RICE                                [Rs20/- per kg]")
        elif r == 3:
            grocery -= 165
            b["First_Floor"].remove("3.OIL                               [Rs165/- per Litre]")
        elif r == 4:
            grocery -= 25
            b["First_Floor"].remove("4.WHEAT FLOUR         [Rs25/- per kg]")
        elif r == 5:
            grocery -= 28
            b["First_Floor"].remove("5.SALT                               [Rs28/- per kg]")
        else:
            r = int(input("Error! Item out of the list.Please enter correct item no. = "))
    elif pr == "n":
        ans = input("Would you like to purchase more from this grocery shop?(y/n)")
    else:
        pr = input("Please type either y or n. ")
    return grocery
#function for bill amount
def billamt(grocery,outfit,gadget,game_zone):
    Totalamt=grocery+outfit+gadget+game_zone
    print("-----------------------------------------")
    print("                 BILL                    ")
    print("-----------------------------------------")
    print('''1.Your purchase amount from 1st floor = {}
2.Your purchase amount from 2nd floor = {}
3.Your purchase amount from 3rd floor = {}
4.Your purchase amount from 4th floor = {}
5.Grand Total Amount = Rs{}'''.format(b["First_Floor"],b["Second_Floor"],b["Third_Floor"],b["Fourth_Floor"],Totalamt))
#function for returning item
def returning(grocery,outfit,gadget):
    ans="y"
    while ans == "y" or ans == "Y":
        floor = int(input('''This is return section.
    1.for Grocery Shop
    2.for Cloth Shop
    3.for Electronic Shop
    Enter the floor number you want to go= '''))
        if floor == 1:
            r = int(input("{}\nEnter the item no. to return= ".format(b["First_Floor"])))
            if r == 1:
                grocery -= 44
                b["First_Floor"].remove("1.SUGAR                           [Rs44/- per kg]")
            elif r == 2:
                grocery -= 20
                b["First_Floor"].remove("2.RICE                                [Rs20/- per kg]")
            elif r == 3:
                grocery -= 165
                b["First_Floor"].remove("3.OIL                               [Rs165/- per Litre]")
            elif r == 4:
                grocery -= 25
                b["First_Floor"].remove("4.WHEAT FLOUR         [Rs25/- per kg]")
            elif r == 5:
                grocery -= 28
                b["First_Floor"].remove("5.SALT                               [Rs28/- per kg]")
            else:
                r = int(input("Error! Item out of the list.Please enter correct item no. = "))
            #return grocery
        elif floor == 2:
            r = int(input("{}\nEnter the item no. to return= ".format(b["Second_Floor"])))
            if r == 1:
                outfit -= 800
                b["Second_Floor"].remove("1.SHIRT                             [Rs800/-]")
            elif r == 2:
                outfit -= 1200
                b["Second_Floor"].remove("2.PANT                              [Rs1200/-]")
            elif r == 3:
                outfit -= 100
                b["Second_Floor"].remove("3.SHOCKS                        [Rs100/-]")
            elif r == 4:
                outfit -= 180
                b["Second_Floor"].remove("4.HAND GLOVES         [Rs180/-]")
            elif r == 5:
                outfit -= 1999
                b["Second_Floor"].remove("5.SWEATER                      [Rs1999/-]")
            else:
                r = int(input("Error! Item out of the list.Please enter correct item no. = "))
            #return outfit
        elif floor == 3:
            r = int(input("{}\nEnter the item no. to return= ".format(b["Third_Floor"])))
            if r == 1:
                gadget -= 10000
                b["Third_Floor"].remove("1.PHONE                  [Rs10000/-]")
            elif r == 2:
                gadget -= 56000
                b["Third_Floor"].remove("2.LAPTOP                 [Rs56000/-]")
            elif r == 3:
                gadget -= 7500
                b["Third_Floor"].remove("3.TELEVISION         [Rs7500/-]")
            elif r == 4:
                gadget -= 2000
                b["Third_Floor"].remove("4.WATCH                [Rs2000/-]")
            elif r == 5:
                gadget -= 200
                b["Third_Floor"].remove("5.KEYBOARD          [Rs200/-]")
            else:
                r = int(input("Error! Item out of the list.Please enter correct item no. = "))
            #return gadget
        else:
            ans = input("You can only return items among 3 floors. So please enter from 1 to 3.\nDo you  want to visit the floor among given?(y/n) ")
        ans = input("Do you  want to visit other floor to return your purchased items?(y/n)")
    billamt(grocery,outfit,gadget,game_zone)
#Entry of mall
ans="y"
while ans == "y" or ans == "Y":
    floor = int(input('''1.for Grocery Shop
2.for Cloth Shop
3.for Electronic Shop
4.for Game Zone
Enter the floor number you want to go= '''))
    if floor == 1:
        grocery = grocery1(grocery)
    elif floor == 2:
        outfit = outfit1(outfit)
    elif floor == 3:
        gadget = gadget1(gadget)
    elif floor == 4:
        game_zone = game_zone1(game_zone)
    else:
        print("There is no floor above  4th floor. So please enter from 1 to 4.")
    ans = input("Do you  want to visit other floor?(y/n)")
#calling function to return purchased items
a = input("Do you want to return your purchased items?(y/n)").lower()
if a == "y":
    returning(grocery,outfit,gadget)
elif a == "n":
    #calling function to show the bill
    billamt(grocery,outfit,gadget,game_zone)
else:
    print("Error!Please restart the program and type either y or n. ")