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
# Challange One :

# my_nums = [15, 81, 5, 17, 20, 21, 13]

# for num in my_nums:
#     if num % 5 == 0:
#         print(f' 1 => {num}')

# else:
#     print('All Numbers Printed')

# # Challange Two :

# myNumbers = range(1, 21)
# for num in myNumbers:

#     if num == 6 or num == 8 or num == 12:
#         continue

#     if num < 10:
#         print(f'0{num} ')
#     else:
#         print(num)

# else:
#     print('All Numbers Printed')

# # Challange Three :
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# for rank_key, rank_value in my_ranks.items():
#     if rank_value == 'A':
#         a = 100
#         print(f'"My Rank in {rank_key} Is A And This Equal {a}')

#     elif rank_value == 'B':
#         b = 80
#         print(f'"My Rank in {rank_key} Is A And This Equal {b}')

#     elif rank_value == 'C':
#         c = 40
#         print(f'"My Rank in {rank_key} Is A And This Equal {c}')

# else:
#     print(f'Total Points Is : {a+b+c+a}')

# # Challange Four :
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}
a, b, c, d = 100, 80, 40, 20
for student_key, students_value in students.items():
    print('-' * 50)
    print(f' -- Student Name => {student_key} ')
    print('-' * 50)

    for child_key, child_value in students_value.items():
        if child_value == 'A':
            print(f' - {child_key} => {a} Points')

        elif child_value == 'D':
            print(f' - {child_key} => {d} Points')

        elif child_value == 'B':
            print(f' - {child_key} => {b} Points')
        else:
            (f' - {child_key} => {c} Points')
