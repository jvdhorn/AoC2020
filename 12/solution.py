#!/usr/bin/python


def parse(inp):

  return [(ln[0], int(ln[1:])) for ln in inp]


def part_1(data):

  headings  = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
  position  = 0
  direction = 0

  for action, steps in data:
    if action in headings:
      position += headings[action] * steps
    elif action == 'R':
      direction = (direction + steps //  90) % 4
    elif action == 'L':
      direction = (direction + steps // -90) % 4
    elif action == 'F':
      position += headings['ESWN'[direction]] * steps

  return int(abs(position.real) + abs(position.imag))


def part_2(data):

  headings = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
  position = 0
  waypoint = 10 + 1j

  for action, steps in data:
    if action in headings:
      waypoint += headings[action] * steps
    elif action == 'R':
      waypoint  = 1j ** (steps // -90 % 4) * waypoint
    elif action == 'L':
      waypoint  = 1j ** (steps //  90 % 4) * waypoint
    elif action == 'F':
      position += waypoint * steps

  return int(abs(position.real) + abs(position.imag))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

