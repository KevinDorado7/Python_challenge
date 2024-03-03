import os
import csv

csvpath=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyPoll/Resources/election_data.csv")

total_votes = 0

with open(csvpath,"r") as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        total_votes=total_votes+1

print(f"Total votes: {total_votes}")
