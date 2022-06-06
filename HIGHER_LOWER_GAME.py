import random
from game_data import data
from art import vs,logo
import os

def ran_data():
  data
  data1=random.choice(data)
  return(data1)
  print(data1['name'])
  
def compare(con,l1,l2):
  if con =="A"and l1[1] > l2[1]:
    return 1
  elif con =="B"and l1[1] < l2[1]:
    return 1
  else:
    return 0

def play_game():
  data1=ran_data()
  data2=ran_data()
  cond=False
  l1=[]
  l2=[]
  score=0

  while cond==False:
    print(logo)
    for n in data1:
      l1.append(data1[n])
      l2.append(data2[n])
    if l1[1] == l2[1]:
      l2=[]
      data2=ran_data()
    print("Compare A:" ,l1[0],', a',l1[2],', from',l1[3],'.')
    print(vs)
    print("Against B:" ,l2[0],', a',l2[2],', from',l2[3],'.')
    con=input("Who has more followers? Type 'A' or 'B':")
    
    ans=compare(con,l1,l2)
    if ans== 1:
      l1=l2
      l2=[]
      data2=ran_data()
      score+=1
      os.cls()
      print("You're right! Current score:",score)

    else:
      cond=True
      print("\nSorry, that's wrong. Final score:",score)
      play_again=input("Do you want to play again?? Y or N: ")
      if play_again == 'Y':
        cond = False
  
play_game()