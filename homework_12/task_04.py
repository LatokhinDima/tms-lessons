class WordIterable:
    def __init__(self, txt: str):
        self.text = txt.split()
        self.word = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.word += 1
        if self.word > len(self.text) - 1:
            raise StopIteration()
        return self.text[self.word]


for i in WordIterable("мама мыла раму"):
    print(i)

assert ['mom', 'was', 'washing', 'the', 'frame'] == [i for i in WordIterable('mom was washing the frame')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] == [i for i in WordIterable('easy peasy lemon squeezy')]
assert ['мама', 'мыла', 'окно'] != [i for i in WordIterable('mom was washing the frame')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] != [i for i in WordIterable('easy_peasy_lemon_squeezy')]
