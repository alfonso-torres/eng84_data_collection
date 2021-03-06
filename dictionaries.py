# Dictionaries?
# Dictionaries use KEY VALUE pairs to save the data
# The data can be retrieved by its value or the key
# Syntax dict{} List[] Tuple()
# With in the dict we can also have list declared

print("---------------------------Dictionary---------------------------")
# Let's create one
dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lesson": 3,
    "completed_lessons_name": ["variables", "data types", "collections"]
    # Key              value:      0              1              2
}

print(dev_ops_student)
# confirm the type
print(type(dev_ops_student))

print((dev_ops_student["name"]))
print(dev_ops_student["completed_lesson"])
print(dev_ops_student["completed_lessons_name"][1])

print(dev_ops_student.keys())
print(dev_ops_student.values())

# add "operators" as a value of completed_lessons_names
dev_ops_student["completed_lessons_name"].append("operators")
print(dev_ops_student["completed_lessons_name"])

# change the completed lesson from 3 to 4
dev_ops_student["completed_lesson"] = 4
print(dev_ops_student["completed_lesson"])

# remove the "data types" from completed_lesson_names
# dev_ops_student["completed_lessons_name"].pop(1)
# dev_ops_student["completed_lessons_name"].pop(dev_ops_student["completed_lessons_name"].index("data types"))
dev_ops_student["completed_lessons_name"].remove("data types")
print(dev_ops_student["completed_lessons_name"])

print("---------------------------Dictionary---------------------------")

print("---------------------------Set---------------------------")
# Sets? The difference is that Sets are unordered
# They are MUTABLE
# Syntax {}

# Let's create a set

car_parts = {"wheels", "windows", "doors"}
print(car_parts)
print(type(car_parts))
car_parts.add("seats")
print(car_parts)
car_parts.discard("doors")
print(car_parts)

print("---------------------------Set---------------------------")

# Forzen sets -
# The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
# fSet.add('v')
