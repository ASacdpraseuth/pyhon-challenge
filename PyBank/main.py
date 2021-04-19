# Dependencies
import os
import csv

pybank_csv = os.path.join('Resources', 'budget_data.csv')

# establish lists
months = []
profit = []
profit_change = []

# open the csv file
with open(pybank_csv) as csv_file:
    # get file in some searchable format
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the header
    csv_header = next(csv_file)

    # csvreader is a list
    for row in csv_reader:

        # getting number of months and profit in csv
        months.append(row[0])
        profit.append(int(row[1]))

    # go through monthly profit/loss to get change in profits
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])

# get biggest increase and decrease in profits
max = max(profit_change)
min = min(profit_change)
max_month = profit_change.index(max) + 1
min_month = profit_change.index(min) + 1





print('Fiancial Analysis')
print('---------------------------------')
print(f'Total Months: {len(months)}')
print(f'Total Profit: ${sum(profit)}')
print(f'Average Change: ${round(sum(profit_change)/len(profit_change), 2)}')
print(f'Greatest Increase in Profits: {months[max_month]} ${max}')
print(f'Greatest Decrease in Profits: {months[min_month]} ${min}')

# write output to a file
import sys

# save a reference to the original standard output
original_stdout = sys.stdout 

with open('analysis.txt', 'w') as f:
    # change the standard output to the file
    sys.stdout = f 
    print('Fiancial Analysis')
    print('---------------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total Profit: ${sum(profit)}')
    print(f'Average Change: ${round(sum(profit_change)/len(profit_change), 2)}')
    print(f'Greatest Increase in Profits: {months[max_month]} ${max}')
    print(f'Greatest Decrease in Profits: {months[min_month]} ${min}')
    # reset the standard output to its original value
    sys.stdout = original_stdout 