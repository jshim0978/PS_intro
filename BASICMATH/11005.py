import math
# 60466175 36   ZZZZZ
if __name__ == '__main__':

    N, B = map(int, input().split())

    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    temp = ''

    while N != 0:
        temp += chars[N % B]
        N //= B
    reversedstring = ''.join(reversed(temp))
    print(reversedstring)


