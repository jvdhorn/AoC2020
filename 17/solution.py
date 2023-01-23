#!/usr/bin/python


def parse(inp):

  grid = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      if col == '#': grid.add((i,j))

  return grid


def simulate(data, dim, steps):

  grid       = {x + (0,) * (dim - len(x)) for x in data}
  neighbours = {()}

  for i in range(dim):
    neighbours = {n+(k,) for n in neighbours for k in (-1,0,1)} - {(0,) * dim}

  for _ in range(steps):
    new = set()
    chk = {tuple(map(int.__add__,a,i)) for a in neighbours for i in grid} | grid

    for i in chk:
      nb = sum(tuple(map(int.__add__,a,i)) in grid for a in neighbours)
      if   i in grid and nb in (2,3): new.add(i)
      elif i not in grid and nb == 3: new.add(i)

    grid = new
      
  return len(grid)


def part_1(data):

  return simulate(data, 3, 6)


def part_2(data):

  return simulate(data, 4, 6)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

