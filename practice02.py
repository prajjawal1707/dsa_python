# DFS

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbor in graph[node]:
#         dfs(neighbor, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited= set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return 
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return 
#     visited.add(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# def dfs(node, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     for neighbour in graph[node]:
#         dfs(neighbour, visited)
# visited = set()
# dfs('A', visited)

# class MinHeap:
#     def __init__(self):
#         self.heap =[]

#     def insert(self,value):
#         self.heap.append(value)
#         i = len(self.heap)-1
#         while i > 0:
#             parent = (i-1)//2
#             if self.heap[parent]<= self.heap[i]:
#                 break
#             self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
#             i = parent

    # def insert(self, value):
    #     self.heap.append(value)
    #     i = len(self.heap)-1
    #     while i > 0:
    #         parent = (i-1)//2
    #         if self.heap[parent] <= self.heap[i]:
    #             break
    #         self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
    #         i = parent
    # def insert(self, value):
    #     self.heap.append(value)
    #     i = len(self.heap) - 1
    #     while i > 0:
    #         parent = (i-1)//2
    #         if self.heap[parent] <= self.heap[i]:
    #             break


# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(arr[i])



# arr= [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i] , arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)
# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j]< arr[min_index]:
#             min_index = j 
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# # arr = [5,6,2,4,9,6]
# # for i in range(len(arr)):
# #     min_index = i
# #     for j in range(i+1, len(arr)):
# #         if arr[j]< arr[min_index]:
# #             min_index = j
# #     arr[i], arr[min_index] = arr[min_index], arr[i]
# # print(arr)

# arr = [5,6,2,4,9,6]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [5,6,2,4,9,6]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] > arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# # def print_num(n):
# #     if n > 5:
# #         return
# #     print(n)
# #     print_num(n+1)
# # print_num(1)

# # def print_num(n):
# #     if n > 5:
# #         return
# #     print(n)
# #     print_num(n+1)
# # print_num(1)

# # def print_num(n):
# #     if n > 5:
# #         return 
# #     print(n)
# #     print_num(n+1)
# # print_num(1)

# # def print_num(n):
# #     if n> 5:
# #         return
# #     print(n)
# #     print_num(n+1)
# # print_num(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n> 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n> 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# def print_num(n):
#     if n > 5:
#         return
#     print(n)
#     print_num(n+1)
# print(1)

# Find the first character that repeats
# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

# word = 'programming'
# seen = set()
# for char in word:
#     if char in seen:
#         print(char)
#         break
#     seen.add(char)

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

# word = 'programming'
# count = {}
# for char in word:
#     if char in count:
#         count[char] = count[char] +1
#     else:
#         count[char] = 1
# for char in word:
#     if count[char] == 1:
#         print(char)
#         break

# word = 'programming'
# count = {}
# for char in word:
#     if char in count:
#         count[char] = count[char]+1
#     else: 
#         count[char] = 1
# for char in word:
#     if count[char] ==1 :
#         print(char)
#         break

# word = 'programming'
# count = {}
# for char in word:
#     if char in count:
#         count[char]  = count[char]+1
#     else:
#         count[char] =1
# for char in word:
#     if count[char] == 1:
#         print(char)
#         break

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

# 20 Remove the duplicates
# word = "programming"
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result + char
# print(result)

# word = 'programming'
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result+ char
# print(result)

# word = 'programming'
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result + char
# print(result)

# word = 'programming'
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result+char
# print(result)

# word = 'programming'
# seen = set()
# result = ""
# for char in word:
#     if char not in seen:
#         seen.add(char)
#         result = result+char
# print(result)

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

# word = 'mississippi'
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
#     highest_count = count[char]
#     most_frequent = char
# print(most_frequent)

# word = "mississippi"
# count = {}
# most_frequent= ""
# highest_count = 0
# for char in word:
#     if char in count:
#         count[char] = count[char]+1
#     else:
#         count[char] = 1
# for char in count:
#     highest_count = count[char]
#     most_frequent = char
# print(most_frequent)

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
#     highest_count = count[char]
#     most_frequent = char
# print(most_frequent)

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
#     highest_count = count[char]
#     most_frequent = char
# print(most_frequent)

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

