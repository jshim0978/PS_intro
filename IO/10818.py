# 5
# 20 10 35 30 7
# 7 35

if __name__ == '__main__':
    n = int(input())


    temp= input().split(' ')

    for i in range(len(temp)):
        temp[i] = int(temp[i])
    temp = sorted(temp)

    print(temp[0], temp[len(temp)-1])

