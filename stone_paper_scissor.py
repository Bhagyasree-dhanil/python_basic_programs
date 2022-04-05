'''
rock papper scissor

1.user input (r,p,s) ,when input not valid create an exception
2.system random input generation (r,p,s)
3.compare user input and system input and criteria
r win when s comes
p win when r comes
s win when p comes
else loses
if same -then tie
4.chance - 5 times
5.score out of 5 


'''
import random
import re
print("Hey welcome to rock paper scissor game...Have fun.Lets start")

attempt=0
random_score=0
user_score=0
while attempt<=5:

    user_input=input("enter your weapon ([R]ock/[P]apper/[s]cissor) : ")
    if not re.match("[RrSsPp]",user_input):
       print("give a valid letter")
       continue

    options=['R','P','S']
    random_value=random.choice(options)
    
    print("your chioce {user} , oppenent choice {comp}".format(user=user_input,comp=random_value))
    
    user_value=user_input.upper()

    if user_value==random_value:
      print("you both are in Tie")

    elif user_value=="P" and random_value=="R":
      print("you won!")
      user_score=user_score+1
    
    elif user_value=="P" and random_value=="R":
      print("you won!")
      user_score=user_score+1

    elif user_value=="S" and random_value=="P":
      print("you won!")
      user_score=user_score+1
    
    else:
      print("opponent won")
      random_score=random_score+1

    attempt=attempt+1

print("Game over")   
if user_score>random_score:
  print("congrats!,what a game.You Won!.your score {user_score} : opponent score {random_score}"\
  .format (user_score=user_score,random_score=random_score))
else:
  print("its not your day! better luck next time.your score {user_score} : opponent score {random_score}"\
  .format (user_score=user_score,random_score=random_score))






