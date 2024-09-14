import time
from random import sample as smp

# Balance
balance = 50
bet = int(input("Bet $: "))
balance -= bet

# Guess teams
guess_team_a = input("A: ").strip().capitalize()
guess_team_b = input("B: ").strip().capitalize()

# Gamble starts
football_teams = ["Man City", "Real Madrid", "Barcelona", "Man Utd"]
teams = smp(football_teams, 2)
team_A, team_B = teams
print(f"{team_A} - ...")
time.sleep(3)
print(f"{team_A} - {team_B}")

# Decision making
guess_1 = guess_team_a in teams
guess_2 = guess_team_b in teams
has_guessed = guess_1 and guess_2

if has_guessed:
    bet *= 2
    balance += bet
    print(balance)
else:
    print(balance)


team_power = {
    "Real Madrid": 70,
    "Barcelona": 65,
    "Man City": 65,
    "Leicster": 60
}