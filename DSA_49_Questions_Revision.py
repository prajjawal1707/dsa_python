# DSA REVISION FILE — Python
# 49 Questions / Concepts Covered So Far
# ------------------------------------------------------------
# Format:
# 1) Algorithm / concept basics
# 2) What the algorithm is saying
# 3) Pseudocode
# 4) Question
# 5) Python solution
#
# Note:
# Some items are foundational exercises rather than separate
# interview questions. They are included because they were part
# of the learning path.

# ============================================================
# 0. BIG-O BASICS
# ============================================================
#
# What is Big-O?
# Big-O describes how an algorithm's time or memory grows as the
# input size n grows.
#
# Common cases:
# O(1)    -> constant work
# O(log n)-> repeatedly cut the search space
# O(n)    -> one pass through n items
# O(n log n) -> common efficient sorting complexity
# O(n^2)  -> compare many pairs / nested loops
#
# PSEUDOCODE:
# Count the dominant amount of work as input size grows.
#
# Example:
# for x in arr:
#     work
# => O(n)
#
# for x in arr:
#     for y in arr:
#         work
# => O(n^2)


# ============================================================
# 1. ARRAY — TRAVERSAL
# ============================================================
#
# Basics:
# An array/list stores values in an ordered sequence.
# Traversal means visiting each element.
#
# Pseudocode:
# FOR each element in array:
#     process element
#
# Question:
# Print every element of an array.

arr = [10, 20, 30, 40]
for x in arr:
    print(x)


# ============================================================
# 2. ARRAY — SUM
# ============================================================
#
# Algorithm:
# Keep a running total while traversing the array.
#
# Pseudocode:
# total = 0
# FOR each x:
#     total = total + x
# PRINT total
#
# Question:
# Find the sum of all elements.

arr = [2, 4, 6, 8]
total = 0
for x in arr:
    total += x
print(total)


# ============================================================
# 3. ARRAY — MAXIMUM
# ============================================================
#
# Algorithm:
# Keep the largest value seen so far.
#
# Pseudocode:
# best = first element
# FOR each x:
#     IF x > best:
#         best = x
#
# Question:
# Find the maximum element.

arr = [7, 2, 9, 4]
mx = arr[0]
for x in arr:
    if x > mx:
        mx = x
print(mx)


# ============================================================
# 4. ARRAY — MINIMUM
# ============================================================
#
# Same idea as maximum, but keep the smallest value.
#
# Pseudocode:
# best = first element
# FOR each x:
#     IF x < best:
#         best = x
#
# Question:
# Find the minimum element.

arr = [7, 2, 9, 4]
mn = arr[0]
for x in arr:
    if x < mn:
        mn = x
print(mn)


# ============================================================
# 5. ARRAY — UPDATE
# ============================================================
#
# Lists support direct index access.
# Pseudocode:
# array[index] = new_value
#
# Question:
# Change the value at index 2 to 99.

arr = [10, 20, 30, 40]
arr[2] = 99
print(arr)


# ============================================================
# 6. ARRAY — DELETE
# ============================================================
#
# Removing an item from the middle of a Python list causes later
# elements to shift left.
#
# Pseudocode:
# Find/delete the target.
# Shift later elements to fill the gap.
#
# Question:
# Remove 30.

arr = [10, 20, 30, 40]
arr.remove(30)
print(arr)


# ============================================================
# 7. ARRAY — INSERT
# ============================================================
#
# Inserting in the middle requires later elements to shift right.
#
# Pseudocode:
# Make space at index.
# Put the new value there.
#
# Question:
# Insert 25 at index 2.

arr = [10, 20, 30, 40]
arr.insert(2, 25)
print(arr)


# ============================================================
# 8. ARRAY — REVERSE USING TWO POINTERS
# ============================================================
#
# Algorithm:
# Keep one pointer at each end and swap while they have not met.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left < right:
#     swap array[left], array[right]
#     left++
#     right--
#
# Question:
# Reverse the array in-place.

arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)


# ============================================================
# 9. ARRAY — SECOND LARGEST
# ============================================================
#
# Algorithm:
# Track the largest and second-largest values while scanning.
#
# Pseudocode:
# largest = -infinity
# second = -infinity
# FOR x:
#     IF x > largest:
#         second = largest
#         largest = x
#     ELSE IF x > second and x != largest:
#         second = x
#
# Question:
# Find the second-largest distinct value.

arr = [10, 5, 20, 8, 20]
largest = float("-inf")
second = float("-inf")

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif largest > x > second:
        second = x

print(second)


# ============================================================
# 10. ARRAY — MISSING NUMBER
# ============================================================
#
# Assumption:
# Numbers are from 0 through n with exactly one missing.
#
# Algorithm:
# XOR cancels equal values:
# a ^ a = 0 and a ^ 0 = a.
#
# Pseudocode:
# result = n
# FOR i, x:
#     result = result XOR i XOR x
# PRINT result
#
# Question:
# Find the missing number.

arr = [3, 0, 1]
n = len(arr)
result = n
for i, x in enumerate(arr):
    result ^= i
    result ^= x
print(result)


# ============================================================
# 11. LINEAR SEARCH
# ============================================================
#
# Algorithm:
# Check elements one by one until target is found.
#
# Pseudocode:
# FOR each element:
#     IF element == target:
#         return index
# return -1
#
# Complexity: O(n)
#
# Question:
# Find target 8.

arr = [4, 7, 8, 2]
target = 8
answer = -1

for i, x in enumerate(arr):
    if x == target:
        answer = i
        break

print(answer)


# ============================================================
# 12. BINARY SEARCH
# ============================================================
#
# Algorithm:
# Works on a SORTED array. Compare target with middle and discard
# half of the search space.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left <= right:
#     mid = (left + right) // 2
#     IF arr[mid] == target: found
#     ELSE IF arr[mid] < target: left = mid + 1
#     ELSE: right = mid - 1
#
# Complexity: O(log n)
#
# Question:
# Find 11 in a sorted array.

arr = [2, 5, 7, 11, 15, 20]
target = 11
left = 0
right = len(arr) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        answer = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(answer)


# ============================================================
# 13. BUBBLE SORT
# ============================================================
#
# Algorithm:
# Repeatedly compare adjacent elements and swap them if they are
# in the wrong order. Large elements "bubble" toward the end.
#
# Pseudocode:
# REPEAT passes:
#     FOR adjacent pairs:
#         IF left > right:
#             swap
#
# Complexity: O(n^2) average/worst for the basic version.
#
# Question:
# Sort the array.

arr = [5, 1, 4, 2, 8]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)


# ============================================================
# 14. SELECTION SORT
# ============================================================
#
# Algorithm:
# Find the smallest remaining value and place it at the next
# sorted position.
#
# Pseudocode:
# FOR i from 0 to n-1:
#     min_index = i
#     FOR j after i:
#         IF arr[j] < arr[min_index]:
#             min_index = j
#     swap arr[i], arr[min_index]
#
# Complexity: O(n^2)
#
# Question:
# Sort the array.

arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)


# ============================================================
# 15. INSERTION SORT
# ============================================================
#
# Algorithm:
# Maintain a sorted left portion. Take the next value and insert
# it into its correct position.
#
# Pseudocode:
# FOR i from 1:
#     key = arr[i]
#     move larger sorted values right
#     put key in the gap
#
# Complexity: O(n^2) worst-case.
#
# Question:
# Sort the array.

arr = [7, 3, 5, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)


# ============================================================
# 16. RECURSION — FACTORIAL
# ============================================================
#
# Recursion:
# A function calls itself on a smaller problem.
# Every recursive algorithm needs a base case.
#
# Pseudocode:
# factorial(n):
#     IF n == 0: return 1
#     return n * factorial(n - 1)
#
# Question:
# Find 5!.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ============================================================
# 17. RECURSION — SUM 1 TO N
# ============================================================
#
# Pseudocode:
# sum(n):
#     IF n == 0: return 0
#     return n + sum(n - 1)
#
# Question:
# Find 1 + 2 + ... + 5.

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(5))


