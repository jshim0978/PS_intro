if __name__ == '__main__':
    testCaseNo = int(input())

    temp = []
    max_alc = 0
    consecutive = 1


    if testCaseNo < 3:
        temp.append(int(input()))
        temp.append(int(input()))
        for firstTwo in range(testCaseNo):
            max_alc += int(input())

    else:
        temp.append(int(input()))
        temp.append(int(input()))
        for i in range(2, testCaseNo):
            temp.append(int(input()))
            biggerSum = max(temp[i-1], temp[i-2])
            if biggerSum == temp[i-1]:
                consecutive += 1
                print('biggerSum = ', biggerSum)
                print('consecutive = ', consecutive)
            else:
                consecutive = 1
                print('biggerSum = ', biggerSum)
                print('consecutive = ', consecutive)
            if consecutive != 3:
                print('i = ', i)
                temp[i] += biggerSum
                print('not 3 temp[i] = ', temp[i])
            else:
                print('is 3 temp[i] = ', temp[i])
                continue
        max_alc = temp[testCaseNo-1]
    print(max_alc)

