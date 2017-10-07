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
    parser.add_argument(
        '-sc',
        '--score',
        dest='sc',
        action='store_const',
        const=1,
        default=0,
        help="show current score"
    )
    parser.add_argument(
        '-cs',
        '--clear-screen',
        dest='cs',
        action='store_const',
        const=1,
        default=0,
        help="clear screen between each move"
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
    if user_input == 'q':
        board.quit()
    return False


def play_game(board, hardcore_mode):
    legal_move = True
    while board.can_play() and (legal_move or not hardcore_mode):
        print(board)
        legal_move = get_move(board)
        if legal_move:
            board.add_new_case()
    print(board)
    return board.get_score()


def start_game(options):
    board = Board(options.s, options.lr, options.c, options.sc, options.cs)
    board.add_new_case()
    score = play_game(board, options.hc)
    print("FINAL SCORE: " + str(score))


if __name__ == '__main__':
    start_game(parse_arguments())
