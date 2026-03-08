import sys
input = sys.stdin.readline

n, m = map(int, input().split())

red = set(map(int, input().split()))
blue = set(map(int, input().split()))

same = len(red & blue)

print(n + m - same - 2)