# ============================================================
# 18. STRING — COUNT VOWELS
# ============================================================
#
# Algorithm:
# Traverse characters and count those belonging to the vowel set.
#
# Pseudocode:
# count = 0
# FOR char:
#     IF char is a vowel:
#         count++
#
# Question:
# Count vowels in "education".

s = "education"
vowels = {"a", "e", "i", "o", "u"}
count = 0

for char in s:
    if char in vowels:
        count += 1

print(count)


# ============================================================
# 19. STRING — REVERSE
# ============================================================
#
# Algorithm:
# Build a new string by putting each new character at the front.
#
# Pseudocode:
# reversed = ""
# FOR char:
#     reversed = char + reversed
#
# Question:
# Reverse "hello".

word = "hello"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)


# ============================================================
# 20. STRING — COUNT SPECIFIC CHARACTER
# ============================================================
#
# Pseudocode:
# count = 0
# FOR char:
#     IF char == target:
#         count++
#
# Question:
# Count 'a' in "banana".

s = "banana"
target = "a"
count = 0

for char in s:
    if char == target:
        count += 1

print(count)


# ============================================================
# 21. FIRST REPEATING CHARACTER
# ============================================================
#
# Algorithm:
# Use a set of characters already seen.
#
# Pseudocode:
# seen = empty set
# FOR char:
#     IF char in seen:
#         return char
#     add char to seen
#
# Question:
# Find first repeating character in "abca".

s = "abca"
seen = set()

for char in s:
    if char in seen:
        print(char)
        break
    seen.add(char)


# ============================================================
# 22. FIRST UNIQUE CHARACTER
# ============================================================
#
# Algorithm:
# Two passes:
# 1) Count every character.
# 2) Scan original order and find count == 1.
#
# Why two passes?
# During the first occurrence we do not yet know whether the
# character will appear later.
#
# Pseudocode:
# count all characters
# FOR char in original string:
#     IF count[char] == 1:
#         return char
#
# Question:
# Find first non-repeating character in "aabbcddee".

s = "aabbcddee"
count = {}

for char in s:
    count[char] = count.get(char, 0) + 1

for char in s:
    if count[char] == 1:
        print(char)
        break


# ============================================================
# 23. ANAGRAM CHECK
# ============================================================
#
# Algorithm:
# Two strings are anagrams if every character has the same
# frequency.
#
# Pseudocode:
# IF lengths differ: false
# count characters in both
# compare frequency maps
#
# Question:
# Check whether "listen" and "silent" are anagrams.

s1 = "listen"
s2 = "silent"

count1 = {}
count2 = {}

for char in s1:
    count1[char] = count1.get(char, 0) + 1

for char in s2:
    count2[char] = count2.get(char, 0) + 1

print(count1 == count2)


# ============================================================
# 24. PALINDROME CHECK
# ============================================================
#
# Algorithm:
# Compare characters from both ends using two pointers.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left < right:
#     IF different: false
#     move both pointers
# true
#
# Question:
# Check "level".

s = "level"
left = 0
right = len(s) - 1
palindrome = True

while left < right:
    if s[left] != s[right]:
        palindrome = False
        break
    left += 1
    right -= 1

print(palindrome)


# ============================================================
# 25. REMOVE DUPLICATE CHARACTERS
# ============================================================
#
# Algorithm:
# Set remembers whether a character has already appeared.
# Preserve original order by appending only the first occurrence.
#
# Pseudocode:
# seen = set
# result = ""
# FOR char:
#     IF char not seen:
#         add char
#         append char
#
# Question:
# Convert "programming" to unique characters in original order.

s = "programming"
seen = set()
result = ""

for char in s:
    if char not in seen:
        seen.add(char)
        result += char

print(result)


