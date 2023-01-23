#!/usr/bin/python


def parse(inp):

  time, buses = inp.read().split()

  return int(time), [x != 'x' and int(x) for x in buses.split(',')]


def part_1(data):

  time, buses = data
  wait, bus   = min((x-time%x, x) for x in buses if x)

  return wait * bus


def check(n, buses):

  return all((bus - n) % bus == offset % bus for offset, bus in buses)


def part_2(data):

  _, buses        = data
  *others, (x, a) = sorted((x, i % x) for i, x in enumerate(buses) if x)

  while others:
    y, b = others.pop()

    for n in range(y):
      if (n * x - a + b) % y == 0:
        x, a = (x * y), (x * y) - (n * x - a)
        break

  return x - a


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

