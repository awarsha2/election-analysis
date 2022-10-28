# Election-Analysis

## Project Overview:
Colorado Board of Elections has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources:
- Data Cource: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, version 1.72.2

## Results:
All results are shown in the following text file, which can be found in the resources folder in the challenge folder.
[election_analysis](challenge/analysis/election_analysis.txt)

- How many votes were cast in this congressional election?
- 369,711 votes were cast total in this election.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- 38,855 votes were cast in Jefferson County (10.5%).
- 306,055 votes were cast in Denver County (82.8%).
- 24,901 votes were cast in Arapahoe County (6.7%).

- Which county had the largest number of votes?
- Denver had the largest number of votes/voter turnout. 

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham recieved:
    - 85,213 votes,
    - 23.0% of the popular vote.
- Diana DeGette recieved:
    - 272,892 votes,
    - 73.8% of the popular vote.
- Raymon Anthony Doana recieved:
    - 11,606 votes,
    - 3.1% of the popular vote.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Diana DeGette won the election. She recieved 272,892 votes, which equates to a decisive 73.8% of the popular vote. 

## Summary:
- In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
The core of the script, which counts votes, can be used in any election of any size. The other parts, such as the parts that count and evaluate county turnout, or calculates popular vote percentage, can be edited and adjusted for whatever kind of election. For example, to upscale this to a national level, we might add functionality to count the number of votes each candidate recieved in each state in addition to or instead of tracking the counties, and we might change the popular vote percentage calculation to track electoral college vote percentage. This could be downscaled to local level elections by removing the county counting or by changing it to track districts in a city. 

