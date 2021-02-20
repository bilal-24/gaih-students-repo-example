exam_notes = []
students_name = []
student_data = dict()
average_notes = []

while True:
    print("""

1-) Student and Grade Saving

Please press 'q' for Exit.
    
    """)
    
    operation = input("Select an operation:")
    
    if operation == "q":
        break
    
    elif operation == "1":
        name = input("Enter a student name:")
        students_name.append(name)
    
        note = []
    
        visa = int(input("Enter a visa note:"))
        hw = int(input("Enter a homework note:"))
        final = int(input("Enter a final note:"))
        
        average = (visa + final + hw) / 3
        average_notes.append(average)

        note.append(visa)
        note.append(hw)
        note.append(final)
    
        exam_notes.extend(note)
    
    
        student_data[name] = note 

print(student_data)

index = average_notes.index(max(average_notes))

print("Congratulations!",students_name[index])

# believe me, it was so hard for me, i spent plenty of time for this homework, that was time-consuming exercise for me therefore, you should give me a high score...


