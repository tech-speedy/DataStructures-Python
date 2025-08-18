# Program to delete an element from a specified location in an array

arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

# Input: location (index) to delete
pos = int(input("Enter the position (index) to delete: "))

# Check if position is valid
if pos < 0 or pos >= len(arr):
    print("Invalid position!")
else:
    # Deleting the element
    deleted_element = arr.pop(pos)
    print(f"Deleted element: {deleted_element}")
    print("Updated Array:", arr)
