class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self):
        return int(self.seconds // 3600)

    @property
    def minutes(self):
        return int(self.seconds // 60 % 60)

#sec = MyTime(2569996.5)

#hours = sec.hours
#minuts = sec.minutes

#print(hours)
#print(minuts)

    def __mul__(self, number):
        return MyTime(self.seconds * number)

    def __truediv__(self, number):
        return MyTime(self.seconds / number)

    def __add__(self, other):
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other):
        return MyTime(self.seconds - other.seconds)

#a = MyTime(10)
#b = MyTime(2)
#d = (a + b) * 2
#print(d.seconds)

    def get_formatted_str(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds % 60:04.1f}'

#seconds1 = MyTime(21569.7)
#times = seconds1.get_formatted_str()
#print(times)

    def __str__(self):
        return f'{self.seconds}s'

#print(MyTime(10))



