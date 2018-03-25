grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    total = 0
    for i in grades:
        total += i
    print total

grades_sum(grades)
