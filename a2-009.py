import sys
input = sys.stdin.readline

N, C = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

teams = list(range(1, N+1))

used = False

while len(teams) > 1:
    nxt = []

    for i in range(0, len(teams), 2):
        a = teams[i]
        b = teams[i+1]

        winner = table[a-1][b-1]

        if not used and C != 0:
            if a == C and winner == b:
                winner = C
                used = True
            elif b == C and winner == a:
                winner = C
                used = True

        nxt.append(winner)

    teams = nxt

print(teams[0])