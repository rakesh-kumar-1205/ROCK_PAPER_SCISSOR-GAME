import random 
print("what did you choose? type 0 for Rock 1 for Paper 2 fro Scissors.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=eval(input("what did you choose? type 0 for Rock 1 for Paper 2 fro Scissors:"))
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number ,you lose!") 
else:
    print(game_images[user_choice])
    
    computers_choice=random.randint(0,2)
    print("computers_choice:")
    print(game_images[computers_choice])
    if user_choice==0 or computers_choice==2 :
        print("you win!")
    elif computers_choice==0 or user_choice==2:
        print("you lose!")
    elif computers_choice > user_choice:
        print("you lose!")
    elif user_choice > computers_choice:
        print("you win!")
    elif computers_choice==user_choice :
        print("its a draw")

