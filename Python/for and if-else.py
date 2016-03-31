
# coding: utf-8

# In[4]:

a, b = (int(i) for i in input().split()) # does not work in Python2
print(True if a == b else False)
print(a == b and True or False) # how does it work?


# In[5]:

genome = 'ATGG'
# genome[2] = 'S' -- mistake
# for lists - genome.insert(2, A) == ['A', 'T', 'A', 'G', 'G']
for i in genome:
    print(i)

# strings are lists too!

guests = ['Ivan', 'Masha', 'Sasha']
guests += ['Olga']
guests += 'Olga'
print(len(guests)) # == 8 (!)
print(guests) # ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']
