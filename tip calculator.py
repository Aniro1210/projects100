#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill=int(input("Enter the bill amount:"))
customer=int(input("No. of customers:"))
tip=(bill/customer)*1.12
rounded_tip=round(tip,2)
print("The amount to be payed by each customer is ",rounded_tip)