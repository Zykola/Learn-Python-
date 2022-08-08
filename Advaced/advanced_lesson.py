# # --------------------------------------------------------
# # -- Advanced_Lessons => Generate Random Serial Numbers --
# # --------------------------------------------------------

# # import string
# # import random

# # x = int(input('Enter To Make Your Strong Passwoed : '))


# # def make_serial(size):

# #     all_chars = string.ascii_letters + string.digits + string.printable # make serial password
# #     chars_count = len(all_chars)  # count serial password
# #     serial_list = []  # all chars

# #     while size > 0:
# #         random_number = random.randint(0, chars_count - 1)
# #         random_character = all_chars[random_number]
# #         serial_list.append(random_character)
# #         size -= 1

# #     print("".join(serial_list))


# # make_serial(x)


# # ----------------------------------------
# # -- Flask => Intro and Your First Page --
# # ----------------------------------------

# from flask import Flask, render_template

# skills_app = Flask(__name__)

# my_skills = [("Html", 80), ("CSS", 75), ("Python", 95),
#              ("MySQL", 45), ('Flutter', 90)]


# @skills_app.route("/")
# def homepage():
#     return render_template("home_page.html",
#                            title="Homepage",
#                            custom_css="home")


# @skills_app.route("/add")
# def add():
#     return render_template("add.html",
#                            title="Add Skill",
#                            custom_css="add")


# @skills_app.route("/about")
# def about():
#     return render_template("about_page.html", title="About Us")


# @skills_app.route("/skills")
# def skills():
#     return render_template("skills.html",
#                            title="My Skills",
#                            page_head="My Skills",
#                            description="This Is My Skills Page",
#                            skills=my_skills,
#                            custom_css="skills")


# if __name__ == "__main__":
#     skills_app.run(debug=True, port=9000)


# ---------------------------------------------------
# -- Web Scraping => Control Browser With Selenium --
# ---------------------------------------------------
# - Control Browser With Selenium For Automated Testing
# - Download File From The Internet
# - Subtitle Download And Add On Your Movies [ Many Modules ]
# - Get Quotes From Websites
# - Get Gold and Currencies Rate
# - Get News From Websites
# - --------------------------------------------

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome(ChromeDriverManager().install())

# browser.get("https://elzero.org")

# browser.find_element_by_css_selector(
#     ".search-field").send_keys("Front-End Developer")

# browser.find_element_by_css_selector(".search-submit").click()

# browser.find_element_by_css_selector(
#     ".all-search-posts .search-post:first-of-type h3 a").click()

# browser.implicitly_wait(5)

# views_count = browser.find_element_by_css_selector(
#     ".z-article-info .z-info:last-of-type span:last-child")

# browser.implicitly_wait(5)

# print(views_count.get_attribute('innerHTML'))

# browser.quit()

# import numpy as np

# my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
# print(my_array5.ndim)
# print(my_array5.shape)

# print("#" * 50)


# reshaped_array5 = my_array5.reshape(4, 5)
# print(reshaped_array5)
