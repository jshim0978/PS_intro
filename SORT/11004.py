import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    temp = [0] * 10001
    for i in range(N):
        key = (int(sys.stdin.readline()))
        temp[key] = temp[key] + 1

    for i in range(10001):
        if temp[i] != 0:
            for j in range(temp[i]):
                print(i)