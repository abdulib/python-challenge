#import reader() for you from the csv module)
from csv import reader

#Open the file using the open() command. Save the output to a variable named opened_file.
opened_netflix_file = open('/Users/ibrahimabdulrahmon/Documents/GitHub/python-challenge/PyBank/budget_data.csv')

#Read in the opened file using the reader() command. Save the output to a variable named read_file.
read_file = reader(opened_netflix_file)

#Transform the read-in file to a list of lists using the list() command. 
#Save the list of lists to a variable name.
budget_data_with_header = list(read_file)

#exclude the header row of the dataset fromour list of list to enable us do the analysis
budget_data = budget_data_with_header[1:]

#print head and demacation
header = 'Financial Analysis'
print(header)

demarcation = '----------------------------------'
print(demarcation)

#print data to verify code is working correctly
#print(budget_data[0:5])

#The total number of months included in the dataset
total_number_of_months = len(budget_data)
months = 'Total Months: ' + str(total_number_of_months)
print(months)

#The net total amount of "Profit/Losses" over the entire period

#Initialize a variable named for the total with a value of zero outside the loop
net_total_amount = 0


#loop(iterate) through all the rows in the list of list  budget dataset. 
# Extract the amount from the dataset and store it in net_total_amount variable
#the amount is the last(second element of each row
#Add the value stored in row to the current value of the net_total_amount after converting it into an interger
for row in budget_data:
    net_total_amount = net_total_amount + int(row[-1])
   



#create variable for the toatal and concantenate to string 
# while simultenously converting the net_total_amount to a string
#print the total
total = 'Total: $' + str(net_total_amount)
print(total)



#The average of the changes in "Profit/Losses" over the entire period

profit_and_loss_list = []

for row in budget_data:
     profit_and_loss_list.append(int(row[-1]))
     profit_and_loss_list


print(profit_and_loss_list[:3])

profit_or_loss_change = []



#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period