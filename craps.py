import random
import sys


def roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    return (die1,die2)

def buyin():
    while True:
        try:
            player_funds = float(input("Welcome! How much would you like to buy in for? "))
            break 
        except ValueError:
            print("You need to put in a reasonable amount of money to play. Don't include a dollar sign.")
    return player_funds

def come_out_wager():
    print("The come out roll is next, enter your pass line wager.")
    while True:
        try:
            wager=float(input())
            break
        except ValueError:
            print("You call that a wager? Enter in a valid input.")
    return wager


def main():


    player_funds=buyin()  #Player inputs initial buyin and initializes this 

    while True:
        wager = come_out_wager()

        if wager > player_funds:
            print("You don't have that much cash! Here, this one is on the house for now.")
            player_funds = player_funds + wager

        player_funds = player_funds - wager

        point_set = False

        while point_set == False:
            throw_dice = input("Type 't' to throw the dice! ")
            if throw_dice == "t":
                both_dice=roll()
                die1=both_dice[0]
                die2=both_dice[1]
                roll_total=die1+die2
                print("The first die is", die1,"and the second die is", die2)
                print("The total of the two dice is", (die1 + die2))
                match roll_total:
                    case 7:
                        print("Lucky 7, you win ", wager)
                        player_funds = player_funds + wager + wager
                    case 11:
                        print("Yo, eleven! You win ", wager)
                        player_funds = player_funds + wager + wager
                    case 2 | 3 | 12:
                        print("Craps, you lose ", wager)
                    case _:
                        print("The point is set at ", roll_total)
                        point_set = True
                        point = roll_total 
        while point_set == True:
            throw_dice = input("Type 't' to throw the dice! ")
            try:
                if throw_dice == "t":
                    both_dice=roll()
                    die1=both_dice[0]
                    die2=both_dice[1]
                    roll_total=die1+die2
                    print("The first die is", die1,"and the second die is", die2)
                    print("The total of the two dice is", (die1 + die2))
            except Exception as e:
                print("You have to throw the dice, you're locked in!")

            if roll_total == 7:
                print("7 out, you lose!")
                point_set = False
                break
            if roll_total == point:
                print("You hit the point, you win!")
                player_funds = player_funds + wager + wager
                point_set = False
                break
                
        print("Your balance is now $", player_funds)
            
        play_more = input("Type 'quit' to quit, or hit enter to continue. ")
        if play_more == "quit":
            break


if __name__=="__main__":
    main()
    
