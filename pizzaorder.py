print("Thank you for choosing Python Pizza Deliveries!")
print("What size Pizza do you want?(L/M/S):")
size = input() # What size pizza do you want? S, M, or L
#add_pepperoni = input() # Do you want pepperoni? Y or N
#extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill=0
if (size=='S'):
  bill=15
  add_pepperoni = input("Do you want pepperoni?(Y/N)")
  if(add_pepperoni=='Y'):
    bill=bill+2
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      bill=bill+1
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      bill=bill+1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
elif(size=='M'):
  bill=20
  add_pepperoni = input("Do you want pepperoni?(Y/N)")
  if(add_pepperoni=='Y'):
    bill=bill+3
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      bill=bill+1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      bill=bill+1
    else:
      print(f"Your final bill is: ${bill}.")
elif(size=='L'):
  bill=25
  add_pepperoni = input("Do you want pepperoni?(Y/N)")
  if(add_pepperoni=='Y'):
    bill=bill+3
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      bill=bill+1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    extra_cheese = str(input("Do you want extra cheese?(Y/N)"))
    if(extra_cheese=='Y'):
      
      bill=bill+1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
print("THANK YOU FOR CHOOSING ANIRO PIZZERIA! VISIT AGAIN.")
  