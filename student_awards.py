# Name: Tala Chuthi
# File Name: student_awards.py
# Description: This program accepts student names and GPAs
# and determines whether each student qualifies for the
# Dean's List or Honor Roll.

def main():

    while True:

        last_name = input("Enter student's last name (or ZZZ to quit): ")

        if last_name.upper() == "ZZZ":
            print("Program ended.")
            break

        first_name = input("Enter student's first name: ")

        try:
            gpa = float(input("Enter student's GPA: "))

        except ValueError:
            print("Invalid GPA. Please enter a number.\n")
            continue

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.\n")

        elif 3.25 <= gpa < 3.5:
            print(f"{first_name} {last_name} has made the Honor Roll.\n")

        else:
            print(f"{first_name} {last_name} did not qualify.\n")


main()