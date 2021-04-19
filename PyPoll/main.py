# Dependencies
import os
import csv

pypoll_csv = os.path.join('Resources', 'election_data.csv')

# establish variables
tvotes = 0
khan = 0
correy = 0
li = 0
tool = 0

# open the csv file
with open(pypoll_csv) as csv_file:
    # get file in some searchable format
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the header
    csv_header = next(csv_file)

    # csvreader is a list
    for row in csv_reader:

        # get total number of votes
        tvotes = tvotes + 1

        # get number of votes per candidate
        if row[2] == 'Khan':
            khan = khan + 1
        elif row[2] == 'Correy':
            correy = correy + 1
        elif row[2] == 'Li':
            li = li + 1
        elif row[2] == "O'Tooley":
            tool = tool + 1

# find winner by making a dictionary
cand = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan, correy, li, tool]
cvdict = dict(zip(cand, votes))
winner = max(cvdict, key=cvdict.get)

print('Election Results')
print('-----------------------')
print(f'Total Votes: {tvotes}')
print('-----------------------')
print(f'Khan: {round(((khan/tvotes) * 100), 3)}% ({khan})')
print(f'Correy: {round(((correy/tvotes) * 100), 3)}% ({correy})')
print(f'Li: {round(((li/tvotes) * 100), 3)}% ({li})')
print(f"O'Tooley: {round(((tool/tvotes) * 100), 3)}% ({tool})")
print('-----------------------')
print(f'Winner: {winner}')
print('-----------------------')

# write output to a file
import sys

# save a reference to the original standard output
original_stdout = sys.stdout 

with open('analysis.txt', 'w') as f:
    # change the standard output to the file
    sys.stdout = f 
    print('Election Results')
    print('-----------------------')
    print(f'Total Votes: {tvotes}')
    print('-----------------------')
    print(f'Khan: {round(((khan/tvotes) * 100), 3)}% ({khan})')
    print(f'Correy: {round(((correy/tvotes) * 100), 3)}% ({correy})')
    print(f'Li: {round(((li/tvotes) * 100), 3)}% ({li})')
    print(f"O'Tooley: {round(((tool/tvotes) * 100), 3)}% ({tool})")
    print('-----------------------')
    print(f'Winner: {winner}')
    print('-----------------------')
    # reset the standard output to its original value
    sys.stdout = original_stdout 