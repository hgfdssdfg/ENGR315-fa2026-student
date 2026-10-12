import os
import sys
import csv
import numpy
"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    file_path = "data/covid/us-counties.csv"
   
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)
    
    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###
#Open the data file, store the data rows as tuples.
data: list = parse_nyt_data(file_path="data/covid/us-counties.csv")
# Find the first positive case in Harrisonburg or rockingham county
def find_first_positive_case_in_harrisonburg(data):
    #create a list to store cases in Harrisonburg
    cases_in_harrisonburg = []
    #Sort through the data to find if the third element is Virginia, second element is Harrisonburg city, and cases are positive
    for entry in data:
        if entry[2] == "Virginia" and entry[1] == "Harrisonburg city" and entry[4] > 0:
            cases_in_harrisonburg.append(entry)
    #When the first positive case is found, return it, If not found, return None
    return cases_in_harrisonburg[0] if cases_in_harrisonburg else None
#Send print the date of the first positive case in Harrisonburg to main


def find_first_positive_case_in_rockingham(data):
    #create a list to store cases in Rockingham
    cases_in_rockingham = []
    #Sort through the data to find if the third element is Virginia, second element is Rockingham, and cases are positive.
    for entry in data:
        if entry[2] == "Virginia" and entry[1] == "Rockingham" and entry[4] > 0:
            cases_in_rockingham.append(entry)
    #When the first positive case is found, return it, If not found, return None
    return cases_in_rockingham[0] if cases_in_rockingham else None
# Send print the date of the first positive case in Rockingham County to main



def day_with_most_cases_in_harrisonburg_city(data):
    #Create an empty list to store all cases in Harrisonburg City
    all_cases_in_harrisonburg_city = []
    most_cases_in_harrisonburg_city = None
    #Start an empty list for the highest number of cases
    highest = 0
    #Find all the cases in Harrisonburg City
    for entry in data:
        if entry[2] == "Virginia" and entry[1] == "Harrisonburg city" and entry[4] > 0:
            all_cases_in_harrisonburg_city.append(entry)
            
    #Find the day with the most cases in Harrisonburg City
    for entry in all_cases_in_harrisonburg_city:
        #If the next entry is higher than the current highest, it replaces it into the list, highest
        if entry[4] > highest:
            #When the highest number of cases is found, store it in the list, most_cases_in_harrisonburg_city
            highest = entry[4]
            most_cases_in_harrisonburg_city = entry
    #Return the most cases in Harrisonburg City
    return most_cases_in_harrisonburg_city[0] if most_cases_in_harrisonburg_city else None


def day_with_most_cases_in_rockingham_county(data):
    #Create an empty list to store all cases in Rockingham County
    all_cases_in_rockingham_county = []
    most_cases_in_rockingham_county = None
    highest = 0
    r_first_date = None
    r_second_date = None
    #Find all the cases in Rockingham County
    for entry in data:
        if entry[2] == "Virginia" and entry[1] == "Rockingham" and entry[4] > 0:
            all_cases_in_rockingham_county.append(entry)
    #Find the day with the most cases in Rockingham County
    for entry in all_cases_in_rockingham_county:
        if entry[4] > highest:
            highest = entry[4]
            most_cases_in_rockingham_county = entry
    return most_cases_in_rockingham_county[0] if most_cases_in_rockingham_county else None


def  seven_day_period_of_most_cases_in_harrisonburg_city(data):
    #Create an empty list to store all cases in Harrisonburg City, the seven day sum and the highest sum
    all_cases_in_harrisonburg_city = []
    seven_day_sum = 0
    highest = 0
    h_first_date = None
    h_second_date = None
    #Find all the cases in Harrisonburg City
    for entry in data:
            if entry[2] == "Virginia" and entry[1] == "Harrisonburg city" and entry[4] > 0:
                all_cases_in_harrisonburg_city.append(entry)
    #Find the seven-day period with the most cases in Harrisonburg City
    for i in range(len(all_cases_in_harrisonburg_city) - 6):
        seven_day_sum = sum(all_cases_in_harrisonburg_city[j][4] for j in range(i, i + 7))
        if seven_day_sum > highest:
            highest = seven_day_sum
            #Store the dates of the seven-day period with the most cases
            h_first_date = all_cases_in_harrisonburg_city[i][0]
            h_second_date = all_cases_in_harrisonburg_city[i + 6][0]
        
    return highest, h_first_date, h_second_date
highest, h_first_date, h_second_date = seven_day_period_of_most_cases_in_harrisonburg_city(data)



def  seven_day_period_of_most_cases_in_rockingham_county(data):
    #Create an empty list to store all cases in Rockingham County, the seven day sum and the highest sum
    all_cases_in_rockingham_county = []
    seven_day_sum = 0
    highest = 0
    r_first_date = None
    r_second_date = None
    #Find all the cases in Rockingham County
    for entry in data:
            if entry[2] == "Virginia" and entry[1] == "Rockingham" and entry[4] > 0:
                all_cases_in_rockingham_county.append(entry)
    #Find the seven-day period with the most cases in Rockingham County
    for i in range(len(all_cases_in_rockingham_county) - 6):
        seven_day_sum = sum(all_cases_in_rockingham_county[j][4] for j in range(i, i + 7))
        if seven_day_sum > highest:
            highest = seven_day_sum
            r_first_date = all_cases_in_rockingham_county[i][0]
            r_second_date = all_cases_in_rockingham_county[i + 6][0]
        
    return highest, r_first_date, r_second_date
highest, r_first_date, r_second_date = seven_day_period_of_most_cases_in_rockingham_county(data)


#Main execution block
if (__name__ == "__main__"):
    print("When was the first positive COVID case in Harrisonburg?", find_first_positive_case_in_harrisonburg(data)[0])
    print("When was the first positive COVID case in Rockingham County?", find_first_positive_case_in_rockingham(data)[0])
    print("On what date was the greatest number of new cases reported in Harrisonburg?", day_with_most_cases_in_harrisonburg_city(data))
    print("On what date was the greatest number of new cases reported in Rockingham County?", day_with_most_cases_in_rockingham_county(data))
    print("The seven-day period with the most cases in Harrisonburg was from {} to {}." .format(h_first_date, h_second_date))
    print("The seven-day period with the most cases in Rockingham County was from {} to {}." .format(r_first_date, r_second_date))