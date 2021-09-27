import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    temp = []
    for i in range(N):
        key = (int(sys.stdin.readline()))
        temp.append(key)

    temp.sort()
    count = 1
    localMax = 0
    localMaxVal = temp[0]

    for i in range(N-1):
        if temp[i] == temp[i+1]:
            count += 1
            if localMax < count:
                localMax = count
                localMaxVal = temp[i]
            else:
                continue
        else:
            if localMax < count:
                localMax = count
                localMaxVal = temp[i]
                count = 1
            else:
                count = 1

    print(localMaxVal)
