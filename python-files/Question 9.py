
# coding: utf-8

# ### Question 9

# Write a program that computes the net amount of a bank account based a transaction log from
# console input. The transaction log format is shown as following:
# 
# D 100
# 
# W 200
# 
# ...
# 
# D means deposit while W means withdrawal.
# 
# Suppose the following input is supplied to the program:
# 
# D 300
# 
# D 300
# 
# W 200
# 
# D 100
# 
# Then, the output should be:
# 
# 500

# ### Version 1

# In[17]:


net_transaction = 0                                                # set initial amount to 0

while True:                                                        # keep checking for input 
    input_trans = input("--> ").split()                            # input value and split      
    if not input_trans:
        break;                                                     # break if there is no input

    net_amount = int(input_trans[1])                               
    if input_trans[0] == 'D':                                      # check if the initial char starts with D for Deposit
        net_transaction += net_amount                              # add it to the net amount
    elif input_trans[0] == 'W':                                    # check if the initial char starts with W for Withdrawal
        net_transaction -= net_amount                              # deduct it from the net amount 

print("The net amount is : {} ".format(net_transaction))           # display the remaining amount


# ### Version 2

# In[23]:


net_amount = 0                                                      # set initial amount to 0  

while True:                                                         # keep checking for input
    s = input("--> ")                                               # input value and split
    if not s:
        break                                                       # break if there is no input
    values = s.split(" ")                                            
    operation = values[0]
    amount = int(values[1])
    if operation=="D":                                              # check if the initial char starts with D for Deposit
        net_amount+=amount                                          # add it to the net amount
    elif operation=="W":                                            # check if the initial char starts with W for Withdrawal
        net_amount-=amount                                          # deduct it from the net amount          
    else:
        pass
print("The net amount is : {} ".format(net_amount))                 # display the remaining amount 

