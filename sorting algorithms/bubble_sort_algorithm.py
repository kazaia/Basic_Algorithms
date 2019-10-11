# Bubble sort algorithm

def bubble_sort(input):
    for i in range(len(input) - 1):
        for j in range(len(input) - 1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j ]

    return input

l = [4, 5, 3, 1, 0, 8]
print(bubble_sort(l))






