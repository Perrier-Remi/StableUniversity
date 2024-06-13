import cutie
import csv
import os


class Initializer:
    """ A class used to initialize the data for stable marriage algorithm.
    @ivar bidder: The chosen bidder.
    @type bidder: str
    @ivar student_pref: The students' preferences.
    @type student_pref: dict
    @ivar school_capacities: The capacity for each school.
    @type school_capacities: dict
    @ivar juliette_pref: The preferences for the juliettes.
    @type juliette_pref: dict
    @ivar school_enrollments: The number of students enrolled in each school.
    @type school_enrollments: dict
    """

    def __init__(self):
        """ Initialize all the necessary attributes for the table marriage algorithm. """
        self.bidder = Initializer.chooseBidder()
        # self.juliette_capacity = self.school_capacity if self.bidder == "Schools" else 1
        self.student_pref, self.school_pref = Initializer.getPreferencesFromCSV(Initializer.chooseCSVFile())
        self.school_capacities = Initializer.chooseSchoolCapacity()
        self.juliette_pref, self.juliette_dict, self.romeo_dict = self.initializeJulietteRomeo()
        self.school_enrollments = self.initializeSchoolEnrollments()

    @staticmethod
    def chooseBidder():
        """ Prompts the user to choose the bidder.
        @return: The chosen bidder.
        @rtype: str
        """
        bidder = ["Schools", "Students"]
        print("Choose the bidder")
        return bidder[cutie.select(bidder, selected_index=0)]

    @staticmethod
    def chooseSchoolCapacity():
        # read the capacities from a CSV file chosen by the user
        csv_files = [f for f in os.listdir('./assets/capacities') if f.endswith('.csv')]
        if not csv_files:
            print("No CSV file found in the current directory")
            print("Please put the CSV file in the current directory and try again")
            print("Exiting...")
            exit()
        print("Choose the CSV file for the school capacities")
        capacity_file = "./assets/capacities/" + csv_files[cutie.select(csv_files, selected_index=0)]

        school_capacities = {}
        with open(capacity_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            row = next(reader)
            for idx in range(0, len(row)):
                school_capacities[headers[idx]] = int(row[idx])

        return school_capacities
        # return cutie.get_number("What are the schools capacities? :", min_value=1, allow_float=False)

    @staticmethod
    def chooseCSVFile():
        """ Prompts the user to choose the CSV file.
        @return: The chosen CSV file.
        @rtype: str
        """
        csv_files = [f for f in os.listdir('./assets/preferences') if f.endswith('.csv')]
        if not csv_files:
            print("No CSV file found in the current directory")
            print("Please put the CSV file in the current directory and try again")
            print("Exiting...")
            exit()
        print("Choose the CSV file")
        return "./assets/preferences/" + csv_files[cutie.select(csv_files, selected_index=0)]

    @staticmethod
    def getPreferencesFromCSV(filename):
        """ Reads the preferences from the CSV file.
        @param filename: The name of the CSV file.
        @type filename: str
        @return: A tuple containing two dictionaries. The first dictionary contains the students' preferences,
                 and the second dictionary contains the schools' preferences.
        @rtype: tuple
        """
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

    def initializeJulietteRomeo(self):
        if self.bidder == "Schools":
            romeo_dict = self.student_pref.copy()
            juliette_dict = {
                school: [student for student in romeo_dict.keys() if romeo_dict[student][0] == school]
                for school in self.school_pref
            }
            juliette_pref = self.school_pref.copy()

        else:
            romeo_dict = self.school_pref.copy()
            juliette_dict = {
                student: [
                    school for school in romeo_dict.keys()
                    if student in romeo_dict[school][:self.school_capacities[school]]
                ]
                for student in self.student_pref
            }
            juliette_pref = self.student_pref.copy()

        return juliette_pref, juliette_dict, romeo_dict


    def initializeSchoolEnrollments(self):
        school_enrollments = self.romeo_dict.copy()

        # initialize the capacity of each school to 0
        for school in school_enrollments:
            school_enrollments[school] = 0

        # for each school, for every student added to the list, increment the capacity
        for juliette in self.juliette_dict.keys():
            for romeo in self.juliette_dict[juliette]:
                school_enrollments[romeo] += 1

        return school_enrollments