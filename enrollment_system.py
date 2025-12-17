print("=== STUDENT ENROLLMENT SYSTEM ===")

name = input("Enter full name: ")
address = input("Enter Address: ")
age = input("Enter age:")

print("\nAvailable Courses:")
print("1. BSIT")
print("2. BSCS")
print("3. BSIS")

course_choice = input("Select course (1-3):")
if course_choice == "1":
	course = "BSIT"
elif course_choice == "2":
	course = "BSCS"
else:
	course = "BSIS"

subjects = int(input("Enter number of subjects:"))
rate = 1500

total_payment = subjects * rate

print("\n=== ENROLLMENT SUMMARY ===")
print("Name:", name)
print("Address:", address)
print("Age:", age)
print("Course:", course)
print("Number of subjects:", subjects)
print("Total Payment: P", total_payment)

