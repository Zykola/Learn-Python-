################## CHALLANGE_ONE ##################
'''
1) Centralized Database
2) Distributed Database
3) Relational Database
4) NoSQL Database
5) Cloud Database
'''
################## CHALLANGE_ONE ##################
import sqlite3

# Connect To Database
################## CHALLANGE_tWO ##################
db = sqlite3.connect('elzero.db')

cr = db.cursor()


def SaveAndClose():

    db.commit()

    db.close()


# CHALLANGE_THREE
cr.execute(
    'create table if not exists users (id integer, name text, dob integer , email text)')

cr.execute("insert into users values( 1, 'Ahmed' , 20/10/1980, 'a@gmail.com')")
cr.execute("insert into users values( 2, 'sayed' , 22/10/1980, 's@gmail.com')")
cr.execute("insert into users values( 3, 'ziad' ,  16/10/1980, 'z@gmail.com')")
cr.execute("insert into users values( 4, 'mohmed' ,10/10/1980, 'm@gmail.com')")
cr.execute("insert into users values( 5, 'sameh' , 27/10/1980, 's@gmail.com')")

SaveAndClose()
################## CHALLANGE_FOUR ##################
cr.execute('select * from users where id = 5')

print(cr.fetchone())
################## CHALLANGE_FIVE ##################
uid = input('enter your id : ')
cr.execute(f'select id from users where id = {uid} ')
result = cr.fetchone()

if result == None:
    print("User Not Found.")

else:
    cr.execute(f'delete from users where id = {uid} ')
    print("User Deleted.")
    print('Show Other Data:')
    data = cr.execute('select * from users')

    for x in data:
        print(
            f"ID => {x[0]}, Name => {x[1]}, Date Of Birth => {x[2]}, Email => {x[3]}")

    SaveAndClose()


############# APP DATABASE #############
# Import SQLite Module
# import sqlite3

# # Create Database And Connect
# db = sqlite3.connect("app_database.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Commit and Close Method


# def commit_and_close():

#     # Save (Commit) Changes
#     db.commit()

#     # Close Database
#     db.close()
#     print("Connection To Database Is Closed")


# # My User ID
# uid = int(input('enter your id : '))

# ## Input Big Message ##
# input_message = '''
# What Do You Want To Do ?
# "s" => Show All Skills
# "a" => Add New Skill
# "d" => Delete A Skill
# "u" => Update Skill Progress
# "q" => Quit The App
# Choose Option:
# '''
# ## Input Option Choose ##
# user_input = input(input_message).strip().lower()

# ## Command List ##
# commands_list = ["s", "a", "d", "u", "q"]

# ## Define The Methods##


# def show_skills():
#     cr.execute(f"select * from skills where user_id = '{uid}' order by name ")

#     results = cr.fetchall()
#     print(f"You Have {len(results)} Skills.")

#     if len(results) > 0:
#         print("Showing Skills With Progress: ")

#         for row in results:

#             print(f"Skill => {row[0]},", end=" ")

#             print(f"Progress => {row[1]}%")

#     commit_and_close()


# def add_skill():

#     sk = input("Write Skill Name: ").strip().capitalize()

#     cr.execute(
#         f"select name from skills where name = '{sk}' and user_id = '{uid}'")

#     results = cr.fetchone()

#     if results == None:
#         prog = input("Write Skill Progress: ").strip()
#         cr.execute(
#             f"insert into skills(name, progress, user_id) values ('{sk}' , {prog}, {uid})")

#     else:
#         new_update = input('would you like update y or n :)')

#         if new_update == 'y':
#             sk = input("Write Skill Name: ").strip().capitalize()
#             prog = input("Write The New Skill Progress ").strip()
#             cr.execute(
#                 f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

#         else:
#             print('as you like')

#     commit_and_close()


# def delete_skill():
#     sk = input("Write Skill Name: ").strip().capitalize()

#     cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")

#     commit_and_close()


# def update_skill():
#     sk = input("Write Skill Name: ").strip().capitalize()

#     prog = input("Write The New Skill Progress ").strip()

#     cr.execute(
#         f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")

#     commit_and_close()


# if user_input in commands_list:
#     if user_input == "s":
#         show_skills()

#     elif user_input == "a":
#         add_skill()

#     elif user_input == "d":
#         delete_skill()

#     elif user_input == "u":
#         update_skill()

#     else:
#         print("App Is Closed.")

# else:
#     print(f"Sorry This Command \"{user_input}\" Is Not Found")
# ############# APP DATABASE #############
