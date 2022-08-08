# Function

#**************************************************************************#
# # Challange One
#يمكن للشخص أن يكتب العملية الحسابية بحروف كبيرة أو صغيرة او Mix بدون مشكلة. مثلا add, ADD, aDd
def calculate(n1, n2, cal=''):

    if cal == 'add'.capitalize() or cal == 'a'.capitalize():
        print(n1+n2)
    elif cal == 'subtract' or cal == 's':
        print(n1 - n2)
    elif cal == 'multiply' or cal == 'm':
        print(n1 * n2)
    else:
        print(n1 + n2)

calculate(10, 20, 'multiply')

#**************************************************************************#
# # Challange Two
# # def addition(*num):
# #     return num * 4


# # print(addition(10, 20, 30, 10, 15))

#**************************************************************************#
# # Challange Three
def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f'Hello {name} Your Skills Is ')
        for skill in skills:
            print(f'- {skill}')

show_skills("Osama")

#**************************************************************************#
#  Challange Four

def say_hello(name='Unknown ', age ='Unknown ', country ='Unknown '):

    return (f'Hello {name} Your Age is {age} And You Live In {country}')

print(say_hello("Osama", 38, "Egypt"))

#**************************************************************************#
# Challange Five
def get_score(**scores):

    for score_key, score_value in scores.items():

        print(f'{score_key} => {score_value}')

get_score(Math=90, Science=80,)

#**************************************************************************#
# # Challange Six

def get_people_scores(name = 'unknown', **skills ):
    if len(skills) > 1:
     if name == 'unknown':
        for skill_key, skill_value in skills.items():
            print(f'{skill_key } => {skill_value}')
     else:
        print(f'Hello {name} This Is Your Score Table:')
        for skill_key, skill_value in skills.items():
            print(f'{skill_key } => {skill_value}')
    else:
        print(f'Hello {name} You Have No Scores To Show')

get_people_scores("Ahmed")

#**************************************************************************#
# Challange Seven

Score = {
    'Math': '90',
    'Science': '80',
    'Language ': '70',
}

def get_score(name ='unknown', **scores_list):

    if len(scores_list) > 1:
        if name == 'unknown':
            for score_Key, score_value in scores_list.items():
                print(f'{score_Key} => {score_value}')
        else:
            print(f'Hello {name} This Is Your Score Table:')
            for score_Key, score_value in scores_list.items():
                print(f'{score_Key} => {score_value}')
    else:
        print(f'Hello {name} You Have No Scores To Show')

get_score('ziad')
