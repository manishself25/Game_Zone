#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input('''Enter your choice (rock, paper, scissors)
                            or
                    To Exit Enter " Q " : ''').lower()
    if user_choice == "q":
        return user_choice
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or        (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"


print("Welcome to Rock, Paper, Scissors!")
user_score = 0
computer_score = 0
ties = 0

for _ in range(5):
    user_choice = get_user_choice()
    if user_choice == "q":
        break 
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
        
    result = determine_winner(user_choice, computer_choice)
    if result == "user":
        user_score += 1
        print("You win this round!")
    elif result == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        ties += 1
        print("This round is a tie!")

print("\nFinal Scores:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
print(f"Ties: {ties}")

if user_score > computer_score:
    print("You win the game!")
elif computer_score > user_score:
    print("Computer wins the game!")
else:
    print("The game is a tie!")
