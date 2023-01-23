#!/usr/bin/python


def parse(inp):

  return sorted(int(ln) for ln in inp)


def part_1(data):

  diff = [j - i for i, j in zip([0]+data, data)]

  return diff.count(1) * (diff.count(3) + 1)


def steps(n):

  if n <= 3:
    return 2 ** max(0, n-1)
  else:
    return sum(steps(n-i) for i in (1,2,3))


def part_2(data):

  total = 1
  acc   = 0

  for i, j in zip([0]+data, data+[max(data)+3]):
    if j - i == 3:
      total *= steps(acc)
      acc    = 0
    else:
      acc   += 1

  return total


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

