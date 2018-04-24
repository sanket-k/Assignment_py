
# coding: utf-8

# ### Question 7

# Write a program that accepts a sentence and calculate the number of letters and digits.
# 
# Suppose the following input is supplied to the program:
# 
# hello world! 123
# 
# Then, the output should be:
# 
# LETTERS 10
# 
# DIGITS 3

# ### Version 1

# In[9]:


string_in = input(" Input a string : ")                          # input sentence

digit = 0                                                        # assign digit variable to 0
letter = 0                                                       # assign letter variable to 0

for i in string_in:                                              # iterate total numeber of charecters 
    if i.isalpha():                                              # check if charecter is an alphabet
        letter += 1                                              # increase letter count by 1
    elif i.isdigit():                                            # check if charecter is an digit
        digit += 1                                               # increase digit count by 1 
    else:
        pass

print("The number of letters are : {}".format(letter))           # display total number of letter
print("The number of digits are  : {}".format(digit))            # display taoal number of digit


# ### Version 2

# In[10]:


string_in = input(" Input a string : ")                          # input sentence

d = {"DIGITS":0, "LETTERS":0}                                    # assign digit and letter variable to 0
for i in string_in:                                              # iterate total numeber of charecters  
    if i.isdigit():                                              # check if charecter is an digit
        d["DIGITS"]+=1                                           # increase digit count by 1  
    elif i.isalpha():                                            # check if charecter is an alphabet
        d["LETTERS"]+=1                                          # increase letter count by 1
    else:
        pass
print("LETTERS", d["LETTERS"])                                   # display total number of letter
print("DIGITS", d["DIGITS"])                                     # display taoal number of digit

