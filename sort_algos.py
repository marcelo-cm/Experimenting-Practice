def insertion_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


def quick_sort(array):
    if len(array) == 1:
        return array
    if len(array) == 0:
        return []
    pivot = array[len(array) // 2]
    left_arr = []
    right_arr = []
    for i in array:
        if i < pivot:
            left_arr.append(i)
        if i > pivot:
            right_arr.append(i)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result


def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
    return array


def selection_sort(array):
    if len(array) <= 1:
        return array
    minimum = None
    min_idx = None
    for i in range(len(array)):
        if not minimum or array[i] < minimum:
            minimum = array[i]
            min_idx = i
    return [minimum] + selection_sort(array[:min_idx] + array[min_idx + 1:])


arr = [5, 3, 23, 15, 235]

print(arr)
insertion_sort(arr)
print(arr)

print("----")

arr = [5, 3, 23, 15, 235]
print(arr)
print(quick_sort(arr))

print("----")

arr = [5, 3, 23, 15, 235]
print(arr)
print(merge_sort(arr))

print("----")

arr = [5, 3, 23, 15, 235]
print(arr)
bubble_sort(arr)
print(arr)

print("----")

arr = [5, 3, 23, 15, 235]
print(arr)
print(selection_sort(arr))
print('commit & push')