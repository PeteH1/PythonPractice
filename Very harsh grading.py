# Generates a percentage to 2 d.p. based on 3 scores
def overall_percentage(hw, assess, exam):
    total_score = hw + assess + exam
    total_perc = (total_score / 175) * 100
    total_perc = round(total_perc, 2)
    return total_perc

# Generates a grade based on a percentage
def overall_grade(total_perc):
    if total_perc >= 99:
        final_grade = "A"
    elif total_perc >= 98:
        final_grade = "B"
    elif total_perc >= 97:
        final_grade = "C"
    else:
        final_grade = "FAIL"
    return final_grade

student_name = input("Enter name: ")
hw_score = int(input("Enter homework score (out of 25): "))
assess_score = int(input("Enter assessment score (out of 50): "))
exam_score = int(input("Enter exam score (out of 100): "))

# Calling functions to generate percentage and grade based on inputs
percentage = overall_percentage(hw_score, assess_score, exam_score)
grade = overall_grade(percentage)

print(student_name + "'s overall percentage is " + str(percentage) + "%")
print(student_name + "'s overall grade is " + grade)