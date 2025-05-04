"""
File: Steeplechase.py
Name: Yoyo:
---------------------------------
This project shows how Katel crosses obstacles to reach the finish line.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()



def jump():
    """
    pre-condition:Karel is at the left side of the wall ,facing east
    post-condition:Karel is at the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is at the left side of the wall ,facing east
    post-condition:Karel is at the right side of the wall
    """
    turn_left()
    while not right_is_clear():
        move()


        # alternative
        # turn_left()
        # move()
        # turn_right()


def cross():
    """
    pre-condition:Karel is at the right side of the wall
    post-condition:Karel is at the upper right,facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is at the upper right,facing south
    post-condition:Karel is at the deeper right,facing south
    """

    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
