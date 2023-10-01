for i in range(101):
    print(i)
    answer = input('Should we break?  ')
    if answer == 'yes':
        break
    while answer == 'yes':
        continue
