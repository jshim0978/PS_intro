if __name__ == '__main__':
    n = int(input())

for i in range(n-1):
    if i == 0:
        print(' '* (n-1) + '*')
    else:
        print(' ' * (n-i-1) + '*' + ' '*(2*i-1) + '*')
print('*'*(2*n-1))
