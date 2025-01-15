# Data-Structure
# built-in= list,tuple,dictionary,set
# user defined= stack , queue ,tree, graph ,linked list

# list 
# tuple =() or 1,2,3 
# Note:tuple with single element (3,) tuples work faster then list
# dict1={'1':5,'3':0}
# set1={1,2,3,4,5}
""" x=set('hello')
print(x)
y=set([1,2,2,2,4,5])
print(y) """


# Dictionary mapping grades to their corresponding GPA values
grade_to_gpa = {
    "A+": 4.0, "A": 4.0, "A-": 3.67,
    "B+": 3.33, "B": 3.0, "B-": 2.67,
    "C+": 2.33, "C": 2.0, "C-": 1.67,
    "D+": 1.33, "D": 1.0, "F": 0.0
}

# Initialize variables
""" num_courses = 0
total_gpa_points = 0
is_done = False

# Loop to collect grades from the user
while not is_done:
    grade = input("Enter a grade (or press Enter to finish): ").strip().upper()  # Read and clean input
    if grade == "":  # Exit loop if input is empty
        is_done = True
    elif grade not in grade_to_gpa:  # Handle invalid grades
        print(f"Unknown grade '{grade}' ignored. Please enter a valid grade.")
    else:  # Process valid grades
        num_courses += 1
        total_gpa_points += grade_to_gpa[grade]

# Calculate and display GPA if at least one grade was entered
if num_courses > 0:
    gpa = total_gpa_points / num_courses
    print(f"Your GPA is {gpa:.3f}")
else:
    print("No valid grades were entered. GPA cannot be calculated.")
 """