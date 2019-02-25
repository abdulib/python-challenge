#import reader function from csv module
from csv import reader

#open dataset
opened_election_data = open('/Users/ibrahimabdulrahmon/Documents/GitHub/python-challenge/PyPoll/election_data.csv')

#read election data
read_election_data = reader(opened_election_data)

#convert read data to a list of list
election_data = list(read_election_data)

#test print header row
print(election_data[0])

#exclude Header row from our dataset for analysis
election_data = election_data[1:]

# test print a few row
print(election_data[:5])

#print headings and line
print('Election Results')