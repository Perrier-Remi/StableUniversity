import csv

from simple_term_menu import TerminalMenu

csv_file = 'input.csv'

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
students_keys = list(students.keys())
schools_keys = list(schools.keys())

def choose_bidder():
    choices = ["Schools", "Students"]
    terminal_menu = TerminalMenu(choices, title="Choose the bidder")
    choice_index = terminal_menu.show()
    if choice_index == 0:
        return choices[choice_index], schools.fromkeys(schools, []), students
    else:
        return choices[choice_index], students.fromkeys(students, []), schools

bidder, juliette_dict, romeo_dict = choose_bidder()
print(bidder)

# romeo_dict = {'Louis': ['ENSEEIHT', 'IMT A', 'ENSIBS'], 'Remi': ['IMT A', 'ENSEEIHT', 'ENSIBS'], 'Jean-Baptiste': ['ENSEEIHT', 'IMT A', 'ENSIBS']}

def stable_mariage():
    exceeded_capacity = False
    while (not exceeded_capacity) :
        for key in romeo_dict:
            print(key)
            juliette_dict[romeo_dict[key][0]]
            exceeded_capacity = True


stable_mariage()
print(juliette_dict)