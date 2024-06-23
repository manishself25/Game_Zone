#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("********** Welcome To Technical KBC Game **********")
import numpy as np
import pyrebase

player= input("Enter your name : ")

questions = ["Who developed Python Programming Language?\n",
            "Which type of Programming does Python support?\n",
           "Which of the following is the correct extension of the Python file?\n",
           "All keywords in Python are in _________?\n",
            "Which of the following is used to define a block of code in Python language?\n",
            "Python supports the creation of anonymous functions at runtime, using a construct called __________", 
            "What is the order of precedence in python?"]

options =[" 1. Wick van Rossum \n 2. Rasmus Lerdorf \n 3. Guido van Rossum \n 4. Niene Stom\n",
          "1. object-oriented programming \n 2. structured programming \n 3. functional programming \n 4. all of the mentioned\n",
          "1. .p \n 2. .pl \n 3. .py \n 4. .python",
          "1. Capitalized \n 2. lower case \n 3. UPPER CASE \n 4. None of the mentioned",
          "1. Indentation \n 2. Key \n 3. Brackets \n 4. All of the mentioned\n",
          "1. pi \n 2. anonymous \n 3. lambda \n 4. none of the mentioned\n",
          "1. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction \n 2. Exponential, Parentheses, Division, Multiplication, Addition, Subtraction \n 3. Parentheses, Exponential, Multiplication, Division, Subtraction, Addition \n 4. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction\n"]

correct=["3","4","3","4","1","3","4"]

answers = ["3. Guido van Rossum","4. all of the mentioned","3. .py","4. None of the mentioned",
           "1. Indentation","3. lambda","4. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"]

ff_options=["2. Rasmus Lerdorf \n 3. Guido van Rossum \n",
            "1. object-oriented programming \n  4. all of the mention\n",
            "3. .py \n 4. .python\n",
            "2. lower case \n 4. None of the mentioned\n",
            "1. Indentation \n 3. Brackets\n",
            "3. lambda \n 4. none of the mentioned\n",
            "3. Parentheses, Exponential, Multiplication, Division, Subtraction, Addition \n 4. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction\n"]
# **********************************************************************
lifeline_name=["Fifty Fifty Lifeline","Change the question"]
lifeline_questions=["Which of the following functions can help us to find the version of python that we are currently working on?\n",
                    "Which keyword is used for function in Python language?\n",
                    "What does pip stand for python?\n"]
lifeline_options=["1. sys.version(1) \n 2. sys.version(0) \n 3. sys.version() \n 4. sys.version \n",
                  "1. Function \n 2. def \n 3. Fun \n 4. Define \n",
                  "1. Pip Installs Python \n 2. Pip Installs Packages \n 3. Preferred Installer Program \n 4. All of the mentioned\n"]
lifeline_correct=["4","2","3"]
lifeline_answers = ["4. sys.version","2. def","3. Preferred Installer Program"]
# *************************************************************************
paisa=[1000,5000,10000,50000,1000000]

tql =np.random.choice(questions,5, replace=False).tolist()
lql=np.random.choice(lifeline_questions)
prize_money=0

i=0
while i<5:
    ques=tql[i]
    qos=questions.index(ques)
        
    print(ques)
    print(options[qos])
    
    
    player_int= input("aapko aata hai yah question? (yes or no)\n ").lower()
    
    if player_int=="yes":
        user_ans=input("bataiye kya lock karege aap Mahoday?\n ")
        if user_ans==correct[qos]:
            print("you selected ", answers[qos] ," which is a correct answer \n")
            print("Badhai ho!!, App ",paisa[i],"jeet gaye hai\n ")
            prize_money=paisa[i]
        else:
            print("oh shit, yah answer galat hai... \n ")
            print("correct answer was ", answers[qos])
            break
    else:
        lifeline=input("Do you want to take Life Line? or want to Quit?\n")
        if lifeline=="yes":
            lno=input("Select a lifeline from these options \n 1.Fifty Fifty Lifeline \n 2. Change the question : ")
            if lno=="1":
                print("you have selected Fifty Fifty Lifeline")
                print(ff_options[qos])
                user_ans=input("bataiye kya lock karege aap Mahoday?\n   \n")
                if user_ans==correct[qos]:
                    print("you selected ", answers[qos] ," which is a correct answer\n")
                    print("Badhai ho!!, App",paisa[i],"jeet gaye hai\n ")
                    prize_money=paisa[i]
                else:
                    print("oh shit, yah answer galat hai... \n ")
                    print("correct answer was ", answers[qos])
                    break
                
            elif lno=="2":
                los=lifeline_questions.index(lql)
                print(lql)
                print(lifeline_options[los])
                user_ans=input("bataiye kya lock karege aap Mahoday?\n ")
                if user_ans==lifeline_correct[los]:
                    print("you selected ", lifeline_answers[los] ," which is a correct answer\n")
                    print("Badhai ho!!, App",paisa[i],"jeet gaye hai\n ")
                    prize_money=paisa[i]
                else:
                    print("oh shit, yah answer galat hai... \n ")
                    print("correct answer was ", lifeline_answers[los])
                    break
                
        else:
            print("chaliye aapki jiti hui rashi aapko online tranfer kar dete hai")
            break
            
    i = i+1   

print(" aapki jeeti hui Rashi hai\n",prize_money,"\n")
print(" chaliye kal milte hai \n shubhratri \n shubhratri \n shubhratri \n")


# In[ ]:


# 2. Which type of Programming does Python support?

# 1. object-oriented programming
# 2. structured programming
# 3. functional programming
# 4. all of the mentioned

# ans 4. all of the mentioned

# 4. Which of the following is the correct extension of the Python file?
# 1. .python
# 2. .pl
# 3. .py
# 4. .p

# ans 3. .py

# 5. Is Python code compiled or interpreted?
# 1. Python code is both compiled and interpreted
# 2. Python code is neither compiled nor interpreted
# 3. Python code is only compiled
# 4. Python code is only interpreted

# ans 1. Python code is both compiled and interpreted

# 6. All keywords in Python are in _________
# 1. Capitalized
# 2. lower case
# 3. UPPER CASE
# 4. None of the mentioned

# ans 4. None of the mentioned

# 8. Which of the following is used to define a block of code in Python language?
# 1. Indentation
# 2. Key
# 3. Brackets
# 4. All of the mentioned

# ans 1. Indentation

# 9. Which keyword is used for function in Python language?
# 1. Function
# 2. def
# 3. Fun
# 4. Define

# ans 2. def

# 12. Which of the following functions can help us to find the version of python that we are currently working on?
# 1. sys.version(1)
# 2. sys.version(0)
# 3. sys.version()
# 4. sys.version

# ans 4. sys.version

# 13. Python supports the creation of anonymous functions at runtime, using a construct called __________
# 1. pi
# 2. anonymous
# 3. lambda
# 4. none of the mentioned

# ans 3. lambda

# 14. What is the order of precedence in python?
# 1. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
# 2. Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
# 3. Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
# 4. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction

# ans 4. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction


# In[ ]:




