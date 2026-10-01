# username = input("What's your name?")
# def greet(name): #The name inaide the parenthesis is called a parameter
#     print("Hello! Welcome to Python! 🐍", name) 


# greet(username)

# def introduce(name, age, course):
#     print("Hey, I'm", name, "I'm", age, " years old, and I study", course)

# introduce("Ben.", 16, "Computer Science")

# def add(a, b):
#     return(a + b)

# result = add(5, 9)
# print(result)


# a function that takes data → processes it → returns a result → stores that result.
# def calculate_total(price, quantity, discount):
#     return(price * quantity - discount)

# result = calculate_total(500, 3, 200)

# print(result)

# def check_age(age):
#     if age < 13:
#         return "You're a child"
#     elif 17>= age >= 13:
#         return "You're a teenager"
#     elif age >= 18:
#         return  "You're an adult"

# result = check_age(18)
# print(result)

# def show_languages(languages):
#     return languages

# fav_lang = show_languages(["Python", "Django", "Flask",])

# for lang in fav_lang:
#     print(lang)

# def get_favorite_languages(languages):
#     for lang in languages:
#         print(lang)

# get_favorite_languages(["Python", "Django", "Flask"])

# def show_student_info(name, course):
#     for name in name:
#         print(name)
#     for course in course:
#         print(course)

# show_student_info("Benjamin", "Computer Science")

# def show_student_info(name, course):
#     print("Name:", name)
#     print("Course:", course)

# show_student_info("Benjamin", "Computer Science")



def calculate_age(current_year, birth_year):
    return current_year - birth_year

def create_student(name, age, course):
    return f"Name: {name}\nAge: {age}\nCourse: {course}"

def get_student_info():
    return create_student("Benjamin", calculate_age(2026, 2010), "Computer Science")

student = get_student_info()
print(student)