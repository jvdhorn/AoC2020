#!/usr/bin/python


def parse(inp):

  return [(ln[:3],int(ln[3:])) for ln in inp]


def simulate(data):

  acc = nxt = 0
  vis = set()

  while nxt not in vis:
    if nxt == len(data): break
    vis.add(nxt)
    ins, val = data[nxt]
    if   ins == 'acc': nxt += 1; acc += val
    elif ins == 'jmp': nxt += val
    elif ins == 'nop': nxt += 1

  return acc, nxt in vis


def part_1(data):

  return simulate(data)[0]


def part_2(data):

  swap = {'jmp':'nop', 'nop':'jmp'}

  for i, (ins, val) in enumerate(data):
    if ins in swap:
      data[i]      = (swap[ins], val)
      result, code = simulate(data)
      data[i]      = (ins, val)

      if code == False:
        return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

