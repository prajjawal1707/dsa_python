# Before:             After:

#     30                 30
#    /                  /
#   20                 15
#     \
#      15

# if 20.left is None and 20.right is None:
#     30.left = None and 30.right = None
# elif 20.left = data:
#     if data < 30:
#         30.left = data 
#     else:
#         30.right = data 
# elif 20.right = data:
#     if data < 30:
#         30.left = data 
#     else:
#         30.right = data 
    

#        50
#       /  \
#     30    70
#    / \    / \
#   20 40  60 80

# if we delete 50 
# so root = root.right.left

# root.data = successor.data
# successor = root.right.left


    #     50
    #    /  \
    #  30    70
    #       /  \
    #      60   80
    #     /
    #    55

# if we delete 50 so successor = root.right.left
# so succesor is 55
# while successor.left is not None:
#     root.data = successor

# def delete(root, target):
#     if root.left is None and root.right is None:
#         target = root
#     elif root.left is not None and root.right is None:
#         target = root.left
#     elif root.right is not None and root.left is None:
#         target = root.right
#     else:
#         target = root.right
#         while root.left is not None:
#             target = root.left

# def delete(root, target):
#     if root.left is None and root.right is None:
#         delete(target)
#     elif root.left is not None and root.right is None:
#         root.left = delete(root.left, target)
#     elif root.left is None and root.right is not None:
#         root.right = delete(root.right, target)
#     else:
#         target = root.right
#         while root.left is not None:
#             target = root.left
            
    


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

#     def remove_min(self):
#         if len(self.heap) == 0:
#             return None
#         if len(self.heap) ==1:
#             return self.heap.pop()
#         minimum = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         i = 0 
#         while True:
#             left = 2 * i + 1
#             right = 2 * i + 2
#             smallest = i
#             if left< len(self.heap) and self.heap[left] < self.heap[smallest]:
#                 smallest = left
#             if right< len(self.heap) and self.heap[right] < self.heap[smallest]:
#                 smallest = right
#             if smallest == i:
#                 break
#             self.heap[i], self.heap[smallest] = (
#                 self.heap[smallest], self.heap[i]
#             )
#             i = smallest
#         return minimum

# arr = [2,7,11,15]
# target = 18
# seen = {}
# for i, x in enumerate(arr):
#     needed = target - x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# arr = [2,7,11,15]
# target = 18
# seen = {}
# for i, x in enumerate(arr):
#     needed = target -x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# arr = [2,7,11,15]
# target = 18
# seen = {}
# for i,x in enumerate(arr):
#     needed = target-x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# arr = [2,7,11,15]
# target = 18
# seen = {}
# for i,x in enumerate(arr):
#     needed = target -x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# arr = [2,7,11,15]
# seen = {}
# target = 18
# for i,x in enumerate(arr):
#     needed = target -x
#     if needed in seen:
#         print(seen[needed], i)
#     seen[x] = i

# arr = [5,3,8,3,5]
# seen = set()
# for x in arr:
#     if x in seen:
#         print(x)
#         break
#     seen.add(x)

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) == 0:
#         return None
#     return self.item.pop()

# def pop(self):
#     if len(self.item) ==0:
#         return None
#     return self.item.pop()

# def peek(self):
#     if len(self.item) == 0:
#         return None
#     return self.item[-1]

# def peek(self):
#     if len(self.item) == 0:
#         return None
#     return self.item[-1]

# def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

# Node= 1
# def insert_at_beginning(self, data):
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node

# def insert_a_beg(self, data):
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head= new_node
# def insert_at_beginning(self, data):
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node

# def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head == None:
#         self.head = new_node
#         return 
#     current = self.head
#     while current.next != None:
#         current = current.next
#     current.next = new_node

# def search(self,target):
#     current = self.head
#     while current != None:
#         if current.data == target:
#             return True
#         current = current.next
#     return False

# def search(self, target):
#     current = self.head
#     while current!= None:
#         if current.data == target:
#             return True
#         current = current.next
#     return False

# def search(self, target):
#     current = self.head
#     while current != None:
#         if current.data == target:
#             return True
#         current= current.next
#     return False

# def search(self,target):
#     current = self.head
#     while current != None:
#         if current.data == target:
#             return True
#         current = current.next
#     return False

# def delete(self, target):
#     if self.head == None:
#         return
#     if self.head.data == target:
#         self.head = self.head.next
#         return
#     current = self.head
#     while current.next != None:
#         if current.next.data == target:
#             current.next = current.next.next
#             return 
#         current = current.next

# def delete(self, target):
#     if self.head == None:
#         return
#     if self.head.data == target:
#         self.head = self.head.next
#         return
#     current = self.head
#     while current.next != None:
#         if current.next.data == target:
#             current.next = current.next.next
#             return
#         current = current.next

# def delete(self, target):
#     if self.head == None:
#         return
#     if self.head.data == target:
#         self. head = self.head.next
#         return
#     current = self.head
#     while current.next != None:
#         if current.next.data == target:
#             current.next = current.next.next
#             return
#         current = current.next

# def delete(self, target):
#     if self.head == None:
#         return 
#     if self.head.data == target:
#         self.head = self.head.next
#         return
#     current = self.head
#     while current.next != None:
#         if current.next.data == target:
#             current.next = current.next.next
#             return
#         current = current.next

# traversing a linked list 

