def print_sum(a,b):
    print(a+b)

if __name__ == '__main__':
    n = int(input())
    temp = []
    for i in range(n):
        a, b = map(int, input().split())
        temp.append(a+b)

    for i in range(n):
        print(temp[i])
