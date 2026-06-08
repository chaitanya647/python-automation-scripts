# =====================================================================
# MODULE: dictionary_and_nested_structures.py
# AUTHOR: Chaitanya Chintappanavar
# DESCRIPTION: Deep dive into mutable mappings (dictionaries) and 
#              multi-dimensional compound data structures.
# =====================================================================

# --- SECTION 1: Dictionary Metadata, Views, and Type Casting ---
print("--- SECTION 1 ---")
adict = {'praveen': '10', 'ajay': '20', 'datta': '30', 'kavya': '40', 'nanda': '50', 'besant': '100'}
print("Data Type:", type(adict))
print("Dictionary Length:", len(adict))
print("Dictionary Keys View:", adict.keys())
print("Dictionary Values View:", adict.values())

# Casting dict views into independent lists
keylist = list(adict.keys())
valuelist = list(adict.values())
print("Casted Key List:", keylist)
print("Casted Value List:", valuelist)
print("Dictionary Items View (Key-Value Tuples):", adict.items())


# --- SECTION 2: Key Retrieval, Value Mutation, and Membership ---
print("\n--- SECTION 2 ---")
adict = {'praveen': '10', 'ajay': '20', 'datta': '30', 'kavya': '40', 'nanda': '50', 'besant': '100'}
print("Value of key 'praveen':", adict['praveen'])

adict['kavya'] = "60"
print("After modifying 'kavya' value:", adict)

adict['satish'] = '55'
print("After adding new key-value pair 'satish':", adict)

print("Is 'praveen' a key in adict?", 'praveen' in adict)
print("Is value of 'praveen' equal to '10'?", adict['praveen'] == "10")


# --- SECTION 3: Dynamic Runtime Key-Value Assignment ---
print("\n--- SECTION 3 ---")
adict = {'praveen': '10', 'ajay': '20', 'datta': '30', 'kavya': '40', 'nanda': '50', 'besant': '100'}

# Simulating automation input strings
keych = input("Enter the key to add/modify:\n")
vall = input("Enter the value for that key:\n")
adict[keych] = vall
print("Updated Dictionary after user input:", adict)


# --- SECTION 4: Map Merging and Destructive Pops ---
print("\n--- SECTION 4 ---")
adict = {'praveen': '10', 'ajay': '20', 'datta': '30', 'kavya': '40', 'nanda': '50', 'besant': '100'}
bdict = {'joy': '77', 'fun': '18'}

adict.update(bdict)
print("After merging bdict using .update():", adict)

# Destructive removal operations
adict.popitem()
print("After .popitem() (Removes last inserted item/LIFO order):", adict)

adict.pop('datta')
print("After .pop('datta') (Removes specific key):", adict)


# --- SECTION 5: Multi-Dimensional Complex Compound Structures ---
print("\n--- SECTION 5 ---")
# A complex array matrix nesting Dictionaries, Tuples, and Lists together
final = [
    {'a': '10', 'b': '44', 'c': '66'}, 
    ('10', '20', '30'), 
    [66, {'joy': 'fun'}], 
    {'p': '88', 'nn': '88'}, 
    {'vv': '22'}
]

print("Type of compound structure:", type(final))
print("Length of outer list structure:", len(final))

print("\n--- Deep Nested Navigation Matrix ---")
print("Targeting index 4 dict key 'vv':", final[4]['vv'])
print("Targeting index 1 tuple:", final[1])
print("Targeting index 1 tuple, sub-index 0 element:", final[1][0])
print("Targeting index 0 dict:", final[0])
print("Targeting index 0 dict key 'c':", final[0]['c'])
print("Targeting index 2 internal list:", final[2])
print("Targeting index 2 list, sub-index 0 element:", final[2][0])
print("Targeting index 2 list, sub-index 1 nested dict:", final[2][1])
print("Targeting index 2 list -> sub-index 1 dict -> key 'joy':", final[2][1]['joy'])
