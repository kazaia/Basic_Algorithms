#Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

#For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).

#The expected complexity of the problem is  O(log(n)).


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

def find_first(input, target):
    index = binary_search(input,target)

    while input[index] == target:
        if index == 0 :
            return 0
        if input[index - 1] == target:
            index -= 1
        else:
            return index

def find_last(input, target):
    index = binary_search(input,target)

    while input[index] == target:
        if index == 0 :
            return 0
        if input[index + 1] == target:
            index += 1
        else:
            return index        
    

print(find_first([0, 1, 2, 3, 3, 3, 3, 3, 7, 8, 9], 3))
print(find_last([0, 1, 2, 3, 3, 3, 3, 3, 7, 8, 9], 3))




