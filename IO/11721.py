
if __name__ == '__main__':
    a_str = input()
    temp = []
    full_len = len(a_str)
    counter = 0
    while full_len > 10 :
        if len(a_str) > 10 :
            temp.append(a_str[10*counter:10*(counter+1)])
            full_len -=10
            print(temp[counter])
            counter += 1
    temp.append(a_str[10*counter:])
    print(temp[counter])


