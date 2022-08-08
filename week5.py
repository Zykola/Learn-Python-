# ========weekfive========
# bool
# ========weekfive========

# # #callange One
# #True
# print(bool('ziad'))
# print(bool(15.5))
# print(bool([14, 15 , 16]))
# print(bool({1,2}))
# #False
# print(bool(''))
# print(bool(0))
# print(bool([]))
# print(bool({}))

# # callange Two
# html = 80
# css = 60
# javascript = 70
# print(html > 50 or css > 50 or javascript > 50)
# print(html > 50 and css > 50 and javascript > 50)

# # callange Three
# num_one = 10
# num_two = 20
# num = 20
# print(num > num_one or num >num_two)
# print(num > num_one and num >num_two)

# # callange Four
# num_one = 10
# num_two = 20
# result = num_one + num_two
# print(result)
# result **= 3
# #result = result * result * result
# print(result)
# result //= 27
# print(result)
# result /= 5
# print(result)
# print(type(str(result)))

# =========38:40========
# challnge One
# name = input('enter name:')
# name = name.strip().capitalize()
# print(f'Hello {name} ,Happy To See You Here.')

# # challnge Two
# # age = input('enter age plz:')
# # age = int(age)
# # print(f'{age == 16} ')

# # challnge Three
# fname = input('enter plz first name :').strip().capitalize()
# lname = input('enter plz last name :').strip().capitalaiize()
# seconedLastname = lname[0]
# print(f'Hello {fname}{seconedLastname}.')

# # # challnge Four
# # email Osama@Nn.Sa
# email = input('Enter email plz :').strip().capitalize()
# userName = email[:email.index('@')]
# theWebSite = email[email.index('@') + 1:email.index('.')]
# TopLevelDomain = email[email.index('.') + 1:]

# print(f'your name is {userName}')
# print(f'Email Service Provider Is {theWebSite}')
# print(f'Email Service Provider Is {TopLevelDomain}')


# age = input('Enter age plz :').strip()
# age = int(age)
# month = age * 12
# weeks = month * 4
# days = weeks * 365
# hours = days * 24
# minutes = hours * 60
# second = minutes * 60

# print('you lived for')
# print(f'{month} month')
# print(f'{weeks:,} weeks')
# print(f'{days:,} days')
# print(f'{hours:,} hours')
# print(f'{minutes:,} minutes')
# print(f'{second:,} second')

# a = int(input('enter mark:'))
# if (a >= 50):
#     {
#         print('true')
#     }
# else:
#     {
#         print('end')
#     }
