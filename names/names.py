import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# making new list with all names
names_3 = names_1 + names_2
# setting up a blank dict
names_dict = {}
# setting up a duplicates list
dup_list = []

# use a for loop with if/else statement
# simplifying the problem to a binary choice
for i in names_3:
    if i in names_dict:
        # if name appears more than once, count up &
        names_dict[i] += 1
        # append it to the duplicates list
        dup_list.append(i)
    else:
        # set name to 1
        names_dict[i] = 1


end_time = time.time()
print (f"{len(dup_list)} duplicates:\n\n{', '.join(dup_list)}\n\n")
# 0.0086 seconds
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
