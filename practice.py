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
            
    


def delete(root, target):
    # 1. Target doesn't exist
    if root is None:
        return None
    # 2. Search for the target
    if target < root.data:
        root.left = delete(root.left, target)
    elif target > root.data:
        root.right = delete(root.right, target)
    # 3. Target found
    else:
        # Case 1: No children
        if root.left is None and root.right is None:
            return None
        # Case 2: Only right child
        elif root.left is None:
            return root.right
        # Case 3: Only left child
        elif root.right is None:
            return root.left
        # Case 4: Two children
        else:
            successor = root.right
            # Find smallest node in right subtree
            while successor.left is not None:
                successor = successor.left
            # Copy successor's value
            root.data = successor.data
            # Delete original successor
            root.right = delete(root.right, successor.data)
    return root


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
