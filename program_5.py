# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_database():
    courses = {}


    while True:
        course_id = input("Enter a course ID (type 'done' to finish): ")
        if course_id == 'done':
            break # to exit the loop
        course_name = input("Enter a course name: ")
        courses[course_id] = course_name

    subject = input("Enter a subject (ex. COS): ")

    check = False  # to ensure the user gets a response
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            check = True # to stop the if not statement from happening
        if not check:
            print("Sorry, no courses were found for that subject.")


course_database()