# ============================================================
# 26. MOST FREQUENT CHARACTER
# ============================================================
#
# Algorithm:
# First count frequencies, then scan for the maximum.
#
# Pseudocode:
# count characters
# best = first character
# FOR char:
#     IF count[char] > count[best]:
#         best = char
#
# Question:
# Find a most frequent character in "mississippi".
#
# If multiple characters tie, this simple scan returns the first
# tied character according to the string's first occurrence.

s = "mississippi"
count = {}

for char in s:
    count[char] = count.get(char, 0) + 1

best = s[0]
for char in s:
    if count[char] > count[best]:
        best = char

print(best)


# ============================================================
# 27. TWO POINTERS — TWO SUM IN SORTED ARRAY
# ============================================================
#
# Algorithm:
# Put one pointer at each end.
# If sum is too small, increase left.
# If sum is too large, decrease right.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left < right:
#     sum = arr[left] + arr[right]
#     IF sum < target: left++
#     IF sum > target: right--
#     ELSE found
#
# Complexity: O(n)
#
# Question:
# Find two values that sum to 9.

arr = [2, 3, 4, 7, 11]
target = 9
left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum < target:
        left += 1
    elif current_sum > target:
        right -= 1
    else:
        print(arr[left], arr[right])
        break


# ============================================================
# 28. TWO POINTERS — REMOVE DUPLICATES FROM SORTED ARRAY
# ============================================================
#
# Algorithm:
# A slow pointer marks where the next unique value belongs.
# The fast pointer scans the array.
#
# Pseudocode:
# slow = 0
# FOR fast from 1:
#     IF arr[fast] != arr[slow]:
#         slow++
#         arr[slow] = arr[fast]
# unique part = arr[:slow+1]
#
# Question:
# Remove duplicates in-place from a sorted array.

arr = [1, 1, 2, 2, 3, 4, 4]
slow = 0

for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]

print(arr[:slow + 1])


# ============================================================
# 29. TWO POINTERS — MOVE ZEROS TO END
# ============================================================
#
# Algorithm:
# Keep a position for the next non-zero value and move non-zero
# values forward.
#
# Pseudocode:
# position = 0
# FOR x:
#     IF x != 0:
#         arr[position] = x
#         position++
# Fill remaining positions with zero.
#
# Question:
# Move all zeros to the end while preserving non-zero order.

arr = [0, 1, 0, 3, 12]
position = 0

for x in arr:
    if x != 0:
        arr[position] = x
        position += 1

while position < len(arr):
    arr[position] = 0
    position += 1

print(arr)


# ============================================================
# 30. TWO POINTERS — REVERSE ONLY VOWELS
# ============================================================
#
# Algorithm:
# Two pointers search for vowels from both ends and swap them.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left < right:
#     if left isn't vowel: left++
#     elif right isn't vowel: right--
#     else swap; move both
#
# Question:
# Reverse only vowels in "leetcode".

s = "leetcode"
chars = list(s)
vowels = {"a", "e", "i", "o", "u"}
left = 0
right = len(chars) - 1

while left < right:
    if chars[left] not in vowels:
        left += 1
    elif chars[right] not in vowels:
        right -= 1
    else:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

print("".join(chars))


# ============================================================
# 31. TWO POINTERS — VALID PALINDROME
# ============================================================
#
# Algorithm:
# Ignore non-alphanumeric characters and compare from both ends.
#
# Pseudocode:
# left = 0
# right = n - 1
# WHILE left < right:
#     skip non-alphanumeric
#     compare lowercase characters
#
# Question:
# Check "A man, a plan, a canal: Panama".

s = "A man, a plan, a canal: Panama"
clean = ""

for char in s.lower():
    if char.isalnum():
        clean += char

left = 0
right = len(clean) - 1
palindrome = True

while left < right:
    if clean[left] != clean[right]:
        palindrome = False
        break
    left += 1
    right -= 1

print(palindrome)


