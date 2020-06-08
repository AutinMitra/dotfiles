from matching.algorithms import galeshapley
from pwn import *

import sys
sys.setrecursionlimit(120000)

def getAns(lines):
  lines = lines.splitlines()
  n, lookfor = [int(i) for i in lines[0].split()];

  college = {}
  people = {}
  id2name = {}

  for i in range(1, n+1):
    people[i-1] = [int(j) for j in lines[i].split()]
  for i in range(n+1, 2*n+1):
    college[i-n-1] = [int(j) for j in lines[i].split()]
  for i in range(2*n+1, 3*n+1):
    id2name[i-2*n-1] = lines[i].strip()

  matching = galeshapley(
    college, people
  )

  matching = dict(map(reversed, matching.items()))

  return id2name[matching[lookfor]]

conn = remote('algo.hsctf.com',4002)

iter = 1;

while(True):
  first = conn.recvuntil(str.encode(str(iter)) + b'!\n')
  # print(first)
  lines = conn.recvline()
  n = int(lines.split()[0])
  lines += b''.join([conn.recvline() for i in range(0, 3*n)])
  ans = getAns(lines);
  conn.send(ans + b"\n")  # print(str)
  print(ans.decode("utf-8") )
  iter += 1
