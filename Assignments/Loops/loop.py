##Caine Mayhew
##CS0-abgreed
##A number guessing game that prompts the user to guess a randomly generated number within a certain number of turns

import random
game = True
name = input("What is your name?")#prompting user input for player name
print("Welcome,", name, "I am thinking of a number between 1 and 20. You get 6 tries to guess the number. Take a guess:")##greeting user


while game == True:#while loop, while game is set to True, the game will run. Otherwise, it won't
    start = 6#only used for subtracting to get the number of turns passed
    turn = 6#how many tries the player has till they lose
    for guess in random.sample(range(1, 21), 1):##range of random sample numbers from 1 to 20, only 1 during each run 
        #print(guess)##just for testing purposes
    while turn > 0:##as long as they have at least 1 turn the game will run
        ask = int(input("Guess a number!!"))#more user input but numbers this time
        turn -= 1##every guess the player makes they lose a turn
        passed = start - turn##subtracting the original number of turns from how many are left to find out how many have passed
        ##print(turn)##testing purposes
        if ask == guess:###if they guess correctly/the numbers match
            print("Congraulations! You guessed correctly, and won the game!")
            print("The secrect number was...", guess, "! You took", passed, "turns to beat the game!")##revealing the number and telling the user how many tries it took them
            choice = input(print("Do you want to play again? [y/n]"))##asking user if they want to play again
            if choice == 'y' or choice == 'Y':##the responses the program will accept for an affirmative response
                print("Great, have fun!")
                game = True##setting loop back to true
                continue##continuing loop
            if choice == 'n' or choice == 'N':##the responses the program will accept for a negative response
                ("That's too bad. See you next time!!")
                game = False
                break##quitting the loop/game
        if ask != guess:##if the guess is incorrect/the numbers do not match 
            print("Sorry, that's not the number I picked.")
            if ask > guess:##if the number guessed is greater than the program's number
                print("You're a little on the high side.")#let them know to go down in their guesses
            if ask < guess:##if the number guessed is less than the programs's number
                print("You're a little on the low side.")##let them know to go up in their guesses
        if turn <=0:##If they run out of turns
            print("Sorry, you've run out of guesses. Better luck next time!")
            print("The secrect number was...", guess, "! You tried", passed, "times!")##let them know they've lost and reveal the actual number!  tell them they used up all their turns
            choice = input(print("Do you want to play again? [y/n]"))##allow them to choose to play again
            if choice == 'y' or choice == 'Y':
                game = True
                continue
            if choice == 'n' or choice == 'N':
                game = False
                break
