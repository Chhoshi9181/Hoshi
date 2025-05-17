# For 100 points, run with C++. You can find the code by clicking the link in README.md

def largest_tent_size(holes):
    n = len(holes)

    if n <= 1:
        return 0

    diagonals = {}

    for i in range(n):
        x1, y1 = holes[i]
        for j in range(i+1, n):
            x2, y2 = holes[j]

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            dx = abs(x1 - x2) / 2
            dy = abs(y1 - y2) / 2

            if dx == dy and ((x1 != x2) and (y1 != y2)):
                diagonal_length = dx * 2

                diagonals[(center_x, center_y, diagonal_length)] = diagonal_length

    if diagonals:
        return max(diagonals.values())
    else:
        return 0

def main():
    n = int(input())

    holes = []
    for _ in range(n):
        x, y = map(int, input().split())
        holes.append((x, y))

    result = largest_tent_size(holes)
    print(int(result))

if __name__ == "__main__":
    main()
