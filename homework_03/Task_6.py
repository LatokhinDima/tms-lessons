dict_1 = {'January': 31,
          'February': 28,
          'March': 31,
          'April': 30,
          'May': 31,
          'June': 30,
          'July': 31,
          'August': 31,
          'September': 30,
          'October': 31,
          'November': 30,
          'December': 31}
month = input('Enter month: ')
day = int(input('Enter day: '))
if month in dict_1 and dict_1[month] >= day:
    print(True)
