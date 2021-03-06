#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('* Welcome to the tip calculator! *')

bill = float(input('What was the total bill? $'))

give = int(input('How much tip would you like to give 10, 12, or 15? '))

people = int(input('How many people to split the bill? '))

#obtain porcent 
porcent = (give / 100)

operation_1 = float(bill) * float(porcent)

#value includes the tip and divided between the relevant people
operation_2 = (bill + operation_1) / people

#so that it shows us two decimals instead of one
aplication = round(operation_2, 2)
aplication = "{:.2f}".format(operation_2)

print(f'Each person pay: $ {aplication}')

#print(operation_2)
