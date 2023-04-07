# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.

# Time complexity is constant.
def even_or_odd(num):

    number = int(num)

    if number % 2 == 0:
        return True  
    else:
        return False
        
print(even_or_odd(48))