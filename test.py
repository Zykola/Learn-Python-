# print('#' * 80)
# print('hello the project is cheak your admin or not admin'.upper())
# print('#' * 80)

# # Login
# admins = ['Ziad', 'Mhomed', 'Yosif', 'Enas', 'Manal', 'Osama']
# name = input('Enter Your Name : ').strip().capitalize()

# # if name in admins
# if name in admins:
#     print(f'Welcome Back {name}')
#     option = input('Please Enter Update OR Delete ').capitalize().strip()

# # if name in admins and update
#     if option == 'Update' or option == 'U':
#         print('okay your Choose Update')
#         theNewName = input('Enter Your New Name :')

#         print(f'the {theNewName} New Name')
#         admins[admins.index(name)] = theNewName
#         print('name is adding')
#         print(admins)

# # if name in admins and Delete
#     elif option == 'Delete' or option == 'D':
#         print('name is delete')
#         admins.remove(name)
#         print(admins)

# # if name is Worng
#     else:
#         print('Worng Option.')

# # if name is not list
# else:
#     print(f'Hello {name} Your Name is Not Admin')
#     status = input('Enter Please Would You like Admin Y or N ? :').capitalize()

# # if user add list
#     if status == 'Yes' or 'Y':
#         print('You Have Been Added')
#         admins.append(name)
#         print(admins)
# # if user not add list
#
#    else:
#         print('You Are Not Added')

# # Challange One

# # # Value
# num = int(input('Enter Please Your Number :'))

# # Cheake Value
# if num == 0:
#     print('Number 0 Is Not Larger Than 0')

# # Logic
# while num > 0:
#     num -= 1
#     if num == 6 or num == 0:
#         continue
#     print(num)

# #End Program
# print(f'{num} Numbers Printed Successfully.')

# # Challange Two
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# index = 0

# while index < len(friends):
#     print(friends[index])
#     index += 1

# print(f'Friends Printed And Ignored Names Count Is {index}')


# # Challange Four

# # value
# my_friends = []
# maxfrinds = 4
# frind = input('Enter your frind :')

# # logic
# while maxfrinds > 0:
#     # Cheake
#     if frind == frind.upper():
#         print('Invalid Name')

#     if frind == frind.lower():
#         print(
#             (f' Frind {frind.capitalize()}  Added => 1st Letter Become Capital'))

#     if frind == frind.capitalize():
#         print((f'Friend {frind} Added'))

#     maxfrinds -= 1
#     print(f'Names Left in List Is {maxfrinds}')
#     frind = input('Enter your frind :')


# myUltimateSkills = {
#     "HTML": {
#         "Main": "80%",
#         "Pugjs": "80%"
#     },
#     "CSS": {
#         "Main": "90%",
#         "Sass": "70%"
#     }
# }
# for skill_Key, skill_Value in myUltimateSkills.items():
#     print(f'skill {skill_Key} ')
#     for child_Key, child_Value in skill_Value.items():
#         print(f'-{child_Key} => {child_Value}')


# def clean_world(word):
#     if len(word) == 1:  # wwwooorrrlld
#         return word

#     if word[0] == word[1]:
#         return clean_world(word[1:])

#     return word[0] + clean_world(word[1:])


# print(clean_world('wwwooorrrlld'))


# from time import time


# def speedTest(func):

#     def wapper():
#         start = time()
#         func()
#         end = time()

#         print(f'Function Runing Time Is : {end - start}')

#     return wapper


# @speedTest
# def testFuction():
#     for num in range(1, 10000):
#         print(num)


# testFuction()
# the_file = None
# the_tries = 5

# while the_tries > 0:

#     try:
#         print("Enter The File Name With Absolute Path To Open")
#         print(f"You Have {the_tries} Tries Left")
#         # print("Example: C:\Users\ziaddif\Desktop\Python\yourfile.extension.py")

#         file_name_and_path = input('File Name => :').strip()
#         the_file = open(file_name_and_path, 'r')
#         print(the_file.read())
#         break

#     except FileNotFoundError:
#         print("File Not Found Please Be Sure The Name is Valid")
#         the_tries -= 1
#     except:
#         print('Error Happen.')

#     finally:
#         if the_file is not None:
#             the_file.close()
#             print("File Closed.")

# else:
#     print("All Tries Is Done")
