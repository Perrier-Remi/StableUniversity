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

dire que c'est à la charge de l'utilisateur que de vérifier que les fichiers csv sont bien formattés


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

## Main

This file contains the main function of the program. It reads the preferences from the CSV file, creates the students and schools, and runs the stable marriage algorithm.

## Todo
 - [ ] rajouter des tests + tests de cas limites
 - [x] uniformiser les noms des tests
 - [ ] faire le README
 - [ ] faire la doc
 - [ ] expliquer la structure de certaines données (juliette, romeo, getPreferencesFromCSV l.89)
