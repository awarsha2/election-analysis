#Add dependencies (imports)
import csv
import os


#print("Hello World")

#assign variable to load file from path
file_to_load = os.path.join('resources', 'election_results.csv')

#assign variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open election results, read file
with open(file_to_load, 'r') as election_data:

    #to do: perform analysis

    print(election_data)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    #write data to file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")


counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

if counties[1] == 'Denver':
    print(counties[1])

for county, voters in counties_dict.items():

    print(county + " county has " + str(voters) + " registered voters.")

