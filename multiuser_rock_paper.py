#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
def get_user1_choice():
    choices1 = ['rock', 'paper', 'scissors']
    user1_choice = input('''Enter user 1 choice (rock, paper, scissors)
                            or
                    To Exit Enter " Q " : ''').lower()
    if user1_choice == "q":
        return user1_choice
    while user1_choice not in choices1:
        user1_choice = input("Invalid choice. Enter user 1 choice (rock, paper, scissors): ").lower()
    return user1_choice

def get_user2_choice():
    choices2 = ['rock', 'paper', 'scissors']
    user2_choice = input('''Enter user 2 choice (rock, paper, scissors)
                            or
                    To Exit Enter " Q " : ''').lower()
    if user2_choice == "q":
        return user2_choice
    while user2_choice not in choices2:
        user2_choice = input("Invalid choice. Enter user 2 choice (rock, paper, scissors): ").lower()
    return user2_choice

def determine_winner(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        return "tie"
    elif (user1_choice == 'rock' and user2_choice == 'scissors') or (user1_choice == 'paper' and user2_choice == 'rock') or (user1_choice == 'scissors' and user2_choice == 'paper'):
        return "user1"
    else:
        return "user2"

print("Welcome to Rock, Paper, Scissors!")
user1_score = 0
user2_score = 0
ties = 0

for _ in range(5):
    user1_choice = get_user1_choice()
    if user1_choice == "q":
        break 

    user2_choice = get_user2_choice()
    if user2_choice == "q":
        break 
    print(f"User 1 chose: {user1_choice}")
    print(f"User 2 chose: {user2_choice}")
        
    result = determine_winner(user1_choice, user2_choice)
    if result == "user1":
        user1_score += 1
        print("User1 win this round!")
    elif result == "user2":
        user2_score += 1
        print("User2 win this round!")
    else:
        ties += 1
        print("This round is a tie!")

print("\nFinal Scores:")
print(f"user 1: {user1_score}")
print(f"user 2: {user2_score}")
print(f"Ties: {ties}")

if user1_score > user2_score:
    print("user 1 win the game!")
elif user2_score > user1_score:
    print("user 2 win the game!")
else:
    print("The game is a tie!")


# In[ ]:




