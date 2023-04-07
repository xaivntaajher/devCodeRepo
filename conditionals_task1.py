legal_driving_age = 16
age = input('What is your age? ')


if int(age) >= legal_driving_age:
    print('You are legally able to drive. ')
elif int(age) <= legal_driving_age:
    print('You are not old enough to drive yet. ')
