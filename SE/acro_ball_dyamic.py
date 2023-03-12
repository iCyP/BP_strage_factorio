import copy
from math import sqrt

zaiko = [9, 0, 9, 2, 8, 6, 10, 8]

recipe = [
    [-1, 1, 0, 1, 0, 0, 0, -1],
    [1, -1, 1, 0, 0, 0, -1, 0],
    [0, -1, -1, 1, 0, 1, 0, 0],
    [-1, 0, 1, -1, 1, 0, 0, 0],
    [0, 0, 0, -1, -1, 1, 0, 1],
    [0, 0, -1, 0, 1, -1, 1, 0],
    [0, 1, 0, 0, 0, -1, -1, 1],
    [1, 0, 0, 0, -1, 0, 1, -1],
    [1, 1, -1, -1, 1, 1, -1, -1],
    [-1, -1, 1, 1, -1, -1, 1, 1],
]


def check(current, rec):
    tmp = copy.copy(current)
    for i, x in enumerate(rec):
        if current[i] + x <= 0:
            return False
    return True


def exec(current, rec):
    res = copy.copy(current)
    for i, x in enumerate(rec):
        res[i] = current[i] + x
    return res


def bunsan(current):
    tmp = sum(current) / 8
    x = 0
    for i in current:
        if i <= 1:
            x += 10
        x += sqrt(pow(i - tmp, 2))
    return x


def minify(current, indices):
    z = []
    for x in recipe:
        if check(current, x):
            z.append(bunsan(exec(current, x)))
        else:
            z.append(10000)
    min_val = z[0]
    min_index = 0
    for i in range(1, len(z)):
        if z[i] < min_val:
            min_val = z[i]
            min_index = i
    indices.append(min_index)
    current = exec(current, recipe[min_index])
    return current, indices, min_val


def main():
    tejun = []
    current = copy.copy(zaiko)
    minv = 1000
    for x in range(1000):
        tmp = 0
        current, tejun, tmp = minify(current, tejun)
        print(current)
        print(tejun)
        if min(current) < 5:
            continue
        else:
            print(sum(zaiko))

            break
    print("As a Result")
    print("balls: " + str(current))
    print("how:" + str(tejun))
    print("sum of balls: " + str(sum(current)))


main()
