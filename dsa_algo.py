# ----------------------------------------------------------------------------------
# 1 traversing an array

# arr= [10,20,30]
# for x in arr:
#     print(x)
#               or 

# arr = [10,20,30]
# for i in range(len(arr)):
#     print(arr[i])

# ----------------------------------------------------------------------------------
# 2. Sum of  array

# arr = [5,10,15]
# total = 0
# for num in arr:
#     total = num + total
# print(total)

# ----------------------------------------------------------------------------------
# 3. Find Largest number

# arr= [4,9,2,15,8]
# largest = arr[0]
# for num in arr:
#     if num > largest:
#         largest = num
# print(largest)

# ----------------------------------------------------------------------------------
# 4 Find smallest number

# arr = [4,9,2,15,8]
# smallest = arr[0]
# for num in arr:
#     if num < smallest:
#         smallest = num
# print(smallest)
# ----------------------------------------------------------------------------------
# 5 linear search

# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found at", i)

# ----------------------------------------------------------------------------------
# 6 reverse using two pointers

# arr= [10,20,30,40,50]
# left =0
# right = len(arr)-1
# while left < right:
#     arr[left],arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)


# ----------------------------------------------------------------------------------
# 7 Find the second largest number

# arr = [10,5,20,18,15]
# largest = arr[0]
# second = arr[0]
# for num in arr:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second:
#         second = num 
# print(second)

# ----------------------------------------------------------------------------------
# 8 Binary Search

# arr= [10,20,30,40,50]
# target = 40
# left = 0
# right = len(arr)-1
# while left<= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("Found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid+1
#     else:
#         right = mid -1
        
# ----------------------------------------------------------------------------------
# 9 Bubble Sort

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)


# ----------------------------------------------------------------------------------
# 10 Selection Sort

# arr= [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i] , arr[min_index] = arr[min_index], arr[i]
# print(arr)

# ----------------------------------------------------------------------------------
# 11 Insertion Sort

# arr = [7,3,5,2]
# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j = j-1
#     arr[j+1] = key
# print(arr)

# 12 Find the missing number 

# arr= [1,2,4,5]
# actual_sum = 0
# expected_sum = 0
# for num in arr:
#     actual_sum = num + actual_sum
# for num in range(1, arr[-1]+1):
#     expected_sum = num + expected_sum
# print(expected_sum - actual_sum)
# print(expected_sum)

# 13 Recursion (print 1 to 5)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print_num(1)

# 14 Recursion countdown and factorial

# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))


# 15 Count vowels -- string

# word = "programming"
# vowel = {'a','e','i','o','u'}
# count = 0
# for char in word:
#     if char in vowel:
#         count = count+1
# print(count)


# 16 Find the first character that repeats

# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

# 17 Find the first charater that appears only once

# word = 'programming'
# count = {}
# for char in word:
#     if char in count:
#         count[char] = count[char]+1
#     else:
#         count[char] = 1
# for char in word:
#     if count[char] == 1:
#         print(char)
#         break

# name = ['P','r','a','j','j','a','w','a','l']
# print("".join(name))

# check that is it anagram or not

# word1 = "listen"
# word2 = "silent"
# count1 = {}
# count2 = {}
# for char in word1:
#     if char in count1:
#         count1[char] = count1[char]+1
#     else:
#         count1[char] =1
# for char in word2:
#     if char in count2:
#         count2[char] = count2[char]+1
#     else:
#         count2[char] = 1
# if count1 == count2:
#     print("anagram")
# else:
#     print("na")

# 19 check that is it palindrom or not by using flag

# word = 'racecar'
# palindrome = True
# i = 0
# j = len(word)-1
# while i < j:
#     if word[i] != word[j]:
#         palindrome = False
#         break
#     i = i+1
#     j = j-1
# if palindrome:
#     print("palindrome")
# else:
#     print("not a palindrome")

# 20 Remove the duplicates

# word = "programming"
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result + char
# print(result)

# 21 find the most frequent char in the word

# word = "mississippi"
# count = {}
# most_frequent = ""
# highest_count = 0
# for char in word:
#     if char in count:
#         count[char] = count[char]+1
#     else:
#         count[char] = 1
# for char in count:
#     if count[char] > highest_count:
#         highest_count = count[char]
#         most_frequent = char
# print(most_frequent)

