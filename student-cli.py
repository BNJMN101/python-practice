print("Hi! Welcome to the Student CLI")

student_info = {
    "name": "Benjamin",
    "age": 16,
    "course": "Computer Science"
}
print("")
print("===================STUDENT SYSTEM===================")
print()
print("1. View student information")
print("2. Change Course")
print("3. Add programming language")
print("4. Show all information")
print("5. Exit")
print()

print("=====================================================")


while True:
    choice = input("What would you like to do? (1-5)")

    if choice == "1":
        answer = input("Do you want to view student info (yes/no)?").lower()
        if answer == "yes":
            print(student_info)
        elif answer == "no":
            print("Alright then.")
        else:
            print("Use yes/no please")
    
    elif choice == "2":
        answer = input("Do you want to change your course? (yes/no)").lower()
        if answer == "yes":
            course_change = input("What would you like to change the course to")
            student_info["course"] = course_change
            print("The course has been successfully updated!")
        elif answer == "no":
            print("Alright")
        else:
            answer == print("Use (yes/no) please")

    elif choice == "3":
        answer = input("Do you want to add a programming language (yes/no)?").lower()
        if answer == "yes":
            language_change = input("What would programming language would you like to add (yes/no)?")
            student_info["programming_language"] = language_change
            print("The programming language has been successfully added!")
        elif answer == "no":
            print("Alright then")
        else:
            print("Use yes/no please")

    elif choice == "4":
        answer = input("Do you want to view all the student info (yes/no)?")
        if answer == "yes":
            print(student_info)
        elif answer == "no":
            print("Alright then.")
        else:
            print("Use yes/no please")

    elif choice == "5":
        answer = input("Do you want to exit the CLI (yes/no)?")
        if answer == "yes":
            break
        elif answer == "no":
            print("Alright.")
        else:
            print("Use yes/no please")
            
    else:
        print("Please pick an option (1-5)")