#!/usr/bin/python


def parse(inp):

  return [list(map(set,ln.split())) for ln in inp.read().split('\n\n')]


def part_1(data):

  return sum(len(set.union(*group)) for group in data)


def part_2(data):

  return sum(len(set.intersection(*group)) for group in data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

