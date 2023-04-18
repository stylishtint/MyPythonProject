"""
File: PotholeFilling.py
Name: SINBO HWANG
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def put_99_beepers():
    for i in range(2):
        put_beeper()


def go_in():
    """
    pre-condition:karel is at the upper left of the pothole,facing east.
    post-condition:karel is in the pothole,facing south.
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:karel is in the pothole,facing south.
    post-condition:karel is at the upper left of the pothole,facing east.
    """
    turn_around()
    move()
    turn_right()
    move()


def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()
    for i in range(4):
        turn_left()
        for i in range(5):
            move()
            put_beeper()
    turn_left()
    move()
    turn_left()
    for i in range(4):
        move()
        put_beeper()
    for i in range(3):
        turn_right()
        for i in range(3):
            move()
            put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