# ============================================================
# 32. SLIDING WINDOW — MAX SUM OF SIZE K
# ============================================================
#
# Algorithm:
# Keep a fixed-size window. When it moves right, subtract the
# outgoing element and add the incoming element.
#
# Pseudocode:
# calculate first k sum
# FOR each next element:
#     remove outgoing
#     add incoming
#     update maximum
#
# Complexity: O(n)
#
# Question:
# Find maximum sum of any 3 consecutive values.

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
mx = window_sum
left = 0

for right in range(k, len(arr)):
    window_sum = window_sum - arr[left] + arr[right]
    left += 1
    mx = max(mx, window_sum)

print(mx)


# ============================================================
# 33. SLIDING WINDOW — MAX VOWELS OF SIZE K
# ============================================================
#
# Algorithm:
# Same fixed-size window idea, but maintain a vowel count.
#
# Pseudocode:
# count vowels in first window
# FOR each incoming char:
#     remove outgoing vowel if needed
#     add incoming vowel if needed
#     update maximum
#
# Question:
# Find maximum vowels in any substring of length 3.

s = "abciiidef"
k = 3
vowels = {"a", "e", "i", "o", "u"}

window_count = 0
for i in range(k):
    if s[i] in vowels:
        window_count += 1

max_vowels = window_count

for i in range(k, len(s)):
    if s[i - k] in vowels:
        window_count -= 1
    if s[i] in vowels:
        window_count += 1
    max_vowels = max(max_vowels, window_count)

print(max_vowels)


# ============================================================
# 34. SLIDING WINDOW — MINIMUM SUBARRAY SUM >= TARGET
# ============================================================
#
# Algorithm:
# Variable-size window.
# Expand right until condition is satisfied, then shrink from
# left while it remains satisfied.
#
# Pseudocode:
# left = 0
# sum = 0
# FOR right:
#     add arr[right]
#     WHILE sum >= target:
#         update minimum length
#         remove arr[left]
#         left++
#
# Question:
# Find the shortest subarray with sum >= 7.

arr = [2, 3, 1, 2, 4, 3]
target = 7
left = 0
sm = 0
minimum = len(arr) + 1

for right in range(len(arr)):
    sm += arr[right]

    while sm >= target:
        length = right - left + 1
        minimum = min(minimum, length)
        sm -= arr[left]
        left += 1

print(minimum if minimum <= len(arr) else 0)


# ============================================================
# 35. SLIDING WINDOW — LONGEST SUBSTRING WITHOUT REPEATING
# ============================================================
#
# Algorithm:
# Maintain a window containing unique characters.
# If a duplicate enters, move left until the duplicate is gone.
#
# Pseudocode:
# left = 0
# seen = set
# FOR right:
#     WHILE s[right] already seen:
#         remove s[left]
#         left++
#     add s[right]
#     update max length
#
# Question:
# Find the longest substring without repeating characters.

s = "abcabcbb"
left = 0
seen = set()
mx = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    mx = max(mx, right - left + 1)

print(mx)


# ============================================================
# 36. SLIDING WINDOW — AT MOST K DISTINCT
# ============================================================
#
# Algorithm:
# Use a frequency dictionary because a character can occur more
# than once inside the window.
#
# Pseudocode:
# add right character to frequency map
# WHILE distinct count > k:
#     decrement left character
#     delete it when count becomes zero
# update maximum length
#
# Question:
# Find longest substring with at most 2 distinct characters.

s = "eceba"
k = 2
left = 0
count = {}
mx = 0

for right in range(len(s)):
    count[s[right]] = count.get(s[right], 0) + 1

    while len(count) > k:
        left_char = s[left]
        count[left_char] -= 1
        if count[left_char] == 0:
            del count[left_char]
        left += 1

    mx = max(mx, right - left + 1)

print(mx)


# ============================================================
# 37. LINKED LIST — BASIC NODE + TRAVERSAL
# ============================================================
#
# Algorithm:
# Each node stores data and a pointer to the next node.
# Traversal follows next until None.
#
# Pseudocode:
# current = head
# WHILE current != None:
#     process current.data
#     current = current.next
#
# Question:
# Build 10 -> 20 -> 30 and print it.

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

