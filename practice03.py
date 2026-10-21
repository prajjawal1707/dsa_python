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

arr = [3, 8, 12, 5, 7, 10, 4]
count = 0
for num in arr:
    if num % 2 == 0:
        count= count+1
print(count)
