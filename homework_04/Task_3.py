for i in range(101):
    print(i)
    while True:
        answer = input('Should we break?  ')
        if answer in ('yes', 'no'):
            break
        else:
            print('Dont understand you  ')

    if answer == 'yes':
        break

