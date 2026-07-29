#         ---------- Student Management System --------------
students = [
    {
        "name": "Ahmed",
        "age": 21,
        "major": "AI",
        "grades": [80, 90, 75]
    },
    {
        "name": "Sara",
        "age": 20,
        "major": "CS",
        "grades": [95, 85, 90]
    },
    {
        "name": "Omar",
        "age": 22,
        "major": "IT",
        "grades": [60, 70, 65]
    }
]

# 1- calculate_average(grades)        

def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    average = total/len(grades)
    return average

# 2- get_grade(average)

def get_grade(average):

    if(average >=90):
        return "A"

    elif(average>=80):
        return "B"

    elif(average>=70):
        return "C"
    
    elif(average>=60):
        return "D"
    
    else:
        return "F"

#3- Print Students Data:

def print_students_data():

  for student in students:
      
      average = calculate_average(student["grades"])
      grade = get_grade(average)

      print(f"Name: {student["name"]}")
      print(f"Age: {student["age"]}")
      print(f"Major: {student["major"]}")
      print(f"Average: {average}")
      print(f"Grade: {grade}")
      print("-" * 30)

#4- Add New Student
def add_student(student_dic):
    students.append(student_dic)

add_student({
        "name": "Sami",
        "age": 26,
        "major": "CS",
        "grades": [95, 50, 90]
    })

print_students_data()     