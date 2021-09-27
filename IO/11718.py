if __name__ == '__main__':

    temp = []
    while(True):
        try:
            a_str = input()
            if(a_str == ''):
                break
            temp.append(a_str)
        except:
            break

    for i in range(len(temp)):
        print(temp[i])
