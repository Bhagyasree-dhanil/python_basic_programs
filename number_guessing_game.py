'''
Number guessing name:
1. accept guessed no as input 
1. create a random no  between on one to ten
2. you have 3 attempts with score reduction  10,5,3.
3 give hints in each attempt.
4.if invalid guess notify :
5.after each step confirm that they want to continue! :

'''
print("Hello Friend! Lets have some fun.Are you ready to Guess no.Go ahead.....")


def user_input(attempt):
      user_response="y"
      guessed_no=0
      if attempt!= 1:
        user_response=str(input("you want to continue y/n : "))
        if user_response.lower()!="y" and user_response.lower()!="n":
           raise Exception("invalid entry")

      if user_response.lower()=="y":
      
        try:
          guessed_no= int(input("Enter your guess: "))
        except :
          raise Exception("sorry! invalid format ")
        if 1<guessed_no and  guessed_no>10 :
          raise ValueError(" Please add a value between one and TEN")

      
      return(guessed_no,user_response)


def scores(attempt):
  if attempt==1:
    print("you earned full score : 10 points")
  if attempt==2:
    print("you done quite good: 5 points")
  if attempt==3:
    print("you have made it at last : 3 points")

def start_game():
    
  import random
  random_no =random.randint(1,10)
  attempt=1
  user_response="y"
  while attempt<=3 and user_response.lower()=="y" :
    
    guessed_no,user_response=user_input(attempt)

    if guessed_no==0:
      break


    if (random_no==guessed_no):
      print("Great! That was a Good Guess.congrats ")
      scores(attempt)
      break

    if (random_no<guessed_no ):
      print("Sorry! Try some lesser no ")
      
    if (random_no>guessed_no ):
      print("Sorry! Try some greater no ")
      
    attempt=attempt+1
    
  else:
    print("Bad luck! you lost the game.")

start_game()
