
# Assignment

## Question 1:

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated
sequence.

#### Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

#### Hints:

If the output received is in decimal form, it should be rounded off to its nearest value (for
example, if the output received is 26.0, it should be printed as 26).

### Version 1


```python
import math                                              #import necessary libraries 
```


```python
#define function to implement formula
def squareRoot(int):
    return (math.floor(math.sqrt((2 * C * D) / H)))
```

#### Formula :  $$ Q = {\sqrt {2 * C * D\over H}} $$


```python
#initialize pre defined values
C = 50
H = 30

D = int(input("enter number : "))                       # input the variable D
print("The answer is {} ".format(squareRoot(D)))        # print answer by calling the defined function
```

    enter number : 100
    The answer is 18 
    

### Version 2


```python
import math                                              #import necessary libraries 
```

#### Formula :  $$ Q = {\sqrt {2 * C * D\over H}} $$


```python
##initialize pre-defined values
C = 50
H = 30

D = int(input("enter number : "))                        # input the variable D
answer = math.floor(math.sqrt((2 * C * D) / H))          # calculate answer by passing through provided formula
print("the answer is {} ".format(answer))                # print answer 
```

    enter number : 150
    the answer is 22 
    

## Question 2

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1,¡ Y-1.

#### Example

Suppose the following inputs are given to the program:
    
3,5

Then, the output of the program should be:
    
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

### Version 1


```python
#define function to display matrix by accepting variables
def displayMatrix(x,y):
    dim_array = [[0 for j in range(y)] for i in range(x)]        # define array
    for i in range(x):                                           # use recurvise loop to reach entered numbers  
        for j in range(y):
            dim_array[i][j] = i * j                              # allocate array by multiplying the row and columns
    return(dim_array)                                            # return array
```


