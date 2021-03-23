# Data Collections in Python

- List and Typles
- Dictionary
- Sets 


### *What is list?* <br/>
- Lists is commonly used to store the data.
- Lists are MUTEBALE.
- Syntax [] used to create a list.
- Indexing a list in Python starts from 0 <br/>
````python
shopping_list = ["bread", "chocolate", "avocados", "milk"]
````
The position of "bread" is `0` = shopping_list[0] <br/>
  The position of "chocolate" is `1` = shopping_list[1] <br/>
  The position of "avocados" is `2` = shopping_list[2] <br/>
  The position of "milk" is `3` = shopping_list[3] <br/>
  
- Different data types can be mixed in the same list
````python
mixed_list = ["bread", "chocolate", "avacados", "milk", 1,2,3]
````
- List methods:
1. We can modify a value from the list as follows:
````python
shopping_list[0] = "orange"
````
2. Add one more element to the end of the list:
````python
shopping_list.append("ice-cream")
````
3. Delete any item from the list or delete the last item from the list:
````python
shopping_list.remove("orange")
````
4. Delete the last item from the list:
````python
shopping_list.pop()
````
5. Delete the item at the given index:
````python
shopping_list.pop(0)
````
6. We can use slices with list:
````python
shopping_list[0:3] # The values from the index 0 to 2 is printed
````
  
### *What is tuple?* <br/>
- Tuples are used to store multiple items in a single variable.
- Tuples are exactly the same as Lists, but they are IMMUTABLE.
- Syntax () used to create a Tuple:
````python
essential = ("paracetamol", "tooth paste", "tea bags")
````
- A tuple is a collection wich is ordered and unchangeable.
- Tuple methods, the same methods can be applied to tuples and list, except for those which can change data:
1. We can use slices with list:
````python
print(essential[0:2]) # The values from the index 0 to 1 is printed
````

### *What is dictionary?* <br/>
- A dictionary consists of a collection of KEY-VALUE pairs.
- Each KEY-VALUE pair maps the key to its associated value.  
- Dictionaries use KEY-VALUE pairs to save the data.
- Syntax dict{} :
````python
dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lesson": 3,
    "completed_lessons_name": ["variables", "data types", "collections"]
    # Key              value:      0              1              2
}
````
- The values can be any type of data
- The data can be retrieved by its value or the key:
````python
print((dev_ops_student["name"])) # value is printed
print(dev_ops_student["completed_lesson"]) # 3 is printed
print(dev_ops_student["completed_lessons_name"][1]) # data types is printed
````
- To get all the KEYs and all the VALUEs:
````python
print(dev_ops_student.keys())
print(dev_ops_student.values())
````
- Add a value in the list with the key "completed_lessons_name":
````python
dev_ops_student["completed_lessons_name"].append("operators")
````
- Change the value of any key:
````python
dev_ops_student["completed_lesson"] = 4
````
- Remove any element from the list with the key "completed_lessons_name":
````python
dev_ops_student["completed_lessons_name"].remove("data types")
````

### *What is sets?* <br/>
- Sets are used to store multiple items in a single variable.
- They are MUTABLE. 
- The difference is that Sets are unordered.
- They return the values in random order.  
- Syntax {} :
````python
car_parts = {"wheels", "windows", "doors"}
````
- We can add elements:
````python
car_parts.add("seats")
````
- We can remove elements:
````python
car_parts.discard("doors")
````
