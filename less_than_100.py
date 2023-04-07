# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value 
# (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# Time complexity is logarithmic time.

numbers_list = [30, 50, 15, 20, 10]

def less_than_hundred(numbers):

    for item in numbers:
        if item >= 100:
            return False
    return True
        
print(less_than_hundred(numbers_list))

