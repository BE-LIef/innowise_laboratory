students = []
def main():
    while True:
        print("-"*3, "Student Grade Analyzer", "-"*3)
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                add_a_new_student()
            elif choice == 2:
                add_a_grades_for_a_student()
            elif choice == 3:
                show_report()
            elif choice == 4:
                find_top_performer()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please enter a valid choice (1-5).")
        except:
            print("Invalid input. Please enter a valid choice (1-5).")
def add_a_new_student():
    name = input("Enter student name:")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists in the system.")
            return
    students.append({"name": name, "grades": []})
def add_a_grades_for_a_student():
    if not students:
        print("No students available. Please add a student first.")
        return
    name = input("Enter student name:")
    found_student = None
    for student in students:
        if student["name"].lower() == name.lower():
            found_student = student
            break
    if found_student is None:
        print(f"Student '{name}' not found.")
        return
    while True:
            grade_input = input("Enter a grade (or 'done' to finish): ")
            if grade_input.lower() == 'done':
                break
            try:
                grade = float(grade_input)
                if 0 <= grade <= 100:
                    found_student["grades"].append(grade) 
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
def show_report():
    if not students:
        print("No students available.")
        return
    print("\n--- Student Report ---")
    averages = []
    has_grades = False
    for student in students:
        if not student["grades"]:
            print(f"{student['name']}'s average grade is N/A.")
            averages.append(None)
        else:
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
            has_grades = True
    if has_grades:
        valid_averages = [avg for avg in averages if avg is not None]
        print("--------------------------")
        print(f"Max Average: {max(valid_averages):.1f}")
        print(f"Min Average: {min(valid_averages):.1f}")
        print(f"Overall Average: {sum(valid_averages)/len(valid_averages):.1f}")
    else:
        print("No students have grades yet.")
def find_top_performer():
    if not students:
        print("No students available.")
        return
    students_with_grades = []
    for student in students:
        if student["grades"]:
            avg = sum(student["grades"]) / len(student["grades"])
            students_with_grades.append((student["name"], avg))
    if not students_with_grades:
        print("No students have grades yet.")
    else:
        top_student = max(students_with_grades, key=lambda x: x[1])
        print(f"The top student is {top_student[0]} with an average grade of {top_student[1]:.1f}.")

if __name__ == "__main__":
    main()