#!/usr/bin/env python3

import sys
import argparse
import getch
from Board import Board


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-s",
        "--size",
        metavar="n",
        dest="s",
        type=int,
        default=4,
        help="size of the grid"
    )
    parser.add_argument(
        '-hc',
        '--hardcore',
        dest='hc',
        action='store_const',
        const=1,
        default=0,
        help="enable the hardcore mode: any illegal move end the game"
    )
    parser.add_argument(
        '-lr',
        '--less-random',
        dest='lr',
        action='store_const',
        const=1,
        default=0,
        help="new blocks are always 2"
    )
    parser.add_argument(
        '-c',
        '--color',
        dest='c',
        action='store_const',
        const=1,
        default=0,
        help="use colors"
    )
    return parser.parse_args()


def get_move(board):
    user_input = getch.getch()
    if user_input == 'w':
        return board.move_top()
    if user_input == 'a':
        return board.move_left()
    if user_input == 's':
        return board.move_bottom()
    if user_input == 'd':
        return board.move_right()
    return False


if __name__ == '__main__':
    options = parse_arguments()
    board = Board(options.s, options.lr, options.c)
    board.add_new_case()
    for i in range(0, 10000):
        print(board)
        if get_move(board):
            board.add_new_case()
        elif options.hc:
            print("LOSER")
            exit(0)
