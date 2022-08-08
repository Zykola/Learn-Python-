from functools import reduce

# Challange_One
values = (0, 1, 2,)

# cheak true or false
if any(values):
    # Is Ture Create my_var
    my_var = 0


my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    # is true
    print("Good")

# is false
else:
    print("Bad")

# Output Good

# Challange_Two
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  #


# Challange_Three
n = 21
l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):  # 10

    print("Good")

# Challange_Four


def remove_chars(text):
    return text


# Challange_Five
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars, friends_map)

for nameclean in cleaned_list:
    print(nameclean)

print('&' * 70)

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(lambda text: text, friends_map)

for nameclean in cleaned_list:
    print(nameclean)

# Challange_Six

def get_names(name):
    return name.endswith('m')


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)
for nameEnd in names:
    print(nameEnd)

print('&' * 70)

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(lambda name: name.endswith('m'), friends_filter)
for nameEnd in names:
    print(nameEnd)

# Challange_Seven
nums = [2, 4, 6, 2]

num = reduce(lambda num1, num2: num1*num2, nums)
print(num)
# Challange_Eight
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills = reversed(skills)
indexskills = (enumerate(skills, 50))

for index, skill in indexskills:
    print(f'{index} - {skill}')
