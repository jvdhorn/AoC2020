#!/usr/bin/python


def parse(inp):

  data = []

  for ln in inp:
    ing, alg = ln.strip(')\n').replace(',','').split('(contains')
    data.append((frozenset(ing.split()), frozenset(alg.split())))

  return data


def part_1(data):

  allergens = dict()

  for ing, alg in data:
    for al in alg:
      allergens[al] = allergens.get(al, ing) & ing

  known = frozenset.union(*allergens.values())

  return sum(i not in known for ing, alg in data for i in ing)


def part_2(data):

  allergens = dict()

  for ing, alg in data:
    for al in alg:
      allergens[al] = allergens.get(al, ing) & ing

  while max(map(len, allergens.values())) > 1:
    for alg, ing in allergens.items():
      if len(ing) == 1:
        for other in set(allergens) - {alg}:
          allergens[other] = allergens[other] - ing

  return ','.join(next(iter(ing)) for alg, ing in sorted(allergens.items()))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

