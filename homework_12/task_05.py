import re


class WordIterable:
    def __init__(self, txt: str):
        self.txt = re.findall(r'[A-ZА-Яa-zа-я]+', txt)
        self.word = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.word += 1
        if self.word > len(self.txt) - 1:
            raise StopIteration()
        return self.txt[self.word]


for i in WordIterable("$/.мама ---. -мыла= .__раму++."):
    print(i)

assert ['mom', 'was', 'washing', 'the', 'frame'] == [i for i in WordIterable('!mom was /washing the frame$')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] == [i for i in WordIterable('@easy! peasy lemon squeezy')]
assert ['мама', 'мыла', '!окно'] != [i for i in WordIterable('mom was washing the frame')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] == [i for i in WordIterable('easy_peasy_lemon_squeezy')]
