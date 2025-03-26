
if __name__ == '__main__':

    x = 2 #int(input())
    y = 2 #int(input())
    z = 2 #int(input())
    n = 3 #int(input())

    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

    print(coordinates)