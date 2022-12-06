def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

def quick_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return []
    pivot = arr[len(arr)//2]
    left_arr = []
    right_arr =  []
    for i in arr:
        if i < pivot:
            left_arr.append(i)
        if i > pivot:
            right_arr.append(i)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left  = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted,right_sorted)

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


arr =  [5,3,2,15,235]

print(arr)
insertion_sort(arr)
print(arr)

print("----")

arr =  [5,3,2,15,235]
print(arr)
print(quick_sort(arr))

print("----")

arr =  [5,3,2,15,235]
print(arr)
print(merge_sort(arr))