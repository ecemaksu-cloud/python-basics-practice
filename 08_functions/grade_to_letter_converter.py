# Convert a numeric grade to a letter grade

def grade_to_letter(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 70 <= grade < 90:
        return "B"
    elif 50 <= grade < 70:
        return "C"
    elif 0 <= grade < 50:
        return "F"
    else:
        return "Invalid grade"

numeric_grade = int(input("Enter your grade: "))

result = grade_to_letter(numeric_grade)

print("Letter grade =", result)
