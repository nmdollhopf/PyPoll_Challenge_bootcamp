# Election Result Tallying with Python

## Background

The Election Commission of Colorado has asked for help on tallying the results of a recent congressional election to ensure the results are consistent between tallying methods. The Commission has provided a data file with ballot information, comprised of the ballot ID, county the ballot was submitted in, and the name of the candidate the ballot was submitted in favor of. Local campaign staffers, Seth and Tom, have suggested used python to read the data and count the results. In addition to checking the number of votes submitted for the candidates, the Commission would also like to know the number of ballots submitted from each county.

## Methods

The `numpy` module for python is an extensible tool for data analysis and was used for the tallying. The data file was read into a `numpy` array using a standard, general method, `numpy.genfromtxt()`, for ease of handling. Python sets were used to get a unique list of the county and candidate names (i.e. a set cannot contain duplicates) for the purposes of defining dictionaries to hold the number of votes for each and loop control. `Numpy`'s `count_nonzero()` method was used on the data array under a conditional test of matching the county or candidate name to get the number of votes cast from that county or for that candidate, respectively. Simple conditional tests were utilized to keep track of the county and candidate with the most votes. Finally, the number of total votes was calculated as the number of elements in the data array, but could be done with a summation of the candidate or county vote counters. Results are printed to the terminal and written to `election_results.csv`, found in the Analysis folder.


## Results

Below is a summary of results from the election.  
* A total 369,711 votes were cast in the election.
* Denver county had the greastet number of ballots cast, 306,055.
    * The number of votes from each county was:
```
           Arapahoe:   24,801   (6.7%)
           Denver:    306,055  (82.8%)
           Jefferson:  38,855  (10.5%)
```  
* With a super majority 73.8% of votes (272,892), **Diana DeGette** wins the election.
    * The number of votes for each candidate was:
```
           Charles Casper Stockham:   85,213  (23.0%)
           Diana DeGette:            272,892  (73.8%)
           Raymon Anthony Doane:      11,606   (3.1%)
```

## Summary

The preceding presents a fast, accurate method to tally the results of the congressional election. The code is extensible as well and can be used for any other election data with minor changes. The first change that should be made is to check that no lines of voting data were duplicated. The method presented above makes that easy by checking the length of a set of the Ballot IDs; because a set is unique, a length matching the number of rows means each Ballot ID is non-duplicated. This can be accomplished in the presented code with `len(set(resultsArray[:,0]))`. Utilizing this line, we see that there are 369,711 unique Ballot IDs, meaning the given dataset was clean and there were no duplicates.

The second change relates to the type of election and what the polling locales are. For instance, if the data includes the state instead of the county for a national election, the code works the same, but the variable names can be changed for clarity. If the data instead contains both the county *and* state, minor tweaks can be made to capture and compare these information. The locale information could be stored and compared as either a single string or a list of strings, though the latter requires further code tweaks for how to locally store the data.  
If the ballot data does include more than one string for the locale, care should be taken to change how the candidate names are read in to ensure it is grabbing the last column of the data file. One option is to change the index from `2` to `-1` as a general case to always grab the last column; that is, change `candidates_set = set(resultsArray[:,2])` to `candidates_set = set(resultsArray[:,-1])` at line 41. Otherwise, the index will have to be set manually for each use case of election data.
 
