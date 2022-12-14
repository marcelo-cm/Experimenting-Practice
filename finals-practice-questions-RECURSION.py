class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1] #get the last element
    def __str__(self):
        return str(self.items)

def sum_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_digits(num // 10)

def reverse_string(string):
    if len(string) < 2:
        return string
    return string[-1] + reverse_string(string[:-1])

def reverse_string_stack(string):
    stack = Stack()
    result = ''
    for i in string:
        stack.push(i)
    for i in string:
        result += stack.pop()
    return result

def sum_reciprocals(num):
    if num <= 1:
        return num
    return (1/num) + sum_reciprocals(num-1)

def sum_squared(nums):
    if len(nums) <= 0:
        return ValueError("ValueError: Please input a vaild list of numbers")
    if len(nums) == 1:
        return nums[0]*nums[0]
    return nums[0]*nums[0] + sum_squared(nums[1:])

num = 2
string = "MARCELO"
print(sum_digits(num))
print(reverse_string(string))
print(reverse_string_stack(string))
print(sum_reciprocals(num))
print(sum_squared([1, 2, 3]))