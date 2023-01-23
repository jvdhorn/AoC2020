#!/usr/bin/python


def parse(inp):

  grid = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      if col == 'L': grid.add(complex(i,j))

  return grid


def simulate(grid, neighbours, tol):

  grid = dict.fromkeys(grid, 0)

  while True:
    new_grid = grid.copy()

    for i in grid:
      occ = sum(map(grid.get, neighbours[i]))
      if   occ >= tol: new_grid[i] = 0
      elif occ == 0  : new_grid[i] = 1

    if grid == new_grid:
      break
    else:
      grid = new_grid

  return sum(grid.values())


def get_neighbours(grid, lim=None):

  directions = {-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j}
  reals      = [int(x.real) for x in grid]
  imags      = [int(x.imag) for x in grid]
  rmin       = min(reals)
  rmax       = max(reals) + 1
  imin       = min(imags)
  imax       = max(imags) + 1
  lim        = lim or max(rmax - rmin, imax - imin)
  neighbours = {x:set() for x in grid}

  for x in grid:
    for d in directions:
      for n in range(1, lim + 1):
        point = x + d * n

        if point in grid:
          neighbours[x].add(point)
          break

        elif not (rmin <= point.real <= rmax
              and imin <= point.imag <= imax):
          break

  return neighbours


def part_1(data):

  return simulate(data, get_neighbours(data, 1), 4)


def part_2(data):

  return simulate(data, get_neighbours(data), 5)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

