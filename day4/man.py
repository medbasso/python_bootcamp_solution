 import random 

choose = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.: "))

game = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
 
game_final = random.choice(game)
if choose == 0:
    print(f"I choose:  \n{game[0]}")
    print(f"computer chose : \n{game_final}")
    if game_final == game[1]:
        print("you lose")
    elif game_final == game[2]:
        print("you win")
    else:
        print("It's a draw")
#2
if choose == 1:
    print(f"I choose : \n{game[1]}")
    print(f"computer chose :  \n{game_final}")
    if game_final == game[0]:
        print("you win")
    elif game_final == game[2]:
        print("you lose")
    else:
        print("It's a draw")
#3
if choose == 2:
    print(f"I choose :  \n{game[2]}")
    print(f"computer chose : \n{game_final}")
    if game_final == game[0]:
        print("you lose")
    elif game_final == game[1]:
        print("you win")
    else:
        print("It's a draw")















