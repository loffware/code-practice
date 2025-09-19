import random


def roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    return (die1,die2)

def main():
    both_dice=roll()
    die1=both_dice[0]
    die2=both_dice[1]
    print("The first die is", die1,"and the second die is", die2)
    print("The total of the two dice is", (die1 + die2))




if __name__=="__main__":
    main()
    
