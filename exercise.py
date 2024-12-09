my_list_1 = [12, 10, 13, 4, 1, 5]
my_list_2 = [6, 1, 7, 8, 9]

# 1) Find Median
my_list_1.extend(my_list_2)
my_list_1.sort()

length_of_the_array = len(my_list_1)
position_of_median = (length_of_the_array + 1) / 2

# cast inorder to convert in to int
position_of_median = int(position_of_median)

median = my_list_1[position_of_median - 1]

print(f"The median of the combined list is: {median}")


# Find Q1 
position_of_q1 = (len(my_list_1) + 1) / 4
position_of_q1 = int(position_of_q1)
value_of_q1 = my_list_1[position_of_q1 - 1]

print(f"The first quartile (Q1) of the combined list is: {value_of_q1}")


# Find Q3
position_of_q3 = (len(my_list_1) + 1) * 3 / 4
position_of_q3 = int(position_of_q3)
value_of_q3 = my_list_1[position_of_q3 - 1]

print(f"The third quartile (Q3) of the combined list is: {value_of_q3}")
