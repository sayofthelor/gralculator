# calculation/Calculate.py
import sys
def indivCalc(majorArray : list, minorArray : list, practiceArray : list, majorPercent : int, minorPercent : int, practicePercent : int):
    totalPercent = 0
    major = 0
    minor = 0
    prac = 0
    for num in majorArray: major += float(num)
    major /= len(majorArray)
    major *= (int(majorPercent) / 100)
    totalPercent += major
    for num in minorArray: minor += float(num)
    minor /= len(minorArray)
    minor *= (int(minorPercent) / 100)
    totalPercent += minor
    for num in practiceArray: prac += float(num)
    prac /= len(practiceArray)
    prac *= (int(practicePercent) / 100)
    totalPercent += prac
    return round(totalPercent, 2)
def allCalc(gradeArray : list):
    totalPercent = 0
    for num in gradeArray: totalPercent += float(num)
    totalPercent /= len(gradeArray)
    return round(totalPercent, 2)
def checkPercentThings(majorPercent : int, minorPercent : int, practicePercent : int):
    if int(majorPercent) + int(minorPercent) + int(practicePercent) != 100: sys.exit("Invalid percentage parameters!")
        
