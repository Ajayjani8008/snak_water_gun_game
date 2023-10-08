import random

def check(player1, player2):
    if player1 == player2:
        return 0
    elif (player1 == "S" and player2 == "W") or (player1 == "W" and player2 == "G") or (player1 == "G" and player2 == "S"):
        return -1
    else:
        return 1
def main():
    print("Welcome to the Snake Water Gun Game!")
    
    while True:
        try:
            total_games = int(input("How many games would you like to play? Enter a number (1-21): "))
            if 1 <= total_games <= 21:
                break
            else:
                print("Please enter a number between 1 and 21.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    computer_score = 0
    player_score = 0
    
    for _ in range(total_games):
        computer = random.choice(["S", "W", "G"])
        
        while True:
            player = input("Choose your choice:\nS for Snake\tW for Water\tG for Gun\n").upper()
            if player in ["S", "W", "G"]:
                break
            else:
                print("Invalid Input! Please enter S, W, or G.")
        
        print("Computer's choice:", computer)  
        print("Your choice:", player)  
        score = check(computer, player)
        
        if score == 0:
            print("It's a Tie!")
        elif score == -1:
            print("Computer wins!")
            computer_score += 1
        elif score == 1:
            print("You win!")
            player_score += 1
    
    print("\nComputer Score:", computer_score)
    print("Player Score:", player_score)
    
    if player_score > computer_score:
        print("Congratulations! You are the winner.")
    elif player_score == computer_score:
        print("It's a tie overall.")
    else:
        print("Sorry, you lost the game.")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
