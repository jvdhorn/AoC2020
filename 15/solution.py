#!/usr/bin/python


def parse(inp):

  return list(map(int, inp.read().split(',')))


def simulate(data, end):

  indices = {n: i for i, n in enumerate(data)}
  last    = data[-1]
  seen    = data.index(last) if last in data[:-1] else None

  for n in range(len(data), end):
    last          = 0 if seen is None else n - seen - 1
    seen          = indices.get(last)
    indices[last] = n

  return last


def part_1(data):

  return simulate(data, 2020)


def part_2(data):

  return simulate(data, 30000000)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

