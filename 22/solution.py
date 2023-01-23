#!/usr/bin/python


def parse(inp):

  a, b = (tuple(map(int, p.split()[2:])) for p in inp.read().split('\n\n'))

  return a, b


def simulate(data, rec):

  a, b   = data
  states = set()

  while a and b:
    if (a,b) in states: return False,
    states.add((a,b))
    i = a[0]; a = a[1:]
    j = b[0]; b = b[1:]
    winner = (j > i if not rec or len(a) < i or len(b) < j
                    else simulate((a[:i],b[:j]), rec)[0])
    if winner: b += (j,i)
    else     : a += (i,j)

  return not (a,b).index(()), sum((i+1) * x for i, x in enumerate((a+b)[::-1]))


def part_1(data):

  return simulate(data, rec = False)[1]


def part_2(data):

  return simulate(data, rec = True)[1]


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

