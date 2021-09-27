def print_sum(a,b):
    print(a+b)

if __name__ == '__main__':

    j = 0
    temp = []
    while(True):
        try:
            a, b = map(int, input().split())
            temp.append(a+b)
        except:
            break

    for i in range(len(temp)):
        print(temp[i])
