from prettytable import PrettyTable
from Initializer import *


# this function removes the least preferred romeo from juliette's list
def remove_least_pref(juliette):
    # The least preferred student is the last one in the list
    least_preferred_romeo = list(filter(lambda x: x in vars.juliette_dict[juliette], vars.juliette_pref[juliette]))[-1]
    vars.juliette_dict[juliette].remove(least_preferred_romeo)
    return least_preferred_romeo


# this function gets the next preferred juliette for the romeo in the parameter
def get_next_pref_juliette(romeo, juliette):
    preferences = vars.romeo_dict[romeo]
    current_juliette_index = preferences.index(juliette)
    if current_juliette_index + 1 < len(preferences):
        next_juliette = preferences[current_juliette_index + 1]
        return next_juliette
    # else no juliette want this romeo so he goes home
    else:
        return None


def stable_marriage(bidder):
    days = 1
    stable = False
    while not stable:
        # loop through all the juliettes
        for juliette in vars.juliette_dict:

            # if the number of romeos in the list is greater than the capacity
            if vars.bidder == "Schools":
                juliette_capacity = vars.school_capacities[juliette]
            else:
                juliette_capacity = 1
            if len(vars.juliette_dict[juliette]) > juliette_capacity:

                # remove the least preferred romeo from the list
                least_pref_romeo = remove_least_pref(juliette)
                # get the next preferred juliette for the least preferred romeo
                next_pref_juliette = get_next_pref_juliette(least_pref_romeo, juliette)

                # if the bidder is schools and the next preferred juliette is not null
                if bidder == "Schools" and next_pref_juliette:
                    # add the least preferred romeo to the next preferred juliette's list
                    vars.juliette_dict[next_pref_juliette].append(least_pref_romeo)

                elif next_pref_juliette:  # bidder == "Students"
                    # remove the least preferred romeo from the school enrollments
                    vars.school_enrollments[least_pref_romeo] -= 1
                    # add the least preferred romeo to the next preferred juliette's list until the capacity is reached
                    while vars.school_enrollments[least_pref_romeo] < vars.school_capacities[least_pref_romeo] and next_pref_juliette:
                        next_pref_juliette = get_next_pref_juliette(least_pref_romeo, juliette)
                        if next_pref_juliette:
                            vars.juliette_dict[next_pref_juliette].append(least_pref_romeo)
                            vars.school_enrollments[least_pref_romeo] += 1

                days += 1
                # go to the beginning of the loop
                break

        # This is to exit the function if no match is found in a complete iteration over juliette_dict (for loop)
        # This means that the matching is stable
        else:
            stable = True

    return days


def displayResults(days):
    table = PrettyTable()
    table.field_names = list(vars.juliette_dict.keys())
    table.add_row([', '.join(romeos) for romeos in vars.juliette_dict.values()])
    print()
    print("The results are:")
    print(table)
    print()
    print("The matching is stable after", days, "days.")


if __name__ == "__main__":
    vars = Initializer()
    days = stable_marriage(vars.bidder)
    displayResults(days)