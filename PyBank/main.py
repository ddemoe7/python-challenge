#Import modules
import os
import csv

#Path to csv
#In the resources folder - renamed file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Variables
totalMonths = 0
netAmount = 0
monthlyChange = []
monthlyCount = []
greatestIncrease = 0
greatestMonthlyIncrease = 0
greatestDecrease = 0
greatestMonthlyDecrease = 0

#Read CSV & clean file
with open(budget_csv) as csvfile:

    #CSV specifies delimiter
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Remove header
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate total months, net amount of profits/losses & set variables
    previousRow = int(row[1])
    totalMonths += 1
    netAmount += int(row[1])
    greatestIncrease = int(row[1])
    greatestMonthlyIncrease = row[0]

    #Read each row of data
    for row in csvreader:

        #Calculate total number of months
        totalMonths += 1

        #Calculate net amount of profits/losses over range
        netAmount += int(row[1])

        #Calculate change from current month to previous
        revenueChange = int(row[1]) - previousRow
        monthlyChange.append(revenueChange)
        previousRow = int(row[1])
        monthlyCount.append(row[0])

        #Calculate the greatest increase
        if int(row[1]) > greatestIncrease:
            greatestIncrease = int(row[1])
            greatestMonthlyIncrease = row[0]
        
        #Calculate the greatest decrease
        if int(row[1]) < greatestDecrease:
            greatestDecrease = int(row[1])
            greatestMonthlyDecrease = row[0]

    #Calculate the average and date
    averageChange = sum(monthlyChange)/ len(monthlyChange)

    highestChange = max(monthlyChange)
    lowestChange = min(monthlyChange)

#Final analysis
print(f"Financial Analysis")
print(f"--------------------")
print(f"Total months: {totalMonths}")
print(f"Total: ${netAmount}")
print(f"Average change: ${averageChange:.2f}")
print(f"Greatest increase in profits: {greatestMonthlyIncrease}: (${highestChange})")
print(f"Greatest decrease in profits: {greatestMonthlyDecrease}: (${lowestChange})")

#Text output
output_path = "Financial Analysis.txt"
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow([f"--------------------"])
    csvwriter.writerow([f'Total months: {totalMonths}'])
    csvwriter.writerow([f'Total: ${netAmount}'])
    csvwriter.writerow([f'Average change: ${averageChange:.2f}'])
    csvwriter.writerow([f'Greatest increase in profits: {greatestMonthlyIncrease}: (${highestChange})'])
    csvwriter.writerow([f'Greatest decrease in profits: {greatestMonthlyDecrease}: (${lowestChange})'])