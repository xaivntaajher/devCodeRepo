# Task 1: Dictionary, Set and Tuple
# Given the following three scenarios, choose the best data structure (between a dictionary, set, or tuple) 
# to efficiently store the data. Each scenario ties directly to one data structure. Each data structure will be used only once. 
# You will need to determine which data structure is best for which scenario, and then implement the data structure in Python.

# Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
# HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.
# months in string
# Natinal Pi Day is 3.14
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
pi = 3
pi_day = months
for month in range(len(pi_day)):
    if month == pi:
        print()
        print(months[month-1])


# Store five fruits or vegetables.
# Add two of your favorite fruits and two of your favorite vegetables to the collection.
# Iterate over the collection and print each one to the console. 
# dictionary
# 5 fruits & vegetables
# 2 favorite fruits
# 2 favorite vegetables
# change favorites

favorite_fruits_veg = {
    'favorite fruit-1': 'oranges',
    'favorite fruit-2': 'grapes',
    'favorite fruit-3': 'pineapples',
    'favorite vegetable-1': 'carrots',
    'favorite vegetable-2': 'cucumber',
}

print()
favorite_fruits_veg['favorite fruit-4'] = 'banana'
favorite_fruits_veg['favorite fruit-5'] = 'apple'
favorite_fruits_veg['favorite vegetable-3'] = 'kale'
favorite_fruits_veg['favorite vegetable-4'] = 'broccoli'

print(favorite_fruits_veg['favorite fruit-1'])
print(favorite_fruits_veg['favorite fruit-2'])
print(favorite_fruits_veg['favorite fruit-3'])
print(favorite_fruits_veg['favorite fruit-4'])
print(favorite_fruits_veg['favorite fruit-5'])
print(favorite_fruits_veg['favorite vegetable-1'])
print(favorite_fruits_veg['favorite vegetable-2'])
print(favorite_fruits_veg['favorite vegetable-3'])
print(favorite_fruits_veg['favorite vegetable-4'])



# Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. 
# The profile should consist of the following information:
# First Name
# Last Name
# Email Address
# Phone Number
# Dictionary

profile = {
    'First Name': 'Barney',
    'Last Name': 'Dinosaur',
    'Email Address': 'barneyisadino@dinosaur.com',
    'Phone Number': '123-456-7890',
}
print()
print(f'First Name: {profile["First Name"]}')
print(f'Last Name: {profile["Last Name"]}')
print(f'Email Address: {profile["Email Address"]}')
print(f'Phone Number: {profile["Phone Number"]}')
print()

# Task 2: List of Dictionaries
# Use a list to store the dictionary of your immediate family members, with each index of the list storing its own dictionary. 
# Dictionary should contain the following keys: 
# 
# create list, store dictionary in list
# create each key storing them in its own dictionary. #nesting dictionary
# print off with index 

# First name
# Last name
# Relation to you

# Once you have stored the List of Dictionary items, write a function/method that will iterate over the List and 
# print off the First Name and Relation of each person in the List.

first_name = ['Mai', 'Caleb', 'Swora', 'Colton']
last_name = ['Her']
relationship = ['Spouse', 'Son', 'Daughter']

immetidate_family = {
    'First Name': first_name,
    'Last Name': last_name,
    'Relationship': relationship
}

# first_name = [
#     {
#     'First Name': 'Mai',
#     'First Name': 'Caleb',
#     'First Name': 'Swora',
#     'First Name': 'Colton',
#     }
# ]
# last_name = [
#     {
#     'Last Name': 'Her',
#     }
# ]
# relationship = [
#     {
#     'Relationship': 'Spouse',
#     'Relationship': 'Son',
#     'Relationship': 'Daughter'
#     }
# ]
   
print(immetidate_family['First Name'][0],['Last Name'][0],['Relationship'][0])