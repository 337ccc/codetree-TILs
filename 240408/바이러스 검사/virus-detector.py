n = int(input())
visitor_num = list(map(int, input().split()))
# 검사자는 팀장과 팀원으로 구성, 팀장은 오직 한 명
leader, member = map(int, input().split())

count = 0
for i in visitor_num:
    # 팀장은 무조건 필요
    count +=1
    visitor = i
    visitor -= leader
    if visitor <= 0:
        continue
    else:
        count += (visitor // member) + 1

print(count)