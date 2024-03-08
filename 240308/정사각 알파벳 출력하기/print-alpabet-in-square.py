# ord() : 문자를 아스키코드로
# chr() : 아스키코드를 문자로
# A는 65

n = int(input())

num = 64
for i in range(n):
    for j in range(n):
        num += 1
        print(chr(num), end='')
    
    print()