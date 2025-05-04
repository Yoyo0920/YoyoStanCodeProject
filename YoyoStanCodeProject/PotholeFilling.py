"""
File: PotholeFilling.py
Name: Yoyo
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *
def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole facing east
    post_condition:Karel is in the pothole facing facing_south
    """
    move()
    turn_right()
    move()

def turn_around():
    turn_right()
    turn_right()

def go_out():
    """
    pre-condition:Karel is in the pothole facing facing_south
    post-conditon:Karel is at the upper left of the pothole facing east
    """
    turn_around()
    move()
    turn_right()
    move()


def main():
    """
    TODO:Yoyo
    """
    pass
    for i in range(3):
        go_in()
        put_99()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
