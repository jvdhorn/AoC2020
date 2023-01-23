#!/usr/bin/python


def parse(inp):

  return tuple(map(int, inp.read().split()))


def transform(n, sub):

  return n * sub % 20201227


def get_loop_size(n):

  count = 0
  i     = 1

  while i != n:
    i = transform(i, 7)
    count += 1

  return count


def part_1(data):

  a, b = data
  i    = 1

  for _ in range(get_loop_size(a)):
    i = transform(i, b)

  return i


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

