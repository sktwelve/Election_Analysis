import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    
    #read the data
    file_reader = csv.reader(election_data)

    #print headers
    headers = next(file_reader)
    print(headers)

    for row in file_reader:   
        #total number of votes
        #list of candidates
        #total for each candidate
        #percentage of total for each candidate
        #winner based on popular vote