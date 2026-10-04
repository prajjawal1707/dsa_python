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
