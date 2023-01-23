#!/usr/bin/python


def parse(inp):

  expressions = []

  for ln in inp:
    ln    = ln.replace('(',' ( ').replace(')', ' ) ').split()
    stack = [[]]

    for char in ln:
      if   char == '(': stack.append([])
      elif char == ')': stack[-2].append(stack.pop())
      else: stack[-1].append(char)

    expressions.append(stack[0])

  return expressions


def evaluate(expr, prio, ops = {'+': int.__add__, '*': int.__mul__}):

  if isinstance(expr, list):
    expr = expr.copy()
  else:
    return int(expr)

  while len(expr) >= 3:
    idx      = next(min(expr.index(op) for op in ch if op in expr)
                    for ch in prio if any(op in expr for op in ch)) - 1
    a, op, b = expr[idx:idx+3]
    expr[idx:idx+3] = [ops[op](evaluate(a,prio), evaluate(b,prio))]

  return expr[0]


def part_1(data):

  return sum(evaluate(expr, prio=['+*']) for expr in data)


def part_2(data):

  return sum(evaluate(expr, prio=['+','*']) for expr in data)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

