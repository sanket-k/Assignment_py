
# coding: utf-8

# ### Question 4

# Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically.
# 
# Suppose the following input is supplied to the program:
# 
# hello world and practice makes perfect and hello world again
# 
# Then, the output should be:
# 
# again and hello makes perfect practice world
# 
# #### Hints:
# 
# We use set container to remove duplicated data automatically and then use sorted() to sort the
# data.

# ### Version 1

# In[19]:


sequencial_sentence = input("Enter a sentence seperated by whitespaces : ")                 # input sequence of words 
sequencial_sentence_spilt = sequencial_sentence.split(' ')                                  # split the words based on whitespaces 
seq_set = set(sequencial_sentence_spilt)                                                    # arrange them alphanumerically
print('\nThe output after removing duplicate words and sorting them alphanumerically is : \n',' '.join(sorted(seq_set)))    # display the arranged sentence


# ### Version 2

# In[23]:


seq = input("Enter a sentence seperated by whitespaces : ")    # input sequence of words           
words = [word for word in seq.split(" ")]                      # split the words based on whitespaces 
print('\nThe output after removing duplicate words and sorting them alphanumerically is : \n'," ".join(sorted(list(set(words)))))     # arrange them alphanumerically and display the output 

