# import my ReadCSV
import ReadCSV
# import numpy libraly
import numpy as np
# import csv libraly
import csv

# number of the last week of the month
week_month = [5, 9, 13, 18, 22, 26, 31, 35, 39, 44, 49, 53]
# day of month
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ConvertMonth(week):
    '''
    Convert week to month\n
    week: week want to convert\n
    return month
    '''
    # init month
    month = 1
    # foreach array number of the last week of the month
    for i in week_month:
        # if week <= the last week of the month, break
        if (week <= i):
            break
        # if month < 12 increase month variable
        if month < 12:
            # increase month variable
            month  = month + 1
    # return month variable
    return month

def ConvertWeek(month, day):
    '''
    Convert month and day to week\n
    month: month want to convert\n
    day: day want to conver\n
    return the week have day and month requested
    '''
    # init sum day of month
    sum_day = 0
    # foreach 0->month - 1 and plus days of each month
    for i in range(0, month - 1):
        # plus days of each month
        sum_day += month_day[i]
     # plus day
    sum_day += day
    # count the previous week
    week = int(sum_day / 7)
    # if the day into the new week, plus day
    if sum_day % 7 > 1:
        # plus day
        week += 1
    # return week have day and month requested
    return week


def Read(InfectiousFile, RainFile, PSIFile):
    '''
    Read and mix data of files\n
    InfectiousFile: path file and number rows patient file\n
    RainFile: path file and number row read rain file\n
    PSIFile: path file and number row read psi file\n
    return data mix
    '''
    # read data patient file
    patientFile = ReadCSV.Read(InfectiousFile).T
    # read data rain file
    rainFile = ReadCSV.Read(RainFile).T
    # read data psi file
    psiFile = ReadCSV.Read(PSIFile).T

    # init data mix
    ret = []

    # foreach data in patientFile
    for patient in patientFile:
        # data year
        year = patient[0]
        # data week
        week = patient[1]
        # convert week to month
        month = ConvertMonth(week)
        
        # init data rain
        index_rain = 0
        # init data psi
        index_psi = 0
        # foreach data rainFile and find data rain
        for rain in rainFile:
            # if find year and month update data rain and break
            if year == rain[0] and month == rain[1]:
                # update data rain
                index_rain = rain[2]
                break
        # init sum psi
        sum_psi = 0
        # init number psi read
        number_psi = 0
        # foreach data in psiFile
        for psi in psiFile:
            # if find year and week, plus averaged psi regions and increase number psi read
            if year == psi[0] and week == ConvertWeek(psi[1], psi[2]):
                # plus averaged psi regions
                sum_psi += (psi[3] + psi[4] + psi[5] + psi[6]) / 4
                # ncrease number psi read
                number_psi += 1
        # if number psi read != 0, averaged psi and update data psi
        if number_psi != 0:
            index_psi = int(sum_psi / number_psi)

        # if have data rain and psi, append data into result
        if index_rain != 0 and number_psi != 0:
            # append data into result
            ret.append([patient[0], patient[1], index_psi, index_rain, patient[2]])
    # return result data mix
    return ret

# write data mix into data file
with open('./dataset/data.csv', 'w') as data_file:
    # init write have 5 rows: 'year', 'week', 'psi', 'rain', 'patient'
    write = csv.DictWriter(data_file, fieldnames=['year', 'week', 'psi', 'rain', 'patient'])

    # read and mix data
    ret = Read(ReadCSV.WeeklyInfectiousFile, ReadCSV.RainFile, ReadCSV.PSIFile)
    # foreach data in data mix and write in row
    for data in ret:
        # write data in row
        write.writerow({'year': data[0], 'week': data[1], 'psi': data[2], 'rain': data[3], 'patient': data[4]})
