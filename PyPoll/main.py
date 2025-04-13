import os
import csv

# File paths
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

# Initialize variables
total_votes = 0
candidates = {}

# Read CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        name = row[2]
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1

# Determine results
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

winner = max(candidates, key=candidates.get)
for name in candidates:
    percent = (candidates[name] / total_votes) * 100
    output += f"{name}: {percent:.3f}% ({candidates[name]})\n"

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print and write to file
print(output)
with open(output_path, "w") as f:
    f.write(output)
