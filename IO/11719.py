import sys

if __name__ == '__main__':

    for line in sys.stdin:
        print(line, end= '')


# while True:
#     try :
#         print(input())
#     except EOFError :                                     # 더이상 읽어들일 것이 없을 때 발생하는 에러
#         break