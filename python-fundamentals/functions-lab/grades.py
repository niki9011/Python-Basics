def grade_text(grade):

    if grade_number < 3:
        return "Fail"
    elif grade_number < 3.5:
        return "Poor"
    elif grade_number < 4.5:
        return "Good"
    elif grade_number < 5.5:
        return "Very Good"
    else:
        return "Excellent"


grade_number = float(input())
print(grade_text(grade_number))
