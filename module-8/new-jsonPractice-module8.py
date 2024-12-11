#Amanda New
#CSD325-A311
#JSON Practice
#Module 8

import json

class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email       

class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Student):
            return {
                "F_Name": o.F_Name,
                "L_Name": o.L_Name,
                "Student_ID": o.Student_ID,
                "Email": o.Email
            }
        return super().default(o)

def print_student_list(student_list):

    for Student in student_list:
        print(f"{Student.F_Name} , {Student.L_Name} : ID = {Student.Student_ID} , Email = {Student.Email}")


def load_students_from_json(student_data):

    with open("c:/csd/csd-325/csd-325/module-8/student.json", "r") as file:
        student_data = json.load(file)

    students = []
    for data in student_data:
        student = Student(data["F_Name"], data["L_Name"], data["Student_ID"], data["Email"])
        students.append(student)

    return students
    

def main():

    student_list = load_students_from_json("c:/csd/csd-325/csd-325/module-8/student.json") 
    print("Original Student List:")
    print(" ")
    print_student_list(student_list)
    print("")

    new_student = Student("Amanda", "New", "61396", "amandanotnew@gmail.com")

    student_list.append(new_student)

    print("===================================")
    print("")
    print("Updated Student List:")
    print("")
    print_student_list(student_list)

    with open("c:/csd/csd-325/csd-325/module-8/student.json", "w") as f:
        json.dump(student_list, f, cls=StudentEncoder, indent=4)
        
    print("")
    print("JSON file was updated!")

if __name__ == "__main__":
    main()