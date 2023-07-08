#making chor_police game using random module
from random import *
#Names of the player
p = input("Enter your name= ")
q = input("Enter your name= ")
r = input("Enter your name= ")
s = input("Enter your name= ")
#Declaring variables for score
k1 = 0
m1 = 0
s1 = 0
c1 = 0
#Function for Raja and Mantri
def command(a):
    global k1,s1
    if  a == "Raja":
        #Giving score to Raja
        k1 += 100
        print('''Raja
              :-Mantri chor ka pta lagao.''')
    elif  a == "Mantri":
        print('''Mantri''')
    elif a == "Sipahi":
        #Giving score to sipahi
        s1 += 10
#Function for score
def score(x):
    global k1,m1,s1,c1
    #Conditions to show the score of players
    if y[x] == ["Raja"]:
        print(f'{x} = {k1}')
    elif y[x] == ["Mantri"]:
        print(f'{x} = {m1}')
    elif y[x] == ["Sipahi"]:
        print(f'{x} = {s1}')
    else:
        print(f'{x} = {c1}')
#Main game start
ans = 'y'
#Using while for users choice
while ans in ('y',"yes",'Y',"Yes"):
    #List for chits
    a = ["Raja","Mantri","Sipahi","Chor"]
    #Selecting random element from the list
    b = choice(a)
    #Dictionary for storing chits
    y = {p:[],q:[],r:[],s:[]}
    #Taking each and every element of y using for loop
    for i in y:
        print("\n~~~",i,"ka chance hai ~~~\n")
        #Taking input from user
        c= int(input('''Choose your chit number:
    1. chit no. 1
    2. chit no. 2
    3. chit no. 3
    4. chit no. 4
    Your chit number = '''))
        #Conditions for user's input
        if c == 1:
            #Storing value in the key
            y[i].append(b)
            #Calling function
            command(b)
        elif c == 2:
            #Using remove function for unique chit
            a.remove(b)
            #Taking new chit
            b = choice(a)
            #Storing value in the key
            y[i].append(b)
            #Calling function
            command(b)
        elif c == 3:
            #Using remove function for unique chit
            a.remove(b)
            #Taking new chit
            b = choice(a)
            #Storing value in the key
            y[i].append(b)
            #Calling function
            command(b)
        elif c == 4:
            #Using remove function for unique chit
            a.remove(b)
            #Taking new chit
            b = choice(a)
            #Storing value in the key
            y[i].append(b)
            #Calling function
            command(b)
        else:
            #To show error
            print("Error! Please choose a valid option.\n")
    #Taking out keys from the dictionary using values
    e = list(y.keys())[list(y.values()).index(["Mantri"])]
    f = list(y.keys())[list(y.values()).index(["Chor"])]
    g = list(y.keys())[list(y.values()).index(["Raja"])]
    h = list(y.keys())[list(y.values()).index(["Sipahi"])]
    #Taking input from user to guess the chor
    d = input(f"{e}: ")
    #Conditions for user's input
    if d == f:
        #if the answer is correct then score will be given to Mantri
        m1 += 50
        print("correct")
    else:
        #If the answer is incorrect then score will be given to Chor
        c1 += 25
        print("wrong")
    #Giving user the correct answer to check
    print("Chor is",f)
    #Taking user's choice
    ans = input("Do you want to play again? Type yes to play otherwise press Enter to exit. ")
#Design for Score board
print("----------------------------------------------------")
print("                   SCOREBOARD                       ")
print("----------------------------------------------------")
#Calling score function in a for loop to show the score of every player
for x in y:
    score(x)