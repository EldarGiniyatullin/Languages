
# coding: utf-8

# In[4]:

a, b = (int(i) for i in input().split()) # does not work in Python2
print(True if a == b else False)
print(a == b and True or False) # how does it work?


# In[5]:

genome = 'ATGG'
# genome[2] = 'S' -- mistake
for i in genome:
    print(i)


# In[ ]:



