#!/usr/bin/python


def parse(inp):

  return tuple(map(int, inp.read().strip()))


def simulate(data, steps):

  link = dict(zip(data, data[1:] + data[:1]))
  high = max(link)
  curr = data[0]

  for _ in range(steps):
    a    = link[curr]
    b    = link[a]
    c    = link[b]
    dest = (curr - 2) % high + 1
    while dest in (a,b,c):
      dest = (dest - 2) % high + 1

    link[curr] = curr = link[c]
    link[c]    = link[dest]
    link[dest] = a

  result = [1]
  while link: result.append(link.pop(result[-1]))

  return result[1:-1]


def part_1(data):

  return ''.join(map(str, simulate(data, 100)))


def part_2(data):

  data     = data + tuple(range(max(data)+1, 1000001))
  a, b, *_ = simulate(data, 10000000)

  return a * b


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