current = node1
while current is not None:
    print(current.data)
    current = current.next


# ============================================================
# 38. LINKED LIST — INSERT AT BEGINNING / END
# ============================================================
#
# Algorithm:
# Beginning:
# new.next = head
# head = new
#
# End:
# walk to the last node
# last.next = new
#
# Question:
# Implement both operations.

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


ll = LinkedList()
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.display()


# ============================================================
# 39. LINKED LIST — SEARCH
# ============================================================
#
# Algorithm:
# Traverse from head and compare each data value.
#
# Pseudocode:
# current = head
# WHILE current:
#     IF current.data == target: return True
#     current = current.next
# return False
#
# Question:
# Search for 30.

def search_linked_list(head, target):
    current = head

    while current is not None:
        if current.data == target:
            return True
        current = current.next

    return False


print(search_linked_list(ll.head, 30))
print(search_linked_list(ll.head, 50))


# ============================================================
# 40. LINKED LIST — DELETE BY VALUE
# ============================================================
#
# Algorithm:
# If deleting head, move head forward.
# Otherwise find the node whose next node is the target and
# bypass that target.
#
# Pseudocode:
# IF head is None: stop
# IF head.data == target:
#     head = head.next
#     stop
# current = head
# WHILE current.next:
#     IF current.next.data == target:
#         current.next = current.next.next
#         stop
#     current = current.next
#
# Question:
# Delete 30 from 10 -> 20 -> 30 -> 40.

def delete_linked_list(head, target):
    if head is None:
        return head

    if head.data == target:
        return head.next

    current = head

    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            return head
        current = current.next

    return head


ll.head = delete_linked_list(ll.head, 30)
ll.display()


# ============================================================
# 41. STACK
# ============================================================
#
# Algorithm:
# Stack = LIFO (Last In, First Out).
# push -> add at top
# pop  -> remove top
# peek -> see top
#
# Pseudocode:
# push(x): append x
# pop(): remove last item
# peek(): read last item
#
# Question:
# Implement a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())
print(stack.pop())


# ============================================================
# 42. QUEUE
# ============================================================
#
# Algorithm:
# Queue = FIFO (First In, First Out).
# enqueue -> add to back
# dequeue -> remove from front
# front -> inspect first
#
# Pseudocode:
# enqueue(x): append x
# dequeue(): remove first item
# front(): read first item
#
# Question:
# Implement a queue.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def front(self):
        if len(self.items) == 0:
            return None
        return self.items[0]


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.front())
print(queue.dequeue())


# ============================================================
# 43. HASH TABLE — FREQUENCY COUNTING
# ============================================================
#
# Algorithm:
# Dictionary maps key -> count.
#
# Pseudocode:
# count = {}
# FOR x:
#     count[x] = count[x] + 1
#
# Question:
# Count values in [5, 5, 7].

arr = [5, 5, 7]
count = {}

for x in arr:
    count[x] = count.get(x, 0) + 1

print(count)


# ============================================================
# 44. HASH TABLE — TWO SUM WITH INDICES
# ============================================================
#
# Algorithm:
# Store previously seen value -> index.
# For current x, needed = target - x.
# If needed is already stored, we have the pair.
#
# Pseudocode:
# seen = {}
# FOR i, x:
#     needed = target - x
#     IF needed in seen:
#         return [seen[needed], i]
#     seen[x] = i
#
# Average complexity: O(n)
#
# Question:
# Find indices whose values sum to 9.

arr = [2, 7, 11, 15]
target = 9
seen = {}

for i, x in enumerate(arr):
    needed = target - x

    if needed in seen:
        print(seen[needed], i)
        break

    seen[x] = i


