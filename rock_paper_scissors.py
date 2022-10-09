# 2 player game ... computer vs User
# player inputs choices of rock,paper & scissors or quits the game to finish the program..
# computer randomly choices either of the 3
# we announce results when user quits
#
#

import random

computer_score = 0
user_score = 0
limit=0
choices = ["rock", "paper", "scissors"]
# print(user_choice)
# print(computer_choice)

while True:
    if limit < 3:
        print(f'{3-limit} choises remaining')
        user_choice = input("Choose ROCK/PAPER/SCISSORS or Q to quit the game: ").lower()
        computer_choice = random.randint(0, 2)
        print(choices[computer_choice])
        limit+=1
        if user_choice =="q":
            break

        elif user_choice not in choices:
            continue
        elif user_choice == choices[computer_choice]:
            continue

        elif user_choice =='rock' and  choices[computer_choice]=='scissors':
            user_score+=1
            continue
        elif user_choice =='paper' and  choices[computer_choice]=='rock':
            user_score+=1
            continue
        elif user_choice =='scissors' and  choices[computer_choice]=='paper':
            user_score+=1
            continue
        else:
            computer_score+=1
            continue
    else:
        break
print(f"user score {user_score}")
print(f"computer score {computer_score}")

