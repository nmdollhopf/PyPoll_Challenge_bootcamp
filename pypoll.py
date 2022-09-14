# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8, 2022

@author: Klaus Dollhopf
"""

import numpy as np
import os

#input data file:
resultsFilePath = os.path.join("Resources", "election_results.csv")
#output results file:
outputFilePath = os.path.join("Analysis","election_results.txt")

#read the dataset in at once and store in a numpy ndarray
resultsArray = np.genfromtxt(resultsFilePath, dtype=str, skip_header=1, delimiter=',')

"""---------Variable declarations---------"""
#dictionaries for results. key will be candidate/county name, values will be votes
candidate_votes = {}
county_votes = {}

total_votes = len(resultsArray)
#total votes is the number of entries in our array (we skipped header line)

#track the most-voted for candidate or from county
winning_votes = 0
winning_candidate = ""
most_county_votes = 0
most_county_name = ""

"""---------------------------------------"""

#print(resultsArray[0])
#print(resultsArray[len(resultsArray)-1])

#a set is unique, each will only be 3 elements long,
#so we put the unique names/counties into sets
#sets are UNORDERED. WILL AFFECT PRINTING ORDER.
candidates_set = set(resultsArray[:,2])
counties_set = set(resultsArray[:,1])
#print(candidates_set) #debugging print function

#loop through the candidate set and put the numbers into the dictionaries
for candidate in candidates_set:
    #get the counts:
    #we create a subarray where we pick out candidate
    #then count the number of elements in that subarray
    candidate_votes[candidate] = np.count_nonzero(resultsArray==candidate)
    #check if they're the largest votes; if so, make them the winner
    if candidate_votes[candidate] > winning_votes:
        winning_votes = candidate_votes[candidate]
        winning_candidate = candidate

#loop through the county set and put the numbers into the dictionaries
for county in counties_set:
    #get the counts:
    #we create a subarray where we pick out county
    #then count the number of elements in that subarray
    county_votes[county] = np.count_nonzero(resultsArray==county)
    #check if they're the largest vote blocks; if so, make them the winner
    if county_votes[county] > most_county_votes:
        most_county_votes = county_votes[county]
        most_county_name = county


#Debugging statements to ensure numbers are correct:
#print(candidate_votes)
#print(totalVotes)
#print(f"The winner is {winning_candidate} with {winning_votes:,} votes, "\
#      f"which is {(candidate_votes[winning_candidate]/total_votes):.1%} of the votes.")    

#print(f"The county with the most votes is {most_county_name} with {most_county_votes:,} votes, "\
#      f"which accounts for {most_county_votes/total_votes:.1%} of the votes.")

    
"""
---------Printing / writing---------
We do these in two separate blocks to be cognizant of the line breaks.
"""
#printing to terminal:
election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:")
print(election_results)
for county in counties_set:
    print(f"{county}: {county_votes[county]/total_votes:.1%} ({county_votes[county]:,})")
print("\n"
      "-------------------------\n"
      f"Largest county turnout: {most_county_name}\n"
      "-------------------------\n")
for candidate in candidates_set:
    print(f"{candidate}: {candidate_votes[candidate]/total_votes:.1%} ({candidate_votes[candidate]:,})")
print("-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_votes:,}\n"
      f"Winning Percentage: {winning_votes/total_votes:.1%}\n"
      "-------------------------")

#file output writing:
output_partA = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:\n")

with open(outputFilePath, "w") as outputFile:
    outputFile.write(output_partA)
    for county in counties_set:
        outputFile.write(f"{county}: {county_votes[county]/total_votes:.1%} ({county_votes[county]:,})\n")
    outputFile.write("\n"
      "-------------------------\n"
      f"Largest county turnout: {most_county_name}\n"
      "-------------------------\n\n")
    for candidate in candidates_set:
        outputFile.write(f"{candidate}: {candidate_votes[candidate]/total_votes:.1%} ({candidate_votes[candidate]:,})\n")
    outputFile.write("\n-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_votes:,}\n"
          f"Winning Percentage: {winning_votes/total_votes:.1%}\n"
          "-------------------------")



