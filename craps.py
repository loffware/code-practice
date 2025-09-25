import random
import sys


def roll():
    #Roll two dice and return die1, die2, total
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    return die1, die2, die1 + die2

def buyin():
    while True:
        try:
            funds = float(input("Welcome! How much would you like to buy in for? "))
            break 
        except ValueError:
            print("You need to put in a reasonable amount of money to play. Don't include a dollar sign.")
    return funds

def come_out_wager():
    print("The come out roll is next, enter your pass line wager.")
    while True:
        try:
            wager=float(input())
            break
        except ValueError:
            print("You call that a wager? Enter in a valid input.")
    return wager

def resolve_come_out(total, wager, funds):
    #handles results of comeout roll. returns updated funds and point (or None).
    if total == 7:
        print("The dice total is", total)
        print("Lucky 7, you win", wager)
        funds +=  wager
        return funds, None
    if total == 11:
        print("The dice total is", total)
        print("Yo, eleven! You win", wager)
        funds += wager
        return funds, None
    if total in (2, 3, 12):
        print("The dice total is", total)
        print(f"Craps, you lose ${wager:.2f}")
        funds -= wager
        return funds, None
    else:
        print("The dice total is", total)
        print("The point is set at", total)
        return funds, total

def play_point_phase(point, wager, funds, interactive=False):
    #Play until point is hit or 7 out
    while True:
        if interactive == True: #prompts user for input if in interactive mode
            input("Press Enter to throw the dice.")
        d1, d2, total = roll()
        print(f"You rolled {d1} + {d2} = {total}")

        if total == 7:
            print("7 out, you lose $", wager)
            funds -= wager
            return funds
        elif total == point:
            print("You hit the point, you win!")
            funds += wager
            return funds


def interactive_mode():
    #Interactive play with user input

    funds=buyin()  #Player inputs initial buyin

    while True:
        print(f"Your current balance is ${funds:.2f}")
        wager = come_out_wager()

        if (wager > funds):
            print("You don't have that much cash! Here, this one is on the house for now.")
            funds += wager

        input("Press Enter to throw the come-out dice!")
        d1, d2, total = roll()
        funds, point = resolve_come_out(total, wager, funds)

        if point:
            funds = play_point_phase(point, wager, funds, interactive=True)

        print(f"Your balance is now ${funds:.2f}")

        play_more = input("Type 'quit' to quit, or press Enter to continue: ")
        if play_more == "quit":
            print("Thanks for playing! Goodbye.")
            break

def main():
    print("Welcome to the craps table! Select mode:")
    print("1) Interactive")
    print("2) Simulation (in progress")
    print("3) Analysis (in progress)")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        interactive_mode()
    else:
        print("Oh, I'm workin' on it already! Sheesh!")




if __name__=="__main__":
    main()
    
