# arr = [5, 2, 8, 1]
# target = 8
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
        
# arr = [5,2,8,1]
# target = 8
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)


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

# s = "hElLo"
# print(s.lower())
# # print(s.upper())
# # print(s.lower())
# print(s.upper())

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch,0) + 1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0) +1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch,0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch,0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch,0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = 0
# for ch  in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# freq = {}
# for ch in "apple":
#     freq[ch] = freq.get(ch, 0)+1
# print(freq)

# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found at", i)
        
# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)

# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)


# nums = [2,7,11,15]
# target = 9
# j = 0
# for i in range(len(nums)):
#     if nums[i] + nums[j] == target:
#         print(i,j)
#         j = j +1
    # for j in range(len(nums)):
    #     if nums[i]+nums[j] == target:
    #         print(i,j)
    #         break
        
# nums = [2,7,11,15]
# target = 18
# seen = {}
# for i,x in enumerate(nums):
#     needed = target - x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i
# nums = [2,7,11,15]

# s = "A man, a plan, ab canal: Panama"
# # for char in s:
#     key = "".join(char)
#     print(key)

# k = s.lower().replace(" ", "").replace(",", "").replace(":", "")
# i = 0
# j = len(k)-1
# while i < j:
#     if k[i] != k[j]:
#         print(False)
#         break
#         i = i+1
#         j = j-1
#     else:
#         print(True)
#         break

# for i in range(len(nums)):
#     # for j in range(len(nums)):
#         if nums[i]+nums[j] == target:
#             j = j + 1
#             print(i,j)

# count = {}
# count[5] = 2
# count[3] = 1
# print(count)

# s = "pwwkew"
# seen = set()
# i = 0
# for ch in s:
#     if ch in seen:
#         print(seen)
#         i = i+1
#         # break
#     else:
#         seen.add(ch)

# arr = [3, 8, 12, 5, 7, 10, 4]
# count = 0
# for num in arr:
#     if num % 2 == 0:
#         count= count+1
# print(count)

# word = "programming"
# count = {}
# for char in word:
#     if char in count:
#         count[char] = count[char] + 1
#     else:
#         count[char] = 1
# print(count[char])

#  Longest Substring Without Repeating Characters
# s = "abcabcbb"
# seen = set()

# word1 = "listen"
# word2 = "silent"
# count1 = {}
# count2 = {}
# for char in word1:
#     if char in count1:
#         count1[char] = count1[char] + 1
# print(count1)

# word = "mississippi"
# count = {}
# most_frequent = ""
# highest_count = 0
# for char in word:
#     if char in count:
#         count[char] = count[char] + 1
#     else:
#         count[char] = 1
# for char in count:
#     if count[char] > highest_count:
#         highest_count = count[char]
#         most_frequent = char
# print(most_frequent)

# s = "leetcode"
# s = list(s)
# print(s)
# s = "abciiidef"
# k = 3
# for char in s:
#     print(char)


# s = "pwwkew"
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

# s = "abciiidef"
# k = 3
# vowel = {'a,','e','i','o','u'}
# window_count = 0
# for i in range(k):
#     if s[i] in vowel:
#         window_count += 1
# max_vowel = window_count
# for i in range(k,len(s)):
#     if s[i-k] in vowel:
#         window_count -=1
#     if s[i] in vowel:
#         window_count += 1
#     max_vowel = max(max_vowel, window_count)


# sum = 250+250+600+600+600+600+300+300+600+600
# sum = 250+500+500+250+650+650+600+600+600+600+500+500+900+900+600+250+900+600+600+200
# print(sum)


# s = "pwwkew"
# seen = set()
# count = {}
# for char in s:
#     if char in seen:
#         break
#     else:
#         seen = seen.add(char)
#     print(seen)
# i = 0 
# j = 3
# print(s[i:j])

