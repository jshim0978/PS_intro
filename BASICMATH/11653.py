#10872, 1676, 2004, 6588  todo~

if __name__ == '__main__':

    number = int(input())

    i = 2

    if number > 1:
        while number > i:
            if (number % i) == 0:
                number //= i
                print(i)
            else:
                i += 1
        print(number)
