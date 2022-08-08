# import random
# x = (random.randrange(10, 50))
# d = (random.randrange(2, 10))
# print(f'Random Number Between 10 And 50 => {x}')
# num = d % 2

# if num == 0 :
#     print(f'Random Even Number Between 2 And 10 => {d}')
# else:
#     print(f'Random Odd Number Between 1 And 9 => {d}')

# import random
# x = (random.randrange(10, 50))
# d = (random.randrange(2, 10))
# y = (random.randrange(1, 9))
# print(f'Random Number Between 10 And 50 => {x}')

# nume = d % 2
# numo = y % 3

# if nume == 0:
#     print(f'Random Even Number Between 2 And 10 => {d}')

# if numo == 0:
#     print(f'Random Odd Number Between 1 And 9 => {y}')


# # challange Two
# import my_mod

# my_mod.say_hello('ziad')
# my_mod.say_welcome('ziad')

# # challange three
# from my_mod import say_welcome

# say_welcome('ziad')

# # challange four
# from my_mod import say_welcome as new_welcome

# new_welcome('ziad')


# # Challange Six

# import datetime

# Date = datetime.datetime(2021,6,25)
# Today = datetime.datetime.now()

# print(f'Days From {Date} To {Today} Is => {(Today - Date).days}')

# # Challange seven

# import datetime

# date = datetime.datetime(2021, 8, 10)

# print(date.strftime('%Y - %m -%d'))
# print(date.strftime('%b %d, %Y'))
# print(date.strftime('%d - %b - %Y'))
# print(date.strftime('%d/ %b /%y'))
# print(date.strftime('%d/ %B /%Y'))


# # Challange eight

# # Challange nine

# def DecoratorFunction(func):
#     def wapper():
#         print('Sugar Added From Decorators"')
#         func()
#         print('#' * 50)
#     return wapper


# @DecoratorFunction
# def make_tea():
#     print("Tea Created")


# @DecoratorFunction
# def make_coffe():
#     print("Coffe Created")


# make_tea()
# make_coffe()
