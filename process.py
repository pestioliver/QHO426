"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries


"""
from tui import *


# TODO: Your code here
def task_16(covid_records):
    total_records()


def task_17(covid_records):
    serial = serial_number()  # 189
    for row in covid_records:
        if serial == int(row[0]):
            print(row)


def task_18(covid_records):
    by_obs = observation_dates()
    progress(operation="+", value=0)
    for row in covid_records:
        date_str = f"{by_obs[0]}/{by_obs[1]}/{by_obs[2]}"
        if date_str == row[1]:
            print(row)


def task_19a(covid_records):
    countries = set()
    for record in covid_records:
        countries.add(record[3])
    return countries


def task_19b(covid_records, countries = None):
    for country in countries:
        print(f"\n Country/Province: {country}")
        for record in covid_records:
            if record[3] == country:
                display_records(record, cols=[0, 1, 2, 4, 5, 6, 7])


def task_20(covid_records, countries):


    task_19a(covid_records)
    for country in countries:
        confirmed = 0
        recovered = 0
        deads = 0
        for record in covid_records:
            if record[3] == country:
                confirmed += int(record[5])
                recovered += int(record[6])
                deads += int(record[7])
        print(country)
        print(f" Confirmed cases : {confirmed} \n Recovered : {recovered} \n Deads : {deads}\n ")



#There is no proper display func in tui.py








