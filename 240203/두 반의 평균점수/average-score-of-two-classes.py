n = int(input())
arr = list(map(int, input().split()))
first, second = map(int, input().split())

answer = (arr[first - 1] + arr[second - 1]) / 2

print(answer)