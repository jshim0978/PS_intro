# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7

def print_sum(a,b):
    print(a+b)

if __name__ == '__main__':
    n = int(input())
    temp = []
    for i in range(n):
        a, b = map(int, input().split())
        temp.append(a+b)

    for i in range(n):

        print('Case #' + str(i+1) + ': ' + str(temp[i]))
