import os
import csv

csvpath=os.path.join("/Python_challenge/PyBank/Resources/budget_data.csv")

total_months=0

net_total=0

past_month_value=None
month_changes=[]

greatest_increase= ["", 0]
greatest_decrease= ["", 0]

with open(csvpath, "r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:
        total_months=total_months+1

        plvalue=int(row[1])
        net_total=plvalue + net_total

        if past_month_value != None:
            change= plvalue - past_month_value
            month_changes.append(change)
            
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
        
            if change < greatest_decrease[1]:
                greatest_decrease[0]= row[0]
                greatest_decrease[1]= change
        past_month_value=plvalue

if len(month_changes)>0:
    average_change= sum(month_changes) / len(month_changes)
else:
    average_change=0


print(f"Total months: {total_months}")
print(f"Total: ${net_total}")
print(f"The average change is $:{average_change:.2f}")
print(f"Greatest increase in profits: ", greatest_increase[0], "($", greatest_increase[1], ")")
print(f"Greatest decrease in profits: ", greatest_decrease[0], "($", greatest_decrease[1], ")")

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average change: ${average_change:.2f}\n"
    f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

output_path=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyBank/Analysis/pybank_analysis.txt")

with open(output_path, "w") as textfile:
    textfile.write(output)
