from simple_term_menu import TerminalMenu
import csv
import json
import os

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

def choose_bidder():
    choices = ["Schools", "Students"]
    terminal_menu = TerminalMenu(choices, title="Choose the bidder")
    choice_index = terminal_menu.show()
    return choices[choice_index],

def choose_csv_file():
    # retrieve all csv files in the current directory
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    terminal_menu = TerminalMenu(csv_files, title="Choose the CSV file")
    choice_index = terminal_menu.show()
    return csv_files[choice_index]

def choose_school_capacity():
    user_input = input("Enter the capacity of the schools: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        return choose_school_capacity()

# this function removes the least preferred romeo from juliette's list
def remove_least_pref(juliette):
    # The least preferred student is the last one in the list
    if bidder == "Schools":
        least_preferred_romeo = list(filter(lambda x: x in juliette_dict[juliette], school_pref[juliette]))[-1]
    else :
        least_preferred_romeo = list(filter(lambda x: x in juliette_dict[juliette], student_pref[juliette]))[-1]
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

def stable_mariage(bidder):
    exceeded_capacity = True
    while (exceeded_capacity) :
        exceeded_capacity = False
        for juliette in juliette_dict.keys():
            if (len(juliette_dict[juliette]) > capacity) :
                least_pref_romeo = remove_least_pref(juliette)
                next_pref_romeo = get_next_pref_romeo(least_pref_romeo, juliette)
                if bidder == "Schools":
                    if next_pref_romeo:
                        juliette_dict[next_pref_romeo].append(least_pref_romeo)
                else:
                    school_capacities[least_pref_romeo] -= 1
                    while (school_capacities[least_pref_romeo] < user_capacity and next_pref_romeo):
                        next_pref_romeo = get_next_pref_romeo(least_pref_romeo, juliette)
                        if next_pref_romeo:
                            juliette_dict[next_pref_romeo].append(least_pref_romeo)
                            school_capacities[least_pref_romeo] += 1
                exceeded_capacity = True


if __name__ == "__main__":
    # input_filename = choose_csv_file()
    # bidder = choose_bidder()
    # user_capacity = choose_school_capacity()
    input_filename = "test2.csv"
    bidder = "Students"
    user_capacity = 1


    student_pref, school_pref = getPreferencesFromCSV(input_filename)
    # romeo_pref, juliette_pref = getPreferencesFromCSV(input_filename)
    if bidder == "Schools":
        capacity = user_capacity

        romeo_dict = student_pref.copy()
        juliette_dict = {
            school: [student for student in romeo_dict.keys() if romeo_dict[student][0] == school]
            for school in school_pref
        }

    else:
        capacity = 1

        romeo_dict = school_pref.copy()

        juliette_dict = {
            student: [
                school for school in romeo_dict.keys()
                if student in romeo_dict[school][:user_capacity]
            ]
            for student in student_pref
        }

        school_capacities = romeo_dict.copy()

        for school in school_capacities:
            school_capacities[school] = 0
        # for each school, for every student added to the list, increment the capacity
        for juliette in juliette_dict.keys():
            for romeo in juliette_dict[juliette]:
                school_capacities[romeo] += 1

    print("Romeo:", json.dumps(romeo_dict, indent=4))
    print("Juliette", json.dumps(juliette_dict, indent=4))
    stable_mariage(bidder)
    print("Result:", json.dumps(juliette_dict, indent=4))