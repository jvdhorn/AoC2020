#!/usr/bin/python


def parse(inp):

  grid = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      if col == '#': grid.add((i,j))

  return grid


def part_1(data):

  h, w = map(max, *data)
  h   += 1
  w   += 1

  return sum((i, 3*i%w) in data for i in range(h))


def part_2(data):

  h, w  = map(max, *data)
  h    += 1
  w    += 1
  trees = 1

  for x, y in (1,1), (3,1), (5,1), (7,1), (1,2):
    trees *= sum((i, x*i//y%w) in data for i in range(0,h,y))

  return trees


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

