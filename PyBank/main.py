#import reader() for you from the csv module)
from csv import reader

#Open the file using the open() command. Save the output to a variable named opened_file.
opened_netflix_file = open('budget_data.csv')

#Read in the opened file using the reader() command. Save the output to a variable named read_file.
read_file = reader(opened_netflix_file)

#Transform the read-in file to a list of lists using the list() command. 
#Save the list of lists to a variable name.
budget_data_with_header = list(read_file)

#exclude the header row of the dataset fromour list of list to enable us do the analysis
budget_data = budget_data_with_header[1:]



#print data to verify code is working correctly
#print(budget_data[0:5])

#The total number of months included in the dataset
total_number_of_months = len(budget_data)
months = 'Total Months: ' + str(total_number_of_months)

#The net total amount of "Profit/Losses" over the entire period
#Initialize a variable named for the total with a value of zero outside the loop
net_total_amount = 0
date_list = []

#loop(iterate) through all the rows in the list of list  budget dataset. 
# Extract the amount from the dataset and store it in net_total_amount variable
#the amount is the last(second element of each row
#Add the value stored in row to the current value of the net_total_amount after converting it into an interger
for row in budget_data:
    net_total_amount = net_total_amount + int(row[-1])
    date_list.append(row[0])
    
#print(date_list[:5])

#create variable for the toatal and concantenate to string 
# while simultenously converting the net_total_amount to a string
#print the total
total = 'Total: $' + str(net_total_amount)

#The average of the changes in "Profit/Losses" over the entire period
profit_and_loss_list = []

for row in budget_data:
     profit_and_loss_list.append(int(row[-1]))
     profit_and_loss_list

#print(profit_and_loss_list[:3])

profit_or_loss_change = []
for index in range(len(profit_and_loss_list)):
    if index == 0:
        pass
    else:
        profit_or_loss_change.append(profit_and_loss_list[index] - profit_and_loss_list[index - 1])

change_sum = sum(profit_or_loss_change)
change_len = len(profit_or_loss_change)

average_change = round(change_sum / change_len, 2)


#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_or_loss_change)
max_change_date_index = profit_or_loss_change.index(greatest_increase) + 1
max_change_date = date_list[max_change_date_index]


#The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(profit_or_loss_change)
min_change_date_index = profit_or_loss_change.index(greatest_decrease) + 1
min_change_date = date_list[min_change_date_index]


#print statements
print('Financial Analysis')
print('----------------------------------')
print(months)
print(total)
print('Average Change: $' + str(average_change))
print('Greatest Increase in Profits: ' + max_change_date + ' (' + str(greatest_increase) + ')')
print('Greatest Decrease in Profits: ' + min_change_date + ' (' + str(greatest_decrease) + ')')


with open('/Users/ibrahimabdulrahmon/Documents/GitHub/python-challenge/PyBank/results.txt', "w") as text_file:
    text_file.write('Financial Analysis')
    text_file.write('\n')
    text_file.write('----------------------------------')
    text_file.write('\n')
    text_file.write(months)
    text_file.write('\n')
    text_file.write(total)
    text_file.write('\n')
    text_file.write('Average Change: $' + str(average_change))
    text_file.write('\n')
    text_file.write('Greatest Increase in Profits: ' + max_change_date + ' (' + str(greatest_increase) + ')')
    text_file.write('\n')
    text_file.write('Greatest Decrease in Profits: ' + min_change_date + ' (' + str(greatest_decrease) + ')')
    
    
