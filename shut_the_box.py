import calculator
from itertools import combinations
import sys
import random
#from itertools import combinations
from box import isvalid,parse_input
import time

def shut_the_box():
    """This is a game used to teach kids how to add and make it more
    fun. You start with two die, and a list from 1 to 9 inclusive. 
    Your oll the die and have to choose numbers form the list that
    add up to your roll. If it's impossible, you lose.
    """
    if len(sys.argv) != 3:
        return
    time_left = int(sys.argv[2])
    player_name = sys.argv[1]
    rolls = list(range(2,13))
    rolls_less = list(range(1,6))
    remaining = [1,2,3,4,5,6,7,8,9]
    def roll_dice():
        if sum(remaining) <= 6:
            return random.choice(rolls_less)
        return random.choice(rolls)
    roll = roll_dice()
    start = time.time()
    while isvalid(roll, remaining) == True:
        roll = roll_dice()
        count = time.time()
        time_left = time_left + (start - count)
        start = time.time()
        if time_left <= 0:
            print("Out of time")
            break
        print("Numbers left: ", remaining)
        print("Roll: ", roll)
        print("Seconds left: ", time_left)
        player_choice = input("Numbers to eliminate: ")
        print(player_choice)
        player_parsed = parse_input(player_choice, remaining)
        if(sum(player_parsed) != roll):
            print("Oops! Those numbers don't add up to your roll.")
            continue
        for x in player_parsed:
            remaining.remove(x)
        if remaining == []:
            print("Good job ", player_name," you shut the box!")
            return



    #if(isvalid(roll, remaining) == False):
    print("Game over ", player_name)
    print("You had ", remaining, " left. Your final score was", end = " ")
    print(sum(remaining))
        #need a break here

if __name__ == '__main__':
    shut_the_box()
