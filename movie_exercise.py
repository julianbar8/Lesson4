import csv
with open ('imdbtitles.csv',newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

    # for row in csvreader:
    #     if row[0] == 'movie'and row[4] >= '2010':
    #         print(row[1])




    for row in csvreader:
        print(row[0],row[1],row[2],row[4],row[6])











# only the films from 2010 onwards should be selected
# 	movies should be the only title type
# 	only the primary title should be used
# 	remove the end date and isadult fields entirely
#
