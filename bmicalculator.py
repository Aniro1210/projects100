#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

#It should tell them the interpretation of their BMI based on the BMI value.

#Under 18.5 they are underweight
#Equal to or over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese.
weight=float(input('Enter your weight(in kgs)-'))
height=float(input("Enter your height (in metres)-"))
bmi=(weight/height**2)
rounded_bmi=round(bmi,2)
print (rounded_bmi)
if(rounded_bmi<18.5):
    print("You are underweight")
elif(18.5<=rounded_bmi<25):
    print("you have normal weight")
elif(25<=rounded_bmi<30):
    print("You are slightly overweight")
elif(30<=rounded_bmi<35):
    print("You are obese.")
else:
    print("You are going to die very soon.")


