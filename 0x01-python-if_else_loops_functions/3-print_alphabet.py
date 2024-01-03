#!/usr/bin/python3
for char in (c for c in map(chr, range(ord('a'), ord('z') + 1)) if c not in 'qe'):
    print(char, end='')
