grade_tutorials= int(input("What is the numerical grade that you have received for tutorials?"))
grade_quizzes= int(input("What is the numerical grade that you have received for tutorials?"))
grade_assignments= int(input("What is the numerical grade that you have received for tutorials?"))
grade_final= int(input("What is the numerical grade that you have received for tutorials?"))
grade=(grade_assignments+grade_final+grade_quizzes+grade_tutorials)/4
if grade>100 or grade<0:
    print("That is not a valid numerical grade.")
elif grade>=90:
    print("You received an A+")
elif grade>=85:
    print("You received an A")
elif grade>=80:
    print("You received an A-")
elif grade>=77:
    print("You received a B+")
elif grade>=73:
    print("You received a B")
elif grade>=70:
    print("You received a B-")
elif grade>=67:
    print("You received a C+")
elif grade>=63:
    print("You received a C")
elif grade>=60:
    print("You received a C-")
elif grade>=57:
    print("You received D+")
elif grade>=53:
    print("You received a D")
elif grade>=50:
    print("You received a D-")
else:
    print("You get an F")
