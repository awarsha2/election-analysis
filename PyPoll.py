#Final reqs/data needed:
## Total # of votes cast
## List of candidates (who recieved votes)
## Total # of votes each candidate recieved
## % of votes each candidate won
## Winner of the election based on pop vote

#Add dependencies (imports)
import csv
import os

#assign variable to load file from path
file_to_load = os.path.join('resources', 'election_results.csv')

#assign variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open election results, read file
with open(file_to_load, 'r') as election_data:

    #read and analyze data
    file_reader = csv.reader(election_data)

    #read and print header row
    headers = next(file_reader)

    print(headers)

    #print each row in csv file (dangerous)
    #for row in file_reader:
        #print(row)


