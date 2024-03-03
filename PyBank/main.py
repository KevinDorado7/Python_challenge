import os
import csv

csvpath=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyBank/Resources/budget_data.csv")

total_months=0

net_total=0

past_month_value=None
month_changes=[]


with open(csvpath, "r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months=total_months+1

        plvalue=int(row[1])
        net_total=plvalue + net_total

        if past_month_value != None:
            change= plvalue - past_month_value
            month_changes.append(change)
        
        past_month_value=plvalue

if len(month_changes)>0:
    average_change= sum(month_changes) / len(month_changes)
else:
    average_change=0


print(f"Total months: {total_months}")
print(f"Total: {net_total}")
print(f"The average change is $:{average_change:.2f}")