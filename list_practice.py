# list_practice.py

# --- 1. List Basics & Metrics ---
alist = ['praveen', 'ajay', 'san', 'kiran', 'sumit', 'praveen', 'sahil', 'srushthi']
print(alist)
print(type(alist))                   # <class 'list'>
print(len(alist))                    # 8
print(alist.count('praveen'))        # 2
print(alist.index('sumit'))          # 4
print(dir(alist))                    # Lists all list methods

# --- 2. Membership & Advanced Slicing ---
print('praveen' in alist)            # True
print('sahil' in alist)              # True
print(alist[6] == "sahila")          # False ('sahil' != 'sahila')
print(alist[3] + alist[5])           # 'kiranpraveen' (Concatenation)

# Slicing and Strides
print(alist[2:7])                    # ['san', 'kiran', 'sumit', 'praveen', 'sahil']
print(alist[2:7:2])                  # ['san', 'sumit', 'sahil'] (Step by 2)
print(alist[-1:-6:-1])               # ['srushthi', 'sahil', 'praveen', 'sumit', 'kiran'] (Reverse)

# --- 3. Nested Indexing & String Methods ---
alist_mod = ['praveen', 'ajay', 'sAn', 'kiraz', 'sumit', 'praveen', 'sahil', 'srushthi']
print(alist_mod[0][3] + alist_mod[3][2])  # 'vr' ('v' from praveen, 'r' from kiraz)

mk = alist_mod[0] + alist_mod[3]     # 'praveenkiraz'
print('z' in mk)                     # True
print('z' in alist_mod[0] + alist_mod[3]) # True

# Case transformations
print(alist_mod[2].islower())        # False (Due to capital 'A' in 'sAn')
print(alist_mod[2].upper())          # 'SAN'
print(alist_mod[2].swapcase())       # 'SaN'

# --- 4. Dynamic User Input Validation ---
alist_final = ['praveen', 'ajay', 'san', 'kiraz', 'sumit', 'praveen', 'sahil', 'srushthi']
print('a' in alist_final[2])         # True
print(alist_final[0][2] == alist_final[2][1]) # True ('a' == 'a')

# Runtime console input matching
user_element = input("Enter the element to be checked:\n")
user_position = int(input("Enter the position index of element:\n"))

print(alist_final[user_position] == user_element)
print("Element index matches:", alist_final.index(user_element))
