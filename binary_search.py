# Binary search
# Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.

def binary_search(input,target, left = 0):
    if len(input) == 0 or ( len(input) == 1 and input[0] != target ):
        return -1

    mid = len(input)// 2
    
    if input[mid] == target:
        return mid + left
    elif input[mid] > target:
        return binary_search( input[: mid], target, left)
    elif input[mid] < target:
        return binary_search( input[ mid+ 1 : ], target, left+ mid+1)
    


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(a, 6))




