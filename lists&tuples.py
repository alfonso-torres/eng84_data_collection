# What is a List
# Lists is commonly used to store the data
# Lists are MUTEBALE
# Syntax [] used to create a list

shopping_list = ["bread", "chocolate", "avacados", "milk"]
              #    0           1           2         3

# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[1])
# print(shopping_list[-2])
# change the value of 0 index from bread to orange
# shopping_list[0] = "orange"
# print(shopping_list)
# print(shopping_list[0])

# add a value in to the list at the end
# shopping_list.append("ice-cream")
# print(shopping_list)

# delete the item 0 to the list
# shopping_list.remove("orange")
# print(shopping_list)
# pop() deletes the last item from the list
# shopping_list.pop()
# print(shopping_list)

# Can we mix data types in a list? Yes
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)

print(mixed_list[1:3])
