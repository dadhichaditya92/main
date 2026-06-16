import random
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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
user_input = int(input("what do you choose? type 0 for rock 1 for paper or 2 for scissors \n"))
if user_input >=0 and user_input <= 2:
    print(game_image[user_input])

computer_choice = random.randint(0,2)
print(f"Computer chose")
print(game_image[computer_choice])
if user_input >= 3 or user_input < 0:
    print("Invalid You lose")
elif user_input == 0 and computer_choice == 2:
    print("you win")
elif user_input == 2 and computer_choice == 0:
    print("computer win")
elif user_input == 1 and computer_choice ==0:
    print("you win")
elif user_input == 0 and computer_choice == 1:
    print("computer win")
elif user_input == computer_choice:
    print("it's a draw")