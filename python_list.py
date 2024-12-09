print ("\n------- Lists -------\n")

my_list = ["dog", "cat", "rabbit", "parrot"]
print (my_list, type(my_list))
print (my_list[3], type(my_list[3]))
# print (my_list[5]) # IndexError: list index out of range

print ("\n------- Lists can have diffrent typed values -------\n")
my_list = [1, 2, "cat", 4, 5]
print (my_list, type(my_list))

print ("\n------- Assigning to a value to the list -------\n")
my_list[1] = "dog"
print (my_list, type(my_list))

print ("\n------- List size (length) -------\n")
print (len(my_list))

print ("\n------- Negative indexing mechanism -------\n")
print (my_list[-1])
print (my_list[-2])

print ("\n------- Fetch desired value set from an array -------\n")
print (my_list[1:4], type(my_list[1:4]))
print (my_list[:3], type(my_list[:3]))
print (my_list[2:], type(my_list[2:]))

my_list = [10, 5, "Cat", "Dog", True]
my_list[1:3] = ["Parrot", 17.0]
print (my_list, type(my_list))

print ("\n------- Insert and append -------\n")
my_list.insert(2, "Rabbit")
print(my_list, len(my_list))

my_list.append("Tiger")
print(my_list, len(my_list))

print ("\n------- Extend an array to another array -------\n")
another_list = ["Lion", "Elephant"]
my_list.extend(another_list)
print(my_list, len(my_list))

print ("\n------- pop() -------\n")
my_list.pop(2)
print(my_list, len(my_list))

print ("\n------- del -------\n")
del my_list[2]
print(my_list, len(my_list))

del my_list # delete / destroy the entire list
# print(my_list) # NameError: name 'my_list' is not defined

print ("\n------- clear() -------\n")
my_list = [10, 5, "Cat", "Dog", True]
my_list.clear()
print(my_list, len(my_list))

print ("\n------- Sorting the list -------\n")
my_list = ["grapes", "apple", "orange", "banana"]
my_list.sort()
print(my_list, len(my_list))

my_list = ["Grapes", "apple", "orange", "banana"]
my_list.sort()
print(my_list, len(my_list))

my_list.sort(key = str.lower)
print(my_list, len(my_list))

my_list = [5, 3, 10, 25, 8]
my_list.sort()
print(my_list, len(my_list))

my_list.sort(reverse = True)
print(my_list, len(my_list))