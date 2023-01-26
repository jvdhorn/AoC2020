#!/usr/bin/python


def parse(inp):

  rules, lines = inp.read().split('\n\n')
  new_rules    = dict()

  for rule in rules.splitlines():
    n, x = rule.split(':')
    if '"' in x:
      x = x.strip('" ')
    else:
      x = tuple(tuple(map(int, part.split())) for part in x.split('|'))
    new_rules[int(n)] = x

  return new_rules, lines.split()


def partition(line, n, cache=dict()):

  result = cache.get((line,n))

  if result is None:

    result = ((line,),)

    for _ in range(n-1):
      result = tuple(res[:-1] + (res[-1][:j], res[-1][j:])
                     for res in result for j in range(1, len(res[-1])))

    cache[line,n] = result

  return result


def get_validator(rules):

  def validate(line, n=0, cache=dict()):

    valid = cache.get((line,n))

    if valid is None:

      rule = rules[n]

      if isinstance(rule, str):
        valid = (line == rule)

      else:
        valid = False
        for subrule in rule:
          for parts in partition(line, len(subrule)):
            valid = all(map(validate, parts, subrule))
            if valid: break
          if valid: break

      cache[line,n] = valid

    return valid

  return validate


def part_1(data):

  rules, lines = data
  validate     = get_validator(rules)

  return sum(map(validate, lines))


def part_2(data):

  rules, lines = data
  rules        = rules.copy()
  rules[8]     = ((42,), (42, 8))
  rules[11]    = ((42, 31), (42, 11, 31))
  validate     = get_validator(rules)

  return sum(map(validate, lines))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

