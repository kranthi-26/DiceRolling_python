import random #it is used to generate random numbers
print("This is our dice stimulator.")
x = "y"
while(x == "y"):
    num = random.randint(1,6) #the method of generating random numbers is randint()
    if num == 1:
        print("-------")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print("-------")
    if num == 2:
        print("-------")
        print("|     |")
        print("| o o |")
        print("|     |")
        print("-------")
    if num == 3:
        print("-------")
        print("|  o  |")
        print("|  o  |")
        print("|  o  |")
        print("-------")
    if num == 4:
        print("-------")
        print("|o   o|")
        print("|     |")
        print("|o   o|")
        print("-------")
    if num == 5:
        print("-------")
        print("|o   o|")
        print("|  o  |")
        print("|o   o|")
        print("-------")
    if num == 6:
        print("-------")
        print("|o   o|")
        print("|o   o|")
        print("|o   o|")
        print("-------")
    x = input("y or n:  ") #press 'y' to roll again and 'n' to stop
    
