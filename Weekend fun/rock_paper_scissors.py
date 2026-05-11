print(" ROCK,  PAPER,  SCISSORS")

first_person = input("PLAYER ONE: Enter(ROCK, PAPER, OR SCISSORS): ")
second_person = input("PLAYER TWO: Enter(ROCK, PAPER, SCISSORS): ")

first = first_person.lower()
second = second_person.lower()

if (first == "rock" and second == "scissors") or (first == "paper" and second == "rock") or (first == "scissors" and second == "paper"):
    print("Player1 wins!!") 

if (second == "rock" and first == "scissors") or (second == "paper" and first == "rock") or (second == "scissors" and first == "paper"):
    print("Player2 wins!!") 
if (first == second):
    print("Tie")
