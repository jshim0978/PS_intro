def print_sum(a,b):
    print(a+b)

if __name__ == '__main__':
    n = int(input())
    temp = []
    tempa = []
    tempb = []
    for i in range(n):
        a, b = map(int, input().split())
        tempa.append(a)
        tempb.append(b)
        temp.append(a+b)
    for i in range(n):

        print('Case #' + str(i+1) + ': ' + str(tempa[i]) + ' + ' + str(tempb[i]) + ' = ' + str(temp[i]))