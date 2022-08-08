#=========threeweek==========
#Numbers
#=========threeweek==========
#========19:20========

#challange One
i = 10
f = 10.0
c = 5+2j 
print(type(i))
print(type(f))
print(type(c))

#challange Two
n = 1+2j
print('the is imag :{}' .format(n.imag))
print('the is real :{}' .format(n.real))

#///////
#challange Three 
x = 10
print(float(x))#10.00000

# #challange four
num = 159.650 
num1 = int(num)
print(int(num1))
print(type(num1))

#challange five
print(100 - 115 )
print(50 * 30 )
print(21 % 4 )
print(110 // 11  )
print(97 //20 )


#========21:23========
#challange One
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

# #challange Two
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1:4:2])

# #challange Three
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[3:5])

# #challange four
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3:5] = ['Elzero', 'Elzero']
print(friends)

#challange five
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,'Nasser')
print(friends)
friends.append('Salem')
#friends.insert(3,'Nasser')
print(friends)

#challange six 
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove('Nasser' )
friends.remove('Osama' )
print(friends)
friends.remove('Salem' )
print(friends)

#challange seven
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

#challange eight
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)

#challange nine
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

# #challange ten
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])

#========24:25========
#challange One
myName = 'ziad',
print(myName)
print(type(myName))

#challange Two
friends = ("Osama", "Ahmed", "Sayed")
x = friends = list(friends)
x[0] = 'Elzero'
print(x)
x = tuple(friends)
print(type(x))
print(len(x))

#challange Three
nums = (1, 2, 3)
letters = ("A", "B", "C")
x = nums + letters
print(x)
print(len(x))

#challange four
my_tuple = (1, 2, 3, 4)
a, b,_, c = my_tuple
print(a)
print(b)
print(c)
