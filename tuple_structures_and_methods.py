# tuple_practice.py

# --- 1. Sequence Metrics & Basics ---
a = ('praveen', 'ajay', 'san', 'sammu', 'praveen')
print(type(a))                  # <class 'tuple'>
print(a.index('praveen'))       # 0 (First occurrence)
print(len(a))                   # 5
print(a.count('praveen'))       # 2
print(dir(a))                   # Lists all tuple methods

# --- 2. Slicing and Strides ---
print(a[0:3])                   # ('praveen', 'ajay', 'san')
print(a[0:5:1])                 # ('praveen', 'ajay', 'san', 'sammu', 'praveen')
print(a[0::])                   # Same as above
print(a[0::2])                  # ('praveen', 'san', 'praveen') -> step by 2

# Reversing a tuple
a_alt = ('praveen', 'ajay', 'san', 'satish', 'praveen')
print(a_alt[-1::-1])            # ('praveen', 'satish', 'san', 'ajay', 'praveen')

# --- 3. Concatenation & Nested Slicing ---
b = ('sun', 'fun', 'run')
c = a_alt + b
print(c)                        # Merged tuple
print(a_alt[0][2:5])            # 'ave' (Slicing characters out of string at index 0)
print(a_alt[3][2:5])            # 'tis' (Slicing characters out of string at index 3)

# --- 4. Membership & Logical Operators ---
print('praveen' in a_alt)       # True
print('sumit' not in a_alt)     # True

# Compound conditions
print('praveen' in a_alt and 'sumit' in a_alt)  # False
print('praveen' in a_alt or 'sumit' in a_alt)   # True

# --- 5. Case Modification & Formatting ---
print(a_alt[0].isupper())       # False
print(a_alt[0].upper())         # 'PRAVEEN'
print("_".join(a_alt))          # 'praveen_ajay_san_satish_praveen'
print(a_alt[0].split('e'))      # ['prav', '', 'n']
