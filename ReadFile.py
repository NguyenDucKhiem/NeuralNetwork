import ReadCSV
import numpy as np

week_month = [5, 9, 13, 18, 22, 26, 31, 35, 39, 44, 49, 53]
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ConvertMonth(week):
    month = 1
    for i in week_month:
        if (week <= i):
            break
        if month <= 12:
            month  = month + 1
    
    return month

def ConvertWeek(month, day):
    sum_day = 0
    for i in range(1, month):
        sum_day += month_day[i]
    
    sum_day += day
    week = int(sum_day / 7)
    if sum_day % 7 > 1:
        week += 1
    return week


def Read():
    patientFile = ReadCSV.Read(ReadCSV.WeeklyInfectiousFile).T
    rainFile = ReadCSV.Read(ReadCSV.RainFile).T
    psiFile = ReadCSV.Read(ReadCSV.PSIFile).T

    ret = []

    for patient in patientFile:
        year = patient[0]
        week = patient[1]
        month = ConvertMonth(week)
        if year == 2018:
            year = 2017
        
        index_rain = 0
        index_psi = 0
        for rain in rainFile:
            if year == rain[0] and month == rain[1]:
                index_rain = rain[2]
                break
        sum_psi = 0
        number_psi = 0
        for psi in psiFile:
            if year == psi[0] and week == ConvertWeek(psi[1], psi[2]):
                sum_psi += (psi[3] + psi[4] + psi[5] + psi[6]) / 4
                number_psi += 1


        if number_psi != 0:
            index_psi = int(sum_psi / number_psi)
        else :
            index_psi = 20
        
        ret.append([patient[0], patient[1], index_psi, index_rain, patient[2]])
    
    return ret
        