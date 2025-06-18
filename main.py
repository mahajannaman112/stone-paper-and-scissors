'''
s for stone 
p for paper 
sc for scissor
'''
import random
computer = random.choice([-1,1,0])

youstr = input("Enter your choice : ")
youdict = {"s":-1 , "p":0, "sc":1}
reversedict = { -1: "stone", 0:"paper", 1:"scissor"}
you = youdict[youstr] 

print(f"Your choice is : {reversedict[you]}")
print(f"computer choice is : {reversedict[computer]}")

if(computer == -1 and you == 0):
    print("you win")
elif(computer == -1 and you == 1):
    print("computer win")
elif(computer == 0 and you == -1):
    print("computer win")
elif(computer ==0 and you ==1):
    print("you win")
elif(computer == 1 and you ==-1):
    print("you win")
elif(computer ==1 and you == 0):
    print("computer win")
else:
    print("its a draw")