# 22 two sum using two pointers in sorted array

# arr = [1,2,4,6,8,9]
# target = 14
# i = 0
# j = len(arr)-1
# while i < j:
#     sum = arr[i] + arr[j]
#     if sum < target:
#         i = i+1
#     elif sum > target:
#         j = j-1
#     else:
#         print("found")
#         break

# 23 reverse only vowels

# s = "leetcode"
# s = list(s)
# vowel = {'a','e','i','o','u'}
# i = 0
# j = len(s)-1
# while i < j:
#     if s[i] not in vowel:
#         i = i+1
#     elif s[j] not in vowel:
#         j = j-1
#     else:
#         s[j], s[i] = s[i], s[j]
#         i = i+1
#         j = j-1
# print(s)

# 24 Sliding window -- max sum of k consecutive elements

# arr = [2,1,5,1,3,2]
# k = 3
# l = 0
# window_sum = arr[k-3] + arr[k-2] + arr[k-1]
# mx = window_sum
# for e in range(k, len(arr)):
#     window_sum = window_sum - arr[l]+arr[e]
#     l = l+1
#     if window_sum > mx:
#         mx = window_sum
# print(mx)

# 25 Maximmum number of vowels -- sliding window

# s ="abciiidef"
# k = 3
# vowel = {'a','e','i','o','u'}
# count = 0
# for i in range(k):
#     if s[i] in vowel:
#         count += 1
# mx = count
# l = 0
# for r in range(k,len(s)):
#     if s[l] in vowel:
#         count -= 1
#     if s[r] in vowel:
#         count += 1
#     l += 1
#     mx = max(mx,count)
# print(mx)
#  or 

# s = "abciiidef"
# k = 3
# vowel = {'a','e','i','o','u'}
# window_count = 0
# for i in range(k):
#     if s[i] in vowel:
#         window_count += 1
# max_vowels = window_count
# for i in range(k, len(s)):
#     if s[i-k] in vowel:
#         window_count -= 1
#     if s[i] in vowel:
#         window_count += 1
#     max_vowel = max(max_vowel, window_count)

# 26 Smallest subarray sum >= target , sliding window

# arr = [2,3,1,2,4,3]
# target = 7
# l = 0
# r = 0 
# sm = 0
# minimum = len(arr)+1
# while r < len(arr):
#     sm = sm +arr[r]
#     while sm >= target:
#         len_window = r-l+1
#         sm = sm - arr[l]
#         l = l+1
#         if len_window < minimum:
#             minimum = len_window
#     r = r+1
# print(minimum)

# 27 Longest substring without repeating characters

# s = "abcabcbb"
# l = 0
# r = 0 
# seen = set()
# mx = 0
# while r < len(s):
#     if s[r] not in seen:
#         seen.add(s[r])
#         sm = r-l+1
#         if sm > mx:
#             mx = sm
#         r = r + 1
#     else:
#         seen.remove(s[l])
#         l = l+1
# print(mx)

# and this is the proffessional way
# s = "abcabcbb"
# l = 0
# r = 0
# seen = set()
# mx = 0
# while r < len(s):
#     while s[r] in seen:
#         seen.remove(s[l])
#         l += 1
#     seen.add(s[r])
#     window_length = r-l+1
#     if window_length > mx:
#         mx = window_length
#     r += 1
# print(mx)

# 28 Longest substring with at most k distinct characters

# s = "eceba"
# k = 2
# seen = {}
# r = 0
# l =0
# mx = 0
# while r < len(s):
#     if s[r] in seen:
#         seen[s[r]] += 1
#     else:
#         seen[s[r]] = 1
#     while len(seen) > k:
#         left_char = s[l]
#         seen[left_char] -= 1
#         if seen[left_char] == 0:
#             del seen[left_char]
#         l += 1
#     window_length = r-l+1
#     if window_length > mx:
#         mx = window_length
#     r += 1
# print(mx)

