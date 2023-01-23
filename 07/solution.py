#!/usr/bin/python


def parse(inp):

  parents  = []
  children = []

  for ln in inp:
    bag, contents = ln.split('contain')
    this          = bag.split()[:2]
    parents.append(this)
    children.append([item.split()[:3] for item in contents.split(',')])

  bags = []

  for n, child in enumerate(children):
    contents = dict()
    for amount, *other in child:
      if amount != 'no': contents[parents.index(other)] = int(amount)
    bags.append(contents)

  return parents, bags


def part_1(data):

  names, bags = data
  target      = names.index(['shiny','gold'])

  def dig(i, cache=dict()):
    if i not in cache:
      cache[i] = {j for item in bags[i] for j in {item}|dig(item) if j==target}
    return cache[i]

  return sum(len(dig(i)) for i in range(len(bags)))


def part_2(data):

  names, bags = data
  start       = names.index(['shiny','gold'])

  def dig(i):
    return 1 + sum(dig(item) * n for item, n in bags[i].items())

  return dig(start) - 1


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

