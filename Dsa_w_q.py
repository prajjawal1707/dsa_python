# Linear serach 

# arr = [5,2,8,1]
# target = 8
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)

# Practice:
# - Search for an element
# - Count occurrences
# - First occurrence


# Binary Search 
# it used in only sorted array --
# first last and middle element we solve it like this

# practice
# Maximum element
# Second largest
# Move all zeros to the end
# Remove duplicates (sorted array)
# Check if array is sorted

# Character Frequency
# Count how many times each character appears.
# Using a dictionary:

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)

# Practice Problems
# Solve:
# - Reverse string
# - Palindrome
# - Count vowels
# - Count words
# - Remove spaces
# - Find first non-repeating character

# Traversing an array 
# arr = [10, 20, 30]
# for x in arr:
#     print(x)
# arr = [10, 20, 30]
# for i in range(len(arr)):
#     print(arr[i])

# For traversing an array, both methods have linear time complexity, 
# (O(n)). Prefer for x in arr when you only need the elements. Use for 
# i in range(len(arr)) when you need the index to access or modify elements.

# A set stores unique elements. Adding 5 twice does not create two copies.
# seen = set()
# seen.add(5)
# seen.add(3)
# seen.add(5)
# print(seen)


# count = {}
# count[5] = 2
# count[3] = 1
# print(count)
# A dictionary stores key-value pairs.
# ------------------------------------------------------------------------------------------
# seen = set() → Have I seen this element before?
# count = {} → How many times have I seen this element?
# seen = {} is actually an empty dictionary, not a set. Use set() for an empty set.
# ------------------------------------------------------------------------------------------

# s = "A man, a plan, a canal: Panama" -- #in this type of question we have to ignore the ,: so we use here
# char.isalnum() -- # by this it will only store the word so after that it will ignore the ,:""
