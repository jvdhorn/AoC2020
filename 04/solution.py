#!/usr/bin/python


def parse(inp):

  data = []

  for item in inp.read().split('\n\n'):
    data.append(dict(entry.split(':') for entry in item.split()))

  return data


def part_1(data):

  return sum(len(set(entry) - {'cid'}) == 7 for entry in data)


def part_2(data):

  verif = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 
                      59  <= int(x[:-2]) <= 76  if x[-2:] == 'in' else False),
    'hcl': lambda x: (len(x) == 7 and x[0] == '#' and
                      set(x[1:]) <= set('0123456789abcdef')),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: len(x) == 9 and x.isnumeric(),
    'cid': lambda x: True,
  }

  valid = 0

  for entry in data:
    if (len(set(entry) - {'cid'}) == 7 and
        all(verif[key](val) for key, val in entry.items())):
      valid += 1

  return valid


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

