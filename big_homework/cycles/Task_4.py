num_lst = [int(i) for i in input().split()]

for i in num_lst:
    if i == 0:
        print('yes')
        break
else:
    print('no')
