#!/usr/bin/python


def parse(inp):

  tiles = inp.read().strip().split('\n\n')
  tiles = {int(head.strip('Tile :')): tuple(body)
           for head, *body in map(str.splitlines, tiles)}

  return tiles


def get_edges(tile):

  first, *_, last = zip(*tile)

  return tuple(map(tuple, (tile[0], last, tile[-1], first)))


def get_connections(tiles):

  edges = {name: set(frozenset((edge,edge[::-1])) for edge in get_edges(tile))
                     for name, tile in tiles.items()}
  conn  = dict()

  for tile in edges:
    for other in edges:
      if len(edges[tile] & edges[other]) == 1:
        conn[tile] = conn.get(tile, set()) | {other}

  return conn


def rot(tile, n = 0):

  return tile if n == 0 else rot(tuple(zip(*tile[::-1])), (n-1)%4)


def orient(tile):

  return sum([(j, j[::-1]) for n in (0,1,2,3) for j in [rot(tile, n)]], ())


def stitch(tiles):

  tiles = {n:tuple(map(tuple, tile)) for n, tile in tiles.items()}
  conn  = get_connections(tiles)

  done  = [next(iter(tiles))]
  pos   = {(0,0): done[0]}

  for tile in done:
    todo      = {other for other in conn[tile] if other not in done}
    own_edges = get_edges(tiles[tile])
    x, y      = next(p for p in pos if pos[p] == tile)

    for other in todo:
      for perm in orient(tiles[other]):
        other_edges = get_edges(perm)
        if own_edges[0] == other_edges[2]:
          tiles[other] = perm
          pos[x-1, y]  = other
          done.append(other)
        if own_edges[2] == other_edges[0]:
          tiles[other] = perm
          pos[x+1, y]  = other
          done.append(other)
        if own_edges[1] == other_edges[3]:
          tiles[other] = perm
          pos[x, y+1]  = other
          done.append(other)
        if own_edges[3] == other_edges[1]:
          tiles[other] = perm
          pos[x, y-1]  = other
          done.append(other)

  tiles = {n: tuple(row[1:-1] for row in tile[1:-1])
                              for n, tile in tiles.items()}
  x, y = zip(*pos)
  cols = []

  for j in range(min(y), max(y)+1):
    cols.append([tile for i in range(min(x), max(x)+1)
                 for tile in tiles[pos[i,j]]])

  return [sum(row, ()) for row in zip(*cols)]


def get_monster():

  monster = ['                  # ',
             '#    ##    ##    ###',
             ' #  #  #  #  #  #   ']

  return to_grid(monster)


def to_grid(arr):

  grid = set()

  for i, row in enumerate(arr):
    for j, col in enumerate(row):
      if col == '#': grid.add(complex(i,j))

  return grid


def part_1(data):

  conn   = get_connections(data)
  result = 1

  for tile in conn:
    if len(conn[tile]) == 2: result *= tile

  return result


def part_2(data):

  complete = stitch(data)
  size     = max(len(complete), len(complete[0]))
  monster  = get_monster()
  monsters = [{complex(i,j) + x for x in monster}
              for i in range(size) for j in range(size)]
  count    = 0

  for perm in orient(complete):
    if count: break
    grid  = to_grid(perm)
    count = sum(monster <= grid for monster in monsters) * len(monster)

  return len(grid) - count


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

