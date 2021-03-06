# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []

#Declare a dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #2 Begin tracking candidates vote count
            candidate_votes[candidate_name] = 0
            
        # add a vote to candidates count
        candidate_votes[candidate_name] += 1
#save results to text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping
    #1 Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4 Print the candidate name and percent of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes: ,})\n")
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
        print(candidate_results)
        txt_file.write(candidate_results)
    

    winning_candidate_summary = (
        f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"----------------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    
       
 
    



    #1. The total number of votes cast..
    #2. A complete list of candidates who received votes
    #3. The percentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote.