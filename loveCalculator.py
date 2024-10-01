print("The Love Calculator is calculating your score...")
name1 = str(input("What is your name?"))
name2 = str(input("What is your Partner's name?"))


name1=name1.lower()
name2=name2.lower()
count_t=name1.count("t") + name2.count("t")
count_r=name1.count("r") + name2.count("r")
count_u=name1.count("u") + name2.count("u")
count_e=name1.count("e") + name2.count("e")
total1=count_t+count_r+ count_u + count_e
count_l=name1.count("l") + name2.count("l")
count_o=name1.count("o") + name2.count("o")
count_v=name1.count("v") + name2.count("v")
count_e=name1.count("e") + name2.count("e")
total2=count_l+count_o+count_v+count_e
love_score=int(str(total1)+str(total2))
if(love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score > 40) and (love_score < 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")