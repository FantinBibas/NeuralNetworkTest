#!/usr/bin/env python3

import random
import math


class Board:

    def __init__(self, size, less_random, color):
        self._size = size
        self._table = [[0 for x in range(size)] for y in range(size)]
        self._empty_case = size * size
        self._less_random = less_random
        self._color = color
        self._have_moved = 0

    def get_table(self):
        return self._table

    def add_value_to_case(self, x, y, value):
        self._table[y][x] += value
        return self

    def add_new_case(self):
        if self._empty_case == 0:
            return self
        value = 2 if self._less_random or bool(random.getrandbits(1)) else 4
        empty_case_idx = random.randint(0, self._empty_case - 1)
        next_empty_case = 0
        for y, row in enumerate(self._table):
            for x, case in enumerate(row):
                if case == 0:
                    if next_empty_case == empty_case_idx:
                        self.add_value_to_case(x, y, value)
                        self._empty_case -= 1
                        return self
                    next_empty_case += 1
        return self

    def move_to_case(self, x, y, dx, dy):
        ix = x + dx
        iy = y + dy
        while (
                self._size > ix >= 0
                and self._size > iy >= 0
                and self._table[iy][ix] == 0
        ):
            ix += dx
            iy += dy

        if not self._size > ix >= 0 or not self._size > iy >= 0:
            return

        next_case = self._table[iy][ix]
        self._table[iy][ix] = 0

        self._have_moved += 1

        if self._table[y][x] == next_case:
            self._table[y][x] *= 2
            self._empty_case += 1
        elif self._table[y][x] == 0:
            self._table[y][x] = next_case
        else:
            x += dx
            y += dy
            self._table[y][x] = next_case
            if y == iy and x == ix:
                self._have_moved -= 1

        self.move_to_case(x, y, dx, dy)

    def move(self, dx, dy):
        dy *= -1
        x = 0 if dx >= 0 else self._size - 1
        y = 0 if dy >= 0 else self._size - 1

        self._have_moved = 0

        for i in range(0, self._size):
            self.move_to_case(x, y, dx, dy)
            if dx == 0:
                x += 1
            else:
                y += 1

        if self._have_moved > 0:
            return True
        return False

    def move_top(self):
        return self.move(0, -1)

    def move_bottom(self):
        return self.move(0, 1)

    def move_right(self):
        return self.move(-1, 0)

    def move_left(self):
        return self.move(1, 0)

    def __str__(self):
        formatted = ""
        max_len = int(math.ceil(math.log10(max(map(max, self._table)))))
        max_len += 1 if max_len % 2 == 0 else 2
        row_separator = "+" + ((("-" * max_len) + "+") * self._size)
        for row in self._table:
            formatted += row_separator + "\n|"
            for case in row:
                if self._color and case != 0:
                    formatted += ("\033[93m%*d\033[39m" % (max_len, case)) + "|"
                else:
                    formatted += ("%*d" % (max_len, case)) + "|"
            formatted += "\n"
        formatted += row_separator
        return formatted
