def print_sum(a,b):
    print(a+b)

if __name__ == '__main__':

    j = 0
    temp = []
    while(True):
        a, b = map(int, input().split())
        if(a == 0 & b == 0):
            break
        temp.append(a+b)


    for i in range(len(temp)):
        print(temp[i])
