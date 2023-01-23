#!/usr/bin/python


def parse(inp):

  return {int(i) for i in inp}


def part_1(data):

  return next(i*(2020-i) for i in data if 2020-i in data)


def part_2(data):

  return next(i*j*(2020-i-j) for i in data for j in data if 2020-i-j in data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

