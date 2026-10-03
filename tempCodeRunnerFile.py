#         print(mid)
#         break
#     elif arr[mid] < target:
#         left = mid +1
#     else:
#         right = mid - 1
        
# arr = [8, 4, 6, 2, 9]
# i = 0
# j = 0
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

# arr = [7,3,5,2]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j+1], arr[j] = arr[j], arr[j+1]
# print(arr)

arr = [8, 4, 6, 2, 9]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
            arr[i] =arr[min_index]
            j = j+1
print(arr)