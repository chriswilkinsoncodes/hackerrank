#!/usr/bin/env python3

# Print a list of all possible coordinates given by (x, y, z) on a 3D
# grid where the sum of x + y + z is not equal to n.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a, b, c] for a in range(x+1) for b in range(y+1)
          for c in range(z+1) if sum([a, b, c]) != n])
