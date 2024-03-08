import os
import csv

#csvpath=os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyPoll/Resources/election_data.csv")
csvpath=os.path.join("PyPoll","Resources","election_data.csv")

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

winner = ""
max_votes= 0

# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {total_votes}")
# print("-------------------------")

output_text = "Election Results\n"
output_text += "-------------------------\n"
output_text += f"Total Votes: {total_votes}\n"
output_text += "-------------------------\n"

for candidate in candidates:
    votes=candidates_votes[candidate]
    percentage= (votes/total_votes)*100
    #print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    output_text+=(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    if votes>max_votes:
        max_votes=votes
        winner = candidate

output_text += "-------------------------\n"
output_text += f"Winner: {winner}\n"
output_text += "-------------------------\n"

# print("-------------------------")
# print(f"Winner: {winner}")
# print("-------------------------")

print(output_text)

output_path= os.path.join("/Users/kevindorado/Desktop/Python_challenge/PyPoll/Analysis/PyPoll_analysis.txt")
with open(output_path,"w") as textfile:
    textfile.write(output_text)