# standard version 
# s = "eceba"
# k = 2
# l = 0
# r = 0
# count = {}
# mx = 0
# while r < len(s):
#     count[s[r]] = count.get(s[r], 0) + 1
#     while len(count) > k:
#         left_char = s[l]
#         count[left_char] -= 1
#         if count[left_char] == 0:
#             del count[left_char]
#         l += 1
#     mx = max(mx, r-l+1)
#     r += 1
# print(mx)

# 29 linked list some basics

# what a node contains
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# creating Nodes
# node1 = Node(10)
# node2 = Node(20)

# connecting nodes
# node1.next = node2

# Traversing a linked list
# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# Insert at beginning
# new_node.next = head
# head = new_node

# Insert at end
# current = head
# while current.next != None:
#     current = current.next
# current.next = new_node

# Delete a middle node
# 10 -> 20 -> 30
# bypass 20:
    # nodel.next = node3

# Delete the last node
# node2.next = None

# Search
# if current.data == target

# def insert_at_beginning(self, data):
#     self.data = data
#     newnode = newnode(data)
#     newnode.head = head
#     head = newnode



# 30 insert at the end

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node


# 31 Search for a target in the linked list
# def search (self, target):
#     current = self.head
#     while current != None:
#         if current.data == target:
#             return True
#         current = current.next
#     return False

# 32 LinkedList Class

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next != None:
#             current = current.next
#         current.next = new_node

#     def search(self,target):
#         current = self.head
#         while current != None:
#             if current.data == target:
#                 return True
#             current = current.next
#         return False

#     def delete(self, target):
#         if self.head == None:
#             return
#         if self.head.data == target:
#             self.head = self.head.next
#             return
#         current = self.head
#         while current.next != None:
#             if current.next.data == target:
#                 current.next = current.next.next
#                 return
#             current = current.next

# Complete Stack class

# class Stack:
    # def __init__(self):
    #     self.item = []
    # def push(self,data):
    #     self.item.append(data)
    # def pop(self):
    #     return self.item.pop()
    # def peek(self):
    #     return self.item[-1]

# to show no error we use it like that

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()
# def peek(self):
#     if len(self.item) == 0:
#         return None
#     return self.item[-1]

# basics of queue
# class queue:
#     def __init__(self):
#         self.items =[]
#     def enqueue(self, data):
#         self.items.append(data)
#     def dequeue(self):
#         if len(self.items) == 0:
#             return None
#         return self.items.pop(0)
#     def front(self):
#         if len(self.items) == 0:
#             return None
#         return self.items[0]


# Frequency Counting -- hash Tables/Python Dictionaries
# count[x] = count.get(x,0)+1

# 33 First repeating element

# arr = [5,3,8,3,5]
# seen = set()
# count = 0
# for x in arr:
#     if x in seen:
#         count = count+1 # in this method i am using the repeated
#         seen.add(x)   #element means i will return last value
# print(x)

# arr = [5,3,8,3,5]
# seen = set()
# for x in arr:
#     if x in seen:
#         print(x)
#         break
#     seen.add(x)

# 34 Two Sum with Indices using Hash Table

# arr = [2,7,11,15]
# target = 18
# seen = {}
# for i, x in enumerate(arr):
#     needed = target - x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# 35 found the first not repeated element using hash table

# s = "aabbcddee"
# seen = {}
# for x in s:
#     seen[x] = seen.get(x,0)+1
# for x in s:
#     if seen[x] == 1:
#         print(x)
#         break

# 36 Group Anagrams using a hash table

# s = ["eat", "tea", "tan", "ate", "nat", "bat"]
# seen = {}
# for x in s:
#     key = "".join(sorted(x))
#     if key in seen:
#         seen[key].append(x)
#     else:
#         seen[key] = [x]
# print(seen[key])

# 37 Longest Consecutive Sequence

# arr = [100,4,200,1,3,2]
# arr = sorted(arr)
# current_length = 1
# max_length = 1
# for i in range(len(arr)-1):
#     diff = arr[i+1] - arr[i]
#     if diff == 1:
#         current_length += 1
#     else:
#         current_length = 1
#     if current_length > max_length:
#         max_length = current_length
# print(max_length)


# it was a sorting approach so here the complexity will be 0(nlogn)

