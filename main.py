###Q1 Calculate the sum of the squared numbers of a list using recursion.
def sum_squared(numList):
    if len(numList) == 1:
        return (numList[0]**2)
    return numList[0]**2 + sum_squared(numList[1:])

print(sum_squared([1,2,3]))

###Q2 Find the sum of digits of a given number using recursion
def sum_digits(num):
    if num//10 == 0:
        return num
    return num%10 + sum_digits(num//10)

print(sum_digits(1348))

###Q3 Write a recursive algorithm to reverse the characters in a given string

def reverse_string(myString):
    if len(myString) == 1:
        return myString[0]
    return reverse_string(myString[1:]) + myString[0]

print(reverse_string("cba"))

###Q4 Calculate the sum of the reciprocals of the positive integers (see below) using recursion

def sum_reciprocals(num):
    if num <= 1:
        return 1
    return (1/num + sum_reciprocals(num-1))

print(sum_reciprocals(10))
print('commit & push')