# s = "pwwkew"
# i = 0
# j = i+1
# while j < len(s)+1:
#     # j = j+1
#     if s[i] != s[j]:
#         j = j+1
#         i = i +1
#         print(s[i:j])
    # else:
    #     print(s[i:j])

# s = "pwwkew"
# seen = ()

# for char in s:
#     if char not in seen:
#         seen = seen.add(char)
#         print(seen)
#     elif char in seen:
#         break
        # print(len(seen))

# how i will solve 
# first take the element between i and j where i and j will be 0 
# and then l and r 
# if char in appeared again we just remove the left element 
# then print len(char)

# s = "pwwkew"
# seen = set()
# i = 0
# j = 1
# for char in s:
#     seen = seen.add(char)
#     print(seen)
    # word = s[i:j]
    # # j = j+1
    # if char not in word:
    #     j = j+1
    #     # print(word)
    # if char in word:
    #     print(word)
    #     i = i +1
    #     break

# s = "pwwkew"
# i = 0
# j = 0
# seen = set()
# max_length = 0
# while j < len(s):
#     if s[j] not in seen:
#         seen.add(s[j])
#         max_length = max(max_length, j-i+1)
#         j = j+1
#     elif s[j] in seen:
#         seen.remove(s[i])
#         i = i+1
# print(max_length)

# Longest Palindromic Substring

# s = "babad"
# i = 0
# j = 1
# seen = set()
# while j < len(s):
    # ...
# s = "babad"

# how to solve it -- first we will take it's first letter then we will add another 
# if both are same then it is also palindrom add in the pd_word if not a palindrome then
# add another check is it palindrom or not if yes add in the pd_word if not exit

# s = "babad"
# seen = set()
# i = 0 
# j = 0
# while j < len(s)-1:
#     j = j+1
#     if s[i] == s[j]:
#         seen.add(s[i])
#         # palindrom =
# print(seen)


# s = "babad"
# seen = set()
# i = 0
# j = 0
# while j < len(s)-1:
#     # if s[i] == s[j]:
#     #     palindrome = True
#     #     j = j+1
#     #     i = i+1
#     # if seen is palindrome:
#     j = j+1
#     seen = seen.add(s[j])
#     print(seen)

# s = "cbbd"
# seen = ""
# for char in s:
#     seen = seen+char
#     i = 0
#     j = len(seen)-1
#     while i < j:
#         if seen[i] != seen[j]:
#             break
#         i = i+1 
#         j = j-1
#         print(seen)

# s = "cbbd"
# i = 0
# j = len(s)
# word = s[i:j]
# print(word)

# how i will solve this question -- first i will take i and j i at 0 and j at len(s)
# and then first check that is it palindrome if not then first i will decrese the value
# of j and still it is not palindrome then i will increase the value of i 

# s = "babad"
# i = 0
# j = len(s)-1
# d_a_ = s[i:j]
# palindrom = True
# while i<j:
#     if s[i] != s[j]:
#         palindrom = False
#         break
#     i += 1
#     j -= 1
# if not palindrom:
#     d_a_ = s[i+1:j]
#     i = i+1
# elif not palindrom:
#     d_a_ = s[i:j-1]
#     j = j-1
# print(d_a_)

# s = "cbbd"
# i = 0
# j = len(s)
# d_a_ = s[i:j]
# # print(d_a_)
# palindrom = True
# while i < j:
#     if s != s[::-1]:
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

# a = ""
# b = "def"
# print(a+b)

# s = "b"
# longest = ""

# for i in range(len(s)):
#     for j in range(i + 1, len(s) + 1):
#         substring = s[i:j]

#         if substring == substring[::-1]:
#             if len(substring) > len(longest):
#                 longest = substring

# print(longest)


s = "cbbd"
start = 0
max_length = 0
for i in range(len(s)):
    # Case 1: Odd-length palindrome
    left = i
    right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        left -= 1
        right += 1
    # Case 2: Even-length palindrome
    left = i
    right = i + 1
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        left -= 1
        right += 1
print(s[start:start + max_length])