
#In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print.

from collections import defaultdict

try:

    n, m = input('Enter the number of words in group A and B: ').split()
    n = int(n)
    m = int(m)

    group_A = []
    print(f'Enter {n} words for group A: ')
    for i in range(n):
        word = input().strip()
        group_A.append(word)

    group_B = []
    print(f'Enter {m} words for group B: ')
    for i in range(m):
        word = input().strip()
        group_B.append(word)

    positions = defaultdict(list)

    for idx in range(n):
        word = group_A[idx]
        positions[word].append(idx + 1)

    for word in group_B:
        if word in positions:
            print(" ".join(map(str, positions[word])))
        else:
            print(-1)

except ValueError as e:
    print(f'Input format error: {e}.')