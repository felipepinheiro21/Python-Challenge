import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    P = []
    months = []

    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    revenue_change =[]

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    total_months = len(months)

    greatest_increase = max(revenue_change)

    greatest_decrease = min(revenue_change)


    print ("Financial Analysis")
    print("....................................................................................")
    print ("Total Months:" + str(total_months))
    print("Total:" + "$" + str(sum(P)))
    print ("Average Change:" + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(P)) + "\n")
    file.write("Average change: " + "$" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")
    file.close()
