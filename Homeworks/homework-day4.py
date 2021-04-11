student1_grades = [60.0, 73.0, 80.0]
student2_grades = [67.0, 75.0, 82.0]
student3_grades = [55.0, 85.0, 74.0]
student4_grades = [77.0, 88.0, 74.0]
student5_grades = [68.0, 95.0, 84.0]

# dictionary that holds students information.
students_grades = {'student1': student1_grades,
                   'student2': student2_grades,
                   'student3': student3_grades,
                   'student4': student4_grades,
                   'student5': student5_grades}


def caculate_passing_grade(grades_list):
    """This function calculates passing grades using following formula :
    passing_grade = midterm_grade * (0.3) + project_garde * (0.3) + final_grade * (0.4)
    """
    passing_grade = grades_list[0] * (0.3) + grades_list[1] * (0.3) + grades_list[2] * (0.4)
    return passing_grade


for k, v in students_grades.items():
    # --debug--print(k, v, end=" ")
    passing_grade = caculate_passing_grade(v)
    # --debug--print("passing_grade: ", passing_grade)
    v.append(passing_grade)
    print(k, v)

# Now sorting by passing grade
sorted_student_grades = sorted(students_grades.items(), key=lambda x: x[1][3], reverse=True)
print("---- Sorted ----")
print(sorted_student_grades)
