import os
import csv

csvpath=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyBank/Resources/budget_data.csv")

total_months=0

with open(csvpath, "r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months=total_months+1

print(f"Total months: {total_months}")
    
