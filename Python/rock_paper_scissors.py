# Make a two-player Rock-Paper-Scissors game. 
# Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

def game():      
    while True:
        player1 = input("Player 1: Rock, Paper, or Scissors?: ").capitalize()
        player2 = input("Player 2: Rock, Paper, or Scissors?: ").capitalize()
        
        if player1 not in ['Rock', 'Paper', 'Scissors'] or player2 not in ['Rock', 'Paper', 'Scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
        break
    
    compare(player1, player2)

def compare(p1, p2):
    if p1 == p2:
        print("Tie!")
    elif (p1 == 'Rock' and p2 == 'Scissors') or \
         (p1 == 'Scissors' and p2 == 'Paper') or \
         (p1 == 'Paper' and p2 == 'Rock'):
             print("Player 1 wins! Congratulations")
    else:
        print("Player 2 wins! Congratulations")

def main():
    game()
    
    while True:
        new_game = input("Do you want to start a new game? (Y/N): ").upper()
        if new_game not in ['Y', 'N']:
            print("Please enter Y or N.")
        elif new_game == 'Y':
            game()
        else:
            break

main()
