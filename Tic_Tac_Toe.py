#!/usr/bin/env python
# coding: utf-8

# In[ ]:

l = [["x1","x2","x3"],
     ["x4","x5","x6"],
     ["x7","x8","x9"]]

def printgrid():
    for i in l:
        print(i)
printgrid()


# In[12]:


print("Tic Tac Toe")
inp = ["x","o"]

out = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

p1 = []
p2 = []
for i in range (3):
    player1 = input("Player 1, What you want to select (x/o): ")
    
    if player1 == "x":
        player2 = "o"
        print("Player 2 have : ",player2)
        
    elif player1 == "o":
        player2 = "x"
        print("Player 2 have : ",player2)
        
    else :
        print("Enter Valid input ( x or o ), only ",2-i," Chance left")
        
    if player1 in inp:
        break
        
        
    

        
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]

l1 = [["1","2","3"],
     ["4","5","6"],
     ["7","8","9"]]
def printgrid():
    for i in l:
        print(i)
printgrid()

flag = 0
for i in range (9):

    z = int(input("player 1 : Select position for input :"))
    p1.append(z)
    print(p1)
    p1.sort()
    
    for a in range(3):
        if z in l[a]:
            v =  l[a].index(z)
            print(a,v)
            
            l[a][v] = player1
            printgrid()
    
    z1 = int(input("player 2 : Select position for input :"))
    p2.append(z1)
    print(p2)
    p2.sort()
    
    for b in range(3):
        if z1 in l[b]:
            v1 =  l[b].index(z1)
            print(b,v1)
            
            l[b][v1] = player2
            printgrid()
            
    for c in range (8):
        
        if p1 in out:
            print("player1 win the match")
            i = 9
            flag = 1
            break

        elif p2 in out:
            print("player2 win the match")
            i = 9
            flag = 1
            break
        
    if flag == 1: break

    if i == 8:
        print("tie")