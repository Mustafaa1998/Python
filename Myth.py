
# coding: utf-8

# # Primitive Types

# ## Integer

# In[5]:


x = int(input("Enter the 1st Number: "))
y = int(input("Enter the 2nd Number: "))
sum = x + y
print ("Your Answer Is:" ,sum)


# ## Float

# In[7]:


import math
x = float(input("Enter the value of x: "))
SquareRoot = math.sqrt(x)
print("Square Root of The Given Number: " , SquareRoot)


# ## Boolean

# In[11]:


Bilal_age = int(input("Enter the Bilal Age:" ))
Hassan_age = int(input("Enter the Hassan Age:" ))
eligibility = Bilal_age >= Hassan_age
print("Hassan is elder Than Bilal: ",eligibility)


# ## Strings

# In[63]:


name = "muhammad Mustafa"
print(name.capitalize())
name1 = "MUSTAFA"
print(name1.casefold())
print(name1.center(10))
Sentence = "you had a great day"
print(Sentence.count("day"))
print(Sentence.find("g"))
age = "33"
print(age.isalpha())
print(age.isdecimal())
print(age.isnumeric())
print(Sentence.istitle())
print(name.replace("muhammad", "Muhammad"))


# # Slicing

# In[65]:


Email = (input("Enter Your Email: " ))
print(Email[2:9])


# # String Indexing

# In[77]:


name = "Muhammad Mustafa"
print(name[0:-1])
print(name[0:-4])
print(name[0:8])
print(name[9:16])

