import random

def game():
    user = input("Rock, Paper, or Scissor?: ").lower()
    computer = random.choice(["rock", "paper", "scissor"])
    print("The computer chose: " + (computer))
    if user == computer: 
        return("Tie Game!")
    if some_condition(user, computer):
        return("You Won!")
    return("You Lost!")

def some_condition(Player1, Player2):
    if (Player1 == "rock" and Player2 == "scissor") \
        or (Player1 == "paper" and Player2 == "rock") \
            or (Player1 == "scissor" and Player2 == "paper"):
        return True
    return False

print(game())

 