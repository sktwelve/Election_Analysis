import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize variables and lists
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    
    #read the data
    file_reader = csv.reader(election_data)

    #print headers
    headers = next(file_reader)
    print(headers)

    #run through the data to count votes
    for row in file_reader:   
        
        #count total
        total_votes += 1

        #create a list candidates
        candidate_name = row[2]
        #make sure only unique names are added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
        
        #add to candidate total
        candidate_votes[candidate_name] += 1

#percentage of total for each candidate
for candidate_name in candidate_votes:

    #retrieve vote count
    votes = candidate_votes[candidate_name]
    #calulate percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    #print result
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winner based on popular vote
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"---------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage}\n"
    f"----------------------------------\n")
print(winning_candidate_summary)



