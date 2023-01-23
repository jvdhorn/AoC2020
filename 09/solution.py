#!/usr/bin/python


def parse(inp):

  return [int(n) for n in inp]


def part_1(data):

  pre = 5 if len(data) < 25 else 25
  
  for n in range(pre, len(data)):
    relevant = set(data[n-pre:n])

    if all(data[n]-i not in relevant-{data[n]} for i in relevant):
      return data[n]


def part_2(data):

  val = part_1(data)

  for i in range(len(data)):
    for j in range(i+2, len(data)):
      rng = data[i:j]
      add = sum(rng)

      if add == val:
        return min(rng) + max(rng)
      elif add > val:
        break


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

