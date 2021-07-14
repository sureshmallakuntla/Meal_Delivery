#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing packages
import pymongo
from pymongo import MongoClient


# In[2]:


#Connection to MongoDB instance
client = pymongo.MongoClient('localhost',27017)


# In[3]:


#Creating a Database
db = client['mealinfoDB']


# In[4]:


#Creating a Collection
collection=db["mealinfo"]


# In[5]:


#meal_info
record  = [{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},
           {"meal_id":1993,"category":"Beverages","cuisine":"Thai"},
           {"meal_id":2539,"category":"Beverages","cuisine":"Thai"},
           {"meal_id":1248,"category":"Beverages","cuisine":"Indian"},
           {"meal_id":2631,"category":"Beverages","cuisine":"Indian"},
           {"meal_id":1311,"category":"Extras","cuisine":"Thai"},
           {"meal_id":1062,"category":"Beverages","cuisine":"Italian"},
           {"meal_id":1778,"category":"Beverages","cuisine":"Italian"},
           {"meal_id":1803,"category":"Extras","cuisine":"Thai"},
           {"meal_id":1198,"category":"Extras","cuisine":"Thai"},
           {"meal_id":2707,"category":"Beverages","cuisine":"Italian"},
           {"meal_id":1847,"category":"Soup","cuisine":"Thai"},
           {"meal_id":1438,"category":"Soup","cuisine":"Thai"},
           {"meal_id":2494,"category":"Soup","cuisine":"Thai"},
           {"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},
           {"meal_id":2490,"category":"Salad","cuisine":"Italian"},
           {"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},
           {"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},
           {"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},
           {"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},
           {"meal_id":1878,"category":"Starters","cuisine":"Thai"},
           {"meal_id":2640,"category":"Starters","cuisine":"Thai"},
           {"meal_id":2577,"category":"Starters","cuisine":"Thai"},
           {"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},
           {"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},
           {"meal_id":2306,"category":"Pasta","cuisine":"Italian"},
           {"meal_id":2139,"category":"Beverages","cuisine":"Indian"},
           {"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},
           {"meal_id":2664,"category":"Salad","cuisine":"Italian"},
           {"meal_id":2569,"category":"Salad","cuisine":"Italian"},
           {"meal_id":1230,"category":"Beverages","cuisine":"Continental"},
           {"meal_id":1207,"category":"Beverages","cuisine":"Continental"},
           {"meal_id":2322,"category":"Beverages","cuisine":"Continental"},
           {"meal_id":2492,"category":"Desert","cuisine":"Indian"},
           {"meal_id":1216,"category":"Pasta","cuisine":"Italian"},
           {"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},
           {"meal_id":1902,"category":"Biryani","cuisine":"Indian"},
           {"meal_id":1247,"category":"Biryani","cuisine":"Indian"},
           {"meal_id":2304,"category":"Desert","cuisine":"Indian"},
           {"meal_id":1543,"category":"Desert","cuisine":"Indian"},
           {"meal_id":1770,"category":"Biryani","cuisine":"Indian"},
           {"meal_id":2126,"category":"Pasta","cuisine":"Italian"},
           {"meal_id":1558,"category":"Pizza","cuisine":"Continental"},
           {"meal_id":2581,"category":"Pizza","cuisine":"Continental"},
           {"meal_id":1962,"category":"Pizza","cuisine":"Continental"},
           {"meal_id":1571,"category":"Fish","cuisine":"Continental"},
           {"meal_id":2956,"category":"Fish","cuisine":"Continental"},
           {"meal_id":2104,"category":"Fish","cuisine":"Continental"},
           {"meal_id":2444,"category":"Seafood","cuisine":"Continental"},
           {"meal_id":2867,"category":"Seafood","cuisine":"Continental"},
           {"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[6]:


#insert_many
db.mealinfo.insert_many(record)


# In[7]:


for i in record:
    print(i)


# In[8]:


#insert_one
rec={"meal_id":2000,"category":"sandwich","cuisine":"Indian"}
db.mealinfo.insert_one(rec)


# In[9]:


#delete
recor = {"meal_id":1445,"category":"Seafood","cuisine":"Continental"}
db.mealinfo.delete_one(recor)


# In[10]:


#find
db.mealinfo.find()


# In[11]:


for i in record:
    print(i)


# In[12]:


#find()
var1=db.mealinfo.find({"category":"Beverages"})


# In[13]:


for i in var1:
    print(i)


# In[14]:


#find_one
db.mealinfo.find_one({"category":"Beverages"})


# In[15]:


#sort
var5=db.mealinfo.find().sort("_id",1)


# In[16]:


for i in var5:
    print(i)


# In[17]:


#limit
db.mealinfo.find().limit(5)


# In[18]:


#del-many
db.mealinfo.delete_many({})


# In[19]:


#update_many
record1 = {"meal_id":1247,"category":"Biryani","cuisine":"Indian"}
var7=db.mealinfo.update_many({"meal_id":72},{"$set":record1})


# In[20]:


#Drop
db.mealinfo.drop()


# In[21]:


print(db.mealinfo.find().count())


# In[ ]:





# In[ ]:




