import os
import csv

csvpath=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyPoll/Resources/election_data.csv")

total_votes = 0

candidates = []
candidates_votes={}

with open(csvpath,"r") as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        total_votes=total_votes+1
        candidate_name= row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidates_votes[candidate_name]=0

        candidates_votes[candidate_name]=candidates_votes[candidate_name] + 1

        if row[2] not in candidates:
            candidates.append(row[2])

print(f"Total votes: {total_votes}")
print("Candidate vote percentage and total votes:")

for candidate in candidates:
    votes=candidates_votes[candidate]
    percentage= (votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
