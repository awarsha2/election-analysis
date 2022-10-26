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

#initialize total vote counter
total_votes = 0

#initialize list of candidates
candidate_options = []

#declare empty dictionary for vote tallies
candidate_votes = {}

#winning candidate, winning count, and winning % trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results, read file
with open(file_to_load, 'r') as election_data:

    #read and analyze data
    file_reader = csv.reader(election_data)

    #read and print header row
    headers = next(file_reader)

    #iterate over each row in the csv file
    for row in file_reader:
        
        #add to total vote count
        total_votes += 1

        #get candidate name from each row
        candidate_name = row[2]

        #check if the candidate is on the list
        if candidate_name not in candidate_options:

            #add candidate to list (if not on list)
            candidate_options.append(candidate_name)

            #begin tracking new candidate's vote count
            candidate_votes[candidate_name] = 0

        #add vote to candidate's count
        candidate_votes[candidate_name] += 1


#debug prints:
#print total votes
#print(total_votes)

#print candidate options
#print(candidate_options)

#print candidate vote tallies
#print(candidate_votes)

#loop through candidate list and dict
for candidate_name in candidate_votes:

    #get vote count of candidate
    votes = candidate_votes[candidate_name]

    #canculate % of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print candidate's name, vote count and % of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning candidate by checking vote counts
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #if true then set winning count/% to candidate's votes/%
        winning_count = votes
        winning_percentage = vote_percentage

        #set winning candidate var to candidate's name
        winning_candidate = candidate_name

#print winner and their vote info!
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
