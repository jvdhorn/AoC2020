#!/usr/bin/python


def parse(inp):

  fields, ticket, nearby = inp.read().split('\n\n')
  fields = {ln.split(':')[0]:Interval(ln.split(':')[1])
            for ln in fields.splitlines()}
  ticket = list(map(int, ticket.splitlines()[1].split(',')))
  nearby = [list(map(int, ln.split(','))) for ln in nearby.splitlines()[1:]]

  return fields, ticket, nearby


class Interval(object):

  def __init__(self, inp):

    *self._interval, = map(int, inp.replace('or','-').split('-'))

  def __contains__(self, other):

    a, b, c, d  = self._interval

    return a <= other <= b or c <= other <= d

  def __repr__(self):

    return str(self._interval)


def part_1(data):

  fields, ticket, nearby = data

  return sum(n for n in sum(nearby,[])
             if not any(n in field for field in fields.values()))


def prod(items):

  items = list(items)
  total = 1

  while items:
    total *= items.pop()

  return total


def part_2(data):

  fields, ticket, nearby = data

  nearby = [other for other in nearby if
            all(any(n in field for field in fields.values()) for n in other)]

  transp = list(enumerate(zip(*nearby)))
  found  = dict()

  while fields:
    for field, interval in fields.items():
      options = [all(n in interval for n in col) for i, col in transp]

      if sum(options) == 1:
        i             = options.index(True)
        found[field]  = transp[i][0]
        transp[i:i+1] = []
        fields.pop(field)
        break


  return prod(ticket[i] for field, i in found.items() if 'departure' in field)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