# arr = [100,4,200,1,3,2]
# seen = set(arr)
# count = 0
# l_sl = 0
# for num in seen:
#     if num-1 in seen:
#         continue
#     count = 1
#     while num + 1 in seen:
#         num = num+1
#         count = count+1
#     if count > l_sl:
#         l_sl = count
# print(l_sl)
                    # or

# arr = [100,4,200,1,3,2]
# i = len(arr)-1
# count = 1
# for num in arr:
#     new = num +1
#     if new in arr:
#         count = count + 1
# print(count)


# if we need to store index both so we use
# s = {}
# s = set()   not this

# Dictionaries don't use .add().
# it uses--
# seen[x] = i


# Binary Search Tree - BST
# left<parent<right


# 38 Insert the data in BST- binary search tree

# def insert(root, data):
#     if root is None:
#         return Node(data)
#     current = root
#     while current is not None:
#         if data < current.data:
#             if current.left is None:
#                 current.left = Node(data)
#                 return
#             current = current.left
#         elif data > current.data:
#             if current.right is None:
#                 current.right = Node(data)
#                 return
#             current = current.right
#         else:
#             return


# 39..
# 39 delete from a bst.
# def delete(root, target):
#     # 1. Target doesn't exist
#     if root is None:
#         return None
#     # 2. Search for the target
#     if target < root.data:
#         root.left = delete(root.left, target)
#     elif target > root.data:
#         root.right = delete(root.right, target)
#     # 3. Target found
#     else:
#         # Case 1: No children
#         if root.left is None and root.right is None:
#             return None
#         # Case 2: Only right child
#         elif root.left is None:
#             return root.right
#         # Case 3: Only left child
#         elif root.right is None:
#             return root.left
#         # Case 4: Two children
#         else:
#             successor = root.right
#             # Find smallest node in right subtree
#             while successor.left is not None:
#                 successor = successor.left
#             # Copy successor's value
#             root.data = successor.data
#             # Delete original successor
#             root.right = delete(root.right, successor.data)
#     return root


            #      delete(root, target)
            #              │
            #         root is None?
            #         /          \
            #       yes           no
            #        ↓             ↓
            #     return       compare target
            #                     /      \
            #                  smaller   larger
            #                    ↓         ↓
            #                go left    go right
            #                     \      /
            #                      target found
            #                           │
            #         ┌─────────────────┼─────────────────┐
            #         ↓                 ↓                 ↓
            #     no children       one child        two children
            #         ↓                 ↓                 ↓
            #    return None      return child      find successor
            #                                            ↓
            #                                     copy successor.data
            #                                            ↓
            #                                     delete successor


# # A node can have a different depth and height.
# Depth = how far DOWN from root
# Height = how far DOWN to the deepest leaf

# BST complexity depends on height.
# - Best/average balanced case → O(log n)
# - Worst-case skewed tree → O(n)

# ----------------------------------------------------------------------------------------------------
# Heaps
# MAX Heap
# The largest value is always at the root.
# Min Heap
# The smallest value is always at the root.
# A heap is also a complete binary tree.
# ------------------------------------------------------------------------------------------------------

# Heap in a Array
# Left child:
# 2*i + 1

# Right child:
# 2*i + 2

# Parent:
# (i - 1) // 2

# -------------------------------------------------------------------------------------------------------
# adding a new number in the heap

# Add 2 at the end
    #     4
    #    / \
    #   7   6
    #  / \  /
    # 10  9 
    
    # Add 2 at the end -> Swap 2 and 6 -> Swap 2 and 4
    #      2
    #    / \
    #   7   4
    #  / \  /
    # 10  9 6
     
# 2                                    1. Add the new element at the END
# ↓                                                ↓ 
# compare with 6                           2. Find its PARENT
# ↓                                                ↓
# swap                                    3. If child < parent
# ↓                                                ↓
# compare with 4                                4. SWAP
# ↓                                                ↓
# swap                                     5. Repeat upward
# ↓                                                ↓
# 2 reaches the root                 6. Stop when parent <= child
# Always compare the new element with its current parent.

# Remove root from min heap:
# 1. Remove root
# 2. Move last element to root
# 3. Compare it with its children
# 4. Swap with the smaller child if necessary
# 5. Continue downward
# This is called heapify down.




# heapq
# Python already has a built-in heap implementation called heapq.
# It implements a min heap. -- 
# import heapq
