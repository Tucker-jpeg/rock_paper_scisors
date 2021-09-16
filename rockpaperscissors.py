import random

rock = '''
    .._______
-----'   ____)
        (_____)
        (_____)
        (____)
-----.__(___)
'''

paper = '''
    .._______
-----'   ____)____
            ______)
            _______)
            _______)
-------.__________)
'''

scissors = '''
    .._______
-----'   ____)____
            ______)
        __________)
        (____)
----.___(___)
'''

my_pick = input("What will you play? Rock, paper, or scissors? ")

comp_picks = [rock, paper, scissors]
comp_choice = random.choice(comp_picks)

if my_pick.lower() == "rock":
    print(rock)
elif my_pick.lower() == "paper":
    print(paper)
elif my_pick.lower() == "scissors":
    print(scissors)
else:
    print("You made a typo, try again.")

win = "You win!"
lose = "You lose!"

print(f"Computer chose: \n {comp_choice}")

if my_pick.lower() == "rock" and comp_choice == paper:
    print(lose)
elif my_pick.lower() == "paper" and comp_choice == scissors:
    print(lose)
elif my_pick.lower() == "scissors" and comp_choice == rock:
    print(lose)
elif my_pick.lower() == "rock" and comp_choice == scissors:
    print(win)
elif my_pick.lower() == "paper" and comp_choice == rock:
    print(win)
elif my_pick.lower() == "scissors" and comp_choice == paper:
    print(win)
else:
    print("It's a tie! Try again.")