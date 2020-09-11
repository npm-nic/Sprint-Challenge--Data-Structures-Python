import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# ----------> o(n^2) ... polynomial <----------
'''
# Replace the nested for loops below with your improvements
for name_1 in names_1: # o(n)
    for name_2 in names_2: # o(n)
        if name_1 == name_2:
            duplicates.append(name_1) # o(c)
'''
# ----------> o(n) ... linear <----------
# create empty {} to hold names
# FOR: all names in names_1
    # add to a dictionary
# FOR: names in name_2
    # IF: name is already in names {}
        # add into duplicates (line 13) 
names = {}
for name in names_1:
    names[name] = True
for name in names_2:
    if name in names:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
