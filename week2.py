# ======weekTwo=======
# all the Strings
# ======weekTwo=======
# -----challange1
name,age,country ="'Ziad',",'"15""','Egypt'
full ='"Hello '+name+'How You Doing \\' +'"""' +'Your Age Is' +age + ' + '+'And Your Country Is: '+country
print(full)
#-----challange2
name,age,country ="'Ziad',",'"15""','Egypt'
full ='"Hello'+name+'How You Doing \\' + '\n'+'"""' +'Your Age Is' +age +'+'+'\n'+'And Your Country Is: '+country
print(full)
#-----challange3
name = 'Elzero'
print(name[1:2])
print(name[2:3])
print(name[5:])
#-----challange4
name = 'Elzero'
print(name[1:4])# "lze"
print(name[::2])# "Ezr"
print(name[-2::-2])# "rzE"
# -----challange5
name1 = '#@#@Elzero#@#@'
print(name1.strip('#@'))
# -----challange6
num1,num2,num3,num4,num5= '9','14','130','950','1500',
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
# -----challange7
name_one = 'Osama'
name_two = 'Osama_Elzero'
print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))
# -----challange8
name_one,name_two = "OSamA","osaMA"
print(name_one.upper())
print(name_two.lower())
# -----challange9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
# -----challange10
name = "Elzero"
print(name.index('z'))
#-----challange11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3' ,'Love',1))
# -----challange12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3' ,'Love'))
# -----challange13
name = "Osama"
age = 38
country = "Egypt"
print(f'My Name Is {name}, And My Age Is {age},And My Country Is {country}')