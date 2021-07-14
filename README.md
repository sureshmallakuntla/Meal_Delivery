# Meal_Delivery
Meal Delivery Database contains different types of meals available in various Countries.

## Importing modules
  ```
  import pymongo 
  import pprint
  import warnings
  from pymongo import MongoClient
  ```
  
 ## Connect to MongoDB instance
 ```
 
 client=pymongo.MongoClient('localhost',PortNumber)
 ```
### Creating a Database
```
db = client['mealinfoDB']
```

### Creating a Collection
```
collection=db["meal_info"]
```

## Commands used in this project:

1.Insert_many()

2.Insert_one()

3.Delete_one()

4.Find()

5.Sort()

6.Limit()

7.Find_one()

8.Delete_many()

9.Update_many()

10.Drop()
