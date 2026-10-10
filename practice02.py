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

word = 'programming'
seen = set()
result = ""
for char in word:
    if char not in seen:
        seen.add(char)
        result = result+char
print(result)

