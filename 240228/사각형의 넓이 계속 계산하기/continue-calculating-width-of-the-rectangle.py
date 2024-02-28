while True:
    a, b, alphabet = input().split()
    a, b = int(a), int(b)
    area = a * b
    print(area)
    if alphabet == 'C':
        break