def combine_lists_recursive(lists, n):
    if n == 1:
        return [[item] for item in lists[0]]
    else:
        combinations = []
        smaller_combinations = combine_lists_recursive(lists[1:], n-1)
        for item in lists[0]:
            for smaller_comb in smaller_combinations:
                combinations.append([item] + smaller_comb)
        return combinations

def print_combinations(combinations):
    for combination in combinations:
        combination = "".join(combination)
        for i in range(26):
            num = combination.count(chr(i + 97))
            if alpha_lst[i] < num:
                alpha_lst[i] = num

n = int(input())
lists = []
for _ in range(n):
    words = input().split()
    lists.append(words)
alpha_lst = [0 for _ in range(26)]

result = combine_lists_recursive(lists, n)
print_combinations(result)

for j in alpha_lst:
    print(j)