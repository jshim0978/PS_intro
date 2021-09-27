if __name__ == '__main__':
    n = int(input())

    temp = []
    temp.append(1)
    temp.append(1)


    for i in range(2, n+2):
        temp.append(temp[i-1] + 2*temp[i-2])

    print(temp[n] % 10007)
