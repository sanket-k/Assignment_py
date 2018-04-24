
# coding: utf-8

# ### Question 11

# Segment the following short text into sentences and words:
# 
# s = u"""DTU course 02820 is taught by Mr. Bartlomiej Wilkowski,
# Mr. Marcin Marek Szewczyk & Finn Arup Nielsen, Ph.D. Some of aspects
# of the course are: machine learning and web 2.0. The telephone to Finn
# is (+45) 4525 3921, and his email is fn@imm.dtu.dk. A book
# published by O’Reilly called ’Programming Collective
# Intelligence’ might be useful. It costs $39.99 or 285.00 kroner in
# Polyteknisk Boghandle. Is ’Text Processing in Python’ appropriate for
# the course? Perhaps! The constructor function in Python is called
# "__init__()". fMRI will not be a topic of the course."""
# 
# Try both with the re module as well as with a function from nltk.

# ### Version 1

# In[18]:


import nltk                                                         # import nltk library

text = input("Enter the sentence : ")                               # input the sentence 

sent_text = nltk.sent_tokenize(text)                                # this gives us a list of sentences

for sentence in sent_text:                                          # now loop over each sentence and tokenize it separately
    tokenized_text = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenized_text)
    print(tagged)                                                   # print the parsed sentence


# ### Version 2

# In[19]:


import re                                                             # import re library

sentence = input("Enter the sentence : ")                             # input the sentence 
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z][0-9]\.)(?<=\.|\?)\s', sentence)    # split sentence using all charecter maekers and breakers

print("the parsed sentence is : ")                                    # iterate through all words and print the parsed sentence  
for i in sentences:
        print(i)


# In[10]:


# from nltk.tokenize import TweetTokenizer, sent_tokenize

# input_text = input()

# tokenizer_words = TweetTokenizer()
# tokens_sentences = [tokenizer_words.tokenize(t) for t in nltk.sent_tokenize(input_text)]
# print(tokens_sentences)


# In[9]:


# from nltk.tokenize import sent_tokenize

# string = "this is a sentaence. it, now deleted by 0"

# sent_tokenize_list = sent_tokenize(string)
# print(sent_tokenize_list)

