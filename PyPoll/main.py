#import reader function from csv module
from csv import reader

#open dataset
opened_election_data = open('/Users/ibrahimabdulrahmon/Documents/GitHub/python-challenge/PyPoll/election_data.csv')

#read election data
read_election_data = reader(opened_election_data)

#convert read data to a list of list
election_data = list(read_election_data)

#test print header row
#print(election_data[0])

#exclude Header row from our dataset for analysis
election_data = election_data[1:]

# test print a few row
#print(election_data[:5])

#print headings and line
print('Election Results')
#print('\n')
demarcation = '------------------------------'
print(demarcation)
#print('\n')

#loop through data to sum election votes
total_votes = 0

for vote in election_data:
    voter = vote[1]
    
    total_votes += 1
    
print('Total Votes: ' + str(total_votes))
#print('\n')
print(demarcation)
#print('\n')


candidates = {}

for vote in election_data:
    candidate = vote[2]
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

#print(candidates)


khan_percent = candidates['Khan'] / total_votes * 100

correy_percent = candidates['Correy'] / total_votes * 100

li_percent = candidates['Li'] / total_votes * 100

otooley_percent = candidates["O'Tooley"] / total_votes * 100



print('Khan: ' + '%.3f' % khan_percent + '%' + ' (' + str(candidates['Khan']) + ')')
#print('\n')
print('Correy: ' + '%.3f' % correy_percent + '%'+ ' (' + str(candidates['Correy']) + ')') 
#print('\n')
print('Li: ' + '%.3f' % li_percent + '%'+ ' (' + str(candidates['Li']) + ')')
#print('\n')
print("O'Tooley: " + '%.3f' % otooley_percent + '%'+ ' (' + str(candidates["O'Tooley"]) + ')')
#print('\n')


print(demarcation)
#print('\n')
print('Winner: ' + 'Khan')
#print('\n')
print(demarcation)