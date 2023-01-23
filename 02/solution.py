#!/usr/bin/python


def parse(inp):

  data = []

  for ln in inp:
    a, b, c, d = ln.replace(':','').replace('-',' ').split()
    data.append((int(a), int(b), c, d))

  return data


def part_1(data):

  return sum(a <= d.count(c) <= b for a, b, c, d in data)


def part_2(data):

  return sum((d[a-1], d[b-1]).count(c) == 1 for a, b, c, d in data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

