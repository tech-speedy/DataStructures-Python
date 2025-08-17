#Python program to find minimum element in an array

arr = [8, 2, 4, 5]
min_value = arr[0]

print("Length of the array is", len(arr))

for i in range(1, len(arr)):
    if arr[i] < min_value:
        min_value = arr[i]
print("Min value is", min_value)

#Python program to find maximum element in an array

arr = [8, 2, 4, 5]
max_value = arr[0]

print("Length of the array is", len(arr))

for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
print("Max value is", max_value)
