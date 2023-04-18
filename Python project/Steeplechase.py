"""
File: Steeplechase.py
Name: Hwang sinbo
---------------------------------
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    """
    pre-condition:K is on the left, facing east
    post-condition:K is on the right
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:K is on the left, facing east
    post-condition:K is on the upper left,facing north
    """
    turn_left()
    # k is facing north, wall is on the right
    while not right_is_clear():
        move()


def cross():
    """
    pre-condition:K is on the upper left,facing north
    post-condition:K is on the upper right,facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:K is on the upper right,facing south
    post-condition:K is on the right
    """
    while front_is_clear():
        move()
    turn_left()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    # while facing_east():
    #     if front_is_clear():
    #         move()
    #     else:
    #         jump()
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
