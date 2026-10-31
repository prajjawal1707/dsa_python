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

# Longest Palindromic Substring
# s = "cbbd"
# start = 0
# max_length = 0
# for i in range(len(s)):
#     # Case 1: Odd-length palindrome
#     left = i
#     right = i
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         if right - left + 1 > max_length:
#             start = left
#             max_length = right - left + 1
#         left -= 1
#         right += 1
#     # Case 2: Even-length palindrome
#     left = i
#     right = i + 1
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         if right - left + 1 > max_length:
#             start = left
#             max_length = right - left + 1
#         left -= 1
#         right += 1
# print(s[start:start + max_length])


# s = "cbbd"
# i = 0
# j = len(s)
# d_a_ = s[i:j]
# # print(d_a_)
# palindrom = True
# while i < j:
#     if s != s[::-1]:                                          it fails at "a"
#         palindrom = False
#         break
#     i += 1
#     j -= 1
# if not palindrom:
#     d_a_ = s[i+1:j]
#     i = i+1
# elif not palindrom:
#     d_a_ = s[i:j+1]
#     j = j-1
# print(d_a_)

# s = "babad"
# i = 0
# j = len(s)-1
# d_a_ = s[i:j]
# palindrom = True
# while i<j:
#     if s[i] != s[j]:
#         palindrom = False
#         break                                       it fails at "cbbd"               
#     i += 1
#     j -= 1
# if not palindrom:
#     d_a_ = s[i+1:j]
#     i = i+1
# elif not palindrom:
#     d_a_ = s[i:j-1]
#     j = j-1
# print(d_a_)


# Palindromic Substrings
# s = "aaa"
# count = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         if (s[i:j]) == s[i:j][::-1]:
#             count += 1
# print(count)

# Container With Most Water

# height = [1,8,6,2,5,4,8,3,7]
# i = 0
# max_area = 0
# for i in range(len(height)):
#     for j in range(len(height)):
#         length = (i-j)
#         a = height[i]
#         b = height[j]
#         c_ht = min(a,b)
#         area = (c_ht * length)
#         if area > max_area:
#             max_area = area
# print(max_area)

# this is my way of solving Container With Most Water this it's cmplexity is o(n^2)

# height = [1,8,6,2,5,4,8,3,7]
# i = 0
# j = len(height)-1
# max_area = 0
# while i < j:
#     a = height[i]
#     b = height[j]
#     length = j-i
#     c_ht = min(a,b)
#     area = (c_ht * length)
#     if area > max_area:
#         max_area = area
#     if a < b:
#         i = i+1
#     else:
#         j = j-1
# print(max_area)

# this is the stardard way of solving this way by using two pointers 