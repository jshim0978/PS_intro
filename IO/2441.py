if __name__ == '__main__':
    n = int(input())



    for i in range(n):
        print('*'*(i+1) + ' '*(2*n-2*i) + '*'*(i+1))

    print('*' * (2*n+2))

    for i in range(n):
        print('*'*(n-i) + ' '*(2*i+2) + '*'*(n-i))
