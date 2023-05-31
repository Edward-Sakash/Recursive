"""Exercise 2 (sum nested lists):
Write a recursive function to find the sum of all elements in a nested list.

def sum_nested_list(nested_list):
total_sum = ________
for element in nested_list:
if isinstance(______, _____):
total_sum += __________(element)
else:
_____ += _________
return _________

Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")"""

# Solution
def sum_nested_list(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):
            total_sum += sum_nested_list(element)  # Recursive call to sum elements in nested lists
        else:
            total_sum += element
    return total_sum

# Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")

print("_______________________________________________")

# Solution 2
def sum_nested_list(nested_list):
    def helper(nested):
        total_sum = 0
        for element in nested:
            if isinstance(element, list):
                total_sum += helper(element)  # Recursive call to helper function for nested lists
            else:
                total_sum += element
        return total_sum

    return helper(nested_list)

# Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")
