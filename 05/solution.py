#!/usr/bin/python


def parse(inp):

  return [(ln[:7],ln[7:].strip()) for ln in inp]


def toint(s):

  return int(s.translate({66:'1', 70:'0', 76:'0', 82:'1'}), 2)


def seat(arg):

  row, col = map(toint, arg)

  return row * 8 + col


def part_1(data):

  return max(map(seat, data))


def part_2(data):

  seats = sorted(map(seat, data))

  return next(i + 1 for i, j in zip(seats, seats[1:]) if i + 2 == j)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

