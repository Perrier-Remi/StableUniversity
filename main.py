# from simple_term_menu import TerminalMenu
import csv
import json

# this function retrieves the data from the CSV file
def getPreferencesFromCSV(filename):
    students = {}
    schools = {}

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

        headers = next(reader)[1:]
        for row in reader:
            student = row[0]
            student_prefs = {}

            # Skip the first column which is the student's name
            for idx, val in enumerate(row[1:]):
                school = headers[idx]
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

# def choose_bidder():
#     choices = ["Schools", "Students"]
#     terminal_menu = TerminalMenu(choices, title="Choose the bidder")
#     choice_index = terminal_menu.show()
#     if choice_index == 0:
#         return choices[choice_index], schools.fromkeys(schools, []), students
#     else:
#         return choices[choice_index], students.fromkeys(students, []), schools
# bidder = "Schools"

# this function removes the least preferred romeo from juliette's list
def remove_least_pref(juliette):
    # The least preferred student is the last one in the list
    least_preferred_romeo = list(filter(lambda x: x in juliette_dict[juliette], schools_pref[juliette]))[-1]
    juliette_dict[juliette].remove(least_preferred_romeo)
    return least_preferred_romeo

# this function gets the next preferred juliette for the romeo in the parameter
def get_next_pref_romeo(romeo, juliette):
    preferences = romeo_dict[romeo]
    current_juliette_index = preferences.index(juliette)
    if (current_juliette_index+1 < len(preferences)) :
        next_juliette = preferences[current_juliette_index + 1]
        return next_juliette
    # else no juliette want this romeo so he goes home

def stable_mariage():
    exceeded_capacity = True
    while (exceeded_capacity) :
        exceeded_capacity = False
        for juliette in juliette_dict.keys():
            if (len(juliette_dict[juliette]) > capacity) :
                least_pref_romeo = remove_least_pref(juliette)
                next_pref_romeo = get_next_pref_romeo(least_pref_romeo, juliette)
                if next_pref_romeo:
                    juliette_dict[next_pref_romeo].append(least_pref_romeo)
                exceeded_capacity = True


if __name__ == "__main__":
    input_filename = input("CSV filename: ")
    capacity = 2
    students_pref, schools_pref = getPreferencesFromCSV(input_filename)
    romeo_dict = students_pref
    juliette_dict = {
        school: [student for student in romeo_dict.keys() if romeo_dict[student][0] == school]
        for school in schools_pref
    }
    print("Romeo:", json.dumps(romeo_dict, indent=4))
    print("Juliette", json.dumps(juliette_dict, indent=4))
    stable_mariage()
    print("Result:", json.dumps(juliette_dict, indent=4))