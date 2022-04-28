# gralculator.py
from sys import exit
from time import sleep as wait
from extras.func import clear, isAFloat, isAnInt
from calculation.Calculate import indivCalc, allCalc, checkPercentThings
true = True; false = False # i'm too used to like every other programming language lol
gradeLoop = true
majorArray = []
minorArray = []
practiceArray = []
gradeArray = []
print("Welcome to the grade calculator!")
while True:
    clear()
    promptInput = input("What would you like to calculate grades for? (indivdual/all): ").lower()
    if "individual" in promptInput:
        clear()
        while true:
            majorPercent = input("Input your major weight percentage: ")
            if isAnInt(majorPercent) == false: print("Invalid number!")
            else: break
        while true:
            minorPercent = input("Input your minor weight percentage: ")
            if isAnInt(minorPercent) == false: print("Invalid number!")
            else: break
        while true:
            practicePercent = input("Input your practice/homework weight percentage: ")
            if isAnInt(practicePercent) == false: print("Invalid number!")
            else: break
        checkPercentThings(majorPercent, minorPercent, practicePercent)
        clear()
        while true:
            majorA = input("Enter a major grade or type 'next' to move on: ")
            if isAFloat(majorA): majorArray.append(majorA)
            elif "next" in majorA and len(majorArray) == 0: print("At least one is required.")
            elif "next" in majorA: break
            else: print("Invalid number!")
        clear()
        while true:
            minorA = input("Enter a minor grade or type 'next' to move on: ")
            if isAFloat(minorA): minorArray.append(minorA)
            elif "next" in minorA and len(minorArray) == 0: print("At least one is required.")
            elif "next" in minorA: break
            else: print("Invalid number!")
        clear()
        while true:
            pracA = input("Enter a practice grade or type 'end' to calculate all grades: ")
            if isAFloat(pracA): practiceArray.append(pracA)
            elif "end" in pracA and len(practiceArray) == 0: print("At least one is required.")
            elif "end" in pracA: break
            else: print("Invalid number!")
        clear()
        print("Calculating..."); wait(1)
        clear()
        finalGrade = indivCalc(majorArray, minorArray, practiceArray, majorPercent, minorPercent, practicePercent)
        clear()
        print("Your grade is: " + str(finalGrade)); break
    elif "all" in promptInput:
        clear()
        print("This is intended for averaging final grades, which you can generate with the 'individual' option.")
        print("If you need them first, press CTRL + C, then open the program again and select 'individual'.")
        while true:
            gradeA = input("Enter a final grade or type 'end' to calculate grades: ")
            if isAFloat(gradeA): gradeArray.append(gradeA)
            elif "end" in gradeA and len(gradeArray) == 0: print("At least one is required.")
            elif "end" in gradeA: break
            else: print("Invalid number!")
        clear()
        print("Calculating..."); wait(1)
        finalGrade = allCalc(gradeArray)
        clear()
        print("Your grade is: " + str(finalGrade)); break
    else: print("Invalid option!"); wait(1)
