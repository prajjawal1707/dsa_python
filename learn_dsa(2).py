#         50
#        /  \
#      30    70
#     / \    / \
#    20 40  60 80

# def insert(root, data):
# Insert 35
# def insert(root, data):
#     while current.data == Node(data):
#         if current.data > data:
#             current.right = Node(data)
#         elif current.data < data:
#             current.left = Node(data)
#         else:
#             current.data = node(data)

# current = root
# while current exists:
#     if data is smaller:
#         if left is empty:
#             attach new node
#             stop
#         otherwise:
#             move left
#     if data is larger:
#         if right is empty:
#             attach new node
#             stop
#         otherwise:
#             move right
#     if equal:
#         stop
        
# def insert(root, data):
#         if root is None:
#             return Node(data)
#         current = root
#         while current is not None:
#             if current.data > data:
#                 if current.left is None:
#                     current.left = Node(data)
#                 else:
#                     current = current.left
#             elif current.data < data:
#                 if current.right is None:
#                     current.right = Node(data)
#                 else:
#                     current = current.right
#             else:
#                 return

# queue = ['A']
# visited = {'A'}
# while queue:
#     current = queue.pop(0)
#     print(current)
#     for neighbour in graph[current]:
#         if neighbour not in visited:
#             visited.add(neighbour)
#             queue.append(neighbour)

