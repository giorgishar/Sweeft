def main_thing():
    t = int(input())
    lst = []
    x = input()
    while x != "":
        lst.append(x)
        x = input()

    c = len(lst[0])
    r = len(lst)
    if t == 1:
        for i in lst:
            print(i)
        return
    if t % 2 == 0:
        print(['0'*c for i in range(r)])

    for a in range((t//2 + 1) % 2 + 1):
        grid = [['O']*c for i in range(r)]

        def detonate(x, y):
            if 0 <= x < r and 0 <= y < c:
                grid[x][y] = '.'

        for i in range(r):
            for j in range(c):
                if lst[i][j] == 'O':
                    for k in [-1, 0, 1]:
                        for l in [-1, 0, 1]:
                            if abs(k - l) == 1 or k == l == 0:
                                detonate(i + k, j + l)
        lst = grid
    for i in lst:
        print("".join(i))


main_thing()