# ============================================================
# 45. HASH TABLE — GROUP ANAGRAMS
# ============================================================
#
# Algorithm:
# Words with the same sorted letters are anagrams.
# Use sorted letters as a dictionary key.
#
# Pseudocode:
# groups = {}
# FOR word:
#     key = sorted letters of word
#     append word to groups[key]
#
# Question:
# Group ["eat","tea","tan","ate","nat","bat"].

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = "".join(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

print(groups)


# ============================================================
# 46. HASH TABLE — LONGEST CONSECUTIVE SEQUENCE
# ============================================================
#
# Algorithm:
# Put all values in a set for O(1)-average membership checks.
# Only start counting from a number whose predecessor is absent.
#
# Pseudocode:
# nums = set(array)
# best = 0
# FOR x in nums:
#     IF x - 1 exists:
#         continue
#     length = 1
#     WHILE x + 1 exists:
#         x++
#         length++
#     best = max(best, length)
#
# Average complexity: O(n)
#
# Question:
# Find the longest consecutive sequence.

arr = [100, 4, 200, 1, 3, 2]
nums = set(arr)
best = 0

for num in nums:
    if num - 1 in nums:
        continue

    length = 1

    while num + 1 in nums:
        num += 1
        length += 1

    best = max(best, length)

print(best)


# ============================================================
# 47. TREES — BUILD + PREORDER / INORDER / POSTORDER
# ============================================================
#
# Tree basics:
# A tree is hierarchical.
# Root = top node.
# Parent -> child relationship.
# Leaf = node with no children.
#
# Binary tree:
# Each node has at most two children: left and right.
#
# Node structure:
# data + left + right
#
# DFS traversal basics:
# Preorder  = Root -> Left -> Right
# Inorder   = Left -> Root -> Right
# Postorder = Left -> Right -> Root
#
# Pseudocode — PREORDER:
# visit(node):
#     IF node is None: return
#     process node
#     visit(left)
#     visit(right)
#
# Pseudocode — INORDER:
#     IF node is None: return
#     visit(left)
#     process node
#     visit(right)
#
# Pseudocode — POSTORDER:
#     IF node is None: return
#     visit(left)
#     visit(right)
#     process node
#
# Question:
# Build this tree and traverse it:
#
#         10
#        /  \
#      20    30
#     /  \
#    40   50

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


node40 = TreeNode(40)
node50 = TreeNode(50)
node20 = TreeNode(20)
node30 = TreeNode(30)
node10 = TreeNode(10)

node20.left = node40
node20.right = node50
node10.left = node20
node10.right = node30


def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)


print("Preorder:")
preorder(node10)

print("Inorder:")
inorder(node10)

print("Postorder:")
postorder(node10)


# ============================================================
# 48. TREES — LEVEL ORDER TRAVERSAL
# ============================================================
#
# Algorithm:
# BFS (Breadth-First Search) visits level by level.
# A queue is used because the first discovered node should be
# processed first.
#
# Pseudocode:
# IF root is None: stop
# queue = [root]
# WHILE queue:
#     current = remove front
#     process current
#     IF left exists: add left
#     IF right exists: add right
#
# Question:
# Print the tree level by level.
#
# Complexity:
# Time O(n), space O(n) in the worst case.
#
# Note:
# Python list.pop(0) is O(n). For production Python, collections.deque
# is preferred for an efficient queue. The version below keeps the
# implementation close to the queue concept we learned.

def level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


level_order(node10)


# ============================================================
# 49. BINARY SEARCH TREE — SEARCH
# ============================================================
#
# BST basics:
# For every node:
#     left subtree values < node
#     right subtree values > node
#
# BST search uses the ordering rule to discard one side.
#
# Pseudocode:
# current = root
# WHILE current exists:
#     IF target == current.data:
#         found
#     ELSE IF target < current.data:
#         current = current.left
#     ELSE:
#         current = current.right
# not found
#
# Average time: O(log n) for a reasonably balanced BST.
# Worst case: O(n) for a highly unbalanced BST.
#
# Question:
# Search for a value in a BST.

# Build:
#
#         50
#        /  \
#      30    70
#     / \    / \
#    20 40  60 80

