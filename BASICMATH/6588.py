#  6588  todo~
import sys

maxVal = 1000001
arr = [True for t in range(maxVal)]
for i in range(2, int((maxVal - 1) ** 0.5) + 1):
    if arr[i]:
        for k in range(i + i, maxVal, i):
            arr[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = False

    for a in range(3, len(arr)):
        if arr[a] and arr[n - a]:
            print(str(n) + " = " + str(a) + " + " + str(n - a))
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
