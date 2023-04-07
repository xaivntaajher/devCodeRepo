# Given a list of names, determine if any names are contained in the list more than once.
#       list [names]
# The function should take in the list as a parameter and return a boolean value 
#       def()
#       True/False
# (True if there are any repeated names, False if there are no repeats).
#       conditional needed to account for repeats ==
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# Time complexity is O(n log n) linear time.

name_list = ['Sage', 'Mike', "Bob", 'Bill', 'Mike', 'Bob']

def repeated_names(name_list):
    
    add_name = False
    
    for name in name_list:
        if name_list.count(name) > 1:
            return True

    if add_name == False:
        return False
    else:
        return True
            
print(repeated_names(name_list))



