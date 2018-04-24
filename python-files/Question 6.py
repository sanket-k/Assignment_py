
# coding: utf-8

# ### Question 6

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# 
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# ### Version 1

# In[52]:


def even(a,z):                                             # define function even accepting start and end number 
    
    sequence = []                                          # create empty array  
    
    for num in range(a,z):                                 # iterate through the total number 
        is_even = True                                     # default as true
        total = str(num)                                   # make the total number as str
        
        for i in total:                                    # iterate through total number
            if int(i) % 2 != 0:                            # check if every digit is divisible by 2 
                is_even = False
        if is_even == True:
            sequence.append(str(num))                      # append if every number is divisible by 2
    return(sequence)                                       # return the array 


# In[53]:


print("the sequence is : \n\n {} ".format(",".join(even(1000,3001))))     # display array after passing through function


# ### Version 2

# In[56]:


seq = []                                                     # create empty array 

for i in range(1000, 3001):                                  # iterate through the total number
    ev = str(i)
    if (int(ev[0])%2==0) and (int(ev[1])%2==0) and (int(ev[2])%2==0) and (int(ev[3])%2==0):          # check if every digit is divisible by 2
        seq.append(ev)                                       # append if every number is divisible by 2 
        
print("the sequence is : \n\n ",",".join(seq))               # return the array  

