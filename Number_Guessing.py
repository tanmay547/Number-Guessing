import random
Computerinput = random.randrange(1,101)
userinput = int(input("Enter Your Number :----- "))
 
if userinput>Computerinput:
    print("Computer Number ",Computerinput)
    print("Your Guess Number Is High")

elif userinput<Computerinput:
    print("Computer Number ",Computerinput)
    print("Your Guess Number Is Low")

else:
    print("Computer Number ",Computerinput)
    print("Your Guess Number Is Equal")