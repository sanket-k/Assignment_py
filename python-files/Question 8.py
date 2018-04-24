
# coding: utf-8

# ### Question 8

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# 
# Suppose the following input is supplied to the program:
# 
# 9
# 
# Then, the output should be:
# 
# 11106

# ### Version 1

# In[17]:


number = input("enter the digit : ")                             # input digit

p1 = int( "%s" % number )                                        
p2 = int( "%s%s" % (number,number) )
p3 = int( "%s%s%s" % (number,number,number) )
p4 = int( "%s%s%s%s" % (number,number,number,number) )

sum_of_all = p1 + p2 + p3 + p4                                   # add all value 

print("the sum value of digti is : {} ".format(sum_of_all))      # display result


# ### Version 2

# In[24]:


number = input("enter number :")                                 # input digit
DIGIT = 4
res = 0
for i in range(1,DIGIT+1):                                       # add all value
    res += int(str(number)*i)                                    # mult and add 
print("the sum value of digti is : {} ".format(res))             # display result

