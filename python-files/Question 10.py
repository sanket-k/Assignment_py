
# coding: utf-8

# ### Question 10

# Write a program to compute:
# 
# f(n)=f(n-1)+100 when n>0
# 
# and f(0)=1
# 
# with a given n input by console (n>0).

# ### version 1

# In[8]:


def f(n):                                                         # define function to accept a digit
    if n == 0:
        return 1                                                  # return 1 if number = 0 
    else:
        return f(n-1)+100                                         # perform recursive function and return value


# In[38]:


input_n = int(input("enter number : "))                           # input digit/value
print("f({0}) = {1}".format((input_n), f(input_n)))               # display the computed value


# In[37]:


def f2(n):
    ans = 0
    if n == 0:
        return 1
    else:
        return f2(n-1)+100


input_n = int(input("enter number : "))

print("f({0}) = {1}".format((input_n), f2(input_n)))

