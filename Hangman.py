#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random
word = ["python","bjp","mahi","hello"]
word_hint = ["coding language of 6 characters", 
             "Strong political party in india of character 3",
             "nick name of dhoni of character 4",
             "when 2 person meet each other what the first word they say to each other, word of character 5"]
random_word = random.choice(word)
print(random_word)
z = word.index(random_word)
a = list(random_word)
print(f"hint of the word is : {word_hint[z]}")
count = 0
l = []
for i in range(len(random_word)):
    l.append("_")
for j in range(len(random_word)):
    print(f"fill the given space {l}")
    l1 = input("guess the character : ")
    if len(l1) < len(random_word):
        if l1 in random_word:
            for k in range(len(a)):
                if a[k] == l1:
                    l[k] = l1
            print("you guess the correct character")
            print(f"you have only {len(random_word)-j-1} attempts")
            s = "".join(l)
            if s == random_word:
                count = j+1
                print(f"Finally you guess the correct word {l}")
                break
        else :
            print("you guess the wrong character")
            print(f"you have only {len(random_word)-j-1} attempts")
    elif l1 == random_word:
        count = j+1
        print("you guess the correct word")
        break
    elif len(l1) >= len(random_word):
        print("you guess the wrong word")


if count == 1:
    print(f"your score is : {len(random_word)-count}")
elif count == 2:
    print(f"your score is : {len(random_word)-count}")
elif count == 3:
    print(f"your score is : {len(random_word)-count}")


# In[ ]:




