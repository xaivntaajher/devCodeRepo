list_of_options = ['dog', 'cat', 'bird', 'mouse']
list_of_choices = ['harry', 'bob', 'bill', 'max']

def display_options(list_of_options):
    print('Option 0 - Exit')
    option_number = 1
    for item in (list_of_options):
        print('Option',option_number,'-',item )
        option_number += 1

def prompt_input_numeric(prompt_string):
    user_input_string = input(prompt_string)
    num_choice = int(user_input_string)
    return num_choice

def validate_choice(list_of_choices):
    valid_choice = False
    while (valid_choice == False):
        display_options(list_of_choices)
        user_item = prompt_input_numeric('Choose a suit size from list above: ')

        if user_item == 0:
            valid_choice = True
            choice = 'Nothing selected'
        elif (user_item >= 1 and user_item <= len((list_of_choices))):
            choice = (list_of_choices)[user_item-1]
            valid_choice = True
        else:
            print('\nThat is not valid choice, please try again. ')
            
    print('good choice!\n')
    return choice

# def choose_suit_size2(list_of_sizes):
#     choice = validate_choice(list_of_sizes)

#     return choice

# display_options(list_of_options)
# print(prompt_input_numeric)
# print(validate_choice)
