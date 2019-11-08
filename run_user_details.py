import csv

with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    for row in csvreader:
        print(row[-1])


