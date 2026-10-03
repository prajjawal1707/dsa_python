# find largest number

arr = [4,9,2,15,8]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(largest)