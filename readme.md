# Exercise 1 (sum recursion):
Write a recursive function to compute the sum of digits in a positive integer.

def sum_of_digits(n):


# Testing the function
num = 10
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.") --> 1 + 2 + 3 + 4 +5 +6 +7 +8+ 9 +10= ?

# Exercise 2 (sum nested lists):
Write a recursive function to find the sum of all elements in a nested list.

def sum_nested_list(nested_list):
    total_sum = ________
    for element in nested_list:
        if isinstance(______, _____):
            total_sum += __________(element)
        else:
            _____ += _________
    return _________

# Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")# Recursive
