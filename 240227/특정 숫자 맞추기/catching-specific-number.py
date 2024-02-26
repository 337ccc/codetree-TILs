while True:
    num = int(input())
    if num == 25:
        print('Good')
        break
    elif num < 25:
        print('Higher')
    else:
        print('Lower')