#!/usr/bin/python


def parse(inp):

  comp  = {'e':1j, 'w':-1j, 'ne':1, 'sw':-1, 'nw':1-1j, 'se':1j-1}
  lines = []

  for ln in inp:
    ln   = ln.strip()
    line = []
    while ln:
      if ln[0] in 'sn': line.append(comp[ln[:2]]); ln = ln[2:]
      else            : line.append(comp[ln[:1]]); ln = ln[1:]
    lines.append(tuple(line))

  return tuple(lines)


def part_1(data):

  tiles = list(map(sum, data))

  return sum(tiles.count(t) % 2 for t in set(tiles))


def part_2(data):

  tiles = list(map(sum, data))
  tiles = {tile for tile in tiles if tiles.count(tile) % 2}
  adj   = {1j, -1j, 1, -1, 1-1j, 1j-1}

  for _ in range(100):
    new = set()

    for tile in {tile + nb for tile in tiles for nb in adj} | tiles:
      neighbours = len({tile + nb for nb in adj} & tiles)
      if (tile not in tiles and neighbours == 2 or
          tile in tiles and 0 < neighbours < 3):
        new.add(tile)

    tiles = new

  return len(tiles)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

