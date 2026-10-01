# name = input("Hi, what's your name? ")

# print("Hey", name) 

# age = int(input("So, how old are you?"))

# if age >= 18:
#     print(age, "So you're an adult!")
# else:
#     print("Nice, you're still a teen")

# print("")
# programming_language = input("So, what programming language do you code in?").lower()

# if programming_language == "python":
#     print("Python is a pretty damn good choice for programming. 🐍")
# elif programming_language == "javascript":
#     print("Ohh, javascript! It's like the most versatile programming language!")
# elif programming_language == "c++":
#     print("Oh shit, c++ is like a high-level language. For making software applications. Impressive")
# else:
#     print("Oh cool! I haven't learnt that yet. ")

# count = 0

# while count < 5:
#     print("I love Python")
#     count = count + 1

# # Loop Program

# number = int(input("Hi, how many times should I say I love Python"))

# count = 0

# while count < number:
#     print("I love Python ")
#     count = count + 1

# while True:
#     language = input("What programming was used to build this program").lower()
#     if language == "python":
#         print("Hell Yeah!")
#         break
#     print("Nah, try again")

# For loops
# For every number in this range

# # range(start, stop, steps)
# for number in range(10, 0, -1):
#     print(number)

# For every language in this list
# languages = ["Python", "JavaScript", "React", "Supabase", "Django", "Flask"]

# languages.insert(6, "FastAPI")

# languages.remove("React")
# languages.pop(3)

# if "Django" in languages:
#     print("Django is in the fucking list, whooooo!!")
# else:
#     print("Aww shit, Django ain't in the list")

# print(len(languages))

# for language in languages:
#     if language == "Python":
#         print("🐍 That's my current focus!")
#     elif language == "JavaScript":
#         print("🌐 Web development!")
#     else:
#         print("Cool Technology").



# Dictionaries - A dictionary stores:
# key --> value
student =  {
    "name": "Benjamin",
    "age": 16,
    "course": "Computer Science"
}
student["course"] = "Software Engineering"
student["programming_language"] = "Python"

# if "programming_language" in student and student["programming_language"] == "Python":
#     print("This is my language 🐍/")

# for key in student:
#     print(key)

for key, value in student.items():
    print(key, ":", value)
#Notes--------------------------------------------------------------------------------------------------
#languages[index]             # access
#languages[index] = "X"       # change
#languages.append("X")        # add to end
#languages.insert(i, "X")     # add at position
#languages.remove("X")        # remove by value
#languages.pop(i)             # remove by index
#"X" in languages             # check existence