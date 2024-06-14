# Project: Stable University

## Statement
Implement a student admission program using the stable marriage algorithm.

Input:
 - Student and school preferences from a file in the format of TD (CSV).
 - User selects who does the bidding.
 - Schools can accept multiple students, students go to one school and schools have capacities.

Output:
 - Student to school assignment.
 - Number of rounds needed to converage.

## Getting Started
### Installation
This project requires the following libraries:
- cutie
- PrettyTable

To install the libraries, run the following command:
```bash
pip3 install -r requirements.txt
```

### Usage
To run the program, run the following command in your terminal:
```bash
python3 main.py
```

You would be asked to choose some parameters in order to setup algorithm configuration:
1. The bidder (student or school).
2. The schools capacities CSV file.
3. The preferences input CSV file.

## Structure
## Schools capacities CSV file
Input files must be located in the `assets/capacities` folder. The file must be a CSV file with the following format:

| School 1 | School 2 | ... | School n |
|----------|----------|-----|----------|
| x        | y        | ... | z        |

Where `x`, `y`, `z`, ... are the capacities of the schools.

**NB :** The name of the school must be corresponding to the name of the school in the preferences file.

### Preferences input CSV file
Input files must be located in the `assets/preferences` folder. The file must be a CSV file with the following format:

| Student   | School 1     | School 2     | ... | School n      |
|-----------|--------------|--------------|-----|---------------|
| Student 1 | prefs of 1,1 | prefs of 1,2 | ... | prefs of 1,n  |
| Student 2 | prefs of 2,1 | prefs of 2,2 | ... | prefs of 2,n  |
| ...       | ...          | ...          | ... | ...           |
| Student m | prefs of m,1 | prefs of m,2 | ... | prefs of m, n |

Each preference cell must be in the following format: `x,y` where `x` is the student's preference for that school and vice versa for `y`.

## Initializer class
`Initializer` allows to initialize the data structure for the first iteration of the marriage algorithm. To better understand 
the data structure, we will explain the `Initializer` class with scenario 2 (`capacities3.csv` and `preferences3.csv`) as 
an example. With students bidder, here is are the attributes initialized:
 - `student_pref`: The students' preferences from `preferences2.csv` with the following format:
```json
{
  "Remi": ["A", "B"],
  "Louis": ["B", "A"],
  "Matthieu": ["A", "B"],
  "Lucas": ["A", "B"],
  "Jean-Baptiste": ["B", "A"],
  "Clement": ["A", "B"]
}
```
- `school_pref`: The schools' preferences from `preferences2.csv` with the following format:
```json
{
  "A": ["Remi", "Matthieu", "Jean-Baptiste", "Lucas", "Clement", "Louis"], 
  "B": ["Remi", "Matthieu", "Lucas", "Jean-Baptiste", "Clement", "Louis"]
}
```
- `school_capacities`: The capacity for each school from `capacities2.csv` with the following format:
```json
{
   "A": 3, 
   "B": 3
}
```
- `romeo_dict`: The preferences for the romeos' dictionary where is equal to `student_pref` for school bidder or `school_pref` for student bidder. So in our case, it's equals to `school_pref`.
- `juliette_pref`: The juliettes' preferences where is equal to `student_pref` for student bidder or `school_pref` for school bidder. So in our case, it's equals to `student_pref`.
- `juliette_dict`: The juliettes' dictionary is the first iteration of the marriage algorithm based on romeo dictionary and school capacities.
```json
{
   "Remi": [], 
   "Louis": ["B"], 
   "Matthieu": ["D"], 
   "Lucas": ["A", "C"]
}
```
- `school_enrollments`: school enrolment at a given time T. So in our case, at the beginning of the algorithm, it's equal to:
```json
{
   "A": 3, 
   "B": 3
}
```

## Algorithm


## Todo
 - [ ] rajouter des tests + tests de cas limites
 - [ ] uniformiser les noms des tests
 - [ ] faire le README
 - [ ] faire la doc
 - [ ] expliquer la structure de certaines données (juliette, romeo, getPreferencesFromCSV l.89)
