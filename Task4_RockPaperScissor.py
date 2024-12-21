import random 

def computer_choice():
    choices = ["rock", "paper", "scissor"] #choices are provided. Computer will choose it randomly.
    return random.choice(choices)

def winner(user,computer): 
    #Determine the winner based on the rules of the game.
    if user == computer: 
        return "tie" #if the choices of the two players are same then it is a tie.
    elif (user == 'rock' and computer == 'scissor') or (user == 'scissor' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return "user" #User wins
    else:
        return "computer" #Computer wins

def game():
    print("Welcome to the Rock-Paper-Scissor (RPS) game.")
    user_score = 0
    computer_score = 0
    while True:
        user = input("Enter rock,paper or scissor = ").lower() #take the input from the user.
        if user not in ['rock','paper','scissor']:
            print("Invalid choice!")  #it prints inavlid choice, if the user's input is inavalid.
            continue

        computer = computer_choice()
        print(f"Computer choice: {computer}") #prints the Computer choices.

        result = winner(user,computer)
        #Determines the result of the rounds
        if result == 'user':
           print("You win!") #if User defeats Computer.
           user_score +=1
        elif result == 'computer':
           print("Computer wins!") #if Computer defeates User.
           computer_score +=1
        else:
            print("It's a tie match.") #if nobody wins then it will declare a tie match.

        print(f"Score : You = {user_score} | Computer = {computer_score}") #delare the current score 

        play_again = input("Do you want to play again? (yes/no) : ").lower() #Ask the user if they want to continue.
        if play_again == 'no':  
            print("Thanks for playing!") #if User don't want to continue.
            break

game()