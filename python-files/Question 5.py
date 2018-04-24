
# coding: utf-8

# ### Question 5

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5
# are to be printed in a comma separated sequence.
# 
# #### Example:
# 
# 0100,0011,1010,1001
# 
# Then the output should be:
# 
# 1010

# ### Version 1

# In[4]:


bi_num = [i for i in input().split(',')]                       # input sequence and split at ','
out_seq = []                                                   # create empty array  

for j in bi_num:                                               # iterate through total number of input
    i = int(j,2) 
    if i%5 == 0:                                               # check if divisible by 5  
        out_seq.append(j)                                      # append if divisible by 5  
print(','.join(out_seq))                                       # join the numbers and display


# ### Version 2

# In[10]:


out_value = []                                                  # create empty array
items=[i for i in input().split(',')]                           # input sequence and split at ','

for j in items:                                                 # iterate through total number of input
    i = int(j, 2)
    if not i%5:                                                 # check if divisible by 5
        out_value.append(j)                                     # append if divisible by 5

print(','.join(out_value))                                      # join the numbers and display 

