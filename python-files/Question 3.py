
# coding: utf-8

# ### Question 3

# ### Note: problem similar to Question 2

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# 
# Note: i=0,1.., X-1; j=0,1,¡ Y-1.
# 
# #### Example
# 
# Suppose the following inputs are given to the program:
#     
# 3,5
# 
# Then, the output of the program should be:
#     
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# ### Version 1

# In[4]:


#define function to display matrix by accepting variables
def displayMatrix(x,y):
    dim_array = [[0 for j in range(y)] for i in range(x)]        # define array
    for i in range(x):                                           # use recurvise loop to reach entered numbers  
        for j in range(y):
            dim_array[i][j] = i * j                              # allocate array by multiplying the row and columns
    return(dim_array)                                            # return array


# In[5]:


x = int(input("Input the number of rows : "))                    # input the number of rows
y = int(input("Input the number of columns : "))                 # input number of columns

print("the 2-Dimensional array is : {}". format(displayMatrix(x,y)))    # display the array


# ### Verision 2

# In[3]:


row_num = int(input("Input number of rows: "))                           # input rows
col_num = int(input("Input number of columns: "))                        # input columns
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]   # allocate array

for row in range(row_num):                                               # recursive loop to reach entered numbers  
    for col in range(col_num):                                     
        multi_list[row][col]= row*col                                    # allocate array by multiplying the row and columns

print("the 2-Dimensional array is : {}".format(multi_list))              # display the array 

