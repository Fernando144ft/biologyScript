# BIOLOGY SCRIPT
import sys

print("BIOLOGY CALCULATOR")
print("PLEASE WRITE THE INPUT EXACTLY AS IT SAYS")
# For the field of view if it is in millimeters:
fieldOfView = (input("Is the field of view in millimeters: (yes/no): "))
if fieldOfView == "yes":
    millimeters = float(input("Enter the Number of Millimeters: "))
    microns = float(millimeters * 1000)

    # Magnification Of 5mm FOV
    print("Magnifications in millimeters:")

    tenX = float(millimeters * 0.4)
    print("For 10x the magnification is: ")
    print(tenX)

    fortyX = float(tenX * 0.25)
    print("For 40x the magnification is: ")
    print(fortyX)

    oneHundredX = float(fortyX * 0.4)
    print("For 100x the magnification is: ")
    print(oneHundredX)

else:
    microns = float(input("FOV in Microns: "))

    # Magnification Of 5mm FOV
    print("Magnifications in millimeters:")

    tenXM = float(microns * 0.4)
    print("For 10x the magnification is: ")
    print(tenXM)

    fortyXM = float(tenXM * 0.25)
    print("For 40x the magnification is: ")
    print(fortyXM)

    oneHundredXM = float(fortyXM * 0.4)
    print("For 100x the magnification is: ")
    print(oneHundredXM)
# Measuring Cells
question = input(str("Do you want to measure the size of a cell: yes/no: "))
if question == "yes":
    microns = float(input("Enter the number of Microns: "))
    cells = int(input("Enter the number of cells: "))
    sizeOfCells = float(microns / cells)
    print("This is the size of the cell in MICRONS")
    print(float(sizeOfCells))

    question2 = (str(input("Do you want to measure the cells nucleus? yes/no: ")))

    if question2 == "yes":
        nucleusNum = int(input("Enter the number of nucleus in the cell: "))
        nucleusSize = float(sizeOfCells / nucleusNum)
        print("This is the size of the nucleus in MICRONS: ")
        print(nucleusSize)

    else:
        print("Script Closed")
        sys.exit(0)
