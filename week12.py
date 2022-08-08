
"""
the file is very good
the file is very good
"""
############## challange One##############
############# challange One ##############
############## challange Two ##############
############## challange Two ##############

############## challange Three ##############
from PIL import Image
myImage = Image.open('C:\\Users\ziaddif\Desktop\Python\elzero-pillow.png')

myBox = (400, 0, 800, 400)
myImageBox = myImage.crop(myBox)
myImageBox = myImageBox.convert('L')
myImageBox.show()

myBoxTwo = (0, 0, 1200, 400)
myImageBoxTwo = myImage.crop(myBoxTwo)
myImageBoxTwo = myImageBoxTwo.convert('L')
myImageBoxTwo = myImageBoxTwo.transpose(3)
# myImageBoxTwo.show()
############## challange Three ##############
############# challange Four  ##############


def say_hello_to(name):
    """ parameter(someone) => Person Name
 Function To Say Hello To Anyone
    """
    print(F'Hello {name}')


print(say_hello_to("Osama"))
# print(say_hello_to.__doc__)
############## challange Four  ##############

############## challange Five  ##############
'''to file other '''
############## challange Five  ##############
# pylint.exe c:/Users/ziaddif/Desktop/Python/week12.py


############## challange Six  ##############
NUM = int(input("Add Your Number:  "))
print(f'The Number Is {NUM}')

if NUM == 0:
    raise ValueError('Number Must Be Larger Than 0')

if type(NUM) != type(int):
    raise Exception('Only Numbers Allowed')
############## challange Six  ##############

############## challange Seven  ##############
# try:
#     LETTER = input("Add Letter From A to Z : ")
#     if len(LETTER) > 1:
#         print('You Must Write One Character Only')


# except:
#     print('1')
############## challange Seven  ##############


############## challange eight  ##############
def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))
############## challange eight  ##############
