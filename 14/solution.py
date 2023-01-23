#!/usr/bin/python


def parse(inp):

  prog = []

  for ln in inp:
    if ln[:4] == 'mask':
      prog.append([ln.split()[-1]])
    else:
      addr, _, val = ln.split()
      prog[-1].append((int(addr.strip('me[]')),int(val)))

  return prog


class ValueMask(str):

  def __call__(self, val):

    binval = '{:036b}'.format(val)

    return int(''.join((m,i)[m == 'X'] for i, m in zip(binval, self)), 2)


def part_1(data):

  mem = dict()

  for mask, *ins in data:
    mask = ValueMask(mask)

    for addr, val in ins:
      mem[addr] = mask(val)

  return sum(mem.values())


class AddressMask(str):

  def __call__(self, addr):

    binaddr = '{:036b}'.format(addr)
    masked  = [''.join((m,i)[m == '0'] for i, m in zip(binaddr, self))]

    while 'X' in masked[0]:
      new = []

      for m in masked:
        new.append(m.replace('X','0',1))
        new.append(m.replace('X','1',1))

      masked = new

    return [int(m, 2) for m in masked]


def part_2(data):

  mem = dict()

  for mask, *ins in data:
    mask = AddressMask(mask)

    for addr, val in ins:
      for addr in mask(addr):
        mem[addr] = val

  return sum(mem.values())


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