bst50 = TreeNode(50)
bst30 = TreeNode(30)
bst70 = TreeNode(70)
bst20 = TreeNode(20)
bst40 = TreeNode(40)
bst60 = TreeNode(60)
bst80 = TreeNode(80)

bst50.left = bst30
bst50.right = bst70
bst30.left = bst20
bst30.right = bst40
bst70.left = bst60
bst70.right = bst80


def bst_search(root, target):
    current = root

    while current is not None:
        if target == current.data:
            return True
        elif target < current.data:
            current = current.left
        else:
            current = current.right

    return False


print(bst_search(bst50, 40))
print(bst_search(bst50, 90))


# ============================================================
# CURRENT TOPIC — BST INSERTION (NEXT TO COMPLETE)
# ============================================================
#
# This is the next operation we were learning.
#
# Rule:
# Walk down the BST.
# Smaller -> left.
# Larger -> right.
# When the correct child position is None, attach a new Node.
#
# Pseudocode:
#
# insert(root, data):
#     IF root is None:
#         return new Node(data)
#
#     current = root
#     WHILE True:
#         IF data < current.data:
#             IF current.left is None:
#                 current.left = new Node(data)
#                 break
#             current = current.left
#
#         ELSE IF data > current.data:
#             IF current.right is None:
#                 current.right = new Node(data)
#                 break
#             current = current.right
#
#         ELSE:
#             # duplicate policy: do nothing
#             break
#
# Question:
# Insert 35 into:
#
#         50
#        /  \
#      30    70
#     / \    / \
#    20 40  60 80
#
# Expected position:
# 50 -> 30 -> 40 -> left of 40
#
# The complete implementation can be written as:

def bst_insert(root, data):
    if root is None:
        return TreeNode(data)

    current = root

    while True:
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
                break
            current = current.left

        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
                break
            current = current.right

        else:
            # Duplicate value: do nothing.
            break

    return root


bst_insert(bst50, 35)

# Result:
#
#         50
#        /  \
#      30    70
#     / \    / \
#    20 40  60 80
#       /
#      35


# ============================================================
# QUICK ALGORITHM CHEAT SHEET
# ============================================================
#
# LINEAR SEARCH
# Idea: check one by one.
# Typical time: O(n)
#
# BINARY SEARCH
# Idea: sorted data; repeatedly discard half.
# Typical time: O(log n)
#
# BUBBLE SORT
# Idea: swap adjacent out-of-order values.
# Time: O(n^2) basic version.
#
# SELECTION SORT
# Idea: repeatedly select minimum.
# Time: O(n^2)
#
# INSERTION SORT
# Idea: insert each value into sorted left portion.
# Time: O(n^2) worst-case
#
# RECURSION
# Idea: solve a smaller version of the same problem.
# Must have a base case.
#
# TWO POINTERS
# Idea: two indices move through a sequence, often from both ends.
# Common time: O(n)
#
# SLIDING WINDOW
# Idea: maintain a contiguous window and update it incrementally.
# Often reduces nested work to O(n).
#
# HASHING
# Idea: dictionary/set gives average O(1) membership/access.
# Useful for frequencies, lookup, grouping, complements.
#
# LINKED LIST
# Idea: nodes connected by pointers.
# Traversal follows next.
#
# STACK
# Idea: LIFO.
# Main operations: push, pop, peek.
#
# QUEUE
# Idea: FIFO.
# Main operations: enqueue, dequeue, front.
#
# TREE DFS
# Preorder: Root -> Left -> Right
# Inorder: Left -> Root -> Right
# Postorder: Left -> Right -> Root
#
# TREE BFS / LEVEL ORDER
# Idea: visit level by level using a queue.
#
# BST SEARCH
# Idea: smaller -> left, larger -> right.
# Average O(log n) if balanced; worst O(n).
#
# BST INSERT
# Idea: follow the BST rule until an empty child position is found.
#
# ============================================================
# END
# ============================================================