# head =0
# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# current = head
# while current != None:
#     print(current.data)
#     current = current.next

# Longest substring with at most k distinct characters
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

# s ="eceba"
# k =2
# l =0
# r =0
# count = {}
# mx =0
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

# traversing an array
# arr = [10,20,30]
# for i,x in enumerate(arr):
#     print(i,x)

# sum of array
# arr =[5,10,15]
# total = 0
# for num in arr:
#     total = total + num 
#     print(total)

# find largest number
# arr = [4,9,2,15,8]
# largest = arr[0]
# for num in arr:
#     if num > largest:
#         largest = num
# print(largest)

# arr = [4,9,15,8,2]
# largest = arr[0]
# for num in arr:
#     if num> largest:
#         largest = num 
# print(largest)

# arr = [4,9,2,15,8]
# largest = arr[0]
# for num in arr:
#     if num > largest:
#         largest = num 
# print(largest)

# arr = [4,9,2,18,9]
# largest = arr[0]
# for num in arr:
#     if num > largest:
#         largest = num
# print(largest)

# arr = [4,9,2,15,8]
# smallest = arr[0]
# for num in arr:
#     if num < smallest:
#         smallest = num
# print(smallest)

# arr = [12,7,19,25]
# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# target= 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# target = 19
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("found at", i)

# arr = [10,20,30,40,50]
# left = 0
# right = len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)

# left = 0
# right = len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)

# left = 0
# right  = len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)

# left = 0
# right = len(arr)-1 
# while left < right :
#     arr[left], arr[right] = arr[right], arr[left]
#     left +=1
#     right -= 1
# print(arr)

# left = 0
# right = len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left +=1
#     right -=1
# print(arr)

# arr = [10,5,20,18,15]
# largest = arr[0] 
# second_largest = arr[0]
# for num in arr:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest:
#         second_largest = num
# print(second_largest)

# arr = [10,5,20,18,15]
# largest = arr[0]
# second_largest = arr[0]
# for num in arr:
#     if num > largest:
#         second_largest = largest
#         largest = num 
#     elif num > second_largest:
#         second_largest = num 
# print(second_largest)

# arr = [10,5,20,18,15]
# largest = arr[0]
# s_large = arr[0]
# for num in arr:
#     if num > largest:
#         s_large = largest
#         largest = num
#     elif num > s_large:
#         s_large = num 
# print(s_large)

# arr = [10,5,20,18,15]
# largest = arr[0]
# s_large = arr[0]
# for num in arr:
#     if num > largest:
#         s_large = largest
#         largest = num
#     elif num > s_large:
#         s_large = num
# print(s_large)

# arr = [10,5,20,18,15]
# largest = arr[0]
# s_largest = arr[0]
# for num in arr:
#     if num > largest:
#         s_largest = largest
#         largest = num
#     elif num > s_largest:
#         s_largest = num 
# print(s_largest)

# arr = [10,5,20,18,15]
# largest = arr[0]
# s_large = arr[0]
# for num in arr:
#     if num > largest:
#         s_large = largest
#         largest = num
#     elif num > s_large:
#         s_large = num 
# print(s_large)

arr = [10,20,30,40,50]
# target = 40
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid+1
#     else:
#         right = mid -1

# target = 40
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid + 1
#     else:
#         right = mid - 1

# target = 40
# left = 0
# right = len(arr)-1
# while left<= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid+1
#     else:
#         right = mid - 1

# target = 40 
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("target found", mid)
#         break
#     elif target > arr[mid]:
#         left = mid+1
#     else:
#         right = mid - 1

# target = 40
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target> arr[mid]:
#         left = mid+1
#     else:
        # right = mid-1

# target = 40
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid + 1
#     else:
#         right = mid - 1

# target = 40
# left = 0
# right = len(arr)-1
# while left <= right:
#     mid = (left+right)//2
#     if arr[mid] == target:
#         print("found at index", mid)
#         break
#     elif target > arr[mid]:
#         left = mid +1
#     else:
#         right = mid-1

# bubble sort 
# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]> arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]> arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]> arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j]> arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j] > arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[j]> arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

# selection sort
# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index], arr[min_index], arr[i]
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
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(li+1, len(arr)):
#         if arr[j]< arr[min_index]:
#             min_index = j
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j]< arr[min_index]:
#             min_index = j
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# arr = [8,4,6,2,9]
# for i in range(len(arr)):
#     min_index = i 
#     for j in range(i+1 ,len(arr)):
#         if arr[j] < arr[j+1]:
#             min_index = j
#     arr[j], arr[min_index] = arr[min_index], arr[i]
# print(arr)


# arr = [10,5,20,18,15]
# largest = arr[0]
# s_l = arr[0]
# for num in arr:
#     if num > largest:
#         s_l = largest
#         largest = num
#     elif num > s_l:
#         s_l = num
# print(s_l)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# queue = ['A']
# visited = {}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     graph['A']
#     for neighbor in graph[current]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)


# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)

#     for neighbor in graph[current]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)

            
            
            
# BFS
# queue = ['A']
# visited = {'A'}

# while queue:
#     current = queue.pop(0)
#     print(current)

#     for neighbor in graph[current]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)

# # BFS
# queue = ['A']
# visited = {"A"}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)
# queue = ["A"]
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

# queue = ['A']
# visited = ['A']
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)