```python
x = int(input("Input the number of rows : "))                    # input the number of rows
y = int(input("Input the number of columns : "))                 # input number of columns

print("the 2-Dimensional array is : {}". format(displayMatrix(x,y)))    # display the array
```

    Input the number of rows : 3
    Input the number of columns : 5
    the 2-Dimensional array is : [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    

### Verision 2


```python
row_num = int(input("Input number of rows: "))                           # input rows
col_num = int(input("Input number of columns: "))                        # input columns
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]   # allocate array

for row in range(row_num):                                               # recursive loop to reach entered numbers  
    for col in range(col_num):                                     
        multi_list[row][col]= row*col                                    # allocate array by multiplying the row and columns

print("the 2-Dimensional array is : {}".format(multi_list))              # display the array 
```

    Input number of rows: 3
    Input number of columns: 5
    the 2-Dimensional array is : [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    

## Question 3

### Note: problem similar to Question 2

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1,¡ Y-1.

#### Example

Suppose the following inputs are given to the program:
    
3,5

Then, the output of the program should be:
    
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

### Version 1


```python
#define function to display matrix by accepting variables
def displayMatrix(x,y):
    dim_array = [[0 for j in range(y)] for i in range(x)]        # define array
    for i in range(x):                                           # use recurvise loop to reach entered numbers  
        for j in range(y):
            dim_array[i][j] = i * j                              # allocate array by multiplying the row and columns
    return(dim_array)                                            # return array
```


```python
x = int(input("Input the number of rows : "))                    # input the number of rows
y = int(input("Input the number of columns : "))                 # input number of columns

print("the 2-Dimensional array is : {}". format(displayMatrix(x,y)))    # display the array
```

    Input the number of rows : 3
    Input the number of columns : 5
    the 2-Dimensional array is : [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    

### Verision 2


```python
row_num = int(input("Input number of rows: "))                           # input rows
col_num = int(input("Input number of columns: "))                        # input columns
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]   # allocate array

for row in range(row_num):                                               # recursive loop to reach entered numbers  
    for col in range(col_num):                                     
        multi_list[row][col]= row*col                                    # allocate array by multiplying the row and columns

print("the 2-Dimensional array is : {}".format(multi_list))              # display the array 
```

    Input number of rows: 3
    Input number of columns: 5
    the 2-Dimensional array is : [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    

## Question 4

Write a program that accepts a sequence of whitespace separated words as input and prints the
words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world

#### Hints:

We use set container to remove duplicated data automatically and then use sorted() to sort the
data.

### Version 1


```python
sequencial_sentence = input("Enter a sentence seperated by whitespaces : ")                 # input sequence of words 
sequencial_sentence_spilt = sequencial_sentence.split(' ')                                  # split the words based on whitespaces 
seq_set = set(sequencial_sentence_spilt)                                                    # arrange them alphanumerically
print('\nThe output after removing duplicate words and sorting them alphanumerically is : \n',' '.join(sorted(seq_set)))    # display the arranged sentence
```

    Enter a sentence seperated by whitespaces : hello world and practice makes perfect and hello world again
    
    The output after removing duplicate words and sorting them alphanumerically is : 
     again and hello makes perfect practice world
    

### Version 2


```python
seq = input("Enter a sentence seperated by whitespaces : ")    # input sequence of words           
words = [word for word in seq.split(" ")]                      # split the words based on whitespaces 
print('\nThe output after removing duplicate words and sorting them alphanumerically is : \n'," ".join(sorted(list(set(words)))))     # arrange them alphanumerically and display the output 
```

    Enter a sentence seperated by whitespaces : hello world and practice makes perfect and hello world again
    
    The output after removing duplicate words and sorting them alphanumerically is : 
     again and hello makes perfect practice world
    

## Question 5

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5
are to be printed in a comma separated sequence.

#### Example:

0100,0011,1010,1001

Then the output should be:

1010

### Version 1


```python
bi_num = [i for i in input().split(',')]                       # input sequence and split at ','
out_seq = []                                                   # create empty array  

for j in bi_num:                                               # iterate through total number of input
    i = int(j,2) 
    if i%5 == 0:                                               # check if divisible by 5  
        out_seq.append(j)                                      # append if divisible by 5  
print(','.join(out_seq))                                       # join the numbers and display
```

    0100,0011,1010,1001
    1010
    

### Version 2


```python
out_value = []                                                  # create empty array
items=[i for i in input().split(',')]                           # input sequence and split at ','

for j in items:                                                 # iterate through total number of input
    i = int(j, 2)
    if not i%5:                                                 # check if divisible by 5
        out_value.append(j)                                     # append if divisible by 5

print(','.join(out_value))                                      # join the numbers and display 
```

    0100,0011,1010,1001
    1010
    

## Question 6

Write a program, which will find all such numbers between 1000 and 3000 (both included) such
that each digit of the number is an even number.

The numbers obtained should be printed in a comma-separated sequence on a single line.

### Version 1


```python
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
```


```python
print("the sequence is : \n\n {} ".format(",".join(even(1000,3001))))     # display array after passing through function
```

    the sequence is : 
    
     2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888 
    

### Version 2


```python
seq = []                                                     # create empty array 

for i in range(1000, 3001):                                  # iterate through the total number
    ev = str(i)
    if (int(ev[0])%2==0) and (int(ev[1])%2==0) and (int(ev[2])%2==0) and (int(ev[3])%2==0):          # check if every digit is divisible by 2
        seq.append(ev)                                       # append if every number is divisible by 2 
        
print("the sequence is : \n\n ",",".join(seq))               # return the array  
```

    the sequence is : 
    
      2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888
    

## Question 7

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3

### Version 1


```python
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
```

     Input a string : hello world! 123
    The number of letters are : 10
    The number of digits are  : 3
    

### Version 2


```python
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
```

     Input a string : hello world! 123
    LETTERS 10
    DIGITS 3
    

## Question 8

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9

Then, the output should be:

11106

### Version 1


```python
number = input("enter the digit : ")                             # input digit

p1 = int( "%s" % number )                                        
p2 = int( "%s%s" % (number,number) )
p3 = int( "%s%s%s" % (number,number,number) )
p4 = int( "%s%s%s%s" % (number,number,number,number) )

sum_of_all = p1 + p2 + p3 + p4                                   # add all value 

print("the sum value of digti is : {} ".format(sum_of_all))      # display result
```

    enter the digit : 9
    the sum value of digti is : 11106 
    

### Version 2


```python
number = input("enter number :")                                 # input digit
DIGIT = 4
res = 0
for i in range(1,DIGIT+1):                                       # add all value
    res += int(str(number)*i)                                    # mult and add 
print("the sum value of digti is : {} ".format(res))             # display result
```

    enter number :9
    the sum value of digti is : 11106 
    

## Question 9

Write a program that computes the net amount of a bank account based a transaction log from
console input. The transaction log format is shown as following:

D 100

W 200

...

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300

D 300

W 200

D 100

Then, the output should be:

500

### Version 1


```python
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
```

    --> D 300
    --> D 300
    --> W 200
    --> D 100
    --> 
    The net amount is : 500 
    

### Version 2


```python
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
```

    --> D 300
    --> D 300
    --> W 200
    --> D 100
    --> 
    The net amount is : 500 
    

## Question 10

Write a program to compute:

f(n)=f(n-1)+100 when n>0

and f(0)=1

with a given n input by console (n>0).

### version 1


```python
def f(n):                                                         # define function to accept a digit
    if n == 0:
        return 1                                                  # return 1 if number = 0 
    else:
        return f(n-1)+100                                         # perform recursive function and return value
```


```python
input_n = int(input("enter number : "))                           # input digit/value
print("f({0}) = {1}".format((input_n), f(input_n)))               # display the computed value
```

    enter number : 3
    f(3) = 301
    


```python
def f2(n):
    ans = 0
    if n == 0:
        return 1
    else:
        return f2(n-1)+100


input_n = int(input("enter number : "))

print("f({0}) = {1}".format((input_n), f2(input_n)))
```

    enter number : 3
    f(3) = 301
    

## Question 11

Segment the following short text into sentences and words:

s = u"""DTU course 02820 is taught by Mr. Bartlomiej Wilkowski,
Mr. Marcin Marek Szewczyk & Finn Arup Nielsen, Ph.D. Some of aspects
of the course are: machine learning and web 2.0. The telephone to Finn
is (+45) 4525 3921, and his email is fn@imm.dtu.dk. A book
published by O’Reilly called ’Programming Collective
Intelligence’ might be useful. It costs $39.99 or 285.00 kroner in
Polyteknisk Boghandle. Is ’Text Processing in Python’ appropriate for
the course? Perhaps! The constructor function in Python is called
"__init__()". fMRI will not be a topic of the course."""

Try both with the re module as well as with a function from nltk.

### Version 1


```python
import nltk                                                         # import nltk library

text = input("Enter the sentence : ")                               # input the sentence 

sent_text = nltk.sent_tokenize(text)                                # this gives us a list of sentences

for sentence in sent_text:                                          # now loop over each sentence and tokenize it separately
    tokenized_text = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenized_text)
    print(tagged)                                                   # print the parsed sentence
```

    Enter the sentence : u"""DTU course 02820 is taught by Mr. Bartlomiej Wilkowski, Mr. Marcin Marek Szewczyk & Finn Arup Nielsen, Ph.D. Some of aspects of the course are: machine learning and web 2.0. The telephone to Finn is (+45) 4525 3921, and his email is fn@imm.dtu.dk. A book published by O’Reilly called ’Programming Collective Intelligence’ might be useful. It costs $39.99 or 285.00 kroner in Polyteknisk Boghandle. Is ’Text Processing in Python’ appropriate for the course? Perhaps! The constructor function in Python is called "__init__()". fMRI will not be a topic of the course."""
    [('u', 'NN'), ("''", "''"), ("''", "''"), ("''", "''"), ('DTU', 'NNP'), ('course', 'NN'), ('02820', 'CD'), ('is', 'VBZ'), ('taught', 'VBN'), ('by', 'IN'), ('Mr.', 'NNP'), ('Bartlomiej', 'NNP'), ('Wilkowski', 'NNP'), (',', ','), ('Mr.', 'NNP'), ('Marcin', 'NNP'), ('Marek', 'NNP'), ('Szewczyk', 'NNP'), ('&', 'CC'), ('Finn', 'NNP'), ('Arup', 'NNP'), ('Nielsen', 'NNP'), (',', ','), ('Ph.D', 'NNP'), ('.', '.')]
    [('Some', 'DT'), ('of', 'IN'), ('aspects', 'NNS'), ('of', 'IN'), ('the', 'DT'), ('course', 'NN'), ('are', 'VBP'), (':', ':'), ('machine', 'NN'), ('learning', 'NN'), ('and', 'CC'), ('web', '$'), ('2.0', 'CD'), ('.', '.')]
    [('The', 'DT'), ('telephone', 'NN'), ('to', 'TO'), ('Finn', 'NNP'), ('is', 'VBZ'), ('(', '('), ('+45', 'NN'), (')', ')'), ('4525', 'CD'), ('3921', 'CD'), (',', ','), ('and', 'CC'), ('his', 'PRP$'), ('email', 'NN'), ('is', 'VBZ'), ('fn', 'JJ'), ('@', 'NNP'), ('imm.dtu.dk', 'NN'), ('.', '.')]
    [('A', 'DT'), ('book', 'NN'), ('published', 'VBN'), ('by', 'IN'), ('O', 'NNP'), ('’', 'NNP'), ('Reilly', 'NNP'), ('called', 'VBD'), ('’', 'RP'), ('Programming', 'NNP'), ('Collective', 'NNP'), ('Intelligence', 'NNP'), ('’', 'NNP'), ('might', 'MD'), ('be', 'VB'), ('useful', 'JJ'), ('.', '.')]
    [('It', 'PRP'), ('costs', 'VBZ'), ('$', '$'), ('39.99', 'CD'), ('or', 'CC'), ('285.00', 'CD'), ('kroner', 'NN'), ('in', 'IN'), ('Polyteknisk', 'NNP'), ('Boghandle', 'NNP'), ('.', '.')]
    [('Is', 'VBZ'), ('’', 'JJ'), ('Text', 'NNP'), ('Processing', 'NNP'), ('in', 'IN'), ('Python', 'NNP'), ('’', 'NNP'), ('appropriate', 'NN'), ('for', 'IN'), ('the', 'DT'), ('course', 'NN'), ('?', '.')]
    [('Perhaps', 'RB'), ('!', '.')]
    [('The', 'DT'), ('constructor', 'NN'), ('function', 'NN'), ('in', 'IN'), ('Python', 'NNP'), ('is', 'VBZ'), ('called', 'VBN'), ('``', '``'), ('__init__', 'NNP'), ('(', '('), (')', ')'), ("''", "''"), ('.', '.')]
    [('fMRI', 'NN'), ('will', 'MD'), ('not', 'RB'), ('be', 'VB'), ('a', 'DT'), ('topic', 'NN'), ('of', 'IN'), ('the', 'DT'), ('course', 'NN'), ('.', '.'), ("''", "''"), ("''", "''"), ("''", "''")]
    

### Version 2


```python
import re                                                             # import re library

sentence = input("Enter the sentence : ")                             # input the sentence 
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z][0-9]\.)(?<=\.|\?)\s', sentence)    # split sentence using all charecter maekers and breakers

print("the parsed sentence is : ")                                    # iterate through all words and print the parsed sentence  
for i in sentences:
        print(i)
```

    Enter the sentence : u"""DTU course 02820 is taught by Mr. Bartlomiej Wilkowski, Mr. Marcin Marek Szewczyk & Finn Arup Nielsen, Ph.D. Some of aspects of the course are: machine learning and web 2.0. The telephone to Finn is (+45) 4525 3921, and his email is fn@imm.dtu.dk. A book published by O’Reilly called ’Programming Collective Intelligence’ might be useful. It costs $39.99 or 285.00 kroner in Polyteknisk Boghandle. Is ’Text Processing in Python’ appropriate for the course? Perhaps! The constructor function in Python is called "__init__()". fMRI will not be a topic of the course."""
    the parsed sentence is : 
    u"""DTU course 02820 is taught by Mr.
    Bartlomiej Wilkowski, Mr.
    Marcin Marek Szewczyk & Finn Arup Nielsen, Ph.D. Some of aspects of the course are: machine learning and web 2.0. The telephone to Finn is (+45) 4525 3921, and his email is fn@imm.dtu.dk.
    A book published by O’Reilly called ’Programming Collective Intelligence’ might be useful.
    It costs $39.99 or 285.00 kroner in Polyteknisk Boghandle.
    Is ’Text Processing in Python’ appropriate for the course?
    Perhaps! The constructor function in Python is called "__init__()".
    fMRI will not be a topic of the course."""
    


```python
# from nltk.tokenize import TweetTokenizer, sent_tokenize

# input_text = input()

# tokenizer_words = TweetTokenizer()
# tokens_sentences = [tokenizer_words.tokenize(t) for t in nltk.sent_tokenize(input_text)]
# print(tokens_sentences)
```

    this is a sentaence. it, now deleted by 0
    [['this', 'is', 'a', 'sentaence', '.'], ['it', ',', 'now', 'deleted', 'by', '0']]
    


```python
# from nltk.tokenize import sent_tokenize

# string = "this is a sentaence. it, now deleted by 0"

# sent_tokenize_list = sent_tokenize(string)
# print(sent_tokenize_list)
```

    ['this is a sentaence.', 'it, now deleted by 0']
    

## Question 12 - 16*

Project Euler is a website with mathematical problems that should/could be solved by
computers. Go to https://projecteuler.net/archives and solve any 4 problems using Python.

As an example the problem number 16 can be solved in one line of Python:

sum(map(int, list(str(2**1000))))

1366

### Problem 1



If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.



```python
def naturalNumbersMult():                                       # define function
    sum1 = 0                                                    # set variable to 0
    for i in range(1,1000):                                     # iteate from pre defined numbers
        if i%3 == 0 or i%5 == 0:                                # check if divisible by 3 or 5
            sum1 += i                                           # if it is then add it to sum
    return sum1                                                 # return the result 
```


```python
print(naturalNumbersMult())                                     # display result
```

    233168
    

### Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.



```python
def evenFib():                                                  # define function                   
    fib_list = [1,2]                                            # define array 
    i = 1
    sum1 = 2
    while True:                                                 # run forever till stopped 
        fib_list.append(fib_list[i-1] + fib_list[i])
        if fib_list[i+1] > 4000000:                             # check condition 
            break                                               # break loop
        if fib_list[i+1]%2 == 0:                                # check if digit divisible by 0
            sum1 += fib_list[i+1]                               # add to sum if divisible
        i +=1                                                    
    return (fib_list, sum1)                                     # return result
```


```python
print("the terms of the fib list are : \n {} ".format(evenFib()[0]))     # display all the terms 
print("\nthe sum of even valued terms : {}".format(evenFib()[1]))        # display the total result 
```

    the terms of the fib list are : 
     [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887] 
    
    the sum of even valued terms : 4613732
    

### Problem 3



The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


```python
import math                                                       # import library
```


```python
def isPrimeNumber(n):                                             # define function and check conditoins
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:                     
            return False
        i +=6
    return True                                                   # return respective conditon
```


```python
def largestPrimeFactor(n):                                        # define function
    largest_prime = 0                                             # set varibale to 0
    for i in range(1,int(math.sqrt(n))-1):                        # iterate the provided number(sqrt)
        if isPrimeNumber(i) and n%i==0:                           # check if the number is prime using defined function
            largest_prime = i
    return largest_prime                                          # return result
```


```python
print(largestPrimeFactor(600851475143))                           # display result
```

    6857
    

### Problem 4



A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.



```python
def isPalindrome(n):                                               # define function   
    if str(n)==str(n)[::-1]:                                       # check if string is a palandrome
        return True                                                # return true is palandrome  
    else:
        return False
```


```python
def largestProductPalindrome():                                    # define function 
    max_product = 0                                                # set variable to 0 
    for i in range(100,1000):                                      # iterate through provided range
        for j in range(100,1000):
            product = i * j
            if product > max_product and isPalindrome(product):    # check if palandrome using defined function  
                max_product = product                              # update if value is greater 
    return max_product                                             # return result 
```


```python
print(largestProductPalindrome())                                  # display result
```

    906609
    
