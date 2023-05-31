"""Exercise (sum recursion):
Write a recursive function to compute the sum of digits in a positive integer.

def sum_of_digits(n):

Testing the function
num = 10
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.") --> 1 + 2 + 3 + 4 +5 +6 +7 +8+ 9 +10= ?"""

# Solution
def sum_of_digits(n):
    # Base case: if n is less than 10, it is a single-digit number
    # Return n as the sum of digits
    if n < 10:
        return n
    else:
        # Recursive case: n is a multi-digit number
        # Calculate the last digit (n % 10) and add it to the sum of remaining digits
        return n % 10 + sum_of_digits(n // 10)

num = 1034521
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.")


print("___________________________________________________")

# Solution 2
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        # Extract the last digit
        last_digit = n % 10
        # Remove the last digit
        remaining_digits = n // 10
        # Check if there are remaining digits
        if remaining_digits == 0:
            # If no remaining digits, return the last digit as the final sum
            return last_digit
        else:
            # Recursively compute the sum of remaining digits
            return last_digit + sum_of_digits(remaining_digits)

num = 1034521
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.")

print("___________________________________________________")







