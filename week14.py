########################## Challange OOP ##########################
class Game:
    def __init__(self, name, developer, year, price_in_pounds):
        self.name = name
        self.developer = developer
        self.year = year
        self.price_in_pounds = price_in_pounds


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds}", end="")
# # Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

########################## Challange OOP ##########################


########################## Challange OOP ##########################
class User:
    def __init__(self, Frist_name, Last_name, age, gender) -> None:

        self.fname = Frist_name
        self.lname = Last_name
        self.age = age
        self.gender = gender

    def isMaleOrFemale(self):
        if self.gender == 'Male':
            return f'Hello Mr {self.fname} {self.lname[0]}.'

        elif self.gender == 'Female':
            return f'Hello Mrs {self.fname} {self.lname[0]}.'

        else:
            print(f'Hello {self.fname} {self.lname[0]}.')

    def countAge(self):
        return [40 - self.age]

    def full_details(self):
        return f'{self.isMaleOrFemale()} {self.countAge()} Years To Reach 40'


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

########################## Challange OOP ##########################


########################## Challange OOP ##########################
class Message:
    print_messag = 'Hello From Class Message'


print(Message.print_messag)
########################## Challange OOP ##########################

########################## Challange OOP ##########################
# class Games:
#     def __init__(self, name):
#         # list_games, count_games
#         # self.list_games = list_games
#         # self.count_games = count_games
#         self.name = name

#     @classmethod
#     def show_games(self):
#             print(f'I Have One Game Called {self.name}')


# my_game = Games("Shadow Of Mordor")
# my_game.show_games()

# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_names.show_games()

########################## Challange OOP ##########################
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


# Create Admin Class Here
class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Moderators(Members):
    def show_info(self):
        return super().show_info()


member_one = Admins("Osama", "Admin")
print(member_one.show_info())

member_two = Moderators("Ahmed", "Moderator")
print(member_two.show_info())

########################## Challange OOP ##########################


class A:

    def __init__(self, one):
        self.one = one


class B(A):

    def __init__(self, one, two):
        super().__init__(one)
        self.two = two


class C(B):

    def __init__(self, one, two, three):
        super().__init__(one, two)
        self.three = three


class Text(C):
    def __init__(self, one, two, three):
        super().__init__(one, two, three)

    def show_name(self):
        return f'The Name Is {self.one}{self.two}{self.three}'


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

########################## Challange OOP ##########################
