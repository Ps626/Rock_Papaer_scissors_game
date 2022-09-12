rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
input1 = int(input("select '0' for 'rock', '1'for 'paper', '2' for 'scissors'"))
combind = ["0", "1", "2"]
random_variable = random.choice(combind)

if input1 == 0:
    print(f"Your Choice \n {rock}")
if input1 == 1:
    print(f"Your Choice \n {paper}")
if input1 == 2:
    print(f"Your Choice \n {scissors}")
if random_variable == "0":
    print(f"computer\'s Choice \n {rock}")
if random_variable == "1":
    print(f"computer\'s  Choice \n {paper}")
if random_variable == "2":
    print(f"computer\'s  Choice \n {scissors}")

assign = int(random_variable)
if input1 == assign:
    print ("it\'s a draw")
elif input1 == 0 and assign == 1:
    print("You Loose.")
elif input1 == 1 and assign == 2:
    print("You Loose.")
elif input1 == 2 and assign == 0:
    print("You Loose.")
else:
    print("You Win !!!")
     
     

# random_variable = random.choice(combind)
             

