
if __name__ == '__main__':
    n = int(input())
    nums = input()
    temp = []
    sum = 0
    for i in range(len(nums)):
        temp.append(nums[i])
        sum += int(temp[i])

    print(sum)
