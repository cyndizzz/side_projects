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

gestures = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
your_gesture = gestures[your_choice]
computer_choice = random.randint(0,2)
computer_gesture = gestures[computer_choice]

print(your_gesture)
print("Computer chose:")
print(computer_gesture)
if your_choice == computer_choice:
    print("It's a draw!")
elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 0):
    print("You lose")
else:
    print("You win")