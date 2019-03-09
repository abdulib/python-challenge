#import reader function from csv module
from csv import reader

#open dataset
opened_election_data = open('PyPoll/election_data.csv')

#read election data
read_election_data = reader(opened_election_data)

#convert read data to a list of list
election_data = list(read_election_data)

#test print header row
#print(election_data[0])

#exclude Header row from our dataset for analysis
election_data = election_data[1:]

#loop through data to sum election votes
total_votes = 0

for vote in election_data:
    voter = vote[1]
    
    total_votes += 1
    

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


#print results
print('Election Results')
print('------------------------------')
print('Total Votes: ' + str(total_votes))
print('------------------------------')
print('Khan: ' + '%.3f' % khan_percent + '%' + ' (' + str(candidates['Khan']) + ')')
print('Correy: ' + '%.3f' % correy_percent + '%'+ ' (' + str(candidates['Correy']) + ')') 
print('Li: ' + '%.3f' % li_percent + '%'+ ' (' + str(candidates['Li']) + ')')
print("O'Tooley: " + '%.3f' % otooley_percent + '%'+ ' (' + str(candidates["O'Tooley"]) + ')')
print('------------------------------')
print('Winner: ' + 'Khan')
print('------------------------------')

#export results to txt file

with open('/Users/ibrahimabdulrahmon/Documents/GitHub/python-challenge/PyPoll/results.txt', 'w') as text_file:
    text_file.write('Election Results')
    text_file.write('\n')
    text_file.write('------------------------------')
    text_file.write('\n')
    text_file.write('Total Votes: ' + str(total_votes))
    text_file.write('\n')
    text_file.write('------------------------------')
    text_file.write('\n')
    text_file.write('Khan: ' + '%.3f' % khan_percent + '%' + ' (' + str(candidates['Khan']) + ')')
    text_file.write('\n') 
    text_file.write('Correy: ' + '%.3f' % correy_percent + '%'+ ' (' + str(candidates['Correy']) + ')') 
    text_file.write('\n')
    text_file.write('Li: ' + '%.3f' % li_percent + '%'+ ' (' + str(candidates['Li']) + ')')
    text_file.write('\n')
    text_file.write("O'Tooley: " + '%.3f' % otooley_percent + '%'+ ' (' + str(candidates["O'Tooley"]) + ')')
    text_file.write('\n')
    text_file.write('------------------------------')
    text_file.write('\n')
    text_file.write('Winner: ' + 'Khan')
    text_file.write('\n')
    text_file.write('------------------------------')