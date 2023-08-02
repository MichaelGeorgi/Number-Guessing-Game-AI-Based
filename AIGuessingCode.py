from RandomNumber import random_number_gen
import random
import time

modes = "\nEasy (a), \nMedium (b), \nHard (c)"
print(modes)
num = 0
score = 0
computer_answer = ""
trys = 0
max_trys = 10

choice = input("Enter Input Here: ").lower()

# Choose Mode
if choice == "a".lower():
    print("\nChoosing Easy Mode...")
    num = 10
elif choice == "b".lower():
    print("\nChoosing Medium Mode...")
    num = 30
elif choice == "c".lower():
    print("\nChoosing Hard Mode")
    num = 50
else:
    print("\nUnvalid Input")
    

random_number = random_number_gen(num)

while computer_answer != random_number and trys < max_trys:
    computer_answer = random.randint(1,num)
    print(computer_answer)
    trys += 1
    time.sleep(.6)
    
if computer_answer == random_number:
    print("\nYou Won In " + str(trys) + " Trys!")
else:
    print("\nYou Lost Due To Exeeding Limit Of 10 Trys..")