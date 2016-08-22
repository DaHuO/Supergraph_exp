#!/usr/bin/python3
from sys import stdin
from collections import deque

def flip(stack, n):
  return stack[0:-n] + [1-x for x in reversed(stack[-n:])]

def binarify(stack):
  n = 0
  for i in stack: n = (n << 1) + i
  return n

def getSteps(stack):
  visited = set()
  q = deque([stack])
  steps = 0;
  while 1:
    newq = deque()
    while q:
      stack = q.popleft()
      if all(stack):
        return steps
      for j in range(len(stack)):
        newStack = flip(stack, j+1)
        b = binarify(newStack)
        if b in visited:
          continue
        visited.add(b)
        newq.append(newStack)
    q = newq
    steps += 1

for i in range(int(stdin.readline().strip())):
  stack = [(1 if x == '+' else 0) for x in reversed(stdin.readline().strip())]
  steps = getSteps(stack);
  print("Case #%d: %d" %((i+1), steps))
