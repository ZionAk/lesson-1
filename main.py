#Take a name as input from the user and tell the total marks of the student as output.
student_marks={"John":84,
"ryan":45,
"jim":76,
"masie":65,
"daniel":43,
"harmony":96}

student_name=input("Whose test result do you want to see?\n")

if student_name.lower() in student_marks:
    print(student_name,"'s total marks:",student_marks[student_name])
else:
    print("That student is not on the list")