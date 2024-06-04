import csv

csv_file = 'input.csv'
university = {}

def read_preferences_from_csv():
    students = {}
    schools = {}

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the first header for students' names
        headers = next(reader)[1:]

        for row in reader:
            student = row[0]
            student_prefs = {}

            # Skip the first column which is the student's name
            for idx, val in enumerate(row[1:], 1):
                school = headers[idx-1]
                # Split the preference into student's preference and school's preference
                student_pref, school_pref = map(int, val.split(','))
                student_prefs[school] = student_pref
                if school not in schools:
                    schools[school] = {}
                schools[school][student] = school_pref

            # add student's preferences to the dictionary
            students[student] = student_prefs

    # Sort preferences based on ranking
    for student in students:
        students[student] = sorted(students[student], key=students[student].get)
    for school in schools:
        schools[school] = sorted(schools[school], key=schools[school].get)

    return students, schools

students, schools = read_preferences_from_csv()
print(students)
print(schools)
