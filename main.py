from os import sys
from Type import type

t = type.Type

for line in sys.stdin:
    v = line.split()
    res = type.getMultiplier(t(int(v[0])), t(int(v[1])), t(int(v[2])), t(int(v[3])), t(int(v[4])))
    print(res)


