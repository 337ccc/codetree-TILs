y = int(input())

if y % 4 == 0:
    if y % 400 == 0:
        print('true')
    elif y % 100 == 0:
        print('false')
    else:
        print('true')
else:
    print('false')