# arr = [2,1,5,1,3,2]
# k = 3
# l = 0
# window_sum = arr[k-3]+arr[k-2]+arr[k-1]
# mx = window_sum
# for e in range(k, len(arr)):
#     window_sum = window_sum - arr[l]+arr[e]
#     l = l+1
#     if window_sum > mx:
#         mx = window_sum
# print(mx)

# arr = [2,1,5,1,3,2]
# k = 3
# l =0
# window_sum = arr[k-3]+arr[k-2]+arr[k-1]
# mx = window_sum
# for e in range(k , len(arr)):
#     window_sum = window_sum - arr[l]+arr[e]
#     l = l+1
#     if window_sum > mx:
#         mx = window_sum
# print(mx)

# arr = [2,1,5,1,3,2]
# k = 3
# l = 0
# window_sum = arr[k-3]+arr[k-2]+arr[k-1]
# mx = window_sum
# for e in range(k, len(arr)):
#     window_sum = window_sum - arr[l] + arr[e]
#     l = l + 1

#     if window_sum > mx:
#         mx = window_sum
# print(mx)

# arr = [2,1,5,1,3,2]
# k = 3
# l =0
# window_sum = arr[k-3]

# import heapq
# graph = {
#     'A': [('B', 2), ('C', 5)],
#     'B': [('A', 2), ('D', 3)],
#     'C': [('A', 5), ('D', 1)],
#     'D': [('B', 3), ('C', 1)]
# }

# distances = {
#     'A': 0,
#     'B': float('inf'),
#     'C': float('inf'),
#     'D': float('inf')
# }

# heap = [(0, 'A')]
# while heap:
#     current_distance, current_node = heapq.heappop(heap)
#     for neighbour, weight in graph[current_node]:
#         new_distance = current_distance + weight
#         if new_distance < distances[neighbour]:
#             distances[neighbour] = new_distance
#             heapq.heappush(heap, (new_distance, neighbour))
# print(distances)

# Create a list called dp with enough space for indexes 0 through n.
# Set the base cases: dp[1] = 1 and dp[2] = 2.
# Use a loop starting at 3 to calculate the remaining values.
# Print dp[6].
# dp = []
# for i in range(3, 5):
#     dp[i] = dp[i-1]+dp[i-2]
#     dp[1] = 1
#     dp[2] = 2
#     if i == 6:
#         print(dp[i])

# n = 6
# dp = [0] * (n + 1) 
# for i in range(3,7):
#     dp[1]=1
#     dp[2]=2
#     dp[i] = dp[i-1]+dp[i-2]
# print(dp[n])

# money = [2, 7, 9, 3, 1]
# i = 0
# while i+4 < len(money):
#     rob = money[i]+money[i+2]+money[i+4]
#     i = i+1
# print(rob)

# money = [2, 7, 9, 3, 1]
# rob = 0
# for i in range(0,len(money), 2):
#     rob = rob + money[i]
# print(rob)

# dp[i]=max(dp[i-1], money[i]+dp[i-2])

# money = [2,7,9,3,1]
# i = 0
# dp = money[i]
# for i in range(len(money)):
#     dp[i] = max(dp[i-1], money[i]+dp[i-2])
#     i = i + 1
#     rob = rob + money[i+n]

# money = [2,100,9,3,1]
# n = len(money) 
# dp = [0] * n 
# dp[0] = money[0] 
# dp[1] = max(money[0], money[1]) 
# # print(dp[1])
# for i in range(2,n):
#     dp[i] = max(dp[i-1], money[i]+dp[i-2])
# print(dp[i])

coins = [1, 2, 5]
amount = 11
1 = 1
2 = 2
3 = 1 + 2
4 = 2 + 2
5 = 5
6 = 5 + 1
7 = 5 + 2




