#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('''Welcome to Game Zone of Manish
*These games for single user*''')
a = True
while a:
    x = input('''Press 1 to Play KBC
    Press 2 to Tic Tac Toe
    Press 3 to Play Hangman
    Press 4 to Rock Paper Scissors :
           or 
    To Exit Press 0
    ''')

    if x == "1":
        import KBC_without_database
    elif x == "2":
        import Tic_Tac_Toe
    elif x == "3":
        import Hangman
    elif x == "4":
        import Rock_Paper_Scissors_with_computer
    elif x == "0":
        import Rock_Paper_Scissors_with_computer
    else:
        print("Enter Valid Option")
