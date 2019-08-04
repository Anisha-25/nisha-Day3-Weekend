#!/usr/bin/env python
# coding: utf-8

# In[1]:


bicycles = ['hero','ranger','bmx','redline']
print (bicycles)
print(bicycles[1])
print(bicycles[3])


# In[2]:


bicycles = ['hero','ranger','bmx','redline']
print (bicycles[0].title())
print(bicycles[1].upper())


# In[4]:


bicycles = ['hero','ranger','bmx','redline']
message = f"My first bicycle was {bicycles[1].title()}."
print(message)


# In[5]:


motorcycles=['honda','yamaha','suzuki']
print(motorcycles) 
motorcycles[0]='ducati'
print(motorcycles)


# In[7]:


motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)


# In[8]:


motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(1,'ducati')
print(motorcycles)


# In[9]:


car =[ ]
car.append('audi')
car.append('bmw')
car.append('volvo')
car.append('swift')
print(car)


# In[10]:


motorcycles=['honda','yamaha','suzuki']
del motorcycles[2]
print(motorcycles)


# In[11]:


motorcycles=['honda','yamaha','suzuki']
motorcycles.pop(1)
print(motorcycles)


# In[12]:


motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.sort()
print(motorcycles)


# In[13]:


motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.reverse()
print(motorcycles)
print(len(motorcycles))


# In[ ]:




