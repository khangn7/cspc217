# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 217 Summer 2023
# INSTRUCTOR: Jonathan Hudson
# Vqb4blV7487iRCgNdqhr
# DO NOT EDIT THE ABOVE LINES

# Student UCID: 30237573
# 

from sys import argv, exit
import os

def main():
    """
    Main, gets filename from command line argument (or prompts if not included), reads file into dictionary
    :return: None
    """
    # Check args
    if (len(argv) != 2):
        print("Need 1 command line arguments")
        print("Usage: main.py infile.txt")
        exit(1)
    
    # Get filename
    infile = argv[1]
    if (not os.path.exists(infile)):
        print(f"{infile} doesn't exist in current directory")
        exit(1)
         
    # Open file
    try:
        infileHandler = open(infile)
    except Exception as e:
        print("error reading file")
        print(e)
        infileHandler.close()
        exit(1)
    
    # Make dict from file
    contact_records = {}
    for line in infileHandler:
        line = line[:-1].split(",") # [:-1] is bc \n
        sick = line[0]
        contact_records[sick] = line[1:]
    
    # Part 1
    # Print data from dict
    print("Contact Records:")
    sick_people = sorted(list(contact_records.keys()))
    for sick in sick_people:
        print(f"  {sick} had contact with {formatList(contact_records[sick])}")
    print()

    # Part 2
    list_p2 = part2(contact_records)
    print("Patient Zero(s):", formatList(list_p2))

    # Part 3
    list_p3 = part3(contact_records)
    print("Potential Zombies:", formatList(list_p3))


    # Part 4
    list_p4 = part4(contact_records)
    print("Neither Patient Zero or Potential Zombie:", formatList(list_p4))

    # # Part 5
    list_p5 = part5(contact_records)
    print("Most Viral People:", formatList(list_p5))

    # Part 6
    list_p6 = part6(contact_records)
    print("Tastiest:", formatList(list_p6))
    print()

    # Part 7
    # print sorted by heights
    dict_p7 = part7(contact_records)
    p7_names = list(dict_p7.keys())
    p7_names.sort(key=(lambda x: dict_p7[x]), reverse=True)
    print("Heights:")
    for name in p7_names:
        print(f"  {name}: {dict_p7[name]}")

    
    infileHandler.close()

    return 0

def formatList(names:list) -> str:
    ## Format a list of items so that they are comma separated and "and" appears
    #  before the last item.
    #  Parameters:
    #    data: the list of items to format
    #  Returns: A string containing the items from data with nice formatting
    names = sorted(names)
    n = len(names)
    if n == 1:
        return names[0]
    if n == 2:
        return names[0] + " and " + names[1]
    return ", ".join(names[:-1]) + " and " + names[-1]

def part2(my_dict:dict) -> list:
    """
    Return possible patient zero(s) from contact records dict
    patient zero is person who is sick but has not got it from anyone in my_dict
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of possible patient zero(s)
    """
    patient_zeros = []

    #process data to make list
    for check_person in my_dict:
        found_in_contacted = False

        # loop through dict values for suspect

        # break and continue not allowed bruh
        # if breaks are used (uncommented) here, time is lower bound
        for key in my_dict:
            for contacted in my_dict[key]:
                if contacted == check_person:
                    found_in_contacted = True
                    # break
            # if found_in_contacted:
            #     break

        if not found_in_contacted:
            patient_zeros.append(check_person)
        

    return sorted(patient_zeros)

def part3(my_dict:dict) -> list:
    """
    Return potential zombies (sick people) from contact records dict
    a zombie is a person who has been in contact with a known sick person but isn't recorded as a sick person
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of potential sick people
    """
    potential_zombies = []

    for key in my_dict:
        for contacted in my_dict[key]:
            if (not my_dict.get(contacted, False)) and (not (contacted in potential_zombies)):
                potential_zombies.append(contacted)

    return sorted(potential_zombies)

def getPeople(my_dict:dict) -> list:
    """
    returns list of people in contact records dict
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of people
    """
    names = []
    for sick_p in my_dict:
        if not (sick_p in names):
            names.append(sick_p)
        for contacted in my_dict[sick_p]:
            if not (contacted in names):
                names.append(contacted)
    return sorted(names)

def part4(my_dict:dict, patient_zeros:list=None, potential_zombies:list=None) -> list:
    """
    Return people in my_dict who are not a patient zero or a potential zombie
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of people described above
    """
    if patient_zeros == None:
        patient_zeros = part2(my_dict)
    if potential_zombies == None:
        potential_zombies = part3(my_dict)
    
    all_names = getPeople(my_dict)
    ret_names = []
    for name in all_names:
        if not (name in ret_names):
            is_zero = name in patient_zeros
            is_zomb = name in potential_zombies
            if (not is_zero) and (not is_zomb):
                ret_names.append(name)
    
    return sorted(ret_names)
            
def part5(my_dict:dict) -> list:
    """
    Return most viral people, people who have contacted most people
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of most viral people
    """
    viral_names = []

    counts = {}
    highest = 0 # will never encounter comparision with 0 or lower
    for sick_p in my_dict:
        n = len(my_dict[sick_p])
        if n > highest:
            highest = n
        counts[sick_p] = n
    
    for sick_p in counts:
        if counts[sick_p] == highest:
            viral_names.append(sick_p)

    return viral_names

def part6(my_dict:dict) -> list:
    """
    Return tastiest people, people who have been contacted by most people
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: list of strs, names of tastiest people
    """
    exposure_count = {}
    for key in my_dict:
        for contacted in my_dict[key]:
            if contacted in exposure_count:
                exposure_count[contacted] += 1
            else:
                exposure_count[contacted] = 1

    highest = max(exposure_count.values())
    tasty_people = []
    for name in exposure_count:
        if exposure_count[name] == highest:
            tasty_people.append(name)

    return sorted(tasty_people)

def part7(my_dict:dict) -> dict:
    """
    Returns height of everyone in my_dict. Height is one plus the highest number of people between a potential zombie and
    a person. Potential zombies have a height of 0, no plus 1

    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :return: dict, key person_name : height
    """
    p_zombies = part3(my_dict)

    all_names = part2(my_dict)
    heights = {}
    for name in all_names:
        populateHeights(my_dict, heights, p_zombies, name)

    return heights

def populateHeights(my_dict:dict, out_dict:dict, p_zombies:list, person:str):
    """
    populates dict initialized somewhere else with heights found through finding height of :param person:
    :param my_dict: dict, key sick_person : values (list) people who came in contact with key
    :param out_dict: empty dict initialized outside this function which will be populate
    :param p_zombies: potential zombies as returned by part3(my_dict)
    :param person: name of person to start finding height for
    """
    if person in out_dict:
        return out_dict[person]
    
    if person in p_zombies:
        if not (person in out_dict):
            out_dict[person] = 0
        return 0

    contact_n = len(my_dict[person])
    heights = [None] * contact_n
    for i in range(contact_n):
        name = my_dict[person][i]
        h = populateHeights(my_dict, out_dict, p_zombies, name)
        heights[i] = h

    highest_height = max(heights)
    
    if not (person in out_dict):
        out_dict[person] = 1 + highest_height

    return 1 + highest_height



if __name__ == "__main__":
    main()
