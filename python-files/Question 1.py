
# coding: utf-8

# ## Assignment

# ### Question 1:
# 
# Write a program that calculates and prints the value according to the given formula:
# 
# Q = Square root of [(2 * C * D)/H]
# 
# Following are the fixed values of C and H:
# 
# C is 50. H is 30.
# 
# D is the variable whose values should be input to your program in a comma-separated
# sequence.
# 
# #### Example
# 
# Let us assume the following comma separated input sequence is given to the program:
# 
# 100,150,180
# 
# The output of the program should be:
# 
# 18,22,24
# 
# #### Hints:
# 
# If the output received is in decimal form, it should be rounded off to its nearest value (for
# example, if the output received is 26.0, it should be printed as 26).

# ### Version 1

# In[1]:


import math                                              #import necessary libraries 


# In[ ]:


#define function to implement formula
def squareRoot(int):
    return (math.floor(math.sqrt((2 * C * D) / H)))


# #### Formula :  $$ Q = {\sqrt {2 * C * D\over H}} $$

# In[19]:


#initialize pre defined values
C = 50
H = 30

D = int(input("enter number : "))                       # input the variable D
print("The answer is {} ".format(squareRoot(D)))        # print answer by calling the defined function


# ### Version 2

# In[18]:


import math                                              #import necessary libraries 


# #### Formula :  $$ Q = {\sqrt {2 * C * D\over H}} $$

# In[21]:


##initialize pre-defined values
C = 50
H = 30

D = int(input("enter number : "))                        # input the variable D
answer = math.floor(math.sqrt((2 * C * D) / H))          # calculate answer by passing through provided formula
print("the answer is {} ".format(answer))                # print answer 

