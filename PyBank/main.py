import os
import csv

# File paths
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "analysis.txt")

# Initialize variables
months = []
profits = []
changes = []

# Read CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

# Calculate changes
for i in range(1, len(profits)):
    changes.append(profits[i] - profits[i - 1])

# Analysis results
total_months = len(months)
total_profit = sum(profits)
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_inc_month = months[changes.index(greatest_increase) + 1]
greatest_dec_month = months[changes.index(greatest_decrease) + 1]

# Output text
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_decrease})"
)

# Print and write to file
print(output)
with open(output_path, "w") as f:
    f